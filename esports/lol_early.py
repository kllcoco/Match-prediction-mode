"""2011-2015 年 LOL 比赛：从 Liquipedia 抓（OE 数据 2016 年前不全）。
同时抓取 S1-S15 世界赛和 MSI（带 intl 标记，严格模式训练时会被屏蔽）。

输出 data/processed/lol_early_games.csv.gz（一局一行，格式同 build_lol）
"""
import re
from datetime import datetime

import pandas as pd

from . import liquipedia as L
from . import net
from .net import DATA

OUT = DATA / "processed" / "lol_early_games.csv.gz"
TIER_PAGES = ["S-Tier_Tournaments", "A-Tier_Tournaments", "B-Tier_Tournaments/2011",
              "B-Tier_Tournaments/2012", "B-Tier_Tournaments/2013"]
SKIP = re.compile(r"Qualifier|Showmatch|All-Star|Wildcard|^LAC|^LAN/|^LNL|^CLS|^OPL|^Oceani|^TCL|^Turkish|"
                  r"^CBLOL|^NLB|^LJL|^VCS|^CIS|^LAT_|^The_Legends|^Gamers_Assembly|^ESL/Pro_Series|"
                  r"^Asian_Indoor|^IeSF|^Thor_Open|Valencia|^Challenger_Series|^CK/|^LSPL", re.I)
MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"

LEAGUE_OF = [
    (r"^World_Championship", "WLDs"), (r"^Mid-Season_Invitational", "MSI"),
    (r"^Champions|^LCK|^OGN", "LCK"), (r"^LPL", "LPL"), (r"^LCS/North_America", "NA LCS"),
    (r"^LCS/Europe", "EU LCS"), (r"^LMS", "LMS"), (r"^Garena_Premier_League", "GPL"),
    (r"^CBLOL", "CBLOL"), (r"^TCL|^Turkish", "TCL"), (r"^OPL|^Oceani", "OPL"), (r"^LJL", "LJL"),
    (r"^Challenger_Series/North_America", "NA CS"), (r"^Challenger_Series/Europe", "EU CS"),
    (r"^NLB", "NLB"), (r"^LSPL", "LSPL"), (r"^Demacia_Cup", "DCup"), (r"^KeSPA", "KeSPA"),
]
INTL = {"WLDs", "MSI"}


def league_of(title):
    for pat, lg in LEAGUE_OF:
        if re.search(pat, title):
            return lg
    return title.split("/")[0].replace("_", " ")


def tier_roots(years=range(2011, 2016)):
    roots = []
    for t in TIER_PAGES:
        d = net.get(L.API.format(wiki="leagueoflegends"),
                    dict(action="parse", page=t, prop="text", format="json"), gap=31, as_json=True)
        for link in re.findall(r'href="/leagueoflegends/([^"#?]+)"', d["parse"]["text"]["*"]):
            y = re.search(r"(20\d\d)", link)
            if y and int(y.group(1)) in years and not SKIP.search(link) and "Tier" not in link and link not in roots:
                roots.append(link)
    for y in range(2011, 2026):  # 世界赛全部要（答案和 full 模式用）
        roots.append(f"World_Championship/{y}")
    for y in range(2015, 2016):
        roots.append(f"Mid-Season_Invitational/{y}")
    return list(dict.fromkeys(roots))


def subpages(root):
    data = net.get(L.API.format(wiki="leagueoflegends"), dict(
        action="query", list="allpages", apprefix=root.replace("_", " ") + "/", aplimit=100, format="json"),
        gap=L.GAP, as_json=True)
    return [p["title"] for p in data["query"]["allpages"]]


def _date(s, fallback):
    m = re.search(rf"({MONTHS})\s+(\d{{1,2}}),?\s+(\d{{4}})", s or "")
    if m:
        return datetime.strptime(f"{m.group(1)} {m.group(2)} {m.group(3)}", "%B %d %Y")
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", s or "")
    if m:
        try:
            return datetime(*map(int, m.groups()))
        except ValueError:
            pass
    return fallback


def _infobox_date(text):
    for key in ("edate", "sdate", "date"):
        m = re.search(rf"\|\s*{key}\s*=\s*(\d{{4}}-\d{{2}}-\d{{2}})", text or "")
        if m:
            try:
                return datetime.strptime(m.group(1), "%Y-%m-%d")
            except ValueError:
                pass
    return None


def scrape(years=range(2011, 2016)):
    rows = []
    roots = tier_roots(years)
    print("赛事数:", len(roots))
    for n, root in enumerate(roots):
        lg = league_of(root)
        root_text = L.wikitext(root) or ""
        fallback = _infobox_date(root_text)
        if fallback is None:
            y = int(re.search(r"(20\d\d)", root).group(1))
            fallback = datetime(y, 6, 30)
        pages = [root] + subpages(root)
        cnt = 0
        for p in pages:
            text = root_text if p == root else (L.wikitext(p) or "")
            ms = L.parse_matches(text) or L.parse_legacy_bracket(text)
            fb = _infobox_date(text) or fallback
            stage = p[len(root):].strip("/") if p != root else ""
            for m in ms:
                d = _date(m["date"], fb)
                base = dict(date=d, year=d.year, league=lg, event=root.replace("_", " "),
                            intl=int(lg in INTL), playoffs=int(bool(re.search(r"Playoff|Bracket|Final", stage + m["round"], re.I)) or m["round"].startswith("R")),
                            stage=stage, round=m["round"], source="liquipedia")
                if m["games"]:
                    for gi, g in enumerate(m["games"], 1):
                        # team1side=blue/red，缺失时默认 team1 蓝方
                        t1_blue = (g.get("side1") or "blue").lower() != "red"
                        a, b = ("1", "2") if t1_blue else ("2", "1")
                        row = dict(base, game=gi,
                                   blue=m["team" + a], red=m["team" + b],
                                   blue_win=int(str(g["winner"]) == a))
                        for i in range(5):
                            pa, pb = g["picks" + a], g["picks" + b]
                            ba, bb = g["bans" + a], g["bans" + b]
                            row[f"bp{i+1}"] = pa[i] if i < len(pa) else None
                            row[f"rp{i+1}"] = pb[i] if i < len(pb) else None
                            row[f"bb{i+1}"] = ba[i] if i < len(ba) else None
                            row[f"rb{i+1}"] = bb[i] if i < len(bb) else None
                            qa, qb = g.get("players" + a, []), g.get("players" + b, [])
                            row[f"bn{i+1}"] = qa[i] if i < len(qa) else None
                            row[f"rn{i+1}"] = qb[i] if i < len(qb) else None
                            for key, short in (("kills", "k"), ("deaths", "d"), ("assists", "a")):
                                va, vb = g.get(key + a, []), g.get(key + b, [])
                                row[f"b{short}{i+1}"] = va[i] if i < len(va) else None
                                row[f"r{short}{i+1}"] = vb[i] if i < len(vb) else None
                        row["gamelength"] = g.get("length")
                        rows.append(row)
                else:
                    # 只有比分：按比分展开成若干局（无 BP）
                    for gi in range(m["score1"] + m["score2"]):
                        win1 = gi < m["score1"]
                        rows.append(dict(base, game=gi + 1, blue=m["team1"], red=m["team2"], blue_win=int(win1)))
                cnt += 1
        print(f"[{n+1}/{len(roots)}] {root}: {cnt} 场系列赛")
    df = pd.DataFrame(rows)
    return df


def build():
    df = scrape()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False, compression="gzip")
    print("保存", OUT, len(df))


if __name__ == "__main__":
    build()
