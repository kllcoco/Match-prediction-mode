"""联网更新：从 Liquipedia 拉取最新赛事结果，并入训练数据，这样随时能预测当下的比赛。

流程：
1. 读 Liquipedia 的 S/A 级赛事列表，找到今年（和去年年底）的赛事
2. 逐个赛事页面（含子页面）解析比赛：
   - 老格式：直接读源码里的 {{Match}} 模板
   - 新格式（比分由接口动态生成）：请求渲染后的 HTML 再解析
3. 存成 data/processed/{lol,cs}_live.csv.gz，build_lol / build_cs 会自动合并

Liquipedia 规定：普通请求 ≥2 秒一次，渲染请求 ≥30 秒一次，这里都遵守。
"""
import html as H
import re
from datetime import datetime, timedelta, timezone

import pandas as pd

from . import liquipedia as L
from . import net
from .net import DATA

OUT = {"lol": DATA / "processed" / "lol_live.csv.gz", "cs": DATA / "processed" / "cs_live.csv.gz"}
WIKI = {"lol": "leagueoflegends", "cs": "counterstrike"}
# LOL 只关心能进世界赛的赛区和国际赛
LOL_KEEP = re.compile(r"^(LCK|LPL|LEC|LCS|LCP|CBLOL|LTA|PCS|VCS|LJL|World_Championship|Mid-Season_Invitational|"
                      r"First_Stand|Esports_World_Cup|Asian_Games)", re.I)
SKIP = re.compile(r"Qualifier|Showmatch|All-Star|Academy|Challengers|/Promotion", re.I)
DAY = 86400


def _parse_html(page, wiki, ttl):
    d = net.get(L.API.format(wiki=wiki), dict(action="parse", page=page, prop="text", format="json"),
                gap=31, as_json=True, ttl=ttl)
    return d["parse"]["text"]["*"] if "parse" in d else ""


def _txt(s):
    return H.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def html_matches(h):
    """解析渲染后的对阵 HTML（新版 match2 组件）。"""
    out = []
    parts = re.split(r'<div class="brkts-(?:matchlist-match|match) ', h)[1:]
    for c in parts:
        names = list(dict.fromkeys(H.unescape(x) for x in re.findall(r'aria-label="([^"]+)"', c[:6000])))
        if len(names) < 2:
            names = list(dict.fromkeys(_txt(x) for x in re.findall(r'class="team-name">(.*?)</div>', c[:8000])))
        sc = re.findall(r'brkts-matchlist-score[^>]*>\s*<div class="brkts-matchlist-cell-content">([^<]*)<', c) or \
            re.findall(r'brkts-opponent-score-inner[^>]*>\s*(?:<b>)?(\d+)', c)
        ts = re.findall(r'data-timestamp="(\d+)"', c)
        if len(names) < 2 or len(sc) < 2 or not sc[0].strip().isdigit() or not sc[1].strip().isdigit():
            continue
        s1, s2 = int(sc[0]), int(sc[1])
        if s1 == s2:
            continue
        date = datetime.fromtimestamp(int(ts[0]), timezone.utc).replace(tzinfo=None) if ts else None
        games = []
        for row in re.findall(r'brkts-popup-body-grid-row">(.*?)data-label-type="result-(?:win|loss)"></div></div>', c, re.S):
            lab = re.search(r'data-label-type="result-(win|loss)"', row)
            champs = re.findall(r'brkts-popup-side-color--(blue|red)"><a [^>]*title="([^"]+)"', row)
            if not lab or len(champs) < 10:
                continue
            games.append(dict(win1=int(lab.group(1) == "win"), side1=champs[0][0],
                              c1=[H.unescape(x) for _, x in champs[:5]], c2=[H.unescape(x) for _, x in champs[5:10]]))
        # 每局选手名 + 表现（K/D/A、伤害）+ 时长
        dets = re.split(r'class="brkts-popup-game-detail with-center-column"', c)[1:]
        for gi, dsec in enumerate(dets[:len(games)]):
            ps = re.findall(r'brkts-popup-game-detail-player-character">.*?</div><a [^>]*title="([^"]+)"', dsec, re.S)
            if len(ps) >= 10:
                games[gi]["p1"], games[gi]["p2"] = ps[:5], ps[5:10]
            st = re.findall(r'brkts-popup-game-detail-player-stats"><div>(\d+)<span class="slash">/</span>(\d+)'
                            r'<span class="slash">/</span>(\d+)</div>(?:\s*<div>\(<i[^>]*></i>&#160;([\d.]+)(K?)\))?', dsec)
            if len(st) >= 10:
                for t, part in (("1", st[:5]), ("2", st[5:10])):
                    games[gi]["k" + t] = [int(x[0]) for x in part]
                    games[gi]["d" + t] = [int(x[1]) for x in part]
                    games[gi]["a" + t] = [int(x[2]) for x in part]
                    games[gi]["dmg" + t] = [float(x[3]) * (1000 if x[4] else 1) if x[3] else None for x in part]
            ln = re.search(r"Game \d+ - (\d+):(\d+)", dsec)
            if ln:
                games[gi]["length"] = int(ln.group(1)) * 60 + int(ln.group(2))
        out.append(dict(team1=names[0], team2=names[1], score1=s1, score2=s2, date=date, games=games))
    return out


