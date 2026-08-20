#!/usr/bin/env python3
"""Recut Limpieza AYER + HOY. Doorway first. Official 11-char only."""
from __future__ import annotations

import json
import re
import ssl
import urllib.error
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path("/Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador")
CUR = ROOT / "research/bangers/curation"
CTX = ssl.create_default_context()
UA = "Mozilla/5.0 domingo-de-limpieza-curator"
ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")

# Authored #1s stay. Forgotten #1 sits in the 15, never opener.
# AYER forgotten #1 = Kulikitaka (the Sunday shout that almost opened).
# HOY forgotten #1 = Toma Mi Vida (2011 house monument).
# Do not steal: Secador funeral, Colmado salsa, Galería porch,
# Malecón couple-walk, Marquesina patio, Barbería típica.

AYER_15 = [
    "E6soE-1p3kw",  # Milly Volvió Juanita — locked #1
    "yWSQxGppcFA",  # Eddy Pégame Tu Vicio
    "GRo0nnF5OXY",  # JuanGa Te Sigo Amando
    "3LCEzvkwWwI",  # Toño Kulikitaka — forgotten #1
    "1pr7Fv-9Z3I",  # Ana Evidencias
    "S5tcXtlhmF8",  # Wilfrido El Jardinero
    "48SWXqe1K-8",  # Myriam Huele a Peligro
    "ydz-OjoIyuo",  # Rosario Dominicana
    "eLTvctdHftc",  # Kinito Cachamba
    "3CqNeJLqvL0",  # Elvis Tu Sonrisa
    "_tNVEhSelH0",  # JuanGa Abrázame Muy Fuerte
    "wit3kfPhXqE",  # Olga Cuando Tú No Estás
    "f7-vEi-uPB8",  # Wilfrido / Rubby Volveré
    "CwfCO_CRKqw",  # Rocío Como Tu Mujer
    "hBhIA8lDi2c",  # Elvis Píntame
]

HOY_15 = [
    "hal7rXfJj5o",  # Toño Dale Vieja Dale — locked #1
    "vqEdCsOgy9E",  # Milly / JLG Toma Mi Vida — forgotten #1
    "bWTfpdD4nRM",  # Olga Vivo La Vida
    "B2SLbC8fnfs",  # Elvis / Manny Imaginarme Sin Ti
    "VkuRIZ7QyDM",  # Chayanne Madre Tierra
    "K3S96fUGrEY",  # JLG Mambo 23
    "P2zOb0HGdxg",  # Natalia Creo en Mí
    "ym2clIz5t4A",  # Manny / Milly Llegaste
    "dyM5fHdbowM",  # Eddy Si Yo Se Lo Pido
    "lswYpEtVAUw",  # Toño Compréndeme
    "sHRzCQEHpU8",  # Manny De Lunes a Lunes
    "0K6ItvTTpe8",  # Miriam Me Enamoré De Ti
    "WENJIxEfyaw",  # JLG La Noviecita
    "qhOPeeZHSWE",  # Rosario Nuevecita de Caja
    "Daf4icdvGPQ",  # Olga Así Yo Soy
]

HOY_DROP = {
    "TOgCeRQvzoY",  # Kany Confieso — Secador door
    "5R1RGl4WQP8",  # Mon Laferte Tu Falta de Querer — Secador door
    "I9cCPQVPv8o",  # Arjona Fuiste Tú — Galería door
    "5AkDqm-cEgg",  # Camilo Tutu — Malecón door
}

HOY_ADD = [
    {
        "id": "SRDkwORUPak",
        "artist": "Toño Rosario",
        "title": "Vuelve Mami",
        "year": 2020,
        "channel": "Toño Rosario",
        "views": 27800000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "qhOPeeZHSWE",
        "artist": "Los Hermanos Rosario",
        "title": "Nuevecita de Caja",
        "year": 2015,
        "channel": "Los Hermanos Rosario",
        "views": 6000000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "-_fCguTGj88",
        "artist": "Milly Quezada, Ilegales",
        "title": "De Colores",
        "year": 2018,
        "channel": "MillyQuezada",
        "views": 1300000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "h-Mft5aVAiM",
        "artist": "Elvis Crespo, El Blachy",
        "title": "Me Mataron",
        "year": 2024,
        "channel": "Elvis Crespo",
        "views": 7800000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
]


def lead(artist: str) -> str:
    return (artist or "").split(",")[0].strip().lower()


def oembed(vid: str) -> dict:
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=14, context=CTX) as r:
        return json.loads(r.read().decode("utf-8"))


def mq_ok(vid: str) -> bool:
    req = urllib.request.Request(
        f"https://i.ytimg.com/vi/{vid}/mqdefault.jpg",
        method="HEAD",
        headers={"User-Agent": UA},
    )
    try:
        with urllib.request.urlopen(req, timeout=14, context=CTX) as r:
            return r.status == 200
    except urllib.error.HTTPError as e:
        return e.code == 200
    except Exception:
        return False


