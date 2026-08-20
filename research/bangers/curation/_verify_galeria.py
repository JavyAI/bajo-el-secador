#!/usr/bin/env python3
"""Verify galería candidate YouTube ids: oEmbed + mqdefault 200 + RYD views."""
import json
import ssl
import time
import urllib.error
import urllib.request
from pathlib import Path

CTX = ssl.create_default_context()

def get_json(url, timeout=12):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 galeria-curation"})
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        return json.loads(r.read().decode("utf-8"))

def head_status(url, timeout=12):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0 galeria-curation"})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code

def oembed(vid):
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    return get_json(url)

def ryd(vid):
    return get_json(f"https://returnyoutubedislikeapi.com/votes?videoId={vid}")

def mq(vid):
    return head_status(f"https://i.ytimg.com/vi/{vid}/mqdefault.jpg")

def main():
    ids = [ln.strip() for ln in Path("/tmp/galeria_ids.txt").read_text().splitlines() if ln.strip()]
    out_path = Path("/tmp/galeria_verify.json")
    out = json.loads(out_path.read_text()) if out_path.exists() else []
    done = {r["id"] for r in out}
    for i, vid in enumerate(ids, 1):
        if vid in done:
            continue
        rec = {"id": vid, "mq": None, "title": None, "author": None, "views": None, "ok": False, "err": None}
        try:
            rec["mq"] = mq(vid)
            oe = oembed(vid)
            rec["title"] = oe.get("title")
            rec["author"] = oe.get("author_name")
            try:
                rec["views"] = ryd(vid).get("viewCount")
            except Exception as e:
                rec["err"] = f"ryd:{e}"
            rec["ok"] = rec["mq"] == 200 and bool(rec["title"])
        except Exception as e:
            rec["err"] = str(e)
        out.append(rec)
        flag = "OK" if rec["ok"] else "FAIL"
        print(f"{i:03d} {flag} {vid} mq={rec['mq']} views={rec['views']} | {rec['author']} | {rec['title']} | {rec['err'] or ''}", flush=True)
        time.sleep(0.12)
        Path("/tmp/galeria_verify.json").write_text(json.dumps(out, ensure_ascii=False, indent=2))
    ok = sum(1 for r in out if r["ok"])
    print(f"DONE {ok}/{len(out)} ok", flush=True)

if __name__ == "__main__":
    main()
