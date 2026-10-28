"""对话模式（本地，不调用任何外部 AI 接口）。

听得懂的问法（随便组合）：
  T1 打 Gen.G 谁赢 / 比分 / 为什么 / BP 怎么ban
  T1 最近状态 / T1 阵容
  切换 cs / 切换 lol      退出：q
"""
import re

from . import predict as P

HELP = __doc__


def _teams(m, text):
    """从一句话里找出队名（按「打/vs/对/和/、」切分）。"""
    parts = re.split(r"\s*(?:vs\.?|VS|打|对阵|对|和|跟|PK|pk)\s*", text)
    out = []
    for p in parts:
        p = re.sub(r"(谁赢|谁会赢|比分|几比几|为什么|理由|BP|bp|ban|禁什么|怎么ban|最近状态|状态|阵容|战绩|会赢吗|吗|呢|？|\?)", "", p).strip()
        if not p:
            continue
        try:
            out.append(P.resolve(m, p))
        except KeyError:
            pass
    return out


def answer(m, text):
    ts = _teams(m, text)
    if len(ts) >= 2:
        r = P.predict(m, m.disp(ts[0]), m.disp(ts[1]))
        a, b = r["profile"][0]["name"], r["profile"][1]["name"]
        if re.search(r"比分|几比几", text):
            top = sorted(r["scores"].items(), key=lambda x: -x[1])[:3]
            return "我觉得最可能的比分：" + "，".join(f"{P.fmt_score(k, a, b)}（{v:.0%}）" for k, v in top)
        if re.search(r"BP|bp|ban|禁", text) and r["draft"]:
            d = r["draft"]
            return (f"{a} 建议禁：{'、'.join(d['bansA'][:5])}；{b} 大概率禁：{'、'.join(d['bansB'][:5])}。\n"
                    f"{a} 可能会拿：{'、'.join(d['picksA'][:5])}；{b} 可能会拿：{'、'.join(d['picksB'][:5])}。")
        return r["text"]
    if len(ts) == 1:
        p = P.profile(m, ts[0])
        s = (f"{p['name']}（{p['region']}）：今年 {p['games_year']} 局，胜率 {(p['wr_year'] or 0):.0%}，"
             f"最近 {p['last10']}，最近比赛 {p['last_match']}。")
        if p.get("big_event"):
            s += f" 最近一次大赛：{p['big_event']}。"
        if p.get("roster"):
            s += f" 当前首发：{' / '.join(p['roster'])}。"
        return s
    return "没听懂～试试：「T1 打 Gen.G 谁赢」「IG 比分」「BLG 最近状态」。输入 help 看说明。"


def loop(game="lol"):
    print("正在加载模型……")
    models = {game: P.build(game)}
    print(HELP)
    while True:
        try:
            text = input(f"[{game}] 你> ").strip()
        except EOFError:
            break
        if text in ("q", "quit", "exit", "退出"):
            break
        if text in ("help", "帮助"):
            print(HELP)
            continue
        m2 = re.match(r"切换\s*(lol|cs)", text, re.I)
        if m2:
            game = m2.group(1).lower()
            if game not in models:
                models[game] = P.build(game)
            print(f"已切换到 {game}")
            continue
        try:
            print("模型> " + answer(models[game], text))
        except Exception as e:  # 对话里出错不退出
            print("模型> 出错了：", e)
