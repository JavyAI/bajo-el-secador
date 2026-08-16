#!/usr/bin/env python3
"""Rewrite Javy's unlisted YouTube playlists to match public/*.json order."""
from __future__ import annotations

import hashlib
import json
import time
import urllib.error
import urllib.request
from pathlib import Path

import browser_cookie3

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://www.youtube.com"
CLIENT = {"clientName": "WEB", "clientVersion": "2.20240815.01.00", "hl": "es", "gl": "DO"}
ROOMS = {
    "salon": "PLHGerkzq-_SQ",
    "barberia": "PLUXmVaLcUP14",
    "colmado": "PLHayRTekRcmM",
}


def cookies():
    return list(browser_cookie3.chrome(domain_name=".youtube.com"))


def sapisid_value(jar):
    by_name = {c.name: c.value for c in jar}
    return by_name.get("__Secure-3PAPISID") or by_name.get("SAPISID")


def auth(sapisid):
    ts = int(time.time())
    digest = hashlib.sha1(f"{ts} {sapisid} {ORIGIN}".encode()).hexdigest()
    return f"SAPISIDHASH {ts}_{digest}"


def innertube(path, payload, jar, sapisid):
    req = urllib.request.Request(
        f"https://www.youtube.com/youtubei/v1/{path}?prettyPrint=false",
        data=json.dumps(payload).encode(),
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0.0.0 Safari/537.36",
            "Origin": ORIGIN,
            "X-Origin": ORIGIN,
            "Referer": "https://www.youtube.com/",
            "Authorization": auth(sapisid),
            "Cookie": "; ".join(f"{c.name}={c.value}" for c in jar),
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=40) as response:
        return json.loads(response.read().decode())


def walk(obj, key, acc=None):
    if acc is None:
        acc = []
    if isinstance(obj, dict):
        if key in obj:
            acc.append(obj[key])
        for value in obj.values():
            walk(value, key, acc)
    elif isinstance(obj, list):
        for value in obj:
            walk(value, key, acc)
    return acc


def playlist_tokens(blob, pid):
    tokens = []
    for token in walk(blob, "token"):
        if not isinstance(token, str):
            continue
        if pid[2:10] in token or ("VL" + pid) in token:
            tokens.append(token)
        elif token.startswith("4qm") and pid[:8] in token:
            tokens.append(token)
    return tokens


def playlist_items(pid, jar, sapisid):
    ctx = {"client": CLIENT}
    data = innertube("browse", {"context": ctx, "browseId": "VL" + pid}, jar, sapisid)
    items = []
    seen = set()

    def absorb(blob):
        lists = walk(blob, "playlistVideoListRenderer") or [blob]
        for lst in lists:
            for renderer in walk(lst, "playlistVideoRenderer"):
                vid = renderer.get("videoId")
                sid = renderer.get("setVideoId")
                if not vid or not sid or sid in seen:
                    continue
                if sid == "to_be_updated_by_client":
                    continue
                seen.add(sid)
                items.append({"id": vid, "setVideoId": sid})

    absorb(data)
    tokens = playlist_tokens(data, pid)
    used = set()
    while tokens:
        token = tokens.pop(0)
        if token in used:
            continue
        used.add(token)
        more = innertube("browse", {"context": ctx, "continuation": token}, jar, sapisid)
        absorb(more)
        for nxt in playlist_tokens(more, pid):
            if nxt not in used:
                tokens.append(nxt)
        time.sleep(0.2)
    return items


def edit(pid, actions, jar, sapisid):
    return innertube(
        "browse/edit_playlist",
        {
            "context": {"client": CLIENT},
            "playlistId": pid,
            "actions": actions,
            "params": "CAFAAQ%3D%3D",
        },
        jar,
        sapisid,
    )


def edit_safe(pid, actions, jar, sapisid):
    try:
        return edit(pid, actions, jar, sapisid)
    except urllib.error.HTTPError:
        ok = None
        for action in actions:
            try:
                ok = edit(pid, [action], jar, sapisid)
            except urllib.error.HTTPError as err:
                print("   skip action", action.get("action"), action.get("setVideoId") or action.get("addedVideoId"), err.code)
            time.sleep(0.2)
        return ok


def chunks(seq, size):
    for i in range(0, len(seq), size):
        yield seq[i : i + size]


def desired_ids(room):
    data = json.loads((ROOT / "public" / f"{room}.json").read_text())
    ids = []
    seen = set()
    for track in data["tracks"]:
        vid = track["id"]
        if vid in seen:
            continue
        seen.add(vid)
        ids.append(vid)
    return ids


def rewrite(room, pid, jar, sapisid):
    want = desired_ids(room)
    have = playlist_items(pid, jar, sapisid)
    print(f"{room} have={len(have)} want={len(want)} first_want={want[0]}")
    for batch in chunks(have, 8):
        actions = [{"action": "ACTION_REMOVE_VIDEO", "setVideoId": item["setVideoId"]} for item in batch]
        edit_safe(pid, actions, jar, sapisid)
        time.sleep(0.35)
    print(f"  cleared {len(have)}")
    added = 0
    for batch in chunks(want, 8):
        actions = [{"action": "ACTION_ADD_VIDEO", "addedVideoId": vid} for vid in batch]
        edit_safe(pid, actions, jar, sapisid)
        added += len(batch)
        time.sleep(0.4)
    try:
        edit(pid, [{"action": "ACTION_SET_PLAYLIST_THUMBNAIL", "thumbnailVideoId": want[0]}], jar, sapisid)
    except Exception as err:
        print("  thumb skip", err)
    time.sleep(0.8)
    now = [item["id"] for item in playlist_items(pid, jar, sapisid)]
    ok = now == want
    print(f"  added={added} now={len(now)} match={ok} first_now={now[:5]}")
    if not ok:
        extra = [vid for vid in now if vid not in want]
        missing = [vid for vid in want if vid not in now]
        print("  extra", extra[:8], "missing", missing[:8])
        if now and now[0] != want[0]:
            print("  FIRST MISMATCH", now[0], "!=", want[0])
    return ok


def main():
    jar = cookies()
    sapisid = sapisid_value(jar)
    if not sapisid:
        raise SystemExit("No SAPISID in Chrome YouTube cookies. Sign into YouTube in Chrome.")
    results = {}
    for room, pid in ROOMS.items():
        results[room] = rewrite(room, pid, jar, sapisid)
    print("DONE", results)
    if not all(results.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
