"""联网搜索：
- web(): 通用网页搜索（Bing），看新闻、阵容变动、伤病、赛程
- wiki(): 在 Liquipedia 里搜赛事 / 队伍页面
- results(): 在本地（已同步的）比赛数据里查两队最近交手和战绩
"""
import base64
import html as H
import re
from urllib.parse import parse_qs, urlparse

from . import liquipedia as L
from . import net


def _real_url(u):
    """Bing 的跳转链接里藏着真实网址（u=a1 + base64）。"""
    u = H.unescape(u)
    if "bing.com/ck/a" in u:
        q = parse_qs(urlparse(u).query).get("u", [""])[0]
        if q.startswith("a1"):
            s = q[2:]
            try:
                return base64.urlsafe_b64decode(s + "=" * (-len(s) % 4)).decode("utf-8", "ignore")
            except ValueError:
                pass
    return u


def web(query, n=8, ttl=1800):
    h = net.get("https://www.bing.com/search", dict(q=query, setlang="zh-Hans", count=20), gap=2.0, ttl=ttl)
    out = []
    for u, t, rest in re.findall(r'<li class="b_algo".*?<h2.*?<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>(.*?)</li>', h, re.S):
        d = re.search(r"<p[^>]*>(.*?)</p>", rest, re.S)
        out.append(dict(title=H.unescape(re.sub("<.*?>", "", t)).strip(), url=_real_url(u),
                        snippet=H.unescape(re.sub("<.*?>", "", d.group(1) if d else "")).strip()))
        if len(out) >= n:
            break
    return out


def wiki(query, game="lol", n=10):
    return L.search(query, "leagueoflegends" if game == "lol" else "counterstrike", n)


def results(team_a, team_b=None, game="lol", n=10):
    """本地数据里查最近比赛（先运行 update 同步最新赛果）。"""
    import pandas as pd
    from .names import norm
    if game == "lol":
        from . import build_lol
        g = build_lol.load()
        df = pd.DataFrame(dict(date=g.date, event=g.event, a=g.blue, b=g.red, win_a=g.blue_win))
    else:
        from . import build_cs
        g = build_cs.load()
        df = pd.DataFrame(dict(date=g.date, event=g.event, a=g.team1, b=g.team2, win_a=g.win1, map=g["map"]))
    na = norm(team_a, game)
    ka, kb = df.a.map(lambda x: norm(x, game)), df.b.map(lambda x: norm(x, game))
    m = (ka == na) | (kb == na)
    if team_b:
        nb = norm(team_b, game)
        m &= (ka == nb) | (kb == nb)
    return df[m].sort_values("date").tail(n)
