"""联网基础：带缓存、限速、重试的 HTTP 请求。"""
import hashlib
import json
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CACHE = DATA / "cache"
UA = "MatchPredictionToy/0.1 (hobby esports research project)"

_session = requests.Session()
_session.headers.update({"User-Agent": UA, "Accept-Encoding": "gzip"})
_last_call: dict[str, float] = {}


def _wait(host: str, gap: float):
    dt = time.time() - _last_call.get(host, 0)
    if dt < gap:
        time.sleep(gap - dt)
    _last_call[host] = time.time()


def get(url: str, params: dict | None = None, gap: float = 1.0, cache: bool = True,
        retries: int = 4, as_json: bool = False, ttl: float | None = None):
    """GET 请求。gap=同一网站两次请求的最小间隔秒数（礼貌爬取）；ttl=缓存有效秒数（None=永久）。"""
    key = hashlib.md5((url + json.dumps(params or {}, sort_keys=True)).encode()).hexdigest()
    path = CACHE / f"{key}.txt"
    if cache and path.exists() and (ttl is None or time.time() - path.stat().st_mtime < ttl):
        text = path.read_text(encoding="utf-8")
        return json.loads(text) if as_json else text
    host = url.split("/")[2]
    for i in range(retries):
        _wait(host, gap)
        try:
            r = _session.get(url, params=params, timeout=30)
            text = r.text
            if r.status_code == 200 and text.strip():
                if as_json:
                    data = json.loads(text)
                    if "error" in data:
                        raise ValueError(data["error"])
                if cache:
                    CACHE.mkdir(parents=True, exist_ok=True)
                    path.write_text(text, encoding="utf-8")
                return json.loads(text) if as_json else text
        except (requests.RequestException, ValueError):
            pass
        time.sleep(gap * 2 ** (i + 1))
    raise RuntimeError(f"请求失败: {url} {params}")


def download(url: str, dest: Path, chunk: int = 1 << 20) -> Path:
    """下载大文件（已存在就跳过）。"""
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    with _session.get(url, stream=True, timeout=600) as r:
        r.raise_for_status()
        with open(tmp, "wb") as f:
            for b in r.iter_content(chunk):
                f.write(b)
    tmp.rename(dest)
    return dest
