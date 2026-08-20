#!/usr/bin/env python3
"""Hygiene + promote research catalogs into public/ayer and public/hoy."""
from __future__ import annotations

import json
import re
import ssl
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path("/Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador")
CUR = ROOT / "research/bangers/curation"
PUB = ROOT / "public"
COVERS = ROOT / "assets/covers"
ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")
CTX = ssl.create_default_context()
UA = "Mozilla/5.0 en-el-secador-verify"

NAMES = {
    "colmado": "colmado",
    "secador": "secador",
    "silla": "silla",
    "limpieza": "limpieza",
    "galeria": "galeria",
    "malecon": "malecon",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def tracks_of(data) -> list:
    return list(data.get("tracks") or data)


def lead(artist: str) -> str:
    return (artist or "").split(",")[0].strip().lower()


def consec_count(tracks: list) -> int:
    n = 0
    for i in range(1, len(tracks)):
        a, b = lead(tracks[i - 1].get("artist")), lead(tracks[i].get("artist"))
        if a and a == b:
            n += 1
    return n


def interleave(tracks: list, protect: int = 15) -> list:
    head = tracks[:protect]
    tail = tracks[protect:]
    if not tail:
        return tracks
    last = lead(head[-1].get("artist")) if head else ""
    remaining = list(tail)
    out = list(head)
    while remaining:
        picked = None
        for i, t in enumerate(remaining):
            if lead(t.get("artist")) != last:
                picked = remaining.pop(i)
                break
        if picked is None:
            picked = remaining.pop(0)
        out.append(picked)
        last = lead(picked.get("artist"))
    return out


def to_public(room: str, era: str, tracks: list) -> dict:
    pub = []
    for i, t in enumerate(tracks):
        vid = t["id"]
        local = COVERS / f"{vid}.jpg"
        art = f"assets/covers/{vid}.jpg" if local.exists() else f"https://i.ytimg.com/vi/{vid}/mqdefault.jpg"
        pub.append(
            {
                "id": vid,
                "artist": t.get("artist") or "",
                "title": t.get("title") or "",
                "youtube": t.get("youtube") or f"https://www.youtube.com/watch?v={vid}",
                "artwork": art,
                "artworkLarge": art,
                "intro": i < 15,
            }
        )
    return {
        "name": NAMES[room],
        "room": room,
        "era": era,
        "shuffle": False,
        "loop": True,
        "introCount": 15,
        "count": len(pub),
        "tracks": pub,
    }


def fetch_status(url: str, timeout: int = 12) -> int:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return 0


def oembed(vid: str) -> dict:
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=12, context=CTX) as r:
        return json.loads(r.read().decode("utf-8"))


def verify_ids(ids: list[str]) -> list[dict]:
    results = []

    def one(vid: str) -> dict:
        rec = {"id": vid, "mq": None, "title": None, "author": None, "ok": False, "err": None}
        try:
            rec["mq"] = fetch_status(f"https://i.ytimg.com/vi/{vid}/mqdefault.jpg")
            oe = oembed(vid)
            rec["title"] = oe.get("title")
            rec["author"] = oe.get("author_name")
            rec["ok"] = rec["mq"] == 200 and bool(rec["title"])
        except Exception as e:
            rec["err"] = str(e)
        return rec

    with ThreadPoolExecutor(max_workers=12) as pool:
        futs = {pool.submit(one, vid): vid for vid in ids}
        for fut in as_completed(futs):
            results.append(fut.result())
    return results


def structural(tracks: list) -> list[str]:
    errs = []
    if len(tracks) != 100:
        errs.append(f"count {len(tracks)} != 100")
    ids = [t.get("id") for t in tracks]
    if len(ids) != len(set(ids)):
        errs.append("duplicate ids")
    bad = [i for i in ids if not ID_RE.fullmatch(i or "")]
    if bad:
        errs.append(f"bad ids {bad[:5]}")
    c = consec_count(tracks)
    if c:
        errs.append(f"consecutive artists {c}")
    if sum(1 for i, t in enumerate(tracks) if t.get("intro")) not in (0, 15) and any(
        "intro" in t for t in tracks
    ):
        pass
    return errs


def promote_one(room: str, era: str, *, fix_consec: bool, write: bool) -> dict:
    src = CUR / f"{room}-{era}.json"
    data = load(src)
    tracks = tracks_of(data)
    before = consec_count(tracks)
    if fix_consec:
        tracks = interleave(tracks, 15)
        data["tracks"] = tracks
        data["count"] = len(tracks)
        src.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    after = consec_count(tracks)
    struct = structural(tracks)
    report = {
        "room": room,
        "era": era,
        "n": len(tracks),
        "consec_before": before,
        "consec_after": after,
        "struct": struct,
        "wrote": False,
    }
    if write and len(tracks) == 100:
        dest = PUB / era / f"{room}.json"
        dest.write_text(json.dumps(to_public(room, era, tracks), ensure_ascii=False, indent=2) + "\n")
        report["wrote"] = True
        report["dest"] = str(dest)
    return report


if __name__ == "__main__":
    write = "--write" in sys.argv
    verify = "--verify" in sys.argv
    jobs = []
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if args:
        for token in args:
            room, era = token.split("-", 1)
            jobs.append((room, era))
    else:
        jobs = [
            ("galeria", "ayer"),
            ("galeria", "hoy"),
            ("malecon", "ayer"),
            ("malecon", "hoy"),
            ("secador", "ayer"),
            ("secador", "hoy"),
            ("colmado", "hoy"),
        ]
    reports = []
    for room, era in jobs:
        src = CUR / f"{room}-{era}.json"
        if not src.exists():
            print(f"SKIP missing {src.name}")
            continue
        n = len(tracks_of(load(src)))
        if n != 100:
            print(f"SKIP {room}-{era} n={n}")
            continue
        r = promote_one(room, era, fix_consec=True, write=write)
        reports.append(r)
        print(
            f"{room}-{era} n={r['n']} consec {r['consec_before']}→{r['consec_after']} "
            f"struct={r['struct'] or 'ok'} wrote={r['wrote']}"
        )

    if verify:
        ids = []
        for r in reports:
            src = CUR / f"{r['room']}-{r['era']}.json"
            ids.extend(t["id"] for t in tracks_of(load(src)))
        uniq = sorted(set(ids))
        print(f"VERIFY {len(uniq)} ids")
        recs = verify_ids(uniq)
        fail = [x for x in recs if not x["ok"]]
        out = ROOT / "research/bangers/curation/_verify_out.json"
        out.write_text(json.dumps(recs, ensure_ascii=False, indent=2))
        print(f"VERIFY ok={len(recs)-len(fail)}/{len(recs)} fail={len(fail)}")
        for x in fail[:30]:
            print(f"  FAIL {x['id']} mq={x['mq']} {x.get('err') or x.get('title')}")
