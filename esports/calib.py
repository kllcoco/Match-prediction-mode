"""跨赛区校准（LOL）：国内比赛学到的「实力分差 → 胜率」用在跨赛区时会过度自信。

用「非 Riot 跨赛区比赛」（IEM、KeSPA 杯、德玛西亚杯、EWC、亚运会…）当验证集：
在每个赛事开打前训练模型，记录「赛区内实力差」和「赛区水位差」，再看实际胜负。
预测某年世界赛时，只用那之前的这类比赛学两个权重（不看世界赛 / MSI）。
"""
import numpy as np
import pandas as pd

from .engine import Logistic
from .net import DATA

OUT = DATA / "processed" / "lol_cross_calib.csv"
MAIN = {"LCK", "LPL", "LEC", "LCS", "PCS", "VCS"}
DEFAULT_W = (0.6, 0.8, 0.0)


def build():
    from . import backtest as B
    f = B.load_frame("lol")
    ff = f[f.skip == 0].copy()
    ff["y"] = ff.date.dt.year
    long = pd.concat([ff[["t1", "y", "league"]].rename(columns={"t1": "t"}),
                      ff[["t2", "y", "league"]].rename(columns={"t2": "t"})]).dropna()
    home = long.groupby(["t", "y"]).league.agg(lambda x: x.mode().iloc[0]).to_dict()
    ff["h1"] = [home.get((t, y)) for t, y in zip(ff.t1, ff.y)]
    ff["h2"] = [home.get((t, y)) for t, y in zip(ff.t2, ff.y)]
    c = ff[ff.h1.isin(MAIN) & ff.h2.isin(MAIN) & (ff.h1 != ff.h2)].copy()
    c["ev"] = c.league_raw + c.date.dt.strftime("%Y-%m")
    rows = []
    for ev, g in c.groupby("ev"):
        m = B.Model("lol", f, g.date.min().normalize(), cross=False)
        s = m.rater.s
        for _, r in g.iterrows():
            S1 = m.rater.strength(r.t1, league="__none")[0]
            S2 = m.rater.strength(r.t2, league="__none")[0]
            rows.append(dict(date=r.date, event=ev, within=(S1 - S2) / 400,
                             league=(s.league.get(r.h1, 0) - s.league.get(r.h2, 0)) / 400,
                             perfz=m.perf_z(r.t1, r.t2), y=r.win1))
    df = pd.DataFrame(rows)
    df.to_csv(OUT, index=False)
    print("跨赛区校准样本:", len(df))
    return df


def weights(cutoff, min_rows=40):
    """只用 cutoff 之前的跨赛区比赛学权重。"""
    if not OUT.exists():
        return DEFAULT_W
    df = pd.read_csv(OUT, parse_dates=["date"])
    df = df[df.date < cutoff]
    if len(df) < min_rows:
        return DEFAULT_W
    cols = ["within", "league", "perfz"] if "perfz" in df else ["within", "league"]
    X = df[cols].values
    y = df.y.values
    lr = Logistic(cols, l2=1e-2).fit(np.vstack([X, -X]), np.r_[y, 1 - y])
    return tuple(float(v) for v in lr.w)


if __name__ == "__main__":
    build()
