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
    def __init__(self, games: pd.DataFrame, cutoff, elo_of=None, window_days=180, meta_days=60, include_intl=False):
        """games: build_lol.load() 原始表（含 bp/rp/bb/rb/bn/rn）"""
        self.cutoff = cutoff
        g = games[(games.date < cutoff) & (games.date >= cutoff - pd.Timedelta(days=window_days))]
        g = g[g.league.isin(["LCK", "LPL", "LEC", "LCS", "EU LCS", "NA LCS", "PCS", "LMS", "VCS", "CBLOL",
                             "LJL", "LCP", "LTA N", "LTA S", "OGN", "TCL", "LLA", "LCL", "OPL", "LCO", "GPL",
                             "LDL", "LCKC"] + (["WLDs", "MSI", "FST", "EWC"] if include_intl else []))]
        pcols = [f"bp{i}" for i in range(1, 6)] + [f"rp{i}" for i in range(1, 6)]
        g = g.dropna(subset=pcols[:1] + pcols[5:6])
        # 每个英雄最常打的位置（上野中下辅）
        rc = {}
        for i in range(5):
            for c in list(g[f"bp{i+1}"]) + list(g[f"rp{i+1}"]):
                if isinstance(c, str):
                    rc.setdefault(c, Counter())[i] += 1
        self.role = {c: v.most_common(1)[0][0] for c, v in rc.items()}
        self.n_games = len(g)
        self._g = g
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
        if include_intl:  # 大赛本身（同一版本）的 BP 权重最高：近 14 天的比赛重复计入 3 次
            rec = g[g.date >= cutoff - pd.Timedelta(days=14)]
            m = pd.concat([m] + [rec] * 3)
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

    # ---------- 训练 BP 模型 ----------
    BP_FEATS = ["presence", "banrate", "pickrate", "strength", "opp_n", "opp_wr", "own_n", "own_wr"]

    def _feat(self, c, own, opp):
        on, ow = own.get(c, (0, 0.5))
        pn, pw = opp.get(c, (0, 0.5))
        return [self.presence.get(c, 0), self.banrate.get(c, 0), self.pickrate.get(c, 0),
                self.strength.get(c, 0), np.log1p(pn), (pw - 0.5) * min(pn, 10) / 10,
                np.log1p(on), (ow - 0.5) * min(on, 10) / 10]

    def train_bp(self, max_games=1500, seed=0):
        """用真实比赛的禁选记录训练两个小模型：会不会 ban 某英雄 / 会不会选某英雄。"""
        from .engine import Logistic
        g = self._g
        if len(g) > max_games:
            g = g.sample(max_games, random_state=seed)
        cands = [c for c, v in sorted(self.presence.items(), key=lambda x: -x[1])[:90]]
        Xb, yb, Xp, yp = [], [], [], []
        for _, r in g.iterrows():
            for me, op in (("b", "r"), ("r", "b")):
                ro = [f"lol:{str(r[f'{me}n{i}']).lower().strip()}" for i in range(1, 6)]
                rp = [f"lol:{str(r[f'{op}n{i}']).lower().strip()}" for i in range(1, 6)]
                own, opp = self.comfort(ro), self.comfort(rp)
                bans = {r[f"{me}b{i}"] for i in range(1, 6)}
                picks = {r[f"{me}p{i}"] for i in range(1, 6)}
                allb = bans | {r[f"{op}b{i}"] for i in range(1, 6)}
                for c in cands:
                    # 去掉本局自己的贡献（避免偷看答案）
                    o2 = dict(own)
                    if c in picks and c in o2:
                        n, w = o2[c]
                        o2[c] = (max(n - 1, 0), w)
                    f = self._feat(c, o2, opp)
                    Xb.append(f)
                    yb.append(int(c in bans))
                    if c not in allb:
                        Xp.append(f)
                        yp.append(int(c in picks))
        self.ban_lr = Logistic(self.BP_FEATS, l2=1e-3).fit(np.array(Xb), np.array(yb))
        self.pick_lr = Logistic(self.BP_FEATS, l2=1e-3).fit(np.array(Xp), np.array(yp))
        return self

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

    def plan(self, rA, rB, n_bans=5, n_picks=5, used=()):
        """给 A vs B 出一套 BP 预案。used：无畏征召下本系列赛已经用过、不能再选的英雄。"""
        cA, cB = self.comfort(rA), self.comfort(rB)
        # 候选只考虑：版本热门（出场率 ≥5%）或某一方的常用英雄（≥3 局）——冷门英雄样本太少，估计不稳
        cand = ({c for c, v in self.presence.items() if v >= 0.05}
                | {c for c, (n, _) in cA.items() if n >= 3} | {c for c, (n, _) in cB.items() if n >= 3}) - set(used)
        if len(cand) < 25:
            cand |= set(sorted(self.presence, key=lambda c: -self.presence[c])[:40]) - set(used)
        if getattr(self, "ban_lr", None) is not None:
            cand = sorted(cand)
            def score(lr, own, opp):
                X = np.array([self._feat(c, own, opp) for c in cand])
                return dict(zip(cand, lr.predict(X)))
            pkA, pkB = score(self.pick_lr, cA, cB), score(self.pick_lr, cB, cA)
            # ban 位 = 对面最可能选、且选了胜率高的英雄（对面选人概率 × 对面在这个英雄上的胜率优势）
            def threat(pk, comf, own_pk, own_comf):
                out = {}
                for c in cand:
                    n, wr = comf.get(c, (0, 0.5))
                    on, owr = own_comf.get(c, (0, 0.5))
                    out[c] = (pk[c] * (1 + max(0.0, wr - 0.5) * min(n, 10) / 5) + 0.3 * self.strength.get(c, 0)
                              # 自己的拿手英雄一般是抢来用，而不是禁掉
                              - own_pk[c] * (1 + max(0.0, owr - 0.5) * min(on, 10) / 5))
                return out
            banA, banB = threat(pkB, cB, pkA, cA), threat(pkA, cA, pkB, cB)
            bansA = sorted(cand, key=lambda c: -banA[c])[:n_bans]
            bansB = [c for c in sorted(cand, key=lambda c: -banB[c]) if c not in bansA][:n_bans]
            banned = set(bansA) | set(bansB)
            picksA = self._by_player(rA, pkA, banned | set(used))
            picksB = self._by_player(rB, pkB, banned | set(used) | set(picksA))
        else:
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

    def _by_player(self, roster, pk, banned):
        """每个位置从该选手自己的英雄池里选：常用 + 胜率高 + 版本强的优先；被禁/已用就换下一个。
        选手英雄池用完（无畏征召后几局）才退回到该位置的版本热门英雄。"""
        out = []
        taken = set(banned)
        for i, p in enumerate((roster or [None] * 5)[:5]):
            n, w = self.pool.get(p, {}), self.poolw.get(p, {})
            own = [c for c in n if c not in taken]
            if own:
                c = max(own, key=lambda c: 0.25 * min(n[c], 8) + 1.5 * ((w[c] + 1) / (n[c] + 2) - 0.5)
                        + 2.0 * pk.get(c, 0) + (0.3 if self.role.get(c) == i else -1.0))
            else:
                meta = [c for c in pk if self.role.get(c) == i and c not in taken]
                c = max(meta, key=lambda c: pk[c]) if meta else None
            if c:
                out.append(c)
                taken.add(c)
        return out

    def _by_role(self, ranked, banned):
        """按上野中下辅各选一个（每个位置取该位置排名最高、没被禁/选的英雄）"""
        out = [None] * 5
        for c in ranked:
            if c in banned:
                continue
            r = self.role.get(c)
            if r is not None and out[r] is None:
                out[r] = c
            if all(out):
                break
        return [c for c in out if c]

    def fearless_series(self, rA, rB, best_of=5):
        """无畏征召逐局推演：每局按 BP 模型选，选过的英雄后面几局都不能再用。"""
        used, games = set(), []
        for k in range(1, best_of + 1):
            p = self.plan(rA, rB, used=used)
            games.append(dict(game=k, picksA=p["picksA"], picksB=p["picksB"], bansA=p["bansA"], bansB=p["bansB"]))
            used |= set(p["picksA"]) | set(p["picksB"])
        return games

    def meta_top(self, k=8):
        return sorted(self.presence.items(), key=lambda x: -x[1])[:k]

    def strongest(self, k=8, min_presence=0.15):
        c = [(x, s) for x, s in self.strength.items() if self.presence.get(x, 0) >= min_presence]
        return sorted(c, key=lambda x: -x[1])[:k]
