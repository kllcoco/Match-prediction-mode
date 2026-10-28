"""把两个游戏的数据转成评分引擎需要的统一格式，并标记哪些比赛在严格模式下要屏蔽。"""
import numpy as np
import pandas as pd

from .names import norm

# ---------------- LOL ----------------
# 赛区统一（改名/合并的联赛视为同一赛区）
LOL_REGION = {
    "NA LCS": "LCS", "LCS": "LCS", "LTA N": "LCS", "LTA": "LCS",
    "EU LCS": "LEC", "LEC": "LEC",
    "OGN": "LCK", "LCK": "LCK", "LMS": "PCS", "PCS": "PCS", "LCP": "PCS",
    "LTA S": "CBLOL", "CBLOL": "CBLOL", "GPL": "GPL", "LPL": "LPL", "VCS": "VCS",
    "LJL": "LJL", "TCL": "TCL", "LCL": "LCL", "OPL": "OPL", "LCO": "OPL", "LLA": "LLA",
    "CLS": "LLA", "LLN": "LLA",
}
# 次级联赛：队伍挂靠到所属大区
LOL_SUB = {"LDL": "LPL", "LSPL": "LPL", "LCKC": "LCK", "CK": "LCK", "NACL": "LCS", "NA CS": "LCS",
           "EU CS": "LEC", "EM": "LEC", "EUM": "LEC", "CBLOLA": "CBLOL", "LJLA": "LJL", "LJLCS": "LJL"}
# Riot 官方国际大赛（严格模式屏蔽）
LOL_BIG = {"WLDs", "MSI", "FST", "MSC"}


BAD_NAMES = {"unknown player", "unknown", "tbd", "n/a", "na", "-", "?", "player", "sub", "substitute"}


def _valid_player(x):
    return isinstance(x, str) and x.strip() and x.strip().lower() not in BAD_NAMES


def lol_frame(g: pd.DataFrame, strict=True) -> pd.DataFrame:
    df = pd.DataFrame({"date": g.date, "t1": g.blue.map(norm), "t2": g.red.map(norm),
                       "win1": g.blue_win.astype(int), "side": 1.0, "map": None,
                       "event": g.event, "league_raw": g.league})
    lg = g.league.map(lambda x: LOL_REGION.get(x) or LOL_SUB.get(x))
    df["league"] = lg
    df["domestic"] = lg.notna()
    df["big"] = g.league.isin(LOL_BIG).astype(int)
    # 校准集：主要赛区的国内季后赛（和世界赛淘汰赛最像，但不是大赛）
    df["cal"] = ((pd.to_numeric(g.playoffs, errors="coerce").fillna(0) > 0) & lg.isin(
        ["LCK", "LPL", "LEC", "LCS", "PCS"]) & (g.league.map(lambda x: x in LOL_REGION))).astype(int)
    df["skip"] = df.big if strict else 0
    for s, col in (("b", "p1"), ("r", "p2")):
        names = g[[f"{s}n{i}" for i in range(1, 6)]].values.tolist()
        df[col] = [[f"lol:{str(x).lower().strip()}" for x in r if _valid_player(x)] or None for r in names]
    # 5 人都有名字才算（否则当作只知道队伍）
    df["p1"] = [r if r and len(r) == 5 else None for r in df.p1]
    df["p2"] = [r if r and len(r) == 5 else None for r in df.p2]
    # 每个选手本局表现 (K, D, A, 伤害)，按上野中下辅顺序
    def stats(sd):
        cols = [[f"{sd}{x}{i}" for x in ("k", "d", "a", "dmg")] for i in range(1, 6)]
        if cols[0][0] not in g:
            return [None] * len(g)
        arr = [g[c].to_numpy(dtype=float, na_value=np.nan) for c in sum(cols, [])]
        out = []
        for j in range(len(g)):
            v = [arr[q][j] for q in range(20)]
            if any(np.isnan(v[q]) for q in (0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18)):
                out.append(None)
                continue
            out.append([tuple(None if np.isnan(x) else float(x) for x in v[4 * i:4 * i + 4]) for i in range(5)])
        return out
    df["st1"], df["st2"] = stats("b"), stats("r")
    df["gamelength"] = pd.to_numeric(g["gamelength"], errors="coerce").values if "gamelength" in g else np.nan
    for sd, col in (("b", "ts1"), ("r", "ts2")):
        cols = [f"{sd}{x}" for x in ("gold", "tow", "drag", "bar")]
        if cols[0] in g:
            v = g[cols].apply(pd.to_numeric, errors="coerce").values
            df[col] = [tuple(r) if not np.isnan(r).any() else None for r in v]
        else:
            df[col] = None
    # 本局双方英雄（用来算英雄池深度）
    for sd, col in (("b", "c1"), ("r", "c2")):
        cc = g[[f"{sd}p{i}" for i in range(1, 6)]].values.tolist()
        df[col] = [[x for x in r if isinstance(x, str)] or None for r in cc]
    df["gnum"] = pd.to_numeric(g["game"], errors="coerce").fillna(1).clip(1, 5).values
    df["fearless"] = fearless_flags(g).values
    df = df[(df.t1 != "") & (df.t2 != "") & (df.t1 != df.t2)]
    return df.sort_values("date", kind="stable").reset_index(drop=True)


