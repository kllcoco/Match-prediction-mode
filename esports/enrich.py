"""给「只有比分」的联网比赛补上首发和选手表现（LOL）。

Liquipedia 国内联赛总览页不带每局详情，所以：
1. 首发：赛事页的参赛名单（TeamParticipants），取每队上野中下辅五个非替补、非离队的人
2. 表现：赛事的 Player Stats 页（每人本赛段场均 K/D/A、参团率、分均伤害），
   换算成和训练数据同口径的「每局表现」填进去（伤害 = 分均伤害 × 31 分钟）
3. 改名认亲：新队名的首发里有 ≥3 人去年在同一支队 -> 认定是同一支队（写入 team_aliases.json）
"""
import html as H
import json
import re
from collections import Counter

import pandas as pd

from . import liquipedia as L
from . import live, net
from .names import norm
from .net import DATA

ALIAS_FILE = DATA / "processed" / "team_aliases.json"
POOL_FILE = DATA / "processed" / "player_pools.json"  # 选手本年英雄池大小（Player Stats 页的 Pool 列）
ROLES = {"top": 0, "jgl": 1, "jungle": 1, "mid": 2, "bot": 3, "adc": 3, "sup": 4, "support": 4}
AVG_MIN = 31.0


def rosters(root):
    """赛事参赛名单 -> {队伍: [上, 野, 中, 下, 辅]}"""
    src = L.wikitext(root) or ""
    out = {}
    for m in re.finditer(r"\{\{Opponent\|([^|\n}]+)", src):
        team = m.group(1).strip()
        blk = src[m.end(): m.end() + 3000]
        blk = blk[: blk.find("{{Opponent|")] if "{{Opponent|" in blk else blk
        ros = [None] * 5
        for p in re.findall(r"\{\{Person\|([^}]*)\}\}", blk):
            parts = [x.strip() for x in p.split("|")]
            kv = dict(x.split("=", 1) for x in parts if "=" in x)
            name = next((x for x in parts if "=" not in x), None)
            if name:
                name = re.sub(r"\s*\(.*?\)\s*$", "", name)  # 去掉消歧义后缀，如 "Berserker (Korean player)"
            if not name or kv.get("type") == "staff" or kv.get("status") in ("sub", "former", "inactive"):
                continue
            role = ROLES.get(kv.get("role", "").split(",")[0].strip().lower())
            if role is not None and ros[role] is None:
                ros[role] = name
        if all(ros):
            out[team] = ros
    return out


def player_stats(root, ttl=None):
    """赛事 Player Stats 页 -> {选手名: dict(gp, w, k, d, a, kp, dpm, role)}"""
    try:
        d = net.get(L.API.format(wiki="leagueoflegends"),
                    dict(action="parse", page=f"{root.replace('_', ' ')}/Player Stats", prop="text", format="json"),
                    gap=31, as_json=True, ttl=ttl)
    except RuntimeError:
        return {}
    if "parse" not in d:
        return {}
    h = d["parse"]["text"]["*"]
    out = {}
    for t in re.findall(r"<table.*?</table>", h, re.S):
        if "DPM" not in t or "KP%" not in t:
            continue
        for r in re.findall(r"<tr[^>]*>(.*?)</tr>", t, re.S):
            c = [H.unescape(re.sub(r"<[^>]+>", "", x)).strip() for x in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", r, re.S)]
            if len(c) < 15 or not c[3].isdigit():
                continue
            try:
                out[c[1]] = dict(role=c[2].lower(), gp=int(c[3]), wr=float(c[6].rstrip("%")) / 100,
                                 k=float(c[8]), d=float(c[9]), a=float(c[10]), kp=float(c[11].rstrip("%")) / 100,
                                 dpm=float(c[14]), pool=int(c[16]) if len(c) > 16 and c[16].isdigit() else None)
            except ValueError:
                continue
    return out


def team_aliases(df_live, old_games):
    """新队名 -> 旧队名（首发 ≥3 人去年同队）"""
    last = {}
    o = old_games[old_games.date >= "2025-01-01"]
    for side in ("b", "r"):
        team = o["blue" if side == "b" else "red"].map(norm)
        for i in range(1, 6):
            for t, p in zip(team, o[f"{side}n{i}"]):
                if isinstance(p, str):
                    last.setdefault(p.lower(), Counter())[t] += 1
    known = set(o.blue.map(norm)) | set(o.red.map(norm))
    alias = {}
    for side in ("b", "r"):
        for t, *ps in df_live[["blue" if side == "b" else "red"] + [f"{side}n{i}" for i in range(1, 6)]].drop_duplicates().values:
            k = norm(t)
            if k in known or k in alias:
                continue
            votes = Counter()
            for p in ps:
                if isinstance(p, str) and p.lower() in last:
                    votes[last[p.lower()].most_common(1)[0][0]] += 1
            if votes and votes.most_common(1)[0][1] >= 3:
                alias[k] = votes.most_common(1)[0][0]
    return alias


def enrich(years=(2026,)):
    from . import build_lol
    p = live.OUT["lol"]
    df = pd.read_csv(p, low_memory=False)
    roots = live.tournaments("lol", set(years))
    filled = 0
    pools = {}
    for root in roots:
        ev = root.replace("_", " ")
        ros = rosters(root)
        if not ros:
            continue
        st = player_stats(root)
        for name, v in st.items():
            if v.get("pool"):
                pools[f"lol:{name.lower()}"] = max(pools.get(f"lol:{name.lower()}", 0), v["pool"])
        # 同位置平均（用来算「比平均对手强多少」）
        role_avg = {}
        for v in st.values():
            role_avg.setdefault(v["role"], []).append(v)
        ravg = {r: dict(kad=sum((x["k"] + x["a"] - x["d"]) * x["gp"] for x in vs) / max(sum(x["gp"] for x in vs), 1),
                        dpm=sum(x["dpm"] * x["gp"] for x in vs) / max(sum(x["gp"] for x in vs), 1)) for r, vs in role_avg.items()}
        rk = {norm(t): r for t, r in ros.items()}
        m = df.event.astype(str).str.replace("_", " ") == ev
        for side in ("b", "r"):
            team = df.loc[m, "blue" if side == "b" else "red"].map(norm)
            for idx, t in zip(team.index, team):
                r = rk.get(t)
                if not r or isinstance(df.at[idx, f"{side}n1"], str):
                    continue
                for i, name in enumerate(r, 1):
                    df.at[idx, f"{side}n{i}"] = name
                    s = st.get(name)
                    if s:
                        df.at[idx, f"{side}k{i}"] = s["k"]
                        df.at[idx, f"{side}d{i}"] = s["d"]
                        df.at[idx, f"{side}a{i}"] = s["a"]
                        df.at[idx, f"{side}dmg{i}"] = s["dpm"] * AVG_MIN
                if s:
                    df.at[idx, "gamelength"] = AVG_MIN * 60
                filled += 1
        print(f"{root}: 名单 {len(ros)} 队, 选手数据 {len(st)} 人")
    df.to_csv(p, index=False, compression="gzip")
    POOL_FILE.write_text(json.dumps(pools, ensure_ascii=False), encoding="utf-8")
    old = build_lol.load()
    old = old[old.source != "liquipedia-live"]
    al = team_aliases(df, old)
    ALIAS_FILE.write_text(json.dumps(al, ensure_ascii=False, indent=1), encoding="utf-8")
    print("补全", filled, "条；自动认亲：", al)


if __name__ == "__main__":
    enrich()