def tournaments(game, years, ttl=12 * 3600):
    roots = []
    for t in ("S-Tier_Tournaments", "A-Tier_Tournaments"):
        h = _parse_html(t, WIKI[game], ttl)
        for link in re.findall(rf'href="/{WIKI[game]}/([^"#?]+)"', h):
            y = re.search(r"(20\d\d)", link)
            if not y or int(y.group(1)) not in years or SKIP.search(link) or "Tier" in link:
                continue
            if game == "lol" and not LOL_KEEP.search(link):
                continue
            if link not in roots:
                roots.append(link)
    return roots


def scrape_root(root, game, ttl):
    wiki = WIKI[game]
    sub = net.get(L.API.format(wiki=wiki), dict(action="query", list="allpages", apprefix=root.replace("_", " ") + "/",
                                                aplimit=100, format="json"), gap=L.GAP, as_json=True, ttl=ttl)
    pages = [root] + [p["title"] for p in sub["query"]["allpages"]
                      if not re.search(r"Statistics|Player Stats|Qualif|Additional|Media|Broadcast", p["title"])]
    rows = []
    rt = net.get(L.API.format(wiki=wiki), dict(action="query", prop="revisions", rvprop="content", rvslots="main",
                                               format="json", redirects=1, titles=root), gap=L.GAP, as_json=True, ttl=ttl)
    pg0 = next(iter(rt["query"]["pages"].values()))
    src0 = pg0["revisions"][0]["slots"]["main"]["*"] if pg0.get("revisions") else ""
    ed = re.search(r"\|\s*edate\s*=\s*(\d{4}-\d{2}-\d{2})", src0)
    if ed and pd.Timestamp(ed.group(1)) < pd.Timestamp(datetime.now(timezone.utc).replace(tzinfo=None)) - pd.Timedelta(days=2):
        ttl = None  # 已结束：永久缓存
    for p in pages:
        text = net.get(L.API.format(wiki=wiki), dict(action="query", prop="revisions", rvprop="content",
                                                     rvslots="main", format="json", redirects=1, titles=p),
                       gap=L.GAP, as_json=True, ttl=ttl)
        pg = next(iter(text["query"]["pages"].values()))
        src = pg["revisions"][0]["slots"]["main"]["*"] if pg.get("revisions") else ""
        ms = L.parse_matches(src)
        if ms and all(m["games"] or m["score1"] + m["score2"] > 0 for m in ms):
            for m in ms:
                m["date"] = _date(m["date"])
        elif re.search(r"\{\{Match\}\}|ShowBracket|\{\{Matchlist|\{\{Bracket", src):
            ms = html_matches(_parse_html(p, wiki, ttl))
        else:
            continue
        for m in ms:
            m["event"] = root.replace("_", " ")
            m["stage"] = p
        rows += ms
    return rows


def _date(s):
    m = re.search(r"([A-Z][a-z]+ \d{1,2},? \d{4})(?: - (\d{1,2}):(\d{2}))?", s or "")
    if not m:
        return None
    try:
        d = datetime.strptime(m.group(1).replace(",", ""), "%B %d %Y")
    except ValueError:
        return None
    if m.group(2):
        d = d.replace(hour=int(m.group(2)), minute=int(m.group(3)))
    return d


