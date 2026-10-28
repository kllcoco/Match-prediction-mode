"""回测：假装站在每届大赛开打前，只用之前的数据训练，然后预测 8 强 -> 冠军，再对答案。"""
import itertools
import json

import numpy as np
import pandas as pd

from . import answers, build_cs, build_lol, games
from .engine import Logistic, Params, Rater, logloss, run, series_prob
from .names import norm
from .net import DATA

from .engine import GATED, PERF, POOL, TEAM_IG
FEATS = {"lol": ["elo", "form", "league", "side", "exp"] + TEAM_IG + PERF + POOL + [k + "_g" for k in GATED],
         "cs": ["elo", "form", "exp", "map", "pkda", "pdmg", "pkp", "pwr"]
         + [k + "_g" for k in ("elo", "form", "exp", "pkda", "pdmg", "pkp", "pwr")]}
BURN_IN_DAYS = 90
CLUTCH = {"on": True}
CAL_DAYS = 1095  # 用最近 3 年的季后赛来校准
# 赛区水位的折扣交给 calib.py 在跨赛区比赛上学习，这里不再手动打折
REGION = {"on": True, "kw": dict(iters=800), "scale": 1.0}
# 由 tune.py 在「非大赛」比赛上挑出来的参数
BEST = {"cs": Params(k_team=8, k_player=8, season_shrink=0.1, idle_days=90),
        "lol": Params(k_team=16, k_player=12, season_shrink=0.2)}


def load_frame(game, strict=True):
    if game == "lol":
        return games.lol_frame(build_lol.load(), strict)
    return games.cs_frame(build_cs.load(), strict)


class Model:
    """某个时间点「训练好」的模型：评分状态 + 逻辑回归权重。"""

    def __init__(self, game, frame, cutoff, params=None, rater_kw=None, cross=True):
        self.game = game
        self.feats = FEATS[game]
        kw = dict(rater_kw or {})
        if game == "lol" and REGION["on"]:
            kw.setdefault("use_league", False)  # 在线赛区分关掉，改用批量赛区模型
        self.rater = Rater(params or BEST[game], **kw)
        hist = run(frame, self.rater, cutoff=cutoff)
        self.temp = 1.0
        self.w_clutch = 0.0
        self.lr = Logistic(self.feats)
        self.lr.w[self.feats.index("elo")] = np.log(10)  # 数据太少时退化成纯 Elo
        tr = hist
        if len(hist):
            start = hist.date.min() + pd.Timedelta(days=BURN_IN_DAYS)
            tr = hist[hist.date >= start]
            if len(tr) >= 300:
                X = tr[self.feats].values
                y = tr.y.values
                # 正反两个视角各来一遍：让模型对「谁是 team1」不敏感
                self.lr.fit(np.vstack([X, -X]), np.r_[y, 1 - y])
                # 淘汰赛温度：只在「国内季后赛 / 顶级赛事」上学一个缩放系数
                c = tr[(tr.cal == 1) & (tr.date >= cutoff - pd.Timedelta(days=CAL_DAYS))]
                if len(c) >= 200:
                    z = c[self.feats].values @ self.lr.w
                    Xc = np.c_[z, c.clutch.values]
                    t = Logistic(["z", "clutch"], l2=1e-3).fit(np.r_[Xc, -Xc], np.r_[c.y.values, 1 - c.y.values])
                    self.temp = float(np.clip(t.w[0], 0.3, 1.2))
                    self.w_clutch = float(np.clip(t.w[1], 0, 10)) if CLUTCH["on"] else 0.0
        self.hist = hist
        self.n_train = len(tr)
        self.cutoff = cutoff
        # 截止日前最近的比赛是不是无畏征召（决定大赛预测时是否按无畏征召算）
        recent = frame[(frame.date < cutoff) & (frame.date >= cutoff - pd.Timedelta(days=120))]
        self.fearless = int(game == "lol" and "fearless" in frame and len(recent) and recent.fearless.mean() > 0.5)
        if game == "cs":
            from .veto import map_pool
            self.pool = map_pool(frame, cutoff)
        self.cross_w = None
        if game == "lol" and REGION["on"]:
            self.set_region_offsets(frame, cutoff)
            if cross:
                from . import calib
                self.cross_w = calib.weights(cutoff)

    def set_region_offsets(self, frame, cutoff):
        """用批量训练的「赛区水位模型」替换在线的赛区分（只在预测时使用）。"""
        from . import region
        from .games import LOL_REGION
        o = region.fit(frame, cutoff, **REGION["kw"])
        n = o.pop("_n", {})
        agg = {}
        for raw, v in o.items():
            r = LOL_REGION.get(raw)
            if r:
                a = agg.setdefault(r, [0.0, 0])
                a[0] += v * n[raw]
                a[1] += n[raw]
        if agg:
            mean = np.mean([a[0] / a[1] for a in agg.values()])
            self.rater.s.league.clear()
            self.rater.s.league.update({r: (a[0] / a[1] - mean) * REGION["scale"] for r, a in agg.items()})
            self.rater.use_league = True
            self.region_offsets = dict(self.rater.s.league)

    def x(self, t1, t2, side=0.0, mp=None):
        f = self.rater.features(t1, t2, side, mp)
        return {k: f[k] for k in self.feats}

    PERF_PART = set(PERF + TEAM_IG + POOL) | {k + "_g" for k in PERF + TEAM_IG}

    def perf_z(self, t1, t2):
        """表现部分的分数：只用选手表现 / 局内数据 / 英雄池这些「看数据」的特征"""
        x = self.x(t1, t2)
        return float(sum(w * x[k] for k, w in zip(self.feats, self.lr.w) if k in self.PERF_PART)) * self.temp

    def is_cross(self, t1, t2):
        h = self.rater.s.home
        return self.cross_w is not None and h.get(t1) and h.get(t2) and h.get(t1) != h.get(t2)

    def p_game(self, t1, t2, side=0.0, mp=None):
        if self.is_cross(t1, t2):
            # 跨赛区：用跨赛区比赛单独校准的权重（更谦虚）
            S1 = self.rater.strength(t1, league="__none")[0]
            S2 = self.rater.strength(t2, league="__none")[0]
            L = self.rater.s.league
            a, b, c = (tuple(self.cross_w) + (0.0,))[:3]
            z = a * (S1 - S2) / 400 + b * (L.get(self.rater.s.home[t1], 0) - L.get(self.rater.s.home[t2], 0)) / 400
            z += c * self.perf_z(t1, t2)
            return float(1 / (1 + np.exp(-z)))
        x = self.x(t1, t2, side, mp)
        z = float(np.dot([x[k] for k in self.feats], self.lr.w)) * self.temp
        z += self.w_clutch * self.rater.features(t1, t2)["clutch"]
        return float(1 / (1 + np.exp(-z)))

    def p_series(self, t1, t2, best_of, fearless=None):
        if self.game == "lol":
            fl = self.fearless if fearless is None else fearless
            if fl:
                # 无畏征召：每局的英雄池影响不同，逐局算胜率再组合
                from .veto import _series_from_maps
                ps = []
                for k in range(1, best_of + 1):
                    self.rater.ctx = (1, k)
                    ps.append(self.p_game(t1, t2))
                self.rater.ctx = (0, 1)
                return _series_from_maps(ps, best_of)
        if self.game == "cs":
            from .veto import series_with_veto
            return series_with_veto(self, t1, t2, best_of)["p"]
        return series_prob(self.p_game(t1, t2), best_of)

    def known(self, t):
        return self.rater.s.n.get(t, 0) > 0