def check(vid: str) -> dict:
    rec = {"id": vid, "ok": False, "title": None, "author": None, "err": None, "artworkOk": False}
    if not ID_RE.match(vid or ""):
        rec["err"] = "id"
        return rec
    try:
        rec["artworkOk"] = mq_ok(vid)
        if not rec["artworkOk"]:
            rec["err"] = "mq"
            return rec
        oe = oembed(vid)
        rec["title"] = oe.get("title")
        rec["author"] = oe.get("author_name")
        rec["ok"] = bool(rec["title"])
        if not rec["ok"]:
            rec["err"] = "empty-oembed"
    except Exception as e:
        rec["err"] = str(e)[:160]
    return rec


def interleave(tracks: list, protect: int = 15) -> list:
    head = tracks[:protect]
    tail = tracks[protect:]
    last = lead(head[-1]["artist"]) if head else ""
    remaining = list(tail)
    out = list(head)
    while remaining:
        picked = None
        for i, t in enumerate(remaining):
            if lead(t["artist"]) != last:
                picked = remaining.pop(i)
                break
        if picked is None:
            picked = remaining.pop(0)
        out.append(picked)
        last = lead(picked["artist"])
    return out


def consec(tracks: list) -> list[tuple[int, str]]:
    hits = []
    for i in range(1, len(tracks)):
        a = lead(tracks[i - 1]["artist"])
        b = lead(tracks[i]["artist"])
        if a == b:
            hits.append((i + 1, tracks[i]["artist"]))
    return hits


def reorder(existing: list[dict], door_ids: list[str], extra: list[dict], drop: set[str]) -> list[dict]:
    by_id = {t["id"]: dict(t) for t in existing}
    for t in extra:
        by_id[t["id"]] = dict(t)
    for vid in drop:
        by_id.pop(vid, None)
    missing = [vid for vid in door_ids if vid not in by_id]
    if missing:
        raise SystemExit(f"missing door ids: {missing}")
    head = []
    for vid in door_ids:
        t = dict(by_id.pop(vid))
        t["intro"] = True
        head.append(t)
    tail = []
    for t in existing:
        if t["id"] in by_id:
            rec = dict(by_id.pop(t["id"]))
            rec["intro"] = False
            tail.append(rec)
    for t in extra:
        if t["id"] in by_id:
            rec = dict(by_id.pop(t["id"]))
            rec["intro"] = False
            tail.append(rec)
    out = interleave(head + tail, protect=15)
    return out


