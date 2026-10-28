"""LOL BP（禁选）模型。

学三样东西（都只用开赛前的数据）：
1. 英雄强度：近 6 个月比赛里「选了这个英雄」对胜率的影响（逻辑回归，扣除双方实力差）
2. 版本热度：近 2 个月职业赛场的 Ban+Pick 率
3. 英雄池：当前首发 5 人近期在各英雄上的场次和胜率
用它们推荐：我该 ban 对面哪些英雄、自己大概率拿什么、整体 BP 谁更占便宜。
"""
import re
from collections import Counter, defaultdict

import numpy as np
import pandas as pd

ABBR = {
    "xin": "Xin Zhao", "ori": "Orianna", "kog": "Kog'Maw", "ez": "Ezreal", "mf": "Miss Fortune",
    "ali": "Alistar", "blitz": "Blitzcrank", "mao": "Maokai", "eve": "Evelynn", "lee": "Lee Sin",
    "tf": "Twisted Fate", "j4": "Jarvan IV", "jarvan": "Jarvan IV", "gp": "Gangplank", "cass": "Cassiopeia",
    "voli": "Volibear", "heimer": "Heimerdinger", "mundo": "Dr. Mundo", "nid": "Nidalee", "asol": "Aurelion Sol",
    "tk": "Tahm Kench", "kass": "Kassadin", "fiddle": "Fiddlesticks", "naut": "Nautilus", "trist": "Tristana",
    "yi": "Master Yi", "ww": "Warwick", "vik": "Viktor", "morg": "Morgana", "lb": "LeBlanc", "cait": "Caitlyn",
    "sej": "Sejuani", "nunu": "Nunu & Willump", "monkeyking": "Wukong", "wu": "Wukong", "kha": "Kha'Zix",
    "khazix": "Kha'Zix", "rek": "Rek'Sai", "kayle": "Kayle", "malph": "Malphite", "zil": "Zilean",
    "chogath": "Cho'Gath", "cho": "Cho'Gath", "vel": "Vel'Koz", "velkoz": "Vel'Koz", "kogmaw": "Kog'Maw",
    "reksai": "Rek'Sai", "kaisa": "Kai'Sa", "drmundo": "Dr. Mundo", "nunuwillump": "Nunu & Willump",
    "renataglasc": "Renata Glasc", "renata": "Renata Glasc", "belveth": "Bel'Veth", "ksante": "K'Sante",
}


class ChampNames:
    def __init__(self, known):
        self.known = sorted({k for k in known if isinstance(k, str)})
        self.key = {self._k(k): k for k in self.known}

    @staticmethod
    def _k(s):
        return re.sub(r"[^a-z]", "", str(s).lower())

    def __call__(self, s):
        if not isinstance(s, str) or not s.strip():
            return None
        k = self._k(s)
        if k in self.key:
            return self.key[k]
        if k in ABBR:
            return ABBR[k]
        cand = [v for kk, v in self.key.items() if kk.startswith(k)]
        return cand[0] if len(cand) == 1 else s.strip().title()


