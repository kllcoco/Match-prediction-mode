"""「标准答案」：每年世界赛 / 每届 Major 的淘汰赛对阵和结果（来自 Liquipedia）。

这些只用于【出题】(给模型 8 强对阵) 和【判卷】(算准确率)，不会进训练集。
输出 data/answers/lol_worlds.json 和 data/answers/cs_majors.json
"""
import json
import re

from . import liquipedia as L
from .net import DATA

ANS = DATA / "answers"

# (Liquipedia 页面, 在各数据集里出现的赛事名关键字)
CS_MAJORS = [
    ("DreamHack/2013/Winter", ["DreamHack Winter 2013"]),
    ("ESL/Major Series One/2014/Katowice", ["EMS One Katowice 2014"]),
    ("ESL/One/2014/Cologne", ["ESL One Cologne 2014"]),
    ("DreamHack/2014/Winter", ["DreamHack Winter 2014"]),
    ("ESL/One/2015/Katowice", ["ESL One Katowice 2015"]),
    ("ESL/One/2015/Cologne", ["ESL One Cologne 2015"]),
    ("DreamHack/2015/Cluj-Napoca", ["DreamHack Open Cluj-Napoca 2015"]),
    ("MLG/2016/Columbus", ["MLG Columbus 2016"]),
    ("ESL/One/2016/Cologne", ["ESL One Cologne 2016"]),
    ("ELEAGUE/2017/Major", ["ELEAGUE Major 2017"]),
    ("PGL/2017/Krakow", ["PGL Major Krakow 2017"]),
    ("ELEAGUE/2018/Major", ["ELEAGUE Major 2018"]),
    ("FACEIT/2018/Major", ["FACEIT Major 2018"]),
    ("Intel Extreme Masters/Season XIII/World Championship", ["IEM Katowice 2019"]),
    ("StarLadder/2019/Major", ["StarLadder Major Berlin 2019"]),
    ("PGL/2021/Stockholm", ["PGL Major Stockholm 2021"]),
    ("PGL/2022/Antwerp", ["PGL Major Antwerp 2022"]),
    ("Intel Extreme Masters/2022/Rio", ["IEM Rio Major 2022"]),
    ("BLAST/Major/2023/Paris", ["BLAST.tv Paris Major 2023"]),
    ("PGL/2024/Copenhagen", ["PGL Major Copenhagen 2024"]),
    ("Perfect World/Major/2024/Shanghai", ["Perfect World Shanghai Major 2024"]),
    ("BLAST/Major/2025/Austin", ["BLAST.tv Austin Major 2025"]),
    ("StarLadder/2025/Major", ["StarLadder Budapest Major 2025"]),
    ("Intel Extreme Masters/2026/Cologne", ["IEM Cologne Major 2026"]),
]


def _infobox(text, key):
    m = re.search(rf"\|\s*{key}\s*=\s*(\d{{4}}-\d{{2}}-\d{{2}})", text or "")
    return m.group(1) if m else None


def _subpages(root, wiki):
    from . import net
    data = net.get(L.API.format(wiki=wiki), dict(action="query", list="allpages", apprefix=root + "/",
                                                 aplimit=100, format="json"), gap=L.GAP, as_json=True)
    return [p["title"] for p in data["query"]["allpages"]]


def knockout(root, wiki):
    """在赛事页及子页面里找 8 队单败淘汰对阵（R1 4 场, R2 2 场, R3M1 决赛）。"""
    pages = [root] + [p for p in _subpages(root, wiki) if not re.search(
        r"Qualif|/Open|/Closed|Minor|RMR|/Europe|/Americas|/Asia|/North America|/South America|/CIS|"
        r"/Oceania|/China|/Middle East|Last Chance|Play-in|Play-In|Showmatch|Statistics", p)]
    # 淘汰赛常见子页面名优先
    pages.sort(key=lambda p: 0 if re.search(r"Playoff|Knockout|Champions_Stage|Champions Stage|Main Event", p) else 1)
    root_text = L.wikitext(root, wiki) or ""
    info = dict(start=_infobox(root_text, "sdate"), end=_infobox(root_text, "edate"))
    for p in pages:
        ms = L.parse_matches(L.wikitext(p, wiki) or "")
        rounds = {m["round"]: m for m in ms if re.fullmatch(r"R[123]M\d", m["round"])}
        if all(k in rounds for k in ("R1M1", "R1M2", "R1M3", "R1M4", "R2M1", "R2M2", "R3M1")):
            series = []
            for k in ("R1M1", "R1M2", "R1M3", "R1M4", "R2M1", "R2M2", "R3M1"):
                m = rounds[k]
                series.append(dict(round=k, team1=m["team1"], team2=m["team2"], score1=m["score1"],
                                   score2=m["score2"], winner=m["team1"] if m["winner"] == 1 else m["team2"],
                                   date=m["date"], games=m["games"]))
            info.update(page=p, format="se8", series=series)
            return info
    # 找不到标准 8 强（如 S1 双败赛制）：返回全部系列赛
    allm = []
    for p in pages:
        if re.search(r"Playoff", p) or p == root:
            allm += L.parse_matches(L.wikitext(p, wiki) or "")
    info.update(page=root, format="custom", series=[dict(
        round=m["round"], team1=m["team1"], team2=m["team2"], score1=m["score1"], score2=m["score2"],
        winner=m["team1"] if m["winner"] == 1 else m["team2"], date=m["date"], games=m["games"]) for m in allm])
    return info