def dump(path: Path, room: str, era: str, tracks: list[dict]) -> None:
    payload = {
        "room": room,
        "era": era,
        "count": len(tracks),
        "introCount": 15,
        "tracks": tracks,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def report(label: str, tracks: list[dict], locked: str, forgotten: str, stolen: set[str]) -> int:
    print(f"\n==== {label} ====")
    print("count", len(tracks), "unique", len({t["id"] for t in tracks}))
    print("id lens", sorted({len(t["id"]) for t in tracks}))
    leads = [lead(t["artist"]) for t in tracks]
    print("consecutive", consec(tracks))
    print("lead top", Counter(leads).most_common(10))
    print("first15 lead", Counter(leads[:15]))
    door = 40
    notes = []
    if tracks[0]["id"] != locked:
        door -= 8
        notes.append("moved authored #1")
    if forgotten not in {t["id"] for t in tracks[:15]}:
        door -= 4
        notes.append("forgotten #1 missing")
    if tracks[0]["id"] == forgotten:
        door -= 4
        notes.append("forgotten #1 as opener")
    stolen_hits = [t for t in tracks[:15] if t["id"] in stolen]
    if stolen_hits:
        door -= 3 * len(stolen_hits)
        notes.append("stolen doorway " + ", ".join(t["title"] for t in stolen_hits))
    c = consec(tracks[:15])
    if c:
        door -= 2 * len(c)
        notes.append(f"consecutive in 15: {c}")
    over = [k for k, v in Counter(leads[:15]).items() if v > 2]
    if over:
        door -= 2
        notes.append(f"lead >2 in 15: {over}")
    door = max(0, min(40, door))
    print("DOOR", door, notes or "clean")
    print("first 15:")
    for i, t in enumerate(tracks[:15], 1):
        mark = "  #1" if t["id"] == locked else ("  forgotten" if t["id"] == forgotten else "")
        print(f"  {i:2}. {t['id']}  {t['artist']} — {t['title']} ({t.get('year')}){mark}")
    return door


def main() -> None:
    ayer = json.loads((CUR / "limpieza-ayer.json").read_text())
    hoy = json.loads((CUR / "limpieza-hoy.json").read_text())

    stolen = {
        # Other rooms' first-15 / authored monuments
        "RgKqxLAhRKE",  # Amor Eterno Secador
        "OkOJGgqcwro",  # Como Olvidar Secador
        "ApAhB3DRkFE",  # La Gata Secador
        "kkF5eGMxwEQ",  # Simplemente Amigos Secador
        "wOjzo02Tmck",  # La Incondicional Secador
        "FwZTgDjRLM0",  # Como La Flor Secador
        "0O4CLgXvbjU",  # Así Fue Secador
        "Uws510cVia4",  # Lo Aprendí Secador HOY
        "P2hM9CLAMu4",  # Corre Secador HOY
        "XEvKn-QgAY0",  # Deja Vu Secador HOY
        "_wL3Pc-EmjA",  # Perdón Perdón Secador HOY
        "5R1RGl4WQP8",  # Tu Falta Secador HOY
        "7TWzV05kQ4w",  # Ya Me Enteré Secador HOY
        "TOgCeRQvzoY",  # Confieso Secador HOY
        "uMLuLLCXXx4",  # Ya Te Olvidé Secador HOY
        "_koz_f4mthE",  # A Pedir Su Mano Colmado
        "1DbXzlhKS5s",  # El Africano Colmado
        "McV4pBRb-Sg",  # Bilirrubina Colmado
        "WPiEbYSF9kE",  # Suavemente Colmado/Marquesina
        "HN6ACmknaiw",  # Dueña Colmado/Marquesina
        "ExCIp6TOnJw",  # Manos de Tijera Colmado HOY
        "u6Q5Lu0Sq3g",  # Llamada De Mi Ex Colmado HOY
        "hpkaifThmOs",  # Kitipun Colmado HOY
        "Re93tMg6sfc",  # La Gran Fiesta Colmado HOY
        "YXnjy5YlDwk",  # Vivir Mi Vida Colmado HOY
        "4R7NmEa8s8M",  # Dueña remake Colmado HOY
        "cenRb14_sMY",  # Qué Rico Colmado HOY
        "dDEVFQnBTp0",  # Ojalá Galería
        "95Wcl9ucitM",  # Ventanita Galería
        "E0f3J0z2SBQ",  # Cama y Mesa Galería
        "l6LjNOYvhMk",  # Con Los Años Galería
        "ncByymoHQRI",  # Tus Besos Galería HOY
        "I9cCPQVPv8o",  # Fuiste Tú Galería HOY
        "CJ_zRSv3Hr8",  # Volví a Nacer Galería HOY
        "3VmoZrxXbmg",  # Flor Pálida Galería HOY
        "00QVU7voMq8",  # Eres Mi Sueño Galería HOY
        "QFs3PIZb3js",  # Propuesta Silla/Malecón HOY
        "bdOXnTbyk0g",  # Darte un Beso Silla/Malecón HOY
        "sPTn0QEhxds",  # Me Enamoré Malecón HOY
        "SEjw5rdyvVg",  # Obsesión Silla
        "BT8Afk8HDxY",  # La Morena Marquesina
    }

    verify_ids = list(dict.fromkeys(AYER_15 + HOY_15 + [t["id"] for t in HOY_ADD]))
    print("verifying", len(verify_ids), "ids")
    results = {}
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(check, vid): vid for vid in verify_ids}
        for fut in as_completed(futs):
            rec = fut.result()
            results[rec["id"]] = rec
            flag = "OK" if rec["ok"] and rec["artworkOk"] else f"FAIL {rec['err']}"
            print(f"  {rec['id']}  {flag}  {rec.get('author')} — {rec.get('title')}")
    bad = [vid for vid, rec in results.items() if not (rec["ok"] and rec["artworkOk"])]
    if bad:
        raise SystemExit(f"verify failed: {bad}")

    ayer_tracks = reorder(ayer["tracks"], AYER_15, [], set())
    hoy_tracks = reorder(hoy["tracks"], HOY_15, HOY_ADD, HOY_DROP)

    if len(ayer_tracks) != 100 or len(hoy_tracks) != 100:
        raise SystemExit(f"counts {len(ayer_tracks)} / {len(hoy_tracks)}")

    dump(CUR / "limpieza-ayer.json", "limpieza", "ayer", ayer_tracks)
    dump(CUR / "limpieza-hoy.json", "limpieza", "hoy", hoy_tracks)

    d1 = report("AYER", ayer_tracks, "E6soE-1p3kw", "3LCEzvkwWwI", stolen)
    d2 = report("HOY", hoy_tracks, "hal7rXfJj5o", "vqEdCsOgy9E", stolen)
    print("\nWROTE", CUR / "limpieza-ayer.json")
    print("WROTE", CUR / "limpieza-hoy.json")
    print(f"DOOR SCORES  AYER {d1}/40  HOY {d2}/40")


if __name__ == "__main__":
    main()