def fearless_flags(g: pd.DataFrame) -> pd.Series:
    """从数据里识别「无畏征召」赛事：一个赛事里多局系列赛从不重复选同一英雄 -> 无畏征召。
    数据不够判断的赛事，按同年多数赛事的情况。"""
    cols = [f"{s}p{i}" for s in "br" for i in range(1, 6)]
    key = g.event.astype(str) + "|" + g.date.dt.date.astype(str) + "|" + \
        [ "|".join(sorted((str(a), str(b)))) for a, b in zip(g.blue, g.red)]
    rep = {}
    for k, s in g[cols].groupby(key):
        if len(s) < 2:
            continue
        seen = [c for row in s.values for c in row if isinstance(c, str)]
        if len(seen) >= 20:
            ev = k.split("|")[0]
            rep.setdefault(ev, []).append(int(len(seen) != len(set(seen))))
    ev_flag = {e: int(np.mean(v) < 0.05) for e, v in rep.items() if len(v) >= 3}
    year_flag = {}
    for e, f in ev_flag.items():
        y = g.loc[g.event.astype(str) == e, "year"]
        if len(y):
            year_flag.setdefault(int(y.iloc[0]), []).append(f)
    year_major = {y: int(np.mean(v) >= 0.5) for y, v in year_flag.items()}
    return pd.Series([ev_flag.get(str(e), year_major.get(int(y), 0) if y == y else 0)
                      for e, y in zip(g.event, g.year)], index=g.index)


# ---------------- CS ----------------
def cs_frame(m: pd.DataFrame, strict=True) -> pd.DataFrame:
    df = pd.DataFrame({"date": m.date, "t1": m.team1.map(lambda x: norm(x, "cs")), "t2": m.team2.map(lambda x: norm(x, "cs")),
                       "win1": m.win1.astype(int), "side": 0.0,
                       "map": m["map"].where(m["map"].notna() & (m["map"] != ""), None),
                       "event": m.event, "league": None, "domestic": False,
                       "match_id": m.match_id, "best_of": m.best_of})
    for c, col in (("roster1", "p1"), ("roster2", "p2")):
        df[col] = [[f"cs:{x.lower()}" for x in r.split("|")] if isinstance(r, str) and r.count("|") >= 3 else None
                   for r in (m[c] if c in m else [None] * len(m))]
    for c, col in (("stats1", "cst1"), ("stats2", "cst2")):
        df[col] = [[tuple(float(v) for v in x.split(",")) for x in r.split("|")] if isinstance(r, str) else None
                   for r in (m[c] if c in m else [None] * len(m))]
    df["big"] = m.major.astype(int)
    from .tune import TIER1
    pat = TIER1["cs"].replace("^(", "^(?:")
    df["cal"] = (m.event.fillna("").str.contains(pat, regex=True)
                 & ~m.event.fillna("").str.contains("Qualif|Open|Closed|Showmatch|Minor|RMR", regex=True)).astype(int)
    df["skip"] = df.big if strict else 0
    df = df[(df.t1 != "") & (df.t2 != "") & (df.t1 != df.t2)]
    return df.sort_values("date", kind="stable").reset_index(drop=True)
