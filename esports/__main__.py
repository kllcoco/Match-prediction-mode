"""命令行入口：python -m esports <命令>

  update [lol|cs]                 联网同步最新赛果
  search <关键词> [--game lol]     网页 + Liquipedia 搜索
  predict <A队> <B队> [--bo 5] [--game lol] [--news]   预测一场比赛（胜率/比分/观点）
  status <队名> [--game lol]       查看队伍档案
  chat [--game lol]               对话模式
  backtest [lol|cs] [--full]      回测往届世界赛 / Major
  report [lol|cs]                 生成全部中文报告到 reports/
"""
import argparse
import sys


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python -m esports", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    p = sub.add_parser("update"); p.add_argument("games", nargs="*", default=["lol", "cs"])
    p = sub.add_parser("search"); p.add_argument("q", nargs="+"); p.add_argument("--game", default="lol")
    p = sub.add_parser("predict"); p.add_argument("a"); p.add_argument("b")
    p.add_argument("--bo", type=int); p.add_argument("--game", default="lol"); p.add_argument("--news", action="store_true")
    p.add_argument("--update", action="store_true", help="预测前先联网同步")
    p = sub.add_parser("status"); p.add_argument("team"); p.add_argument("--game", default="lol")
    p = sub.add_parser("chat"); p.add_argument("--game", default="lol")
    p = sub.add_parser("backtest"); p.add_argument("game", nargs="?", default="lol"); p.add_argument("--full", action="store_true")
    p = sub.add_parser("report"); p.add_argument("games", nargs="*", default=["lol", "cs"])
    a = ap.parse_args(argv)

    if a.cmd == "update":
        from . import live, build_lol, build_cs
        for g in a.games:
            live.update(g)
            (build_lol if g == "lol" else build_cs).build()
    elif a.cmd == "search":
        from . import search
        q = " ".join(a.q)
        print("== Liquipedia ==")
        for t in search.wiki(q, a.game):
            print(" ", t)
        print("== 网页 ==")
        for r in search.web(q):
            print(f"  {r['title']}\n    {r['url']}\n    {r['snippet'][:100]}")
    elif a.cmd == "predict":
        from . import predict as P
        m = P.build(a.game, update=a.update)
        print(P.predict(m, a.a, a.b, a.bo, news=a.news)["text"])
    elif a.cmd == "status":
        from . import predict as P, chat
        m = P.build(a.game)
        print(chat.answer(m, a.team + " 状态"))
    elif a.cmd == "chat":
        from . import chat
        chat.loop(a.game)
    elif a.cmd == "backtest":
        from . import backtest as B
        o = B.backtest(a.game, strict=not a.full)
        print(B.summary(o))
    elif a.cmd == "report":
        from . import report
        sys.argv = ["report", *a.games]
        report.main(a.games)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
