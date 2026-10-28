"""生成中文预测报告（Markdown）：每届 8 强对阵 + 观点 + 判卷，以及爆冷专项、BP 检验。"""
import json
from collections import Counter

import numpy as np
import pandas as pd

from . import answers, backtest as B, build_lol, draft as D, explain
from .net import ROOT

REPORTS = ROOT / "reports"


def display_map(game):
    """统一名 -> 好看的原名"""
    from .names import norm
    if game == "lol":
        g = build_lol.load()
        raw = pd.concat([g.blue, g.red])
    else:
        from . import build_cs
        g = build_cs.load()
        raw = pd.concat([g.team1, g.team2])
    vc = raw.value_counts()
    out = {}
    for name in vc.index:
        k = norm(name, game)
        if k not in out:
            out[k] = name
    return lambda k: out.get(k, k)


def draft_for(model, cutoff, games_df):
    def elo_of(b, r, d):
        return 0.0
    return D.Draft(games_df, cutoff)


def event_report(game, model, ev, res, disp, dr=None):
    lines = [f"### {ev['name']}", ""]
    lines.append(f"训练数据截止：{res['cutoff']}（之后的比赛模型都没见过）  ")
    if "path" in res:
        p = res["path"]
        top = sorted(res["probs"].items(), key=lambda x: -x[1]["champ"])[:4]
        lines.append("夺冠概率：" + "，".join(f"{disp(t)} {v['champ']:.0%}" for t, v in top) + "  ")
        lines.append(f"**预测冠军：{disp(p['champion'])}**　｜　实际冠军：{disp(res['real']['champion'])} "
                     f"{'✅' if res['hit_champ'] else '❌'}  ")
        lines.append(f"预测 4 强命中 {res['hit_semi']}/4，决赛队伍命中 {res['hit_final']}/2")
    elif "pred_champion" in res:
        lines.append(f"（特殊赛制）预测冠军：{disp(res['pred_champion'])}，实际：{disp(res['real']['champion'])} "
                     f"{'✅' if res['hit_champ_custom'] else '❌'}")
    lines += ["", "| 轮次 | 对阵 | 模型看好 | 胜率 | 实际 | 判 |", "|---|---|---|---|---|---|"]
    for s in res["series"]:
        fav = s["t1"] if s["p1"] >= 0.5 else s["t2"]
        pf = max(s["p1"], 1 - s["p1"])
        lines.append(f"| {s['round']} | {disp(s['t1'])} vs {disp(s['t2'])} | {disp(fav)} | {pf:.0%} | "
                     f"{disp(s['winner'])} {s['score']} | {'✅' if s['correct'] else '❌'} |")
    # 8 强每场的观点
    if "path" in res:
        lines += ["", "**赛前观点（8 强）：**", ""]
        for s in res["series"][:4]:
            plan = None
            if dr is not None:
                plan = dr.plan(model.rater.s.roster.get(s["t1"]), model.rater.s.roster.get(s["t2"]))
            txt, _ = explain.opinion(model, s["t1"], s["t2"], s["bo"], display=disp, draft=plan)
            lines.append(f"- **{disp(s['t1'])} vs {disp(s['t2'])}**：{txt}")
    lines.append("")
    return "\n".join(lines)


def run(game, strict=True, with_draft=True):
    B.GAME["g"] = game
    frame = B.load_frame(game, strict)
    disp = display_map(game)
    raw = build_lol.load() if game == "lol" else None
    out, md = [], []
    for ev in answers.load(game):
        if not ev["series"] or not ev.get("start"):
            continue
        cutoff = pd.Timestamp(ev["start"])
        if not strict:
            d = pd.to_datetime([ev["series"][0].get("date", "")[:20]], errors="coerce")
            if not pd.isna(d[0]):
                cutoff = d[0].normalize()
        if frame.date.min() >= cutoff:
            continue
        m = B.Model(game, frame, cutoff)
        res = B.evaluate_event(m, ev, None)
        res["cutoff"] = str(cutoff.date())
        dr = D.Draft(raw, cutoff) if (game == "lol" and with_draft and cutoff.year >= 2016) else None
        md.append(event_report(game, m, ev, res, disp, dr))
        out.append(res)
    s = B.summary(out)
    mode = "严格模式（训练时不看任何世界赛/MSI/Major）" if strict else "完整模式（看过往届大赛 + 当届小组赛）"
    title = {"lol": "英雄联盟世界赛 S1-S15 回测", "cs": "CS Major 回测"}[game]
    head = [f"# {title} · {mode}", "",
            f"- 系列赛预测命中率：**{s['series_acc']:.1%}**（{s['series']} 场；瞎猜 50%）",
            f"- 4 强命中：{s['semi']:.1%}　决赛队伍命中：{s['final']:.1%}　冠军命中：**{s['champ']:.1%}**（瞎猜 12.5%）",
            f"- 对真实冠军给出的平均夺冠概率：{s['champ_prob']:.1%}　对数损失：{s['logloss']:.3f}（越低越好，瞎猜 0.693）", ""]
    REPORTS.mkdir(exist_ok=True)
    name = f"{game}_backtest_{'strict' if strict else 'full'}.md"
    (REPORTS / name).write_text("\n".join(head + md), encoding="utf-8")
    print("写入", REPORTS / name, s)
    return out, s


