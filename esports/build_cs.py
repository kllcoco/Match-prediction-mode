"""把 CS 原始数据整理成「一张地图一行」的统一表 data/processed/cs_maps.csv.gz

列: date, event, match_id, best_of, team1, team2, map, win1, major(Major 正赛标记), source
另有 veto 表 cs_vetoes.csv.gz（2015-2020，每场 BO3 的禁/选图）。
"""
import json
import re

import pandas as pd

from .net import DATA
from .sources import RAW

OUT = DATA / "processed" / "cs_maps.csv.gz"
VETO = DATA / "processed" / "cs_vetoes.csv.gz"
MAJORS_FILE = DATA / "answers" / "cs_majors.json"

# 各数据源负责的时间段（避免重复）
CUT_MATEUS = "2015-11-03"
CUT_NAFIS = "2020-03-19"
CUT_EKTARR = "2023-01-01"


def majors():
    return json.loads(MAJORS_FILE.read_text(encoding="utf-8"))


def is_major_event(name: str, date, mj) -> int:
    """Major 正赛（含挑战者/传奇阶段）。Minor/RMR/预选赛不算。"""
    if isinstance(name, str) and name:
        low = name.lower()
        if re.search(r"minor|rmr|qualif|road to|showmatch|all-star|закрыт|открыт", low):
            return 0
        for m in mj:
            if any(k.lower() == low or (k.lower() in low and "stage" in low) for k in m["event_names"]):
                return 1
        return 0
    # 无赛事名的数据：按 Major 日期窗口判断
    for m in mj:
        if m["start"] <= str(date)[:10] <= m["end"]:
            return 1
    return 0


def camilo():
    c = pd.DataFrame(json.load(open(RAW / "cs_2013_2020/csgo_matches_50k.json")))
    c = c[c.date < CUT_MATEUS]
    rows = []
    for i, r in c.iterrows():
        s1, s2 = int(r.team1_score), int(r.team2_score)
        if s1 == s2:
            continue
        mid = f"c{i}"
        if max(s1, s2) > 3:  # BO1 比分是回合数
            rows.append((r.date, "", mid, 1, r.team1, r.team2, "", int(s1 > s2)))
        else:
            bo = 2 * max(s1, s2) - 1
            for k in range(s1):
                rows.append((r.date, "", mid, bo, r.team1, r.team2, "", 1))
            for k in range(s2):
                rows.append((r.date, "", mid, bo, r.team1, r.team2, "", 0))
    df = pd.DataFrame(rows, columns=["date", "event", "match_id", "best_of", "team1", "team2", "map", "win1"])
    df["source"] = "camilo"
    return df


def mateus():
    r = pd.read_csv(RAW / "cs_2015_2020/results.csv")
    ev = pd.read_csv(RAW / "cs_2015_2020/players.csv", usecols=["event_id", "event_name"]).drop_duplicates("event_id")
    r = r.merge(ev, on="event_id", how="left")
    p = pd.read_csv(RAW / "cs_2015_2020/picks.csv")
    bo = pd.to_numeric(p.set_index("match_id").best_of.astype(str).str.extract(r"(\d)")[0], errors="coerce").to_dict()
    df = pd.DataFrame(dict(date=r.date, event=r.event_name.fillna(""), match_id="m" + r.match_id.astype(str),
                           best_of=r.match_id.map(bo).fillna(1).astype(int), team1=r.team_1, team2=r.team_2,
                           map=r._map, win1=(r.map_winner == 1).astype(int)))
    pl = pd.read_csv(RAW / "cs_2015_2020/players.csv", usecols=["player_name", "team", "match_id"])
    ros = pl.groupby(["match_id", "team"]).player_name.apply(lambda x: "|".join(sorted(map(str, x)))).to_dict()
    df["roster1"] = [ros.get((mid, t)) for mid, t in zip(r.match_id, r.team_1)]
    df["roster2"] = [ros.get((mid, t)) for mid, t in zip(r.match_id, r.team_2)]
    df = df[df["map"] != "Default"]
    df["source"] = "mateus"
    p = p.merge(ev, on="event_id", how="left")
    return df, p


