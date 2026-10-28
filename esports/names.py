"""队名统一：不同数据源对同一支队伍写法不同（NaVi / Natus Vincere / natus vincere）。"""
import re
import unicodedata

# 规范化后的写法 -> 统一名
ALIASES = {
    # CS
    "navi": "natusvincere", "natusvincerenavi": "natusvincere",
    "nip": "ninjasinpyjamas", "mousesports": "mouz", "vp": "virtuspro",
    "fazeclan": "faze", "teamliquid": "liquid", "teamvitality": "vitality",
    "teamspirit": "spirit", "c9": "cloud9", "envyus": "envy", "nv": "envy",
    "teamenvyus": "envy", "teamdignitas": "dignitas", "sklgaming": "sk", "skgaming": "sk",
    "mibrteam": "mibr", "furiaesports": "furia", "g2esports": "g2", "fnaticesports": "fnatic",
    "teamfalcons": "falcons", "themongolz": "mongolz", "auroragaming": "aurora",
    "paingaming": "pain", "betboomteam": "betboom", "team3dmax": "3dmax", "3dmaxesports": "3dmax",
    "heroicesports": "heroic", "ence esports": "ence", "teamencesports": "ence",
    "complexitygaming": "complexity", "col": "complexity", "evilgeniuses": "eg",
    "astralisesports": "astralis", "hellraisersesports": "hellraisers", "hr": "hellraisers",
    "gambitesports": "gambit", "gambitgaming": "gambit", "tsm": "solomid", "teamsolomid": "solomid",
    "optiicgaming": "optic", "opticgaming": "optic", "luminositygaming": "luminosity",
    "sinnersesports": "sinners", "nemigagaming": "nemiga", "eternalfireesports": "eternalfire",
    "gamerlegionesports": "gamerlegion", "b8esports": "b8", "monteesports": "monte",
    "parivisionesports": "parivision", "teamtitan": "titan", "cphwolves": "copenhagenwolves",
    "teamldlc": "ldlc", "ldlcwhite": "ldlc", "ldlcblue": "ldlc", "teamldlccom": "ldlc",
    "flipsid3tactics": "flipsid3", "f3": "flipsid3", "kinguinesports": "kinguin",
    "pentasports": "penta", "teamkinguin": "kinguin", "ibp": "ibuypower",
    "counterlogicgaming": "clg", "cloud9g2a": "cloud9", "teamimmunity": "immunity",
    # LOL
    "sktelecomt1": "t1", "sktelecomt1k": "t1", "skt": "t1", "skt1": "t1", "sktt1": "t1",
    "t1esports": "t1", "samsunggalaxy": "samsung", "ssg": "samsung", "geng": "geng",
    "gengesports": "geng", "kingzonedragonx": "kingzone", "kzdx": "kingzone",
    "invictusgaming": "ig", "royalnevergiveup": "rng", "royalclub": "rng",
    "edwardgaming": "edg", "edgm": "edg", "funplusphoenix": "fpx", "topesports": "tes",
    "bilibiligaming": "blg", "jdgaming": "jdg", "jdgintelesportsclub": "jdg",
    "weibogaming": "wbg", "suninggaming": "sn", "suning": "sn", "lngesports": "lng",
    "teamwe": "we", "dplusk": "dk", "dpluskia": "dk", "damwongaming": "dk", "damwongamingdk": "dk",
    "dwg": "dk", "dwgkia": "dk", "hanwhalifeesports": "hle", "hanwhalife": "hle",
    "kttolster": "kt", "ktrolster": "kt", "ktbullets": "kt", "ktarrows": "kt",
    "teamsolomidlol": "tsm", "cloud9lol": "cloud9", "100thieves": "100t", "g2esportslol": "g2",
    "fnaticlol": "fnatic", "madlions": "madlions", "rogue": "rogue", "teamliquidhonda": "liquid",
    "flashwolves": "flashwolves", "ahqesportsclub": "ahq", "ahqesports": "ahq",
    "gamaniabears": "gamaniabears", "taipeiassassins": "taipeiassassins", "tpa": "taipeiassassins",
    "counterlogicgamingeurope": "clgeu", "clgeu": "clgeu", "moscowfive": "moscowfive", "m5": "moscowfive",
    "najinblacksword": "najinblacksword", "najinwhiteshield": "najinwhiteshield",
    "azubufrost": "cjentusfrost", "cjentusfrost": "cjentusfrost", "azububblaze": "cjentusblaze",
    "cjentusblaze": "cjentusblaze", "samsungwhite": "samsungwhite", "samsungblue": "samsungblue",
    "samsunggalaxywhite": "samsungwhite", "samsunggalaxyblue": "samsungblue",
    "gigabytemarines": "gigabytemarines", "gamt": "gamt", "teamflash": "teamflash",
    "omg": "omg", "ohmygod": "omg", "starhornroyalclub": "rng",
    "anyoneslegend": "al", "ninjasinpyjamaslol": "nip", "thundertalkgaming": "tt",
    "kwangdongfreecs": "kdf", "afreecafreecs": "kdf", "nongshimredforce": "ns",
    "fearx": "fearx", "liivsandbox": "fearx", "sandboxgaming": "fearx", "brion": "bro",
    "oksavingsbankbrion": "bro", "hanjinbrion": "bro",
}