def build_cs():
    out = []
    for page, names in CS_MAJORS:
        k = knockout(page, "counterstrike")
        k.update(name=names[0], event_names=names)
        out.append(k)
        print(names[0], k["start"], k["end"], k["format"], [s["winner"] for s in k["series"]][-1:] if k["series"] else None)
    ANS.mkdir(parents=True, exist_ok=True)
    (ANS / "cs_majors.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")


def build_lol():
    out = []
    for y in range(2011, 2026):
        k = knockout(f"World Championship/{y}", "leagueoflegends")
        k.update(name=f"S{y - 2010} {y} 世界赛", year=y, season=y - 2010)
        out.append(k)
        print(k["name"], k["start"], k["end"], k["format"], k["series"][-1]["winner"] if k["series"] else None)
    ANS.mkdir(parents=True, exist_ok=True)
    (ANS / "lol_worlds.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")


def load(game):
    return json.loads((ANS / ("lol_worlds.json" if game == "lol" else "cs_majors.json")).read_text(encoding="utf-8"))


if __name__ == "__main__":
    import sys
    if "cs" in sys.argv:
        build_cs()
    else:
        build_lol()
        fix_recent_lol()


def lol_from_oe(year):
    """2022 年起 Liquipedia 比分是动态加载的，改从 OE 数据反推淘汰赛（最后 7 个系列赛）。"""
    from . import build_lol
    from .names import norm
    g = build_lol.load()
    w = g[(g.league == "WLDs") & (g.year == year)].sort_values("date")
    series = []
    for _, r in w.iterrows():
        pair = frozenset((r.blue, r.red))
        win = r.blue if r.blue_win else r.red
        if series and series[-1]["pair"] == pair and (r.date - series[-1]["last"]).days <= 1:
            s = series[-1]
        else:
            s = dict(pair=pair, wins={}, last=r.date, first=r.date)
            series.append(s)
        s["wins"][win] = s["wins"].get(win, 0) + 1
        s["last"] = r.date
    ko = series[-7:]
    out = []
    for s in ko:
        t1, t2 = sorted(s["pair"])
        out.append(dict(team1=t1, team2=t2, score1=s["wins"].get(t1, 0), score2=s["wins"].get(t2, 0),
                        winner=max(s["wins"], key=s["wins"].get), date=str(s["first"]), games=[]))
    qf, sf, f = out[:4], out[4:6], out[6]
    # 按半区重排八强：半决赛 1 的两支队来自哪两场八强
    def src(t):
        return next(i for i, q in enumerate(qf) if t in (q["team1"], q["team2"]))
    order = [src(sf[0]["team1"]), src(sf[0]["team2"]), src(sf[1]["team1"]), src(sf[1]["team2"])]
    qf = [qf[i] for i in order]
    for k, s in zip(["R1M1", "R1M2", "R1M3", "R1M4", "R2M1", "R2M2", "R3M1"], qf + sf + [f]):
        s["round"] = k
    return dict(format="se8", series=qf + sf + [f], page="OE data")


def fix_recent_lol():
    data = load("lol")
    for ev in data:
        if ev["year"] >= 2022 and ev["format"] != "se8":
            ev.update(lol_from_oe(ev["year"]))
            print(ev["name"], [(s["round"], s["team1"], s["score1"], s["score2"], s["team2"]) for s in ev["series"]])
    (ANS / "lol_worlds.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
