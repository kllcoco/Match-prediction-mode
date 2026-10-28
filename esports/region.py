"""赛区水位模型（批量训练）：不看世界赛，也能估计赛区之间的实力差。

模型：  蓝方胜率的对数几率 = 蓝方优势 + 蓝方5人平均水平 - 红方5人平均水平 + 队伍默契差
        选手水平 = 他所属赛区的「水位」 + 个人偏差
个人偏差和队伍默契都有先验收缩（默认接近 0），而赛区水位没有收缩。
所以：一个在 A 赛区中游的选手转会到 B 赛区就称霸，模型最省力的解释就是「B 赛区水位更低」。
跨赛区的非 Riot 比赛（IEM、EWC、亚运会等）也会直接提供证据。
"""
from collections import Counter, defaultdict

import numpy as np
import pandas as pd

ELO_PER_LOGIT = 400 / np.log(10)


def fit(frame: pd.DataFrame, cutoff, window_days=730, half_life=365, sd_player=0.6, sd_team=0.4,
        sd_league=3.0, iters=400, lr=0.05, period_days=182, sd_walk=0.25):
    g = frame[(frame.date < cutoff) & (frame.date >= cutoff - pd.Timedelta(days=window_days)) & (frame.skip == 0)]
    g = g[g.league_raw.notna()]
    if len(g) < 200:
        return {}
    age = (cutoff - g.date).dt.days.values
    w = 0.5 ** (age / half_life)
    # 实体：有选手名就用选手，否则用「队伍」当作 5 个一样的人
    # 选手按「半年」分段：每段水平可以缓慢变化（随机游走），模拟成长/下滑
    per = ((cutoff - g.date).dt.days.values // period_days).astype(int) if period_days else np.zeros(len(g), int)
    ents_b, ents_r = [], []
    for p1, p2, t1, t2, k in zip(g.p1, g.p2, g.t1, g.t2, per):
        ents_b.append([f"{x}@{k}" for x in p1] if isinstance(p1, list) and p1 else [f"team:{t1}"])
        ents_r.append([f"{x}@{k}" for x in p2] if isinstance(p2, list) and p2 else [f"team:{t2}"])
    # 每个选手归属：他出场最多的联赛（原始联赛名，次级联赛单独算）
    cnt = defaultdict(Counter)
    for eb, er, lg in zip(ents_b, ents_r, g.league_raw):
        for e in eb + er:
            cnt[e][lg] += 1
    base = defaultdict(Counter)
    for e, c in cnt.items():
        base[e.split("@")[0]].update(c)
    ent_idx = {e: i for i, e in enumerate(cnt)}
    ent_lg = [base[e.split("@")[0]].most_common(1)[0][0] for e in cnt]
    # 相邻时间段的同一选手 -> 随机游走约束
    chain = []
    for e, i in ent_idx.items():
        if "@" in e:
            b, k = e.rsplit("@", 1)
            j = ent_idx.get(f"{b}@{int(k) + 1}")
            if j is not None:
                chain.append((i, j))
    chain = np.array(chain, dtype=int).reshape(-1, 2)
    leagues = sorted(set(ent_lg))
    lg_idx = {l: i for i, l in enumerate(leagues)}
    ent_lgi = np.array([lg_idx[l] for l in ent_lg])
    teams = sorted(set(g.t1) | set(g.t2))
    t_idx = {t: i for i, t in enumerate(teams)}
    n = len(g)
    # 稀疏设计：每局每方最多 5 个实体，权重 1/k
    rows, cols, vals = [], [], []
    for i, (eb, er) in enumerate(zip(ents_b, ents_r)):
        for e in eb:
            rows.append(i); cols.append(ent_idx[e]); vals.append(1 / len(eb))
        for e in er:
            rows.append(i); cols.append(ent_idx[e]); vals.append(-1 / len(er))
    rows, cols, vals = np.array(rows), np.array(cols), np.array(vals)
    tb = np.array([t_idx[t] for t in g.t1])
    tr = np.array([t_idx[t] for t in g.t2])
    y = g.win1.values.astype(float)
    side = g.side.values.astype(float)
    # 参数
    m = np.zeros(len(leagues))
    d = np.zeros(len(ent_idx))
    u = np.zeros(len(teams))
    h = 0.0
    W = w.sum()
    # Adam
    params = [m, d, u, np.array([h])]
    mom = [np.zeros_like(p) for p in params]
    vel = [np.zeros_like(p) for p in params]
    for it in range(1, iters + 1):
        s = m[ent_lgi] + d
        z = np.zeros(n)
        np.add.at(z, rows, vals * s[cols])
        z += u[tb] - u[tr] + params[3][0] * side
        p = 1 / (1 + np.exp(-z))
        r = w * (p - y) / W  # dL/dz
        gs = np.zeros(len(d))
        np.add.at(gs, cols, vals * r[rows])
        gm = np.zeros(len(m))
        np.add.at(gm, ent_lgi, gs)
        gd = gs + d / (sd_player ** 2 * n)
        if len(chain):
            diff = (d[chain[:, 0]] - d[chain[:, 1]]) / (sd_walk ** 2 * n)
            np.add.at(gd, chain[:, 0], diff)
            np.add.at(gd, chain[:, 1], -diff)
        gm = gm + m / (sd_league ** 2 * n)
        gu = np.zeros(len(u))
        np.add.at(gu, tb, r)
        np.add.at(gu, tr, -r)
        gu += u / (sd_team ** 2 * n)
        gh = np.array([(r * side).sum()])
        for k, (P, G) in enumerate(zip(params, (gm, gd, gu, gh))):
            mom[k] = 0.9 * mom[k] + 0.1 * G
            vel[k] = 0.999 * vel[k] + 0.001 * G * G
            P -= lr * (mom[k] / (1 - 0.9 ** it)) / (np.sqrt(vel[k] / (1 - 0.999 ** it)) + 1e-8)
    # 以「出场最多的那批联赛」平均为 0 点
    size = Counter(ent_lg)
    out = {l: float(m[lg_idx[l]]) * ELO_PER_LOGIT for l in leagues}
    out["_n"] = {l: size[l] for l in leagues}
    return out