# CS 专用（和 LOL 缩写冲突的放这里，例如 rng）
CS_ALIASES = {
    "astana": "astanadragons", "cphf": "copenhagenflames", "cw": "copenhagenwolves", "dig": "dignitas",
    "fnc": "fnatic", "imt": "immortals", "itb": "intothebreach", "qbf": "quantumbellatorfire",
    "rng": "renegades", "tl": "liquid", "vg": "vici", "vit": "vitality", "lg": "luminosity",
    "nv": "envy", "envyus": "envy", "f3": "flipsid3", "lgb": "lgbesports", "keydstars": "keyd",
    "cphwolves": "copenhagenwolves", "pkd": "playingducks", "myxmg": "myxmg", "esc": "escgaming",
    "ibp": "ibuypower", "bravado": "bravadogaming", "outsiders": "virtuspro",
}

# Liquipedia LOL 页面常用缩写
ALIASES.update({
    "nws": "najinwhiteshield", "shr": "rng", "ssb": "samsungblue", "ssw": "samsungwhite", "fnc": "fnatic",
    "koo": "roxtigers", "kootigers": "roxtigers", "roxt": "roxtigers", "og": "origen", "anx": "albusnoxluna",
    "lz": "longzhu", "longzhugaming": "longzhu", "msf": "misfits", "afs": "kdf", "grf": "griffin", "spy": "splyce",
    "gen": "geng", "madl": "madlions", "najinsword": "najinblacksword", "fw": "flashwolves", "h2k": "h2kgaming",
    "c9": "cloud9", "imt": "immortals", "tl": "liquid", "eg": "evilgeniuses", "fpx": "fpx", "blg": "blg",
    "drx": "drx", "dragonx": "drx", "dplus": "dk", "hle": "hle", "lng": "lng", "wbg": "wbg", "tes": "tes", "jdg": "jdg",
})

DROP_WORDS = r"(esports?|gaming|e-sports|team|club|clan)$"


_DYN = None


def _dynamic():
    """数据自动推断出的改名（enrich.py 生成）"""
    global _DYN
    if _DYN is None:
        import json
        from pathlib import Path
        f = Path(__file__).resolve().parent.parent / "data" / "processed" / "team_aliases.json"
        _DYN = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
    return _DYN


def norm(name, game=None) -> str:
    k = _norm(name, game)
    return _dynamic().get(k, k) if game != "cs" else k


def _norm(name, game=None) -> str:
    if name is None or (isinstance(name, float)):
        return ""
    s = unicodedata.normalize("NFKD", str(name)).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"[^a-z0-9]+", "", s)
    if game == "cs" and s in CS_ALIASES:
        return CS_ALIASES[s]
    if s in ALIASES:
        return ALIASES[s]
    t = re.sub(DROP_WORDS, "", s)
    t = re.sub(r"^team", "", t) or s
    return ALIASES.get(t, t or s)