def upsets(results, game, label):
    """爆冷专项：模型认为 <50% 的一方赢了 = 爆冷。看模型的概率说得准不准。"""
    rows = []
    for r in results:
        for s in r["series"]:
            p_w = s["p1"] if s["winner"] == s["t1"] else 1 - s["p1"]
            rows.append(dict(event=r["name"], t1=s["t1"], t2=s["t2"], winner=s["winner"], p_winner=p_w, score=s["score"]))
    df = pd.DataFrame(rows)
    df["p_dog"] = np.minimum(df.p_winner, 1 - df.p_winner)
    df["upset"] = df.p_winner < 0.5
    bins = [0, 0.2, 0.3, 0.4, 0.5]
    df["bin"] = pd.cut(df.p_dog, bins)
    tab = df.groupby("bin", observed=True).agg(场数=("upset", "size"), 冷门实际赢=("upset", "sum"),
                                               模型给冷门的平均概率=("p_dog", "mean"))
    tab["冷门实际胜率"] = tab["冷门实际赢"] / tab["场数"]
    return df, tab


def bp_check(strict=True, full=False):
    """BP 检验：世界赛淘汰赛里，模型赛前推荐的 ban 位和真实 ban 位重合多少。"""
    g = build_lol.load()
    frame = B.load_frame("lol", strict)
    from .names import norm
    hits, base_hits, n, phits, pbase, pn = 0, 0, 0, 0, 0, 0
    per = []
    for ev in answers.load("lol"):
        if ev["year"] < 2016:
            continue
        cutoff = pd.Timestamp(ev["start"])
        ko_start = pd.to_datetime(ev["series"][0]["date"].split(" - ")[0].split(" {")[0], errors="coerce")
        if full and not pd.isna(ko_start):
            cutoff = ko_start.normalize()
        m = B.Model("lol", frame, cutoff)
        dr = D.Draft(g, cutoff, include_intl=full).train_bp()
        meta_bans = [c for c, _ in sorted(dr.banrate.items(), key=lambda x: -x[1])[:5]]
        ko = g[(g.league == "WLDs") & (g.year == ev["year"])].sort_values("date")
        ko = ko[ko.date >= ko_start.normalize()] if not pd.isna(ko_start) else ko.tail(30)
        h = b = k = 0
        for _, r in ko.iterrows():
            for side, opp, bans in (("blue", "red", [r[f"bb{i}"] for i in range(1, 6)]), ("red", "blue", [r[f"rb{i}"] for i in range(1, 6)])):
                bans = {x for x in bans if isinstance(x, str)}
                if len(bans) < 3:
                    continue
                me, op = norm(r[side]), norm(r[opp])
                plan = dr.plan(m.rater.s.roster.get(me), m.rater.s.roster.get(op))
                pred = set(plan["bansA"][:5])
                h += len(pred & bans)
                b += len(set(meta_bans) & bans)
                k += len(bans)
        if k:
            per.append((ev["name"], h / k, b / k, k // 5))
            hits += h
            base_hits += b
            n += k
    return per, hits / max(n, 1), base_hits / max(n, 1)


def main(games=("lol", "cs")):
    allres = {}
    for game in games:
        for strict in (True, False):
            allres[(game, strict)] = run(game, strict)
    lines = ["# 爆冷专项", "",
             "爆冷 = 模型赛前认为胜率不到 50% 的一方赢了。",
             "好模型不是「把冷门都猜中」，而是「说冷门有 30% 机会时，冷门真的大约 30% 会赢」。", ""]
    for (game, strict), (res, s) in allres.items():
        df, tab = upsets(res, game, "")
        disp = display_map(game)
        lines += [f"## {'LOL' if game == 'lol' else 'CS'} · {'严格' if strict else '完整'}模式", "",
                  f"- 淘汰赛共 {len(df)} 场，其中爆冷 {int(df.upset.sum())} 场（{df.upset.mean():.0%}）",
                  f"- 模型押中冷门（押了概率 <50% 的冷门... 即模型本身看好、但大众不看好）的统计见下表", "",
                  tab.to_markdown(floatfmt=".0%") if hasattr(tab, "to_markdown") else tab.to_string(), "",
                  "最意外的 5 场（模型给胜者的概率最低）：", ""]
        for _, r in df.sort_values("p_winner").head(5).iterrows():
            lines.append(f"- {r.event}：{disp(r.winner)} 赢了（{r.score}），模型赛前只给它 {r.p_winner:.0%}")
        lines.append("")
    if "lol" in games:
        per, acc, base = bp_check(True)
        lines += ["# BP 检验（LOL 世界赛淘汰赛）", "",
                  f"模型赛前推荐的 5 个 ban 位，平均命中真实 ban 位 **{acc:.0%}**；"
                  f"只按「版本 ban 率前 5」机械地猜，命中 {base:.0%}。", "",
                  "| 赛事 | 模型 ban 位命中 | 版本热门基准 | 局数 |", "|---|---|---|---|"]
        lines += [f"| {e} | {a:.0%} | {b:.0%} | {k} |" for e, a, b, k in per]
    (REPORTS / "upsets_and_bp.md").write_text("\n".join(lines), encoding="utf-8")
    print("写入", REPORTS / "upsets_and_bp.md")


if __name__ == "__main__":
    import sys
    main(sys.argv[1:] or ["lol", "cs"])
