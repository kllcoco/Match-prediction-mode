"""把 LOL 原始数据整理成统一的「一局一行」表 data/processed/lol_games.csv.gz

列: date, year, league, event, intl(国际大赛标记), playoffs, patch, blue, red, blue_win,
    bp1..bp5 / rp1..rp5 (蓝/红方英雄，按上野中下辅), bb1..bb5 / rb1..rb5 (禁用)
"""
import re

import pandas as pd

from .net import DATA
from .sources import RAW

OUT = DATA / "processed" / "lol_games.csv.gz"
POS = ["top", "jng", "mid", "bot", "sup"]

# Riot 官方国际大赛：严格模式下训练时全部屏蔽
RIOT_INTL = {"WLDs", "MSI", "FST", "MSC"}


def _read_oe(path):
    cols = ["gameid", "league", "year", "split", "playoffs", "date", "game", "patch", "side",
            "position", "playername", "teamname", "champion", "ban1", "ban2", "ban3", "ban4", "ban5", "result",
            "gamelength", "kills", "deaths", "assists", "damagetochampions",
            "totalgold", "towers", "dragons", "barons"]
    df = pd.read_csv(path, usecols=cols, low_memory=False, dtype=str)
    return df


def oe_games() -> pd.DataFrame:
    parts = [_read_oe(RAW / "oe_2014_2023.csv")]
    parts[0] = parts[0][~parts[0].year.isin(["2024", "2025"])]
    parts += [_read_oe(RAW / f"oe_{y}.csv") for y in (2024, 2025)]
    df = pd.concat(parts, ignore_index=True)
    df = df.dropna(subset=["teamname", "side"])
    team = df[df.position == "team"].copy()
    ply = df[df.position.isin(POS)].copy()

    # 每局两行(蓝/红) -> 一行
    team["result"] = pd.to_numeric(team.result, errors="coerce")
    t = team.set_index(["gameid", "side"])
    t = t[~t.index.duplicated()]
    blue = t.xs("Blue", level="side")
    red = t.xs("Red", level="side")
    g = blue[["league", "year", "split", "playoffs", "date", "game", "patch", "teamname", "result"]].rename(
        columns={"teamname": "blue", "result": "blue_win"})
    g = g.join(red[["teamname"]].rename(columns={"teamname": "red"}), how="inner")
    for s, src in (("b", blue), ("r", red)):
        for i in range(1, 6):
            g[f"{s}b{i}"] = src[f"ban{i}"]
    ply["pi"] = ply.position.map({p: i + 1 for i, p in enumerate(POS)})
    pk = ply.drop_duplicates(["gameid", "side", "pi"]).pivot_table(
        index="gameid", columns=["side", "pi"], values="champion", aggfunc="first")
    for s, side in (("b", "Blue"), ("r", "Red")):
        for i in range(1, 6):
            col = (side, i)
            g[f"{s}p{i}"] = pk[col] if col in pk.columns else None
    pn = ply.drop_duplicates(["gameid", "side", "pi"]).pivot_table(
        index="gameid", columns=["side", "pi"], values="playername", aggfunc="first")
    for s, side in (("b", "Blue"), ("r", "Red")):
        for i in range(1, 6):
            col = (side, i)
            g[f"{s}n{i}"] = pn[col] if col in pn.columns else None
    # 选手表现：击杀/死亡/助攻/对英雄伤害（训练和联网搜索都拿得到的数据）
    for col, short in (("kills", "k"), ("deaths", "d"), ("assists", "a"), ("damagetochampions", "dmg")):
        ply[col] = pd.to_numeric(ply[col], errors="coerce")
        pv = ply.drop_duplicates(["gameid", "side", "pi"]).pivot_table(
            index="gameid", columns=["side", "pi"], values=col, aggfunc="first")
        for s, side in (("b", "Blue"), ("r", "Red")):
            for i in range(1, 6):
                g[f"{s}{short}{i}"] = pv[(side, i)] if (side, i) in pv.columns else None
    g["gamelength"] = pd.to_numeric(blue["gamelength"], errors="coerce")
    # 团队局内数据：经济、推塔、小龙、大龙（联网的单场页也有同样的字段）
    for col, short in (("totalgold", "gold"), ("towers", "tow"), ("dragons", "drag"), ("barons", "bar")):
        g["b" + short] = pd.to_numeric(blue[col], errors="coerce")
        g["r" + short] = pd.to_numeric(red[col], errors="coerce")
    g = g.reset_index()
    g["date"] = pd.to_datetime(g.date, errors="coerce")
    g = g.dropna(subset=["date", "blue_win"])
    g["blue_win"] = g.blue_win.astype(int)
    g["year"] = g.date.dt.year
    g["event"] = g.league + " " + g.year.astype(str) + " " + g.split.fillna("")
    g["intl"] = g.league.isin(RIOT_INTL).astype(int)
    g["source"] = "oe"
    return g


