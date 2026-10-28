"""调参：只用「非大赛」比赛的预测误差来挑参数（不看世界赛/Major 答案，避免作弊）。"""
import itertools
import sys

import numpy as np

from .backtest import load_frame
from .engine import Params, Rater, logloss, run


# 顶级赛事（非 Major）：和 Major 淘汰赛最像的验证集
TIER1 = {
    "cs": r"^(IEM|Intel Extreme|ESL One|ESL Pro League|BLAST|DreamHack Masters|StarLadder|EPICENTER|ECS Season|"
          r"FACEIT Major|EPL|PGL|Perfect World|ELEAGUE Premier|ELEAGUE CS:GO Premier|Esports World Cup|Thunderpick World)",
    "lol": r"^(LCK|LPL|LEC|EU LCS|NA LCS|LCS|LMS|PCS|OGN|Champions|IEM|EWC|DCup|KeSPA)",
}


def score(frame, params, rater_kw, since="2015-06-01", game=None):
    r = Rater(params, **rater_kw)
    h = run(frame, r)
    h = h[h.date >= since]
    if game:
        h = h[h.event.str.contains(TIER1[game].replace("^(", "^(?:"), regex=True) & ~h.event.str.contains("Qualif|Open|Closed|Showmatch", regex=True)]
    return logloss(h.elo_p, h.y), float(np.mean((h.elo_p >= 0.5) == (h.y == 1))), len(h)


def grid(game, space, rater_kw=None, quiet=False):
    frame = load_frame(game, strict=True)
    keys = list(space)
    best = None
    for vals in itertools.product(*space.values()):
        p = Params(**dict(zip(keys, vals)))
        ll, acc, n = score(frame, p, rater_kw or {}, game=game)
        print(dict(zip(keys, vals)), f"logloss={ll:.4f} acc={acc:.3f} n={n}", flush=True)
        if best is None or ll < best[0]:
            best = (ll, dict(zip(keys, vals)))
    print("最佳:", best)
    return best


if __name__ == "__main__":
    g = sys.argv[1]
    if g == "cs":
        grid("cs", dict(k_team=[16, 24, 32], k_player=[0, 4, 8], season_shrink=[0.1, 0.3], idle_days=[90]))
    else:
        grid("lol", dict(k_team=[16, 24, 32], k_player=[4, 8, 12], k_league=[8, 16], season_shrink=[0.2, 0.4]))
