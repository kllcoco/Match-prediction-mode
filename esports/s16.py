"""S16（2026 世界赛）预测与存档、赛后判卷。

当前进度 -> 预测方式：
  瑞士轮进行中：用模型把剩下的瑞士轮 + 淘汰赛模拟 N 次（蒙特卡洛），得到每队进 8 强 / 4 强 / 决赛 / 夺冠的概率
  8 强对阵已出：直接按真实对阵精确计算
淘汰赛抽签规则官方细节不全，这里近似为：3-0 队对 3-2 队，3-1 队之间互打，尽量避开同赛区，3-0 队分在不同半区。

用法：
  python -m esports.s16           预测并存档到 predictions/ 和 reports/
  python -m esports.s16 grade     世界赛结束后，联网同步赛果并给存档的预测判卷
"""
import json
import random
from collections import Counter, defaultdict
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from . import explain, predict as P
from .engine import series_prob
from .net import DATA, ROOT

EVENT = "World Championship/2026"
PRED_DIR = ROOT / "predictions"


def swiss_state(m):
    """从已同步的数据里读出瑞士轮的已赛结果和战绩。"""
    from . import build_lol
    g = build_lol.load()
    w = g[(g.event.astype(str).str.replace("_", " ") == EVENT) & (g.source == "liquipedia-live")]
    if not len(w):
        raise RuntimeError("还没有 2026 世界赛数据，先运行：python -m esports update lol")
    from .names import norm
    # 按系列赛聚合（同一天同一对手）
    w = w.sort_values("date")
    series = []
    for _, r in w.iterrows():
        pair = frozenset((norm(r.blue), norm(r.red)))
        win = norm(r.blue) if r.blue_win else norm(r.red)
        if series and series[-1]["pair"] == pair and (r.date - series[-1]["last"]).total_seconds() < 12 * 3600:
            s = series[-1]
        else:
            s = dict(pair=pair, wins=Counter(), last=r.date, first=r.date)
            series.append(s)
        s["wins"][win] += 1
        s["last"] = r.date
    swiss = [s for s in series if s["first"] >= pd.Timestamp("2026-10-22")]
    rec = defaultdict(lambda: [0, 0])
    played = set()
    for s in swiss:
        a, b = sorted(s["pair"])
        win = max(s["wins"], key=s["wins"].get)
        lose = b if win == a else a
        rec[win][0] += 1
        rec[lose][1] += 1
        played.add(frozenset((a, b)))
    return dict(rec), played, swiss


def simulate(m, rec, played, n=20000, seed=7):
    teams = sorted(rec)
    pg = {(a, b): m.p_game(a, b) for a in teams for b in teams if a != b}
    home = m.rater.s.home
    rng = random.Random(seed)
    res = {t: Counter() for t in teams}
    champs = Counter()

    def play(a, b, bo):
        p = pg[(a, b)] if bo == 1 else series_prob(pg[(a, b)], bo)
        return (a, b) if rng.random() < p else (b, a)

    for _ in range(n):
        r = {t: list(v) for t, v in rec.items()}
        seen = set(played)
        while True:
            active = [t for t in teams if r[t][0] < 3 and r[t][1] < 3]
            if not active:
                break
            groups = defaultdict(list)
            for t in active:
                groups[tuple(r[t])].append(t)
            for key, grp in groups.items():
                rng.shuffle(grp)
                # 尽量避免重复交手
                while len(grp) >= 2:
                    a = grp.pop()
                    j = next((i for i, b in enumerate(grp) if frozenset((a, b)) not in seen), 0)
                    b = grp.pop(j)
                    seen.add(frozenset((a, b)))
                    bo = 3 if (key[0] == 2 or key[1] == 2) else 1
                    w, l = play(a, b, bo)
                    r[w][0] += 1
                    r[l][1] += 1
                if grp:  # 落单（理论上不会发生）
                    t = grp.pop()
                    r[t][0] += 1
        adv = [t for t in teams if r[t][0] == 3]
        if len(adv) != 8:
            continue
        for t in adv:
            res[t]["top8"] += 1
        # 淘汰赛抽签（近似）
        by = defaultdict(list)
        for t in adv:
            by[r[t][1]].append(t)
        for v in by.values():
            rng.shuffle(v)
        high = by[0] + by[1]
        low = by[2] + by[1]
        qf, used = [], set()
        for h in high:
            if h in used:
                continue
            used.add(h)
            opts = [x for x in low + high if x not in used]
            same = [x for x in opts if home.get(x) != home.get(h)]
            o = (same or opts)[0]
            used.add(o)
            qf.append((h, o))
        if len(qf) != 4:
            continue
        # 两个 3-0 队分到不同半区
        order = [0, 2, 1, 3] if len(by[0]) >= 2 else [0, 1, 2, 3]
        qf = [qf[i] for i in order]
        w1 = [play(a, b, 5)[0] for a, b in qf]
        for t in w1:
            res[t]["semi"] += 1
        w2 = [play(w1[0], w1[1], 5)[0], play(w1[2], w1[3], 5)[0]]
        for t in w2:
            res[t]["final"] += 1
        c = play(w2[0], w2[1], 5)[0]
        res[c]["champ"] += 1
        champs[c] += 1
    tot = sum(champs.values())
    return {t: {k: v / tot for k, v in res[t].items()} for t in teams}, tot