GAME = {"g": "lol"}


def nm(x):
    return norm(x, GAME["g"])


def _bo(s):
    w = max(s["score1"], s["score2"])
    return 2 * w - 1


def simulate_se8(model, qf, bos):
    """8 队单败：返回 每队进 4 强/决赛/夺冠 的概率 + 按「最可能」一路走下去的预测对阵。"""
    teams = [t for m in qf for t in m]
    P = {}

    def ps(a, b, bo):
        key = (a, b, bo)
        if key not in P:
            P[key] = model.p_series(a, b, bo)
            P[(b, a, bo)] = 1 - P[key]
        return P[key]

    # 概率：精确计算
    r1 = {}
    for (a, b) in qf:
        r1[a] = ps(a, b, bos[0])
        r1[b] = 1 - r1[a]
    halves = [(qf[0], qf[1]), (qf[2], qf[3])]
    r2 = {}
    for (m1, m2) in halves:
        for a in m1:
            r2[a] = r1[a] * sum(r1[b] * ps(a, b, bos[1]) for b in m2)
        for b in m2:
            r2[b] = r1[b] * sum(r1[a] * ps(b, a, bos[1]) for a in m1)
    top = [t for t in qf[0] + qf[1]]
    bot = [t for t in qf[2] + qf[3]]
    r3 = {}
    for a in top:
        r3[a] = r2[a] * sum(r2[b] * ps(a, b, bos[2]) for b in bot)
    for b in bot:
        r3[b] = r2[b] * sum(r2[a] * ps(b, a, bos[2]) for a in top)
    # 确定性路线
    w1 = [a if ps(a, b, bos[0]) >= 0.5 else b for a, b in qf]
    sf = [(w1[0], w1[1]), (w1[2], w1[3])]
    w2 = [a if ps(a, b, bos[1]) >= 0.5 else b for a, b in sf]
    champ = w2[0] if ps(w2[0], w2[1], bos[2]) >= 0.5 else w2[1]
    path = dict(qf=[(a, b, ps(a, b, bos[0])) for a, b in qf], sf=[(a, b, ps(a, b, bos[1])) for a, b in sf],
                final=(w2[0], w2[1], ps(w2[0], w2[1], bos[2])), champion=champ)
    probs = {t: dict(semi=r1[t], final=r2[t], champ=r3[t]) for t in teams}
    return probs, path


