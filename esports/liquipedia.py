"""Liquipedia 维基：读取赛事页面源码，并把里面的比赛模板解析成结构化数据。

Liquipedia 要求礼貌访问（每 2 秒最多 1 次），这里统一间隔 4 秒并做本地缓存。
"""
import re

from . import net

API = "https://liquipedia.net/{wiki}/api.php"
GAP = float(__import__("os").environ.get("LIQUIPEDIA_GAP", "4.0"))


def wikitext(title: str, wiki: str = "leagueoflegends") -> str | None:
    data = net.get(API.format(wiki=wiki), dict(
        action="query", prop="revisions", rvprop="content", rvslots="main",
        format="json", redirects=1, titles=title), gap=GAP, as_json=True)
    page = next(iter(data["query"]["pages"].values()))
    revs = page.get("revisions")
    return revs[0]["slots"]["main"]["*"] if revs else None


def search(query: str, wiki: str = "leagueoflegends", limit: int = 10) -> list[str]:
    data = net.get(API.format(wiki=wiki), dict(
        action="query", list="search", srsearch=query, format="json", srlimit=limit),
        gap=GAP, as_json=True)
    return [x["title"] for x in data["query"]["search"]]


def _blocks(text: str, name: str):
    """找出所有 {{name ...}} 模板块（处理嵌套花括号）。"""
    for m in re.finditer(r"\{\{\s*" + name + r"\s*[\n|]", text):
        depth, i = 0, m.start()
        while i < len(text) - 1:
            if text.startswith("{{", i):
                depth += 1
                i += 2
            elif text.startswith("}}", i):
                depth -= 1
                i += 2
                if depth == 0:
                    yield m.start(), text[m.start():i]
                    break
            else:
                i += 1


def _params(block: str) -> dict:
    """解析模板的顶层参数 |key=value。"""
    inner = block[2:-2]
    out, depth, cur = {}, 0, ""
    parts = []
    i = 0
    while i < len(inner):
        two = inner[i:i + 2]
        if two in ("{{", "[["):
            depth += 1
            cur += two
            i += 2
            continue
        if two in ("}}", "]]"):
            depth -= 1
            cur += two
            i += 2
            continue
        if inner[i] == "|" and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += inner[i]
        i += 1
    parts.append(cur)
    for p in parts[1:]:
        if "=" in p:
            k, v = p.split("=", 1)
            out[k.strip()] = v.strip()
    return out


def _clean(v: str) -> str:
    v = re.sub(r"<!--.*?-->", "", v, flags=re.S)
    return v.strip()


def _opponent(v: str):
    """{{TeamOpponent|name|score=2}} -> (name, score)"""
    m = re.search(r"\{\{\s*TeamOpponent\s*\|([^|}]*)", v)
    name = _clean(m.group(1)) if m else None
    if name and "=" in name:
        name = None
    s = re.search(r"score\s*=\s*(\w+)", v)
    if not name:
        t = re.search(r"\|\s*template\s*=\s*([^|}]+)", v) or re.search(r"\|\s*1\s*=\s*([^|}]+)", v)
        name = _clean(t.group(1)) if t else None
    score = s.group(1) if s else None
    return name, score