def run(n=20000):
    m = P.build("lol")
    rec, played, swiss = swiss_state(m)
    probs, tot = simulate(m, rec, played, n)
    order = sorted(probs, key=lambda t: -probs[t].get("champ", 0))
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    data = dict(created=now, data_until=str(m.frame.date.max()), n_sims=tot,
                swiss_record={m.disp(t): rec[t] for t in order},
                probs={m.disp(t): {k: round(v, 4) for k, v in probs[t].items()} for t in order},
                region={m.disp(t): m.rater.s.home.get(t) for t in order},
                predicted_champion=m.disp(order[0]))
    PRED_DIR.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d")
    path = PRED_DIR / f"s16_2026_{stamp}.json"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    # 报告
    L = [f"# S16（2026 英雄联盟全球总决赛）预测", "",
         f"- 生成时间：{now}；数据截至：{data['data_until'][:16]}（已包含本届入围赛和瑞士轮已赛结果）",
         f"- 方法：完整模式模型（看过所有往届大赛）+ 蒙特卡洛模拟剩余瑞士轮和淘汰赛 {tot} 次",
         f"- **预测冠军：{data['predicted_champion']}**（夺冠概率 {probs[order[0]]['champ']:.0%}）", "",
         "| 队伍 | 赛区 | 瑞士轮战绩 | 进8强 | 进4强 | 进决赛 | 夺冠 |", "|---|---|---|---|---|---|---|"]
    for t in order:
        p = probs[t]
        L.append(f"| {m.disp(t)} | {m.rater.s.home.get(t, '?')} | {rec[t][0]}-{rec[t][1]} | {p.get('top8', 0):.0%} | "
                 f"{p.get('semi', 0):.0%} | {p.get('final', 0):.0%} | {p.get('champ', 0):.1%} |")
    L += ["", "## 模型观点", ""]
    top = [t for t in order[:4]]
    L.append(f"夺冠热门前四：{'、'.join(m.disp(t) for t in top)}。下面是热门之间的假想对决：")
    L.append("")
    for i in range(len(top)):
        for j in range(i + 1, len(top)):
            r = P.predict(m, m.disp(top[i]), m.disp(top[j]), 5)
            L.append(f"- **{m.disp(top[i])} vs {m.disp(top[j])}**：" + r["text"].split("**观点**：")[-1])
    L += ["", "## 已赛瑞士轮结果", ""]
    for s in swiss:
        a, b = sorted(s["pair"])
        L.append(f"- {s['first'].strftime('%m-%d')} {m.disp(a)} {s['wins'][a]}:{s['wins'][b]} {m.disp(b)}")
    L += ["", f"> 存档：`{path.relative_to(ROOT)}`。世界赛结束后运行 `python -m esports.s16 grade` 判卷。"]
    rp = ROOT / "reports" / "s16_2026_prediction.md"
    rp.write_text("\n".join(L), encoding="utf-8")
    print("\n".join(L[:30]))
    print("存档：", path, rp)
    return data


def grade():
    """世界赛结束后：同步赛果，对所有存档的预测判卷。"""
    from . import live, build_lol, answers
    live.update("lol", years={2026})
    build_lol.build()
    ko = answers.lol_from_oe(2026) if False else None
    g = build_lol.load()
    w = g[(g.event.astype(str).str.replace("_", " ") == EVENT) & (g.date >= pd.Timestamp("2026-11-02"))].sort_values("date")
    if not len(w):
        print("淘汰赛还没打完/没有数据")
        return
    last = w.iloc[-1]
    champ = last.blue if last.blue_win else last.red
    top8 = sorted(set(w.blue) | set(w.red))
    out = [f"# S16 预测判卷（{datetime.now(timezone.utc):%Y-%m-%d}）", "", f"实际冠军：**{champ}**", f"实际 8 强：{'、'.join(top8)}", ""]
    from .names import norm
    for f in sorted(PRED_DIR.glob("s16_2026_*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        pc = d["predicted_champion"]
        pred8 = sorted(d["probs"], key=lambda t: -d["probs"][t].get("top8", 0))[:8]
        hit8 = len({norm(x) for x in pred8} & {norm(x) for x in top8})
        pchamp = next((v.get("champ", 0) for k, v in d["probs"].items() if norm(k) == norm(champ)), 0)
        out.append(f"- {f.name}（{d['created']}）：预测冠军 {pc} {'✅' if norm(pc) == norm(champ) else '❌'}；"
                   f"8 强猜中 {hit8}/8；给真实冠军的夺冠概率 {pchamp:.0%}")
    (ROOT / "reports" / "s16_2026_grade.md").write_text("\n".join(out), encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    import sys
    grade() if "grade" in sys.argv else run()