def liquipedia_games() -> pd.DataFrame:
    """2011-2013 年（OE 之前）从 Liquipedia 抓到的比赛，见 esports/lol_early.py"""
    p = DATA / "processed" / "lol_early_games.csv.gz"
    return pd.read_csv(p, parse_dates=["date"]) if p.exists() else pd.DataFrame()


def keep_cols():
    return ["date", "year", "league", "event", "intl", "playoffs", "patch", "game", "blue", "red", "blue_win",
            *[f"bp{i}" for i in range(1, 6)], *[f"rp{i}" for i in range(1, 6)],
            *[f"bb{i}" for i in range(1, 6)], *[f"rb{i}" for i in range(1, 6)],
            *[f"bn{i}" for i in range(1, 6)], *[f"rn{i}" for i in range(1, 6)],
            *[f"{s}{x}{i}" for s in "br" for x in ("k", "d", "a", "dmg") for i in range(1, 6)], "gamelength",
            *[f"{s}{x}" for s in "br" for x in ("gold", "tow", "drag", "bar")], "source"]


def build():
    g = oe_games()
    early = liquipedia_games()
    if len(early):
        early = early[early.year <= 2015]
        early["patch"] = None
    g = g[g.year >= 2016]  # 2015 年及以前用 Liquipedia（OE 早期缺 LCK/LPL）
    live = DATA / "processed" / "lol_live.csv.gz"
    if live.exists():  # 联网更新拿到的新比赛（只要基础数据之后的）
        lv = pd.read_csv(live, low_memory=False)
        lv["date"] = pd.to_datetime(lv.date, format="mixed")
        lv = lv[lv.date > g.date.max()]
        # 同一场比赛可能出现在赛事主页和子页面里，按「时间+双方+第几局」去重
        lv = lv.sort_values("date").drop_duplicates(subset=["date", "blue", "red", "game"], keep="last")
        print("并入联网新数据:", len(lv), "局")
        g = pd.concat([g, lv], ignore_index=True)
    g = pd.concat([early, g], ignore_index=True)
    for c in keep_cols():
        if c not in g.columns:
            g[c] = None
    # 英雄名统一：Liquipedia 是小写/缩写（aurora、ez），统一成 OE 的标准写法
    from .draft import ChampNames
    champ_cols = [f"{s}{x}{i}" for s in "br" for x in "pb" for i in range(1, 6)]
    oe = g[g.source == "oe"]
    cn = ChampNames(pd.unique(oe[champ_cols].values.ravel()))
    lp = g.source != "oe"
    for c in champ_cols:
        g[c] = g[c].astype(object)
        g.loc[lp, c] = g.loc[lp, c].map(lambda x: cn(x) if isinstance(x, str) else None)
    keep = keep_cols()
    g = g[keep].sort_values("date").reset_index(drop=True)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    g.to_csv(OUT, index=False, compression="gzip")
    print("LOL 局数:", len(g), "范围", g.date.min(), "->", g.date.max())
    return g


def load() -> pd.DataFrame:
    g = pd.read_csv(OUT, low_memory=False)
    g["date"] = pd.to_datetime(g.date, format="mixed")
    return g


if __name__ == "__main__":
    build()
