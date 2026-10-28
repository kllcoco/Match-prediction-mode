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


ROLE_CN = ["上单", "打野", "中单", "下路", "辅助"]


def _pname(p):
    return p.split(":", 1)[-1] if isinstance(p, str) else "?"


def _player_champs(m, player, k=3):
    """某个选手的招牌英雄：(英雄, 场次, 胜率)"""
    d = m.draft
    if d is None:
        return []
    n, w = d.pool.get(player, {}), d.poolw.get(player, {})
    return sorted(((c, n[c], (w[c] + 1) / (n[c] + 2)) for c in n if n[c] >= 2), key=lambda x: (-x[1], -x[2]))[:k]


def analysis(m, a_name, b_name, best_of=None):
    """完整赛前分析：数据对比 / BP / 胜负手 / 逐局胜率 / 比分。"""
    a, b = resolve(m, a_name), resolve(m, b_name)
    bo = best_of or (5 if m.game == "lol" else 3)
    A, B = m.disp(a), m.disp(b)
    s = m.rater.s
    ra, rb = s.roster.get(a) or [], s.roster.get(b) or []
    L = [f"# {A} vs {B}（BO{bo}）赛前分析", ""]

    # 一、逐位置对比
    L += ["## 一、逐位置对比（首发近 20 局表现）", "",
          f"| 位置 | {A} | {B} | 对位伤害差/分 | 对位KDA差 | 分均死亡 | 谁占优 |", "|---|---|---|---|---|---|---|"]
    lane_edge = []
    for i in range(min(5, len(ra), len(rb))):
        pa, _ = m.rater.perf([ra[i]])
        pb, _ = m.rater.perf([rb[i]])
        f = lambda x: "—" if x != x else f"{x:+.1f}"
        sa = np.nan_to_num(pa[1]) + 0.3 * np.nan_to_num(pa[0]) - np.nan_to_num(pa[3])
        sb = np.nan_to_num(pb[1]) + 0.3 * np.nan_to_num(pb[0]) - np.nan_to_num(pb[3])
        who = A if sa > sb else B
        lane_edge.append((abs(sa - sb), i, who))
        L.append(f"| {ROLE_CN[i]} | {_pname(ra[i])} | {_pname(rb[i])} | {f(pa[1])} / {f(pb[1])} | {f(pa[0])} / {f(pb[0])} | "
                 f"{'—' if pa[3] != pa[3] else f'{pa[3]:.2f}'} / {'—' if pb[3] != pb[3] else f'{pb[3]:.2f}'} | {who} |")
    ta, tb = s.tstats.get(a), s.tstats.get(b)
    if ta and tb:
        ga, gb = np.mean([x[0] for x in ta]), np.mean([x[0] for x in tb])
        oa, ob = np.mean([x[1] for x in ta]), np.mean([x[1] for x in tb])
        L += ["", f"团队局内：近 15 局经济占比 {A} {50 + ga * 100:.1f}% / {B} {50 + gb * 100:.1f}%；"
                  f"资源控制（推塔+小龙+2×大龙 场均差）{A} {oa * 10:+.1f} / {B} {ob * 10:+.1f}"]

    # 二、BP
    if m.draft is not None:
        d = m.draft
        plan = d.plan(ra, rb)
        L += ["", "## 二、BP 分析", ""]
        meta = "、".join(f"{c}({p:.0%})" for c, p in d.meta_top(6))
        L.append(f"- 版本热门（近期出场率=选+禁）：{meta}")
        strong = "、".join(c for c, _ in d.strongest(5))
        if strong:
            L.append(f"- 数据里胜率贡献最大的强势英雄：{strong}")
        for team, ros in ((A, ra), (B, rb)):
            sig = []
            for i, p in enumerate(ros[:5]):
                ch = _player_champs(m, p, 2)
                if ch:
                    sig.append(f"{ROLE_CN[i]}{_pname(p)}：" + "、".join(f"{c}({n}局{wr:.0%})" for c, n, wr in ch))
            if sig:
                L.append(f"- {team} 招牌英雄：" + "；".join(sig))
        def why(c, ros):
            for i, p in enumerate(ros[:5]):
                n = d.pool.get(p, {}).get(c, 0)
                if n >= 2:
                    return f"（针对{ROLE_CN[i]} {_pname(p)}，近期 {n} 局）"
            return "（版本强势）"
        L.append(f"- {A} 建议先禁：" + "、".join(c + why(c, rb) for c in plan["bansA"][:3]))
        L.append(f"- {B} 大概率先禁：" + "、".join(c + why(c, ra) for c in plan["bansB"][:3]))
        if getattr(m, "fearless", 0):
            pa_, pb_ = m.rater.pool(ra), m.rater.pool(rb)
            L.append(f"- 无畏征召：英雄池深度 {A} {pa_:.0f} vs {B} {pb_:.0f}（每人近 30 局用过的不同英雄数）")
            for gm in d.fearless_series(ra, rb, bo):
                L.append(f"  - 第{gm['game']}局预计：{A} {'/'.join(gm['picksA'])}　vs　{B} {'/'.join(gm['picksB'])}")

    # 三、胜负手
    x = m.x(a, b)
    con = m.lr.contributions(x)
    for k in list(con):
        if k.endswith("_g") and k[:-2] in con:
            con[k[:-2]] += con.pop(k)
    GROUP = {"实力底蕴（长期战绩/经验）": ["elo", "exp"], "近期状态": ["form"],
             "选手对位（输出/KDA/死亡/参团）": ["pdmg", "pkda", "pdeath", "pkp", "pwr"],
             "局内运营（经济/资源）": ["tgold", "tobj"], "英雄池/无畏征召": ["pool", "pool_f"], "蓝色方": ["side"]}
    gs = {g: sum(con.get(k, 0) for k in ks) for g, ks in GROUP.items()}
    L += ["", "## 三、胜负手", ""]
    pro_a = [g for g, v in sorted(gs.items(), key=lambda z: -z[1]) if v > 0.03]
    pro_b = [g for g, v in sorted(gs.items(), key=lambda z: z[1]) if v < -0.03]
    if m.is_cross(a, b):
        L.append(f"- 跨赛区对决（{s.home.get(a)} vs {s.home.get(b)}）：赛区水位差 {(s.league.get(s.home.get(a), 0) - s.league.get(s.home.get(b), 0)):+.0f} 分")
    L.append(f"- {A} 的优势：" + ("、".join(pro_a) if pro_a else "不明显"))
    L.append(f"- {B} 的优势：" + ("、".join(pro_b) if pro_b else "不明显"))
    key = sorted(lane_edge, reverse=True)[:2]
    for mag, i, who in key:
        if mag >= 0.3:
            L.append(f"- 关键对位：{ROLE_CN[i]} {_pname(ra[i])} vs {_pname(rb[i])}，数据上 {who} 明显占优——这条线打崩/打穿往往决定走势")
    if ta and tb:
        early = A if ga > gb else B
        L.append(f"- 节奏：{early} 平时更能把经济领先滚起来；另一方的机会在于拖住前期、靠团战和资源反打")

    # 四、逐局胜率 & 比分
    L += ["", "## 四、胜率与比分", ""]
    per = []
    for k in range(1, bo + 1):
        m.rater.ctx = (getattr(m, "fearless", 0), k)
        per.append(m.p_game(a, b))
    m.rater.ctx = (0, 1)
    ps = m.p_series(a, b, bo)
    L.append("- 逐局胜率（" + A + "）：" + "，".join(f"第{k}局 {p:.0%}" for k, p in enumerate(per, 1)))
    # 逐局胜率不同 -> 精确算各比分
    need = bo // 2 + 1
    dist = {}
    def rec(k, w, l, prob):
        if w == need or l == need:
            key = f"{w}:{l}"
            dist[key] = dist.get(key, 0) + prob
            return
        p = per[k]
        rec(k + 1, w + 1, l, prob * p)
        rec(k + 1, w, l + 1, prob * (1 - p))
    rec(0, 0, 0, 1.0)
    top = sorted(dist.items(), key=lambda z: -z[1])
    L.append(f"- 系列赛胜率：{A} {ps:.0%} — {1 - ps:.0%} {B}")
    L.append("- 比分概率：" + "，".join(f"{fmt_score(k, A, B)} {v:.0%}" for k, v in top))
    best = top[0][0]
    fav = A if ps >= 0.5 else B
    pf = max(ps, 1 - ps)
    L += ["", f"**结论：{fav} 晋级（{pf:.0%}），最可能比分 {fmt_score(best, A, B)}。**"
              + ("五五开的比赛，比分 2:1 / 3:2 的可能性也很高。" if pf < 0.6 else "")]
    return "\n".join(L)
