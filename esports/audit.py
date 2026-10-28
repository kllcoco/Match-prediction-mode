"""答案泄漏审计：检查严格模式下，训练数据里有没有混进「当届大赛」的比赛。

逐届检查三件事：
1. 训练用的比赛（skip=0）里，有没有日期落在大赛期间、且双方都是该届淘汰赛队伍的比赛
   —— 抓「同一场比赛换了个赛事名 / 换了数据源 / 时区差一天」这类隐蔽泄漏
2. 截止日之后的比赛有没有被用来训练（时间穿越）
3. 训练集里任意一场「大赛」比赛（skip 标记失效）
"""
import pandas as pd

from . import answers, backtest as B
from .names import norm


def audit(game):
    B.GAME["g"] = game
    f = B.load_frame(game, strict=True)
    train = f[f.skip == 0]
    rows = []
    for ev in answers.load(game):
        if not ev["series"] or not ev.get("start"):
            continue
        start = pd.Timestamp(ev["start"])
        end = pd.Timestamp(ev["end"]) if ev.get("end") else start + pd.Timedelta(days=40)
        teams = {norm(s[k], game) for s in ev["series"] for k in ("team1", "team2")}
        # 1. 大赛期间（前后各放宽 2 天）双方都是淘汰赛队伍的训练比赛
        w = train[(train.date >= start - pd.Timedelta(days=2)) & (train.date <= end + pd.Timedelta(days=2))]
        sus = w[w.t1.isin(teams) & w.t2.isin(teams)]
        # 3. 训练集中被标为大赛的比赛（理论上为 0）
        big_in_train = int((train.big == 1).sum())
        rows.append(dict(event=ev["name"], window=f"{start.date()}~{end.date()}", suspicious=len(sus),
                         events=", ".join(sorted(set(sus.event.fillna("(无赛事名)").astype(str))))[:150]))
    df = pd.DataFrame(rows)
    # 2. 时间穿越：Model 只用 cutoff 之前的数据（代码层面由 engine.run 的 cutoff 保证），这里抽查一届
    ev = [e for e in answers.load(game) if e.get("start")][-1]
    m = B.Model(game, f, pd.Timestamp(ev["start"]))
    travel = int((m.hist.date >= pd.Timestamp(ev["start"])).sum())
    return df, big_in_train, travel


if __name__ == "__main__":
    for g in ("lol", "cs"):
        df, big, travel = audit(g)
        print(f"===== {g} =====")
        print(df.to_string(index=False))
        print("训练集中带大赛标记的比赛数:", big, "｜ 截止日之后被用来训练的比赛数:", travel)