class Draft:
    def __init__(self, games: pd.DataFrame, cutoff, elo_of=None, window_days=180, meta_days=60):
        """games: build_lol.load() 原始表（含 bp/rp/bb/rb/bn/rn）"""
        self.cutoff = cutoff
        g = games[(games.date < cutoff) & (games.date >= cutoff - pd.Timedelta(days=window_days))]
        g = g[g.league.isin(["LCK", "LPL", "LEC", "LCS", "EU LCS", "NA LCS", "PCS", "LMS", "VCS", "CBLOL",
                             "LJL", "LCP", "LTA N", "LTA S", "OGN", "TCL", "LLA", "LCL", "OPL", "LCO", "GPL",
                             "LDL", "LCKC"])]
        pcols = [f"bp{i}" for i in range(1, 6)] + [f"rp{i}" for i in range(1, 6)]
        g = g.dropna(subset=pcols[:1] + pcols[5:6])
        self.n_games = len(g)
        names = pd.unique(g[pcols].values.ravel())
        self.cn = ChampNames(names)
        # --- 1. 英雄强度（逻辑回归，L2 收缩，扣除实力差）---
        champs = sorted({c for c in names if isinstance(c, str)})
        idx = {c: i for i, c in enumerate(champs)}
        X = np.zeros((len(g), len(champs) + 1))
        for r, row in enumerate(g[pcols].values):
            for j, c in enumerate(row):
                if isinstance(c, str):
                    X[r, idx[c]] += 1 if j < 5 else -1
        if elo_of is not None:
            X[:, -1] = [elo_of(b, rr, d) for b, rr, d in zip(g.blue, g.red, g.date)]
        y = g.blue_win.values.astype(float)
        self.strength = {}
        if len(g) > 200:
            w = self._ridge_logit(np.vstack([X, -X]), np.r_[y, 1 - y], lam=4.0 / max(len(g), 1) * 50)
            self.strength = {c: float(w[idx[c]]) for c in champs}
        # --- 2. 版本热度 ---
        m = g[g.date >= cutoff - pd.Timedelta(days=meta_days)]
        if len(m) < 100:
            m = g
        bcols = [f"bb{i}" for i in range(1, 6)] + [f"rb{i}" for i in range(1, 6)]
        pk = Counter(c for c in m[pcols].values.ravel() if isinstance(c, str))
        bn = Counter(c for c in m[bcols].values.ravel() if isinstance(c, str))
        n = max(len(m), 1)
        self.presence = {c: (pk[c] + bn[c]) / n for c in set(pk) | set(bn)}
        self.pickrate = {c: pk[c] / n for c in pk}
        self.banrate = {c: bn[c] / n for c in bn}
        # --- 3. 选手英雄池 ---
        self.pool = defaultdict(Counter)   # 选手 -> 英雄 -> 场次
        self.poolw = defaultdict(Counter)  # 选手 -> 英雄 -> 胜场
        for s, w in (("b", 1), ("r", 0)):
            for i in range(1, 6):
                for pl, c, win in zip(g[f"{s}n{i}"], g[f"{s}p{i}"], g.blue_win):
                    if isinstance(pl, str) and isinstance(c, str) and pl.strip().lower() != "unknown player":
                        key = f"lol:{pl.lower().strip()}"
                        self.pool[key][c] += 1
                        self.poolw[key][c] += int(win == w)

    @staticmethod
    def _ridge_logit(X, y, lam=0.05, iters=30):
        n, d = X.shape
        w = np.zeros(d)
        for _ in range(iters):
            p = 1 / (1 + np.exp(-(X @ w)))
            g = X.T @ (p - y) / n + lam * w
            H = (X.T * (p * (1 - p))) @ X / n + lam * np.eye(d)
            step = np.linalg.solve(H, g)
            w -= step
            if np.abs(step).max() < 1e-6:
                break
        return w

    # ---------- 队伍画像 ----------
    def comfort(self, roster):
        """当前首发的英雄池：英雄 -> (场次, 胜率)"""
        cnt, win = Counter(), Counter()
        for p in roster or []:
            cnt.update(self.pool.get(p, {}))
            win.update(self.poolw.get(p, {}))
        return {c: (cnt[c], (win[c] + 1) / (cnt[c] + 2)) for c in cnt}

    def value(self, c, comf):
        """某队拿到英雄 c 的价值 = 版本热度 + 英雄强度 + 自己的熟练度"""
        n, wr = comf.get(c, (0, 0.5))
        return (2.0 * self.presence.get(c, 0) + 3.0 * self.strength.get(c, 0)
                + 0.08 * min(n, 10) + 1.0 * (wr - 0.5) * min(n, 10) / 10)

    def plan(self, rA, rB, n_bans=5, n_picks=5):
        """给 A vs B 出一套 BP 预案。"""
        cA, cB = self.comfort(rA), self.comfort(rB)
        cand = set(self.presence) | set(cA) | set(cB)
        thrB = sorted(cand, key=lambda c: -self.value(c, cB))  # 对面最想拿的
        thrA = sorted(cand, key=lambda c: -self.value(c, cA))
        bansA = thrB[:n_bans]
        bansB = [c for c in thrA if c not in bansA][:n_bans]
        banned = set(bansA) | set(bansB)
        picksA = [c for c in thrA if c not in banned][:n_picks]
        picksB = [c for c in thrB if c not in banned and c not in picksA][:n_picks]
        edge = sum(self.strength.get(c, 0) for c in picksA) - sum(self.strength.get(c, 0) for c in picksB)
        sig = lambda comf: sorted(((c, n, wr) for c, (n, wr) in comf.items() if n >= 3), key=lambda x: (-x[1], -x[2]))[:5]
        return dict(bansA=bansA, bansB=bansB, picksA=picksA, picksB=picksB, edge=edge,
                    signatureA=sig(cA), signatureB=sig(cB))

    def meta_top(self, k=8):
        return sorted(self.presence.items(), key=lambda x: -x[1])[:k]

    def strongest(self, k=8, min_presence=0.15):
        c = [(x, s) for x, s in self.strength.items() if self.presence.get(x, 0) >= min_presence]
        return sorted(c, key=lambda x: -x[1])[:k]