def parse_matches(text: str) -> list[dict]:
    """解析新版 {{Match ...}} 模板：队伍、比分、每张图/每局胜者、BP。"""
    out = []
    # 每个 Match 前面的 |R1M1= 之类标记表示轮次
    for pos, blk in _blocks(text, "Match"):
        head = text[max(0, pos - 30):pos]
        rid = re.findall(r"\|\s*(R\d+M\d+|[A-Za-z0-9]+)\s*=\s*$", head)
        p = _params(blk)
        t1, s1 = _opponent(p.get("opponent1", ""))
        t2, s2 = _opponent(p.get("opponent2", ""))
        if not t1 or not t2:
            continue
        games = []
        for k in sorted((k for k in p if re.fullmatch(r"map\d+", k)), key=lambda k: int(k[3:])):
            mp = _params(p[k]) if p[k].startswith("{{") else {}
            if not mp:
                continue
            w = mp.get("winner", "")
            if not w and mp.get("score1", "").isdigit() and mp.get("score2", "").isdigit():
                w = "1" if int(mp["score1"]) > int(mp["score2"]) else "2"
            if not w:  # 新版 CS 页面只给上下半场/加时比分：t1t, t1ct, t1o1t ...
                h1 = sum(int(v) for k, v in mp.items() if re.fullmatch(r"(o\d+)?t1(t|ct)", k) and v.isdigit())
                h2 = sum(int(v) for k, v in mp.items() if re.fullmatch(r"(o\d+)?t2(t|ct)", k) and v.isdigit())
                if h1 != h2:
                    w = "1" if h1 > h2 else "2"
                    mp.setdefault("score1", str(h1))
                    mp.setdefault("score2", str(h2))
            if w not in ("1", "2"):
                continue
            g = dict(winner=int(w), map=_clean(mp.get("map", "")),
                     side1=mp.get("team1side", ""),
                     score1=mp.get("score1"), score2=mp.get("score2"))
            for t in (1, 2):
                g[f"picks{t}"] = [_clean(m) for m in re.findall(
                    r"character\s*=\s*([^|}]+)", " ".join(mp.get(f"t{t}p{i}", "") for i in range(1, 6)))]
                g[f"picks{t}"] += [_clean(mp[f"t{t}c{i}"]) for i in range(1, 6) if mp.get(f"t{t}c{i}")]
                g[f"bans{t}"] = [_clean(mp[f"t{t}b{i}"]) for i in range(1, 6) if _clean(mp.get(f"t{t}b{i}", ""))]
                g[f"players{t}"] = [re.sub(r"\s*\(.*?\)\s*$", "", _clean(m)) for m in re.findall(
                    r"player\s*=\s*([^|}]+)", " ".join(mp.get(f"t{t}p{i}", "") for i in range(1, 6)))]
                for key in ("kills", "deaths", "assists"):
                    g[f"{key}{t}"] = [int(x) if x.isdigit() else None for x in (
                        (re.search(rf"{key}\s*=\s*(\d*)", mp.get(f"t{t}p{i}", "")) or [None, ""])[1] for i in range(1, 6))]
                ln = re.match(r"(\d+):(\d+)", mp.get("length", ""))
                g["length"] = int(ln.group(1)) * 60 + int(ln.group(2)) if ln else None
            games.append(g)
        w1 = sum(g["winner"] == 1 for g in games)
        w2 = sum(g["winner"] == 2 for g in games)
        if s1 and s2 and s1.isdigit() and s2.isdigit() and int(s1) != int(s2):
            w1, w2 = int(s1), int(s2)  # 官方比分优先（有判负/弃权的情况）
        if w1 == w2:
            continue
        out.append(dict(round=rid[-1] if rid else "", team1=t1, team2=t2, score1=w1, score2=w2,
                        winner=1 if w1 > w2 else 2, date=_clean(p.get("date", "")), games=games))
    return out


def parse_legacy_bracket(text: str) -> list[dict]:
    """解析老式对阵表参数：R1D1team= / R1D1score= / R1W1team= ..."""
    slots = {}
    for k, v in re.findall(r"\|\s*(R\d+[DWG]\d+)(team|score)\s*=\s*([^|\n}]*)", text):
        slots.setdefault(k, {})
    for k, kind, v in re.findall(r"\|\s*(R\d+[DWG]\d+)(team|score)\s*=\s*([^|\n}]*)", text):
        slots[k][kind] = _clean(v)
    out = []
    by_round = {}
    for k in slots:
        r, idx = re.match(r"R(\d+)[DWG](\d+)", k).groups()
        by_round.setdefault(int(r), []).append((int(idx), k))
    for r in sorted(by_round):
        lst = sorted(by_round[r])
        for a, b in zip(lst[::2], lst[1::2]):
            A, B = slots[a[1]], slots[b[1]]
            try:
                s1, s2 = int(A.get("score", "")), int(B.get("score", ""))
            except ValueError:
                continue
            if not A.get("team") or not B.get("team") or s1 == s2:
                continue
            out.append(dict(round=f"R{r}", team1=A["team"], team2=B["team"], score1=s1, score2=s2,
                            winner=1 if s1 > s2 else 2, date="", games=[]))
    return out


def page_matches(title: str, wiki: str = "leagueoflegends") -> list[dict]:
    text = wikitext(title, wiki)
    if not text:
        return []
    return parse_matches(text) or parse_legacy_bracket(text)
