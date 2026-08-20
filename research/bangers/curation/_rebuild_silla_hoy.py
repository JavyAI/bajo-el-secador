#!/usr/bin/env python3
"""Cut Romeo dump from Barbería HOY. Keep first 15. Fill with other official bachata."""
from __future__ import annotations

import json
import re
import ssl
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path("/Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador")
PUB = ROOT / "public/hoy/silla.json"
CUR = ROOT / "research/bangers/curation/silla-hoy.json"
COVERS = ROOT / "assets/covers"
CTX = ssl.create_default_context()
UA = "Mozilla/5.0 en-el-secador-verify"
ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")

# Official-looking HOY bachata that is not another Romeo album cut.
TIPICA_GUESTS = (
    "antony",
    "luis vargas",
    "raulín",
    "raulin",
    "frank reyes",
    "chaval",
    "teodoro",
    "zacarías",
    "zacarias",
    "joe veras",
    "monchy",
    "elvis martínez",
    "elvis martinez",
    "kiko",
    "luis segura",
    "del amargue",
)

CANDIDATES = [
    ("0-M3MkMCSso", "Antony Santos", "A Fuerza de Dolor"),
    ("cQTg0EKt9rc", "Antony Santos, Akon", "Hay Amores de Más"),
    ("TF7DZgRM_cw", "Luis Vargas", "Yo Tengo Un Ángel"),
    ("FdDaPzhTIQs", "Luis Vargas", "Mal Herido"),
    ("ed6XePWlMPY", "Luis Vargas", "Tarde Te Arrepientes"),
    ("sEDubeD2CKw", "Luis Vargas", "Volvió El Dolor"),
    ("ZB7mMiILVmQ", "Frank Reyes", "El Tubi"),
    ("Sq4In2ZvhTw", "Frank Reyes", "Me Haces Mucha Falta Amor"),
    ("Mp9Zax95fYI", "Frank Reyes", "Me Dejaste Abandonado"),
    ("ovfqdQrI8uE", "Raulín Rodríguez", "Cómo Serás Tú"),
    ("7ZCa6wELRVc", "Raulín Rodríguez", "Mi Gran Amor"),
    ("0tAWnSebr_8", "Raulín Rodríguez", "Hablamos En La Cama"),
    ("5HirJ6k5yzA", "Alex Bueno", "Que Vuelva"),
    ("QgCHwYbx_Q4", "Alex Bueno", "Yo Me Iré"),
    ("ePtOXORN96A", "Zacarías Ferreira", "Dime Que Faltó"),
    ("yUu6bxxRUGI", "Zacarías Ferreira", "Todos Juntos"),
    ("VY5zYtdhOCI", "Joe Veras", "Inténtalo Tú"),
    ("tP_XZ0teEno", "Yoskar Sarante, El Chaval de la Bachata", "Tres Veces"),
    ("Xr_jslGVFvo", "Grupo Extra", "Me Emborracharé"),
    ("IFfLjoKsHX0", "Grupo Extra", "Qué Mal Te Hice Yo"),
    ("nKN8tTN-_O0", "Grupo Extra", "Tengo Una Necesidad"),
    ("Q2HftVyi6wc", "Grupo Extra, Lirow", "Cuando Te Vuelva a Ver"),
    ("9kbFdKX1rJw", "Grupo Extra", "Lejos de Ti"),
    ("W1_7r-7D74I", "Grupo Extra", "Te Vas"),
    ("uXLkI5Lknpo", "Grupo Extra", "Dile a Él"),
    ("DjEttgmfNCU", "Henry Santos, JFab, Paola Fabre", "Cuando Te Toco"),
    ("rmerQRm3GJk", "Héctor Acosta", "Me Voy"),
    ("5MjbxCOy1Bo", "El Chaval de la Bachata", "La Locura de Tu Amor"),
    ("f6-QuSDqcNk", "Yoskar Sarante", "Tú, Él y Yo"),
    ("Ahsc80j8in8", "Yoskar Sarante", "Amor a Medio Tiempo"),
    ("Lpj2epjATXM", "Yoskar Sarante", "Quién Eres Tú"),
    ("g81JtMbrJtw", "Pinto Picasso", "París"),
    ("uUeNpTC7UWI", "Pinto Picasso", "No Me Toca"),
    ("2wHa_op488g", "Frank Reyes", "Como Hojas al Viento"),
    ("ot6wDVHqVNw", "Héctor Acosta", "Sin Perdón"),
    ("ZoO36O1sgyg", "Héctor Acosta", "Tu Veneno"),
    ("eshFzjIZZzA", "Bachata Heightz, Héctor Acosta", "Me Puedo Matar"),
    ("mp-g0oAGrOw", "Héctor Acosta", "Si No Me Falla El Corazón"),
    ("R5V-A-iu9dg", "Henry Santos", "Te Di"),
    ("VJSBbSlykM8", "Teodoro Reyes", "El Huequito"),
    ("4GU0sTsIpzo", "Teodoro Reyes", "Mis Dos Estrellas"),
    ("z285rG7DkhA", "Teodoro Reyes", "Me Dejó Por Otro"),
    ("b0vDALH-CUw", "Kewin Cosmos", "Déjame Tenerte"),
    ("S50Vs_y1W2A", "Kewin Cosmos", "La Vecina"),
    ("tNw9Rc3GbcE", "Daniel Santacruz", "Desnudos"),
    ("p2YCzaZNRqQ", "Daniel Santacruz", "No Me Sueltes"),
    ("1S7SJcEKfuY", "Elvis Martínez", "Tú Sabes Bien"),
    ("m9Xxk7pXE3s", "Elvis Martínez", "Rica"),
]


