#!/usr/bin/env python3
"""Create, rename, and rewrite Javy's unlisted YouTube playlists
to match public/ayer and public/hoy catalogs."""
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
MAP_PATH = ROOT / "public" / "playlists.json"
MUSIC = "https://music.youtube.com/playlist?list="

ROOMS = [
    {
        "id": "colmado",
        "catalog": "colmado.json",
        "ayer": {"name": "Sopita Colmado", "id": "PLHayRTekRcmM"},
        "hoy": {"name": "Sopita Colmado de noche", "id": None},
    },
    {
        "id": "secador",
        "catalog": "secador.json",
        "ayer": {"name": "Sopita Secador", "id": "PLHGerkzq-_SQ"},
        "hoy": {"name": "Sopita Secador de noche", "id": None},
    },
    {
        "id": "barberia",
        "catalog": "silla.json",
        "ayer": {"name": "Sopita Barbería", "id": "PLUXmVaLcUP14"},
        "hoy": {"name": "Sopita Barbería de noche", "id": None},
    },
    {
        "id": "limpieza",
        "catalog": "limpieza.json",
        "ayer": {"name": "Sopita Limpieza", "id": "PLPt3jPOVTIrw"},
        "hoy": {"name": "Sopita Limpieza de noche", "id": None},
    },
    {
        "id": "galeria",
        "catalog": "galeria.json",
        "ayer": {"name": "Sopita Galería", "id": None},
        "hoy": {"name": "Sopita Galería de noche", "id": None},
    },
    {
        "id": "malecon",
        "catalog": "malecon.json",
        "ayer": {"name": "Sopita Malecón", "id": None},
        "hoy": {"name": "Sopita Malecón de noche", "id": None},
    },
    {
        "id": "tierra",
        "catalog": "abuela.json",
        "ayer": {"name": "Sopita Mi Tierra", "id": "PLYEH_60hjSxM"},
        "hoy": {"name": "Sopita Mi Tierra de noche", "id": "PLT4NHEltF4xE"},
    },
]


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
        body = response.read().decode()
        return json.loads(body) if body else {}


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


def first_playlist_id(obj):
    found = []

    def hunt(node):
        if isinstance(node, dict):
            value = node.get("playlistId")
            if isinstance(value, str) and value.startswith("PL"):
                found.append(value)
            for child in node.values():
                hunt(child)
        elif isinstance(node, list):
            for child in node:
                hunt(child)

    hunt(obj)
    return found[0] if found else None


def playlist_title(pid, jar, sapisid):
    data = innertube("browse", {"context": {"client": CLIENT}, "browseId": "VL" + pid}, jar, sapisid)
    meta = (data.get("metadata") or {}).get("playlistMetadataRenderer") or {}
    return meta.get("title") or ""


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
        time.sleep(0.15)
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
                print("   skip", action.get("action"), action.get("addedVideoId") or action.get("setVideoId"), err.code)
            time.sleep(0.15)
        return ok


def chunks(seq, size):
    for i in range(0, len(seq), size):
        yield seq[i : i + size]


def desired_ids(catalog_file, era):
    data = json.loads((ROOT / "public" / era / catalog_file).read_text())
    ids = []
    seen = set()
    for track in data.get("tracks") or []:
        vid = track.get("id")
        if not vid or vid in seen:
            continue
        seen.add(vid)
        ids.append(vid)
    return ids


def load_map():
    if MAP_PATH.exists():
        return json.loads(MAP_PATH.read_text())
    return {}


def save_map(blob):
    MAP_PATH.write_text(json.dumps(blob, ensure_ascii=False, indent=2) + "\n")


def create_playlist(title, jar, sapisid):
    data = innertube(
        "playlist/create",
        {"context": {"client": CLIENT}, "title": title, "privacyStatus": "UNLISTED"},
        jar,
        sapisid,
    )
    pid = first_playlist_id(data)
    if not pid:
        raise RuntimeError("create returned no playlistId: " + json.dumps(data)[:400])
    return pid


def rename_playlist(pid, title, jar, sapisid):
    edit(pid, [{"action": "ACTION_SET_PLAYLIST_NAME", "playlistName": title}], jar, sapisid)


def rewrite(label, pid, want, jar, sapisid):
    have = playlist_items(pid, jar, sapisid)
    have_ids = [item["id"] for item in have]
    print(f"  {label} have={len(have_ids)} want={len(want)}")
    if have_ids == want:
        print("  already matches")
        return True
    if have:
        for batch in chunks(have, 8):
            actions = [{"action": "ACTION_REMOVE_VIDEO", "setVideoId": item["setVideoId"]} for item in batch]
            edit_safe(pid, actions, jar, sapisid)
            time.sleep(0.25)
        print(f"  cleared {len(have)}")
    added = 0
    for batch in chunks(want, 8):
        actions = [{"action": "ACTION_ADD_VIDEO", "addedVideoId": vid} for vid in batch]
        edit_safe(pid, actions, jar, sapisid)
        added += len(batch)
        time.sleep(0.3)
    if want:
        try:
            edit(pid, [{"action": "ACTION_SET_PLAYLIST_THUMBNAIL", "thumbnailVideoId": want[0]}], jar, sapisid)
        except Exception as err:
            print("  thumb skip", err)
    time.sleep(0.5)
    now = [item["id"] for item in playlist_items(pid, jar, sapisid)]
    ok = now == want
    print(f"  added={added} now={len(now)} match={ok}")
    if not ok:
        extra = [vid for vid in now if vid not in want]
        missing = [vid for vid in want if vid not in now]
        print("  extra", extra[:6], "missing", missing[:6])
    return ok


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--room", action="append", help="Limit to room id, repeatable")
    args = parser.parse_args()
    only = set(args.room or [])

    jar = cookies()
    sapisid = sapisid_value(jar)
    if not sapisid:
        raise SystemExit("No SAPISID in Chrome YouTube cookies. Sign into YouTube in Chrome.")

    saved = load_map()
    results = {}

    for room in ROOMS:
        if only and room["id"] not in only:
            continue
        room_id = room["id"]
        saved_room = saved.get(room_id) or {}
        out_room = {}
        for era in ("ayer", "hoy"):
            spec = room[era]
            name = spec["name"]
            saved_era = saved_room.get(era) or {}
            pid = spec["id"] or saved_era.get("id")
            if not pid:
                print(f"CREATE {name}")
                pid = create_playlist(name, jar, sapisid)
                print(f"  id={pid}")
                time.sleep(0.4)
            else:
                print(f"USE {name} {pid}")
            try:
                current = playlist_title(pid, jar, sapisid)
            except Exception as err:
                current = f"<err {err}>"
            if current != name:
                print(f"  rename {current!r} -> {name!r}")
                rename_playlist(pid, name, jar, sapisid)
                time.sleep(0.3)
            want = desired_ids(room["catalog"], era)
            ok = rewrite(f"{room_id}/{era}", pid, want, jar, sapisid)
            results[f"{room_id}:{era}"] = ok
            out_room[era] = {
                "id": pid,
                "name": name,
                "url": MUSIC + pid,
                "catalog": f"public/{era}/{room['catalog']}",
            }
        saved[room_id] = out_room
        save_map(saved)

    print("DONE", results)
    print("MAP", MAP_PATH)
    if not all(results.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