def nafis():
    n = pd.read_csv(RAW / "cs_2020_2022/CSGO_match_result_until_2022.csv")
    n["date"] = pd.to_datetime(n.match_time, unit="ms")
    n = n[n.date >= CUT_NAFIS]
    ros = n.groupby(["match_url", "team"]).player_name.apply(lambda x: "|".join(sorted(set(map(str, x))))).to_dict()
    n = n.drop_duplicates(["match_url", "team", "map_name"])
    n["t1"] = n[["team", "opponent"]].min(axis=1)
    n["t2"] = n[["team", "opponent"]].max(axis=1)
    n = n[n.team == n.t1]  # 每张图只保留一个视角
    bo = n.match_tag.str.extract(r"bo(\d)")[0].fillna(1).astype(int)
    df = pd.DataFrame(dict(date=n.date.dt.strftime("%Y-%m-%d"), event=n.event, match_id="n" + n.match_url.str.extract(r"matches/(\d+)")[0],
                           best_of=bo, team1=n.team, team2=n.opponent, map=n.map_name, win1=n.map_won.astype(int)))
    df["roster1"] = [ros.get((u, t)) for u, t in zip(n.match_url, n.team)]
    df["roster2"] = [ros.get((u, t)) for u, t in zip(n.match_url, n.opponent)]
    df["source"] = "nafis"
    return df


def ektarr():
    e = pd.read_csv(RAW / "cs_2023_2026/cs2_all_tiers_games.csv",
                    usecols=["match_id", "tournament", "team1", "team2", "is_total", "bestOf", "score1_game",
                             "score2_game", "map_name", "datetime", "score1_match", "score2_match",
                             *[f"team{t}_player{i}" for t in (1, 2) for i in range(1, 6)]])
    for t in (1, 2):
        e[f"roster{t}"] = ["|".join(sorted(str(x).split(" (")[0] for x in row if isinstance(x, str))) or None
                           for row in e[[f"team{t}_player{i}" for i in range(1, 6)]].values]
    e = e[e.datetime >= CUT_EKTARR]
    maps = e[~e.is_total].dropna(subset=["score1_game", "score2_game"])
    maps = maps[maps.score1_game != maps.score2_game]
    df = pd.DataFrame(dict(date=maps.datetime.str[:10], event=maps.tournament, match_id="e" + maps.match_id.astype(str),
                           best_of=maps.bestOf, team1=maps.team1, team2=maps.team2, map=maps.map_name,
                           win1=(maps.score1_game > maps.score2_game).astype(int),
                           roster1=maps.roster1, roster2=maps.roster2))
    # 只有总比分、没有地图明细的系列赛：按比分展开
    tot = e[e.is_total & ~e.match_id.isin(maps.match_id)].dropna(subset=["score1_match", "score2_match"])
    rows = []
    for _, r in tot.iterrows():
        for k in range(int(r.score1_match or 0)):
            rows.append((r.datetime[:10], r.tournament, f"e{r.match_id}", r.bestOf, r.team1, r.team2, "", 1, r.roster1, r.roster2))
        for k in range(int(r.score2_match or 0)):
            rows.append((r.datetime[:10], r.tournament, f"e{r.match_id}", r.bestOf, r.team1, r.team2, "", 0, r.roster1, r.roster2))
    df = pd.concat([df, pd.DataFrame(rows, columns=df.columns)])
    df["source"] = "ektarr"
    return df


def liquipedia_extra(after):
    """联网更新拿到的新比赛（只要 ektarr 数据之后的）"""
    p = DATA / "processed" / "cs_live.csv.gz"
    if not p.exists():
        return pd.DataFrame()
    lv = pd.read_csv(p)
    lv = lv[lv.date.astype(str).str[:10] > str(after)[:10]]
    print("并入联网新数据:", len(lv), "张图")
    return lv


def build():
    mj = majors()
    m, picks = mateus()
    ek = ektarr()
    df = pd.concat([camilo(), m, nafis(), ek, liquipedia_extra(ek.date.max())], ignore_index=True)
    df["date"] = pd.to_datetime(df.date.astype(str).str[:10])
    df["event"] = df.event.fillna("")
    df["major"] = [is_major_event(e, d, mj) for e, d in zip(df.event, df.date)]
    df = df.sort_values(["date", "match_id"]).reset_index(drop=True)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False, compression="gzip")
    picks.to_csv(VETO, index=False, compression="gzip")
    print("CS 地图数:", len(df), df.date.min(), "->", df.date.max(), "Major 地图数:", df.major.sum())
    return df


def load():
    return pd.read_csv(OUT, parse_dates=["date"], low_memory=False)


if __name__ == "__main__":
    build()