def lead(artist: str) -> str:
    return (artist or "").split(",")[0].strip().lower()


def is_romeo(artist: str) -> bool:
    return "romeo" in (artist or "").lower()


def oembed(vid: str) -> dict:
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=12, context=CTX) as r:
        return json.loads(r.read().decode("utf-8"))


def mq_ok(vid: str) -> bool:
    req = urllib.request.Request(
        f"https://i.ytimg.com/vi/{vid}/mqdefault.jpg",
        method="HEAD",
        headers={"User-Agent": UA},
    )
    try:
        with urllib.request.urlopen(req, timeout=12, context=CTX) as r:
            return r.status == 200
    except urllib.error.HTTPError as e:
        return e.code == 200
    except Exception:
        return False


def check(vid: str, artist: str, title: str) -> dict:
    rec = {"id": vid, "artist": artist, "title": title, "ok": False, "author": None, "yt": None, "err": None}
    try:
        if not mq_ok(vid):
            rec["err"] = "mq"
            return rec
        oe = oembed(vid)
        rec["yt"] = oe.get("title")
        rec["author"] = oe.get("author_name")
        rec["ok"] = bool(rec["yt"])
    except Exception as e:
        rec["err"] = str(e)
    return rec


def interleave(tracks: list, protect: int = 15) -> list:
    head = tracks[:protect]
    tail = tracks[protect:]
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


def to_public(tracks: list) -> dict:
    pub = []
    for i, t in enumerate(tracks):
        vid = t["id"]
        local = COVERS / f"{vid}.jpg"
        art = f"assets/covers/{vid}.jpg" if local.exists() else f"https://i.ytimg.com/vi/{vid}/mqdefault.jpg"
        pub.append(
            {
                "id": vid,
                "artist": t["artist"],
                "title": t["title"],
                "youtube": f"https://www.youtube.com/watch?v={vid}",
                "artwork": art,
                "artworkLarge": art,
                "intro": i < 15,
            }
        )
    return {
        "name": "silla",
        "room": "silla",
        "era": "hoy",
        "shuffle": False,
        "loop": True,
        "introCount": 15,
        "count": len(pub),
        "tracks": pub,
    }


