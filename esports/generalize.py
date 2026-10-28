"""泛化测试：模型学到的是「怎么看数据」，还是「记住了谁强」？

做法：用 Y 年之前的比赛训练，测 Y 年的四大赛区比赛（每年滚动，2017-2025）。
把测试比赛按「新面孔数」分组（首发里职业场次 < 20 的人数），比较三种模型：
  认名字：只用 Elo / 状态 / 经验（靠记住队伍和选手的历史胜负）
  看数据：只用选手表现 + 团队局内数据 + 赛区（不需要认识这个人，搜到他的数据就能算）
  结合：两者一起
"""
import numpy as np
import pandas as pd

from .backtest import load_frame, BEST
from .engine import Logistic, PERF, TEAM_IG, Rater, logloss, run

MAIN = {"LCK", "LPL", "LEC", "LCS", "EU LCS", "NA LCS"}
SETS = {
    "认名字(Elo)": ["elo", "form", "exp", "side"],
    "看数据(表现)": TEAM_IG + PERF + ["side"],
    "结合": ["elo", "form", "exp", "side"] + TEAM_IG + PERF,
    "结合+自适应": ["elo", "form", "exp", "side"] + TEAM_IG + PERF
                  + [k + "_g" for k in ["elo", "form", "exp"] + TEAM_IG + PERF],
}


def add_gate(h):
    """新人比例 g∈[0,1]：每个特征再配一个「× g」的版本，让模型学会新人多时该信谁。"""
    g = (h.nnew / 5).clip(0, 1)
    for k in ["elo", "form", "exp"] + TEAM_IG + PERF:
        h[k + "_g"] = h[k] * g
    return h


def main():
    f = load_frame("lol", strict=True)
    h = run(f, Rater(BEST["lol"], use_league=False))
    h["year"] = h.date.dt.year
    h = add_gate(h)  # 与 engine 内置的 *_g 特征一致
    rows = []
    for y in range(2017, 2026):
        tr = h[(h.year < y) & (h.year >= 2016)]
        te = h[(h.year == y) & h.league_raw.isin(MAIN)]
        for name, fs in SETS.items():
            X = tr[fs].values
            lr = Logistic(fs, l2=1e-3).fit(np.vstack([X, -X]), np.r_[tr.y.values, 1 - tr.y.values])
            p = lr.predict(te[fs].values)
            for grp, mask in (("全部", te.nnew >= 0), ("新面孔≥2人", te.nnew >= 2), ("新面孔≥3人", te.nnew >= 3)):
                if mask.sum() < 20:
                    continue
                rows.append(dict(year=y, model=name, group=grp, n=int(mask.sum()),
                                 acc=float(np.mean((p[mask] >= .5) == (te.y.values[mask] == 1))),
                                 ll=logloss(p[mask], te.y.values[mask])))
    df = pd.DataFrame(rows)
    agg = df.groupby(["group", "model"]).apply(
        lambda d: pd.Series(dict(局数=d.n.sum(), 命中率=np.average(d.acc, weights=d.n), 对数损失=np.average(d.ll, weights=d.n))))
    print(agg.round(3).to_string())
    return df, agg


if __name__ == "__main__":
    main()