def evaluate_event(model, ev, display):
    """对一届比赛做预测并判卷。"""
    ser = ev["series"]
    res = dict(name=ev["name"], series=[], unknown=[])
    for s in ser:
        a, b = nm(s["team1"]), nm(s["team2"])
        for t, raw in ((a, s["team1"]), (b, s["team2"])):
            if not model.known(t) and raw not in res["unknown"]:
                res["unknown"].append(raw)
        bo = _bo(s)
        p = model.p_series(a, b, bo)
        res["series"].append(dict(round=s["round"], t1=a, t2=b, p1=p, winner=nm(s["winner"]), bo=bo,
                                  score=f'{s["score1"]}-{s["score2"]}', correct=int((p >= 0.5) == (nm(s["winner"]) == a))))
    if ev.get("format") != "se8" and ser:
        # 非标准赛制（如 S1 双败）：冠军 = 最后一场的胜者；预测冠军 = 参赛队中胜率最高者
        last = max(ser, key=lambda s: pd.to_datetime(s.get("date", "")[:22].split(" {")[0], errors="coerce") or pd.Timestamp(0))
        teams = sorted({nm(s["team1"]) for s in ser} | {nm(s["team2"]) for s in ser})
        avg = {t: np.mean([model.p_game(t, o) for o in teams if o != t]) for t in teams}
        pc = max(avg, key=avg.get)
        res.update(real=dict(champion=nm(last["winner"])), pred_champion=pc, hit_champ_custom=int(pc == nm(last["winner"])))
    if ev.get("format") == "se8":
        qf = [(nm(s["team1"]), nm(s["team2"])) for s in ser[:4]]
        bos = [_bo(ser[0]), _bo(ser[4]), _bo(ser[6])]
        probs, path = simulate_se8(model, qf, bos)
        real_sf = {nm(s["team1"]) for s in ser[4:6]} | {nm(s["team2"]) for s in ser[4:6]}
        real_f = {nm(ser[6]["team1"]), nm(ser[6]["team2"])}
        real_c = nm(ser[6]["winner"])
        pred_sf = {t for m in path["sf"] for t in m[:2]}
        pred_f = set(path["final"][:2])
        res.update(probs=probs, path=path, real=dict(semi=sorted(real_sf), final=sorted(real_f), champion=real_c),
                   hit_semi=len(pred_sf & real_sf), hit_final=len(pred_f & real_f),
                   hit_champ=int(path["champion"] == real_c), p_real_champ=probs[real_c]["champ"])
    return res


def backtest(game, strict=True, params=None, rater_kw=None, verbose=True, events=None):
    GAME["g"] = game
    frame = load_frame(game, strict)
    evs = answers.load(game)
    if events:
        evs = [e for e in evs if e["name"] in events or str(e.get("year")) in events]
    out = []
    for ev in evs:
        if not ev["series"] or not ev.get("start"):
            continue
        cutoff = pd.Timestamp(ev["start"])
        if not strict:  # 完整模式：截止到淘汰赛第一天（小组赛/瑞士轮都可以看）
            d = pd.to_datetime([s.get("date", "")[:20] for s in ev["series"][:1]], errors="coerce")
            if len(d) and not pd.isna(d[0]):
                cutoff = d[0].normalize()
        if frame.date.min() >= cutoff:
            continue
        m = Model(game, frame, cutoff, params, rater_kw)
        r = evaluate_event(m, ev, None)
        r["cutoff"] = str(cutoff.date())
        r["weights"] = dict(zip(m.feats, map(float, m.lr.w)))
        r["temp"] = m.temp
        r["w_clutch"] = m.w_clutch
        out.append(r)
        if verbose:
            acc = np.mean([s["correct"] for s in r["series"]])
            line = f'{r["name"]:<36} 系列赛命中 {acc:5.0%}'
            if "hit_champ_custom" in r:
                line += f'  [特殊赛制] 预测冠军={r["pred_champion"]} 实际={r["real"]["champion"]} {"✔" if r["hit_champ_custom"] else "✘"}'
            if "hit_champ" in r:
                line += f'  4强{r["hit_semi"]}/4 决赛{r["hit_final"]}/2 冠军{"✔" if r["hit_champ"] else "✘"}  预测冠军={r["path"]["champion"]} 实际={r["real"]["champion"]}'
            if r["unknown"]:
                line += f"  [未知队伍:{r['unknown']}]"
            print(line)
    return out


def summary(out):
    s = [x for r in out for x in r["series"]]
    acc = np.mean([x["correct"] for x in s])
    ll = logloss([x["p1"] for x in s], [int(x["winner"] == x["t1"]) for x in s])
    se = [r for r in out if "hit_champ" in r]
    d = dict(events=len(out), series=len(s), series_acc=float(acc), logloss=ll,
             semi=float(np.mean([r["hit_semi"] / 4 for r in se])) if se else None,
             final=float(np.mean([r["hit_final"] / 2 for r in se])) if se else None,
             champ=float(np.mean([r["hit_champ"] for r in se])) if se else None,
             champ_prob=float(np.mean([r["p_real_champ"] for r in se])) if se else None)
    return d


if __name__ == "__main__":
    import sys
    g = sys.argv[1] if len(sys.argv) > 1 else "cs"
    o = backtest(g, strict="full" not in sys.argv)
    print(json.dumps(summary(o), ensure_ascii=False, indent=1))
