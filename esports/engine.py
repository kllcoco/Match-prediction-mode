"""核心模型：评分系统（Elo）+ 小型逻辑回归。两个游戏通用。

队伍实力 S = 队伍分 + 5 名选手平均分 + 赛区分
  - 选手分跟着人走：选手转会到别的赛区，就把两个赛区的实力「连」起来，
    这样即使不看世界赛，也能大致估计赛区之间的差距。
  - 赛区分只在跨赛区的比赛（非 Riot 国际赛：IEM、EWC、亚运…）里更新。
逻辑回归在这些特征上学习「各因素该占多大权重」，输出单局/单图胜率。
"""
import math
from collections import defaultdict, deque
from dataclasses import dataclass, field

import numpy as np
import pandas as pd

FEATURES = ["elo", "form", "league", "side", "exp", "map"]
FEATURE_CN = {
    "elo": "综合实力分差", "form": "近期状态", "league": "赛区强弱",
    "side": "蓝色方优势", "exp": "比赛经验", "map": "地图熟练度", "clutch": "大赛表现",
}


@dataclass
class Params:
    k_team: float = 24.0
    k_player: float = 16.0
    k_league: float = 12.0
    k_map: float = 18.0
    season_shrink: float = 0.25   # 跨年时队伍分回归均值的比例
    idle_days: float = 120.0      # 长时间不比赛开始回归
    form_alpha: float = 0.15
    clutch_alpha: float = 0.05
    k_big: float = 1.0            # 大赛内比赛的更新倍数；回测显示调大没有帮助，默认不加速


@dataclass
class State:
    team: dict = field(default_factory=lambda: defaultdict(float))
    player: dict = field(default_factory=lambda: defaultdict(float))
    league: dict = field(default_factory=lambda: defaultdict(float))
    tmap: dict = field(default_factory=lambda: defaultdict(float))
    form: dict = field(default_factory=lambda: defaultdict(float))
    n: dict = field(default_factory=lambda: defaultdict(int))
    home: dict = field(default_factory=dict)        # 队伍 -> 所在赛区
    roster: dict = field(default_factory=dict)      # 队伍 -> 最近一次首发
    last: dict = field(default_factory=dict)        # 队伍 -> 最近比赛日期
    year: int = 0
    recent: dict = field(default_factory=lambda: defaultdict(lambda: deque(maxlen=10)))
    clutch: dict = field(default_factory=lambda: defaultdict(float))  # 大赛（季后赛/顶级赛事）超预期程度


def expect(d):
    return 1.0 / (1.0 + 10 ** (-d / 400.0))


class Rater:
    """按时间顺序吃比赛，边看边更新评分；每局开赛前先把特征记下来（不偷看结果）。"""

    def __init__(self, params: Params | None = None, use_players=True, use_league=True):
        self.p = params or Params()
        self.s = State()
        self.use_players = use_players
        self.use_league = use_league

    # ---------- 实力 ----------
    def players_of(self, team, roster=None):
        r = roster if roster else self.s.roster.get(team)
        return list(r) if r else []

    def strength(self, team, roster=None, league=None):
        s = self.s
        ps = self.players_of(team, roster) if self.use_players else []
        pv = float(np.mean([s.player[x] for x in ps])) if ps else 0.0
        lg = league or s.home.get(team)
        lv = s.league[lg] if (self.use_league and lg) else 0.0
        return s.team[team] + pv + lv, pv, lv

    def _age(self, team, date):
        s = self.s
        last = s.last.get(team)
        if last is not None:
            idle = (date - last).days
            if idle > self.p.idle_days:
                f = min(0.5, (idle - self.p.idle_days) / 365.0)
                s.team[team] *= (1 - f)
                s.form[team] *= (1 - f)

    def _new_year(self, year):
        if year != self.s.year:
            if self.s.year:
                k = 1 - self.p.season_shrink
                for t in list(self.s.team):
                    self.s.team[t] *= k
                for t in list(self.s.player):
                    self.s.player[t] *= (1 - self.p.season_shrink / 2)
                for t in list(self.s.tmap):
                    self.s.tmap[t] *= k
            self.s.year = year

    def features(self, t1, t2, side=0.0, mp=None, r1=None, r2=None, l1=None, l2=None):
        s = self.s
        S1, _, L1 = self.strength(t1, r1, l1)
        S2, _, L2 = self.strength(t2, r2, l2)
        m = (s.tmap[(t1, mp)] - s.tmap[(t2, mp)]) / 400.0 if mp else 0.0
        return dict(elo=(S1 - S2) / 400.0, form=s.form[t1] - s.form[t2], league=(L1 - L2) / 400.0,
                    side=side, exp=math.log1p(s.n[t1]) - math.log1p(s.n[t2]), map=m,
                    clutch=s.clutch[t1] - s.clutch[t2])

    # ---------- 更新 ----------
    def update(self, row):
        """row: date, t1, t2, win1, (league), (side), (map), (p1 list), (p2 list), (domestic)"""
        s, P = self.s, self.p
        date = row["date"]
        self._new_year(date.year)
        t1, t2 = row["t1"], row["t2"]
        for t, r in ((t1, row.get("p1")), (t2, row.get("p2"))):
            self._age(t, date)
            if r:
                s.roster[t] = r
            if row.get("domestic") and row.get("league"):
                s.home[t] = row["league"]
        mp = row.get("map") or None
        f = self.features(t1, t2, row.get("side", 0.0), mp)
        S1, pv1, L1 = self.strength(t1)
        S2, pv2, L2 = self.strength(t2)
        e = expect(S1 - S2)
        y = row["win1"]
        d = y - e
        kb = P.k_big if row.get("big") else 1.0
        s.team[t1] += P.k_team * kb * d
        s.team[t2] -= P.k_team * kb * d
        if self.use_players:
            for x in self.players_of(t1):
                s.player[x] += P.k_player * d
            for x in self.players_of(t2):
                s.player[x] -= P.k_player * d
        h1, h2 = s.home.get(t1), s.home.get(t2)
        if self.use_league and h1 and h2 and h1 != h2:
            s.league[h1] += P.k_league * d
            s.league[h2] -= P.k_league * d
        if mp:
            em = expect(s.tmap[(t1, mp)] - s.tmap[(t2, mp)] + (S1 - S2))
            s.tmap[(t1, mp)] += P.k_map * (y - em)
            s.tmap[(t2, mp)] -= P.k_map * (y - em)
        if row.get("cal") or row.get("big"):
            c = P.clutch_alpha
            s.clutch[t1] = (1 - c) * s.clutch[t1] + c * d
            s.clutch[t2] = (1 - c) * s.clutch[t2] - c * d
        a = P.form_alpha
        s.form[t1] = (1 - a) * s.form[t1] + a * d
        s.form[t2] = (1 - a) * s.form[t2] - a * d
        s.n[t1] += 1
        s.n[t2] += 1
        s.recent[t1].append(y)
        s.recent[t2].append(1 - y)
        s.last[t1] = s.last[t2] = date
        return f, e


