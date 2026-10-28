"""把模型的数字翻译成「人话」观点。

原理：逻辑回归里每个因素对胜率的贡献 = 权重 × 特征值。
贡献越大的理由越先说；和结论相反的最大因素作为「风险提示」。
措辞有多套模板随机组合，避免每次都一模一样。
"""
import math
import random

import numpy as np

from .engine import series_prob


def _pick(rng, *opts):
    return rng.choice(opts)


def score_dist(p, best_of):
    """单局胜率 -> 各比分概率，如 {'3:0':0.2, '3:1':...}"""
    need = best_of // 2 + 1
    out = {}
    for lost in range(need):
        out[f"{need}:{lost}"] = math.comb(need - 1 + lost, lost) * p ** need * (1 - p) ** lost
        out[f"{lost}:{need}"] = math.comb(need - 1 + lost, lost) * (1 - p) ** need * p ** lost
    return out


def recent(model, t):
    r = list(model.rater.s.recent.get(t, []))
    return sum(r), len(r) - sum(r)


def form_word(w, l):
    if w + l == 0:
        return "暂无近期数据"
    x = w / (w + l)
    return "状态火热" if x >= 0.8 else "状态不错" if x >= 0.6 else "状态一般" if x >= 0.4 else "状态低迷"


def reasons(model, a, b, x, contrib, display, rng):
    """生成每个因素的说明文字。返回 [(贡献值, 文字)]，贡献 >0 表示利好 a。"""
    s = model.rater.s
    out = []
    A, B = display(a), display(b)
    for f, c in contrib.items():
        if abs(c) < 0.03:
            continue
        fav, und = (A, B) if c > 0 else (B, A)
        if f == "elo":
            diff = abs(x["elo"]) * 400
            txt = _pick(rng,
                        f"综合实力分 {fav} 比 {und} 高约 {diff:.0f} 分",
                        f"从长期战绩算出来的实力分看，{fav} 领先 {und} 约 {diff:.0f} 分",
                        f"{fav} 整体硬实力更强（实力分高 {diff:.0f}）")
        elif f == "form":
            wa, la = recent(model, a)
            wb, lb = recent(model, b)
            txt = _pick(rng,
                        f"近期状态：{A} 最近 {wa}胜{la}负（{form_word(wa, la)}），{B} 最近 {wb}胜{lb}负（{form_word(wb, lb)}）",
                        f"{fav} 最近手感比对手好（{A} {wa}-{la}，{B} {wb}-{lb}，比赛结果都好于赛前预期）")
        elif f == "league":
            la, lb = s.home.get(a, "?"), s.home.get(b, "?")
            d = abs(x["league"]) * 400
            fl, ul = (la, lb) if c > 0 else (lb, la)
            txt = _pick(rng,
                        f"赛区对比：模型估计 {fl} 赛区整体比 {ul} 强约 {d:.0f} 分",
                        f"{fav} 来自更强的赛区（{fl} > {ul}，差约 {d:.0f} 分）")
        elif f == "side":
            txt = "蓝色方有先手选英雄的优势"
        elif f == "exp":
            na, nb = s.n.get(a, 0), s.n.get(b, 0)
            txt = _pick(rng, f"{fav} 的职业比赛经验更多（{A} {na} 局 / {B} {nb} 局）",
                        f"老牌队伍经验更足：{A} 打过 {na} 局，{B} 打过 {nb} 局")
        elif f == "map":
            continue
        else:
            txt = f
        out.append((c, txt))
    return sorted(out, key=lambda z: -abs(z[0]))


def opinion(model, a, b, best_of, display=str, draft=None, seed=0, extra=None):
    """返回一段中文观点。draft: LOL 的 BP 预案(draft.plan 的结果)；CS 自动做地图 BP 模拟。"""
    rng = random.Random(f"{a}-{b}-{seed}")
    x = model.x(a, b)
    contrib = model.lr.contributions(x)
    pg = model.p_game(a, b)
    veto = None
    if model.game == "cs":
        from .veto import series_with_veto
        veto = series_with_veto(model, a, b, best_of)
        ps = veto["p"]
    else:
        ps = series_prob(pg, best_of)
    fav, und = (a, b) if ps >= 0.5 else (b, a)
    pf = max(ps, 1 - ps)
    sd = score_dist(pg, best_of)
    best_score = max(sd, key=sd.get)
    if ps < 0.5:  # 比分换成「看好方:对手」
        l, r = best_score.split(":")
        best_score = f"{r}:{l}"
    A, B, F, U = display(a), display(b), display(fav), display(und)
    lines = []
    head = _pick(rng, f"我看好 {F}", f"我的判断：{F} 晋级", f"倾向 {F}")
    lines.append(f"{head}（系列赛胜率 {pf:.0%}，最可能比分 {F} {best_score}）。")
    rs = reasons(model, a, b, x, contrib, display, rng)
    pro = [t for c, t in rs if (c > 0) == (fav == a)]
    con = [t for c, t in rs if (c > 0) != (fav == a)]
    if pro:
        lines.append(_pick(rng, "理由：", "主要依据：", "为什么：") + "；".join(pro[:3]) + "。")
    if con:
        lines.append(_pick(rng, "不过要注意：", "风险点：", "但是：") + con[0] + "。")
    if veto and veto["maps"]:
        pm = veto["pm"]
        seq = "，".join(f"{display(t)}禁{m}" for t, m in veto["bans"][:2])
        picks = "，".join(f"{display(t)}选{m}（{A}胜率{pm[m]:.0%}）" for t, m in veto["picks"])
        dec = veto["maps"][-1]
        lines.append(f"地图BP推演：{seq}；{picks}；决胜图 {dec}（{A}胜率{pm[dec]:.0%}）。")
    if draft:
        sa = "、".join(c for c, n, w in draft["signatureA"][:3]) or "暂无"
        sb = "、".join(c for c, n, w in draft["signatureB"][:3]) or "暂无"
        lines.append(f"BP预测：{A} 的招牌英雄 {sa}；{B} 的招牌英雄 {sb}。"
                     f"{A} 应优先禁 {'、'.join(draft['bansA'][:3])}，{B} 大概率禁 {'、'.join(draft['bansB'][:3])}。")
        if abs(draft["edge"]) > 0.15:
            who = A if draft["edge"] > 0 else B
            lines.append(f"按当前版本强势英雄算，{who} 的 BP 更占便宜。")
    risk = "爆冷概率很低" if pf >= 0.8 else "有一定爆冷可能" if pf >= 0.62 else "基本五五开，谁赢都不奇怪"
    lines.append(f"总结：{risk}。")
    if extra:
        lines.append(extra)
    return " ".join(lines), ps
