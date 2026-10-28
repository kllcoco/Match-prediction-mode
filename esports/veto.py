"""CS 地图 BP（veto）模拟：
BO3 流程: A禁 B禁 A选 B选 A禁 B禁 剩下的是决胜图
每队都按模型算出的「自己在这张图的胜率」来禁最差、选最好。
"""
import pandas as pd

ORDER = {
    1: ["ban", "ban", "ban", "ban", "ban", "ban"],
    3: ["ban", "ban", "pick", "pick", "ban", "ban"],
    5: ["ban", "ban", "pick", "pick", "pick", "pick"],
}


def map_pool(frame, cutoff, days=120, size=7):
    rec = frame[(frame.date < cutoff) & (frame.date >= cutoff - pd.Timedelta(days=days)) & frame["map"].notna()]
    vc = rec["map"].value_counts()
    return list(vc.index[:size])


def _series_from_maps(ps, best_of):
    need = best_of // 2 + 1
    # dp[(赢, 输)] 概率
    dp = {(0, 0): 1.0}
    win = 0.0
    for p in ps:
        nd = {}
        for (w, l), q in dp.items():
            for (dw, dl, pr) in ((1, 0, p), (0, 1, 1 - p)):
                k = (w + dw, l + dl)
                if k[0] == need:
                    win += q * pr
                elif k[1] < need:
                    nd[k] = nd.get(k, 0) + q * pr
        dp = nd
    return win


def series_with_veto(model, t1, t2, best_of):
    pool = list(model.pool)
    pm = {mp: model.p_game(t1, t2, 0.0, mp) for mp in pool}  # t1 在每张图的胜率
    if len(pool) < 7 or best_of not in ORDER:
        p = model.p_game(t1, t2)
        from .engine import series_prob
        return dict(p=series_prob(p, best_of), picks=[], bans=[], maps=[], pm=pm)
    left = list(pool)
    picks, bans = [], []
    for i, act in enumerate(ORDER[best_of]):
        me = t1 if i % 2 == 0 else t2
        val = (lambda m: pm[m]) if me == t1 else (lambda m: 1 - pm[m])
        m = (max if act == "pick" else min)(left, key=val)
        left.remove(m)
        (picks if act == "pick" else bans).append((me, m))
    maps = [m for _, m in picks] + left[:1]
    p = _series_from_maps([pm[m] for m in maps], best_of) if best_of > 1 else pm[maps[0]]
    return dict(p=p, picks=picks, bans=bans, maps=maps, pm=pm)