# ---------- 小型逻辑回归（纯 numpy，不依赖 sklearn） ----------
class Logistic:
    def __init__(self, feats=FEATURES, l2=1e-3):
        self.feats = feats
        self.l2 = l2
        self.w = np.zeros(len(feats))
        self.b = 0.0

    def fit(self, X, y, iters=300, lr=0.5):
        X = np.asarray(X, float)
        y = np.asarray(y, float)
        n = len(y)
        w, b = np.zeros(X.shape[1]), 0.0
        # 牛顿法（特征少，几步就收敛）
        Xb = np.hstack([X, np.ones((n, 1))])
        theta = np.zeros(Xb.shape[1])
        for _ in range(25):
            z = Xb @ theta
            p = 1 / (1 + np.exp(-z))
            g = Xb.T @ (p - y) / n + self.l2 * np.r_[theta[:-1], 0]
            H = (Xb.T * (p * (1 - p))) @ Xb / n + self.l2 * np.diag(np.r_[np.ones(len(theta) - 1), 0])
            step = np.linalg.solve(H + 1e-9 * np.eye(len(theta)), g)
            theta -= step
            if np.abs(step).max() < 1e-7:
                break
        self.w, self.b = theta[:-1], theta[-1]
        return self

    def predict(self, X):
        X = np.asarray(X, float)
        return 1 / (1 + np.exp(-(X @ self.w + self.b)))

    def contributions(self, x: dict):
        """每个特征把胜率往哪边推了多少（对数几率空间）。用于生成解释。"""
        return {f: float(self.w[i] * x[f]) for i, f in enumerate(self.feats)}


def logloss(p, y):
    p = np.clip(np.asarray(p), 1e-6, 1 - 1e-6)
    y = np.asarray(y)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def series_prob(p, best_of):
    """单局胜率 p -> BO(n) 系列赛胜率"""
    need = best_of // 2 + 1
    tot = 0.0
    for lost in range(need):
        tot += math.comb(need - 1 + lost, lost) * p ** need * (1 - p) ** lost
    return tot


def run(games: pd.DataFrame, rater: Rater, cutoff=None, train_mask=None):
    """按时间顺序跑一遍，返回每局开赛前的特征表（用于训练逻辑回归）。

    games 需要列: date, t1, t2, win1, 以及可选 league/side/map/p1/p2/domestic/skip
    skip=1 的比赛（被屏蔽的大赛）完全不看。
    """
    rows = []
    recs = games.to_dict("records")
    for r in recs:
        if cutoff is not None and r["date"] >= cutoff:
            break
        if r.get("skip"):
            continue
        f, e = rater.update(r)
        f["y"] = r["win1"]
        f["elo_p"] = e
        f["date"] = r["date"]
        f["cross"] = int(bool(r.get("cross")))
        f["event"] = r.get("event") or ""
        f["cal"] = int(bool(r.get("cal") or r.get("big")))
        rows.append(f)
    return pd.DataFrame(rows)