def to_lol_rows(ms):
    rows = []
    for m in ms:
        lg = _league_of(m["event"])
        games = m["games"] or [dict(win1=int(i < m["score1"])) for i in range(m["score1"] + m["score2"])]
        for gi, g in enumerate(games, 1):
            if "win1" not in g:  # 旧格式（wiki 源码模板）字段名不同，转成统一格式
                g = dict(win1=int(g.get("winner") == 1), side1=(g.get("side1") or "blue").lower(),
                         c1=g.get("picks1", []), c2=g.get("picks2", []), p1=g.get("players1", []),
                         p2=g.get("players2", []), k1=g.get("kills1", []), k2=g.get("kills2", []),
                         d1=g.get("deaths1", []), d2=g.get("deaths2", []), a1=g.get("assists1", []),
                         a2=g.get("assists2", []), length=g.get("length"))
            blue1 = g.get("side1", "blue") == "blue"
            a, b = ("1", "2") if blue1 else ("2", "1")
            r = dict(date=m["date"], year=m["date"].year if m["date"] else None, league=lg, event=m["event"],
                     intl=int(lg in ("WLDs", "MSI", "FST")), playoffs=int(bool(re.search(r"Playoff|Knockout|Final", m["stage"]))),
                     patch=None, game=gi, blue=m["team" + a], red=m["team" + b],
                     blue_win=g["win1"] if blue1 else 1 - g["win1"], source="liquipedia-live")
            for i in range(5):
                for s, t in (("b", a), ("r", b)):
                    cs, ps = g.get("c" + t, []), g.get("p" + t, [])
                    r[f"{s}p{i+1}"] = cs[i] if i < len(cs) else None
                    r[f"{s}n{i+1}"] = ps[i] if i < len(ps) else None
                    for x in ("k", "d", "a", "dmg"):
                        v = g.get(x + t, [])
                        r[f"{s}{x}{i+1}"] = v[i] if i < len(v) else None
            r["gamelength"] = g.get("length")
            rows.append(r)
    return pd.DataFrame(rows)


def _league_of(event):
    e = event.replace("_", " ")
    for pat, lg in ((r"^World Championship", "WLDs"), (r"^Mid-Season Invitational", "MSI"), (r"^First Stand", "FST"),
                    (r"^Esports World Cup", "EWC"), (r"^Asian Games", "ASI"), (r"^LCK", "LCK"), (r"^LPL", "LPL"),
                    (r"^LEC", "LEC"), (r"^LCS", "LCS"), (r"^LCP", "LCP"), (r"^CBLOL", "CBLOL"), (r"^LTA", "LTA N")):
        if re.search(pat, e):
            return lg
    return e.split("/")[0]


def to_cs_rows(ms):
    rows = []
    for m in ms:
        mid = f"lp{abs(hash((m['team1'], m['team2'], str(m['date']))))}"
        bo = 2 * max(m["score1"], m["score2"]) - 1
        if m["games"]:
            for g in m["games"]:
                rows.append(dict(date=m["date"], event=m["event"], match_id=mid, best_of=bo, team1=m["team1"],
                                 team2=m["team2"], map=g.get("map") or "", win1=int(g["winner"] == 1)))
        else:
            for i in range(m["score1"] + m["score2"]):
                rows.append(dict(date=m["date"], event=m["event"], match_id=mid, best_of=bo, team1=m["team1"],
                                 team2=m["team2"], map="", win1=int(i < m["score1"])))
    df = pd.DataFrame(rows)
    if len(df):
        df["source"] = "liquipedia-live"
    return df


def update(game, since=None, years=None, verbose=True):
    """拉取 since 之后的比赛（默认：已有数据的最后一天之后）。"""
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    years = years or {now.year, (now - timedelta(days=120)).year}
    roots = tournaments(game, years)
    if verbose:
        print(f"[{game}] 发现 {len(roots)} 个赛事：", ", ".join(roots[:12]), "..." if len(roots) > 12 else "")
    allm = []
    for i, root in enumerate(roots):
        ms = scrape_root(root, game, ttl=6 * 3600)
        allm += ms
        if verbose:
            print(f"  [{i+1}/{len(roots)}] {root}: {len(ms)} 场")
    ms = [m for m in allm if m.get("date")]
    if since is not None:
        ms = [m for m in ms if m["date"] >= pd.Timestamp(since)]
    df = to_lol_rows(ms) if game == "lol" else to_cs_rows(ms)
    if len(df):
        key = ["date", "blue", "red", "game"] if game == "lol" else ["date", "team1", "team2", "map", "win1"]
        df = df.drop_duplicates(subset=key, keep="last").sort_values("date")
        df.to_csv(OUT[game], index=False, compression="gzip")
    print(f"[{game}] 新比赛数据：{len(df)} 局/图 -> {OUT[game]}")
    return df


if __name__ == "__main__":
    import sys
    for g in (sys.argv[1:] or ["lol", "cs"]):
        update(g)