def main() -> None:
    live = json.loads(PUB.read_text())["tracks"]
    head = live[:15]
    used = {t["id"] for t in head}

    def keep_old(t: dict) -> bool:
        a = t["artist"]
        if lead(a) == "prince royce":
            return False
        if is_romeo(a):
            low = a.lower()
            return any(g in low for g in TIPICA_GUESTS)
        return True

    keep_tail = []
    titles = {t["title"].strip().lower() for t in head}
    for t in live[15:]:
        if not keep_old(t):
            continue
        key = t["title"].strip().lower()
        if key in titles:
            continue
        keep_tail.append({"id": t["id"], "artist": t["artist"], "title": t["title"]})
        used.add(t["id"])
        titles.add(key)

    # Three shop-known solo Romeo after the 15, not the album dump.
    extra_romeo = [
        ("mhHqonzsuoA", "Romeo Santos", "Imitadora"),
        ("jk4HYngf65w", "Romeo Santos", "Cancioncitas de Amor"),
        ("4eCL0l9iD5A", "Romeo Santos", "Hilito"),
    ]
    # Four more Royce after the six already in the 15.
    extra_royce = [
        ("OST41MmjdTQ", "Prince Royce", "El Amor Que Perdimos"),
        ("OdaIbTUGmHM", "Prince Royce", "La Carretera"),
        ("-lDsqOsJL7k", "Prince Royce", "Culpa al Corazón"),
        ("XNGWDH-6yv8", "Prince Royce", "Corazón Sin Cara"),
    ]
    for vid, artist, title in extra_romeo + extra_royce:
        if vid not in used:
            keep_tail.append({"id": vid, "artist": artist, "title": title})
            used.add(vid)

    print("checking candidates")
    recs = []
    with ThreadPoolExecutor(max_workers=10) as pool:
        futs = [pool.submit(check, vid, artist, title) for vid, artist, title in CANDIDATES]
        for fut in as_completed(futs):
            recs.append(fut.result())

    ok = [r for r in recs if r["ok"] and r["id"] not in used]
    fail = [r for r in recs if not r["ok"]]
    print(f"candidates ok={len(ok)} fail={len(fail)}")
    for r in fail:
        print(" FAIL", r["id"], r["artist"], r["title"], r.get("err"), r.get("author"))
    for r in ok:
        key = r["title"].strip().lower()
        if key in titles:
            print(" SKIP dup", r["title"])
            continue
        print(" OK  ", r["id"], r["artist"], "—", r["title"], "|", r["author"])
        keep_tail.append({"id": r["id"], "artist": r["artist"], "title": r["title"]})
        used.add(r["id"])
        titles.add(key)

    tracks = head + keep_tail
    print(f"before pad n={len(tracks)}")
    if len(tracks) < 100:
        print(f"NEED {100-len(tracks)} more")
    tracks = tracks[:100]
    tracks = interleave(tracks, 15)

    from collections import Counter

    print("n", len(tracks), "consec", sum(1 for i in range(1, len(tracks)) if lead(tracks[i]["artist"]) == lead(tracks[i - 1]["artist"])))
    print("leads", Counter(lead(t["artist"]) for t in tracks).most_common(15))
    print("romeo any", sum(1 for t in tracks if is_romeo(t["artist"])))
    print("romeo solo", sum(1 for t in tracks if lead(t["artist"]) == "romeo santos" and "," not in t["artist"]))
    print("royce", sum(1 for t in tracks if lead(t["artist"]) == "prince royce"))
    print("first15", [t["title"] for t in tracks[:15]])

    if len(tracks) != 100:
        raise SystemExit(f"not 100: {len(tracks)}")

    CUR.write_text(json.dumps({"room": "silla", "era": "hoy", "count": 100, "introCount": 15, "tracks": [
        {**t, "official": True, "intro": i < 15} for i, t in enumerate(tracks)
    ]}, ensure_ascii=False, indent=2) + "\n")
    PUB.write_text(json.dumps(to_public(tracks), ensure_ascii=False, indent=2) + "\n")
    print("wrote", CUR, PUB)


if __name__ == "__main__":
    main()
