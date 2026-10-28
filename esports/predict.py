"""预测任意一场比赛：先联网同步最新赛果 -> 整理双方档案 -> 模型判断 -> 给出胜率、比分和观点。"""
import difflib
from datetime import datetime

import numpy as np
import pandas as pd

from . import backtest as B, explain
from .names import norm


def build(game, update=False, cutoff=None, strict=False):
    """训练一个「截至现在」的完整模型（包含所有大赛数据）。"""
    if update:
        from . import live, build_lol, build_cs
        live.update(game)
        (build_lol if game == "lol" else build_cs).build()
    B.GAME["g"] = game
    frame = B.load_frame(game, strict=strict)
    cutoff = pd.Timestamp(cutoff) if cutoff else frame.date.max() + pd.Timedelta(days=1)
    m = B.Model(game, frame, cutoff)
    m.frame = frame
    from .enrich import POOL_FILE
    if game == "lol" and POOL_FILE.exists():  # 联网汇总数据里的英雄池大小
        import json
        m.rater.s.pool_override.update(json.loads(POOL_FILE.read_text(encoding="utf-8")))
    from .report import display_map
    m.disp = display_map(game)
    m.draft = None
    if game == "lol":
        from . import build_lol, draft
        try:
            m.draft = draft.Draft(build_lol.load(), cutoff, include_intl=not strict).train_bp()
        except Exception:
            m.draft = None
    return m


def resolve(m, name):
    """把用户输入的队名（IG、GEN、geng、Gen.G…）对应到数据里的队伍。"""
    k = norm(name, m.game)
    s = m.rater.s
    if s.n.get(k, 0) > 0:
        return k
    known = [t for t, n in s.n.items() if n > 0]
    # 显示名包含 / 前缀
    low = name.lower().replace(" ", "")
    hits = [t for t in known if m.disp(t).lower().replace(" ", "").startswith(low)]
    if hits:
        return max(hits, key=lambda t: s.last.get(t, pd.Timestamp(0)))
    close = difflib.get_close_matches(k, known, n=3, cutoff=0.6)
    if close:
        return max(close, key=lambda t: s.last.get(t, pd.Timestamp(0)))
    raise KeyError(f"找不到队伍：{name}")


def profile(m, t, year=None):
    """一支队伍的数据档案。"""
    f = m.frame
    year = year or m.cutoff.year
    g = f[((f.t1 == t) | (f.t2 == t)) & (f.date < m.cutoff)]
    won = np.where(g.t1 == t, g.win1, 1 - g.win1)
    gy = g.date.dt.year == year
    s = m.rater.s
    out = dict(name=m.disp(t), region=s.home.get(t, "?"), games_year=int(gy.sum()),
               wr_year=float(won[gy.values].mean()) if gy.any() else None,
               last10=f"{int(won[-10:].sum())}胜{len(won[-10:]) - int(won[-10:].sum())}负",
               strength=float(m.rater.strength(t)[0]), last_match=str(s.last.get(t, ""))[:10])
    big = g[g.big == 1]
    if len(big):
        last_ev = big.event.iloc[-1]
        e = big[big.event == last_ev]
        we = np.where(e.t1 == t, e.win1, 1 - e.win1)
        out["big_event"] = f"{last_ev}：{int(we.sum())}胜{len(we) - int(we.sum())}负"
    ros = s.roster.get(t)
    if ros:
        out["roster"] = [p.split(":", 1)[1] for p in ros]
    return out


def head_to_head(m, a, b, n=5):
    f = m.frame
    g = f[(((f.t1 == a) & (f.t2 == b)) | ((f.t1 == b) & (f.t2 == a))) & (f.date < m.cutoff)]
    wa = np.where(g.t1 == a, g.win1, 1 - g.win1)
    recent = g.tail(n * 3)
    return int(wa.sum()), int(len(wa) - wa.sum()), (str(recent.date.max())[:10] if len(recent) else None)


def predict(m, a_name, b_name, best_of=None, news=False):
    a, b = resolve(m, a_name), resolve(m, b_name)
    bo = best_of or (5 if m.game == "lol" else 3)
    pa, pb = profile(m, a), profile(m, b)
    plan = m.draft.plan(m.rater.s.roster.get(a), m.rater.s.roster.get(b)) if m.draft else None
    h2h = head_to_head(m, a, b)
    txt, ps = explain.opinion(m, a, b, bo, display=m.disp, draft=plan)
    pg = m.p_game(a, b)
    sd = explain.score_dist(pg, bo)
    lines = [f"## {pa['name']} vs {pb['name']}（BO{bo}）", ""]
    for p in (pa, pb):
        line = (f"- **{p['name']}**（{p['region']}）：今年 {p['games_year']} 局，胜率 "
                f"{(p['wr_year'] or 0):.0%}，最近 {p['last10']}，最近比赛 {p['last_match']}")
        if p.get("big_event"):
            line += f"，最近大赛 {p['big_event']}"
        if p.get("roster"):
            line += f"，首发 {' / '.join(p['roster'])}"
        lines.append(line)
    lines.append(f"- 历史交手（按局）：{pa['name']} {h2h[0]} : {h2h[1]} {pb['name']}")
    lines += ["", f"**胜率**：{pa['name']} {ps:.0%} — {1 - ps:.0%} {pb['name']}（单局胜率 {pg:.0%}）", ""]
    top = sorted(sd.items(), key=lambda x: -x[1])[:4]
    lines.append("**比分预测**：" + "，".join(f"{fmt_score(k, pa['name'], pb['name'])}（{v:.0%}）" for k, v in top))
    lines += ["", "**观点**：" + txt]
    if m.game == "lol" and m.draft is not None and getattr(m, "fearless", 0):
        fs = m.draft.fearless_series(m.rater.s.roster.get(a), m.rater.s.roster.get(b), bo)
        lines += ["", f"**无畏征召 BP 推演**（用过的英雄后面不能再选；英雄池深度 {pa['name']} "
                      f"{_pool_txt(m, a)} vs {pb['name']} {_pool_txt(m, b)}）："]
        for gm in fs[:bo]:
            lines.append(f"- 第{gm['game']}局：{pa['name']} {'/'.join(gm['picksA'])}　vs　{pb['name']} {'/'.join(gm['picksB'])}")
    if news:
        from . import search
        try:
            res = search.web(f"{pa['name']} vs {pb['name']} {m.cutoff.year}", n=5)
            lines += ["", "**网上最新消息**（供参考，模型不直接使用）："]
            lines += [f"- [{r['title']}]({r['url']})：{r['snippet'][:80]}" for r in res]
        except Exception as e:  # 搜索失败不影响预测
            lines.append(f"（网页搜索失败：{e}）")
    return dict(a=a, b=b, p_series=ps, p_game=pg, scores=sd, text="\n".join(lines), profile=(pa, pb), draft=plan)


def _pool_txt(m, t):
    v = m.rater.pool(m.rater.s.roster.get(t))
    return "未知" if v != v else f"{v:.0f} 个英雄"


def fmt_score(k, a, b):
    """'3:1' -> 'A 3:1'；'1:3' -> 'B 3:1'（总是让赢家在前）"""
    x, y = map(int, k.split(":"))
    return f"{a} {x}:{y}" if x > y else f"{b} {y}:{x}"


def bracket(m, qf_pairs, bos=(5, 5, 5)):
    """给定 8 强对阵（[(A,B),(C,D),(E,F),(G,H)]，前两组是上半区）预测到冠军。"""
    qf = [(resolve(m, a), resolve(m, b)) for a, b in qf_pairs]
    probs, path = B.simulate_se8(m, qf, list(bos))
    return probs, path
