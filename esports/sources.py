"""下载原始数据集（都是公开数据）。

LOL: Oracle's Elixir 每局比赛数据（HF 镜像 2014-2023 + Kaggle 镜像 2024/2025）
CS : HLTV 抓取的公开数据集（Kaggle）
"""
import zipfile

from .net import DATA, download

RAW = DATA / "raw"
KAGGLE = "https://www.kaggle.com/api/v1/datasets/download/"

LOL_FILES = {
    "oe_2014_2023.csv": "https://huggingface.co/datasets/eligrayy/OE-LoL-Esports-Dataset/resolve/main/OE-LoL-Esports-Data.csv",
    "oe_2024.csv": KAGGLE + "toofxd/lol-esports-match-data-from-oracleselixir/2024_LoL_esports_match_data_from_OraclesElixir.csv",
    "oe_2025.csv": KAGGLE + "toofxd/lol-esports-match-data-from-oracleselixir/2025_LoL_esports_match_data_from_OraclesElixir.csv",
}

CS_ZIPS = {
    "cs_2015_2020": "mateusdmachado/csgo-professional-matches",      # 2015-11 ~ 2020-03，地图级 + veto
    "cs_2013_2020": "camilohernndez/csgo-50000-professional-matches-results",  # 2013-11 ~ 2020-06，系列赛比分
    "cs_2020_2022": "nafisbarizki/csgo-top-tier-match-jan-2020-dec-2022",  # 地图级
    "cs_2023_2026": "ektarr/counter-strike-pro-matches",               # 2023-01 ~ 至今，地图级
}


def fetch_all():
    for name, url in LOL_FILES.items():
        print("下载", name)
        download(url, RAW / name)
    for name, ref in CS_ZIPS.items():
        z = download(KAGGLE + ref, RAW / f"{name}.zip")
        out = RAW / name
        if not out.exists():
            zipfile.ZipFile(z).extractall(out)
        print("下载", name, "OK")


if __name__ == "__main__":
    fetch_all()
