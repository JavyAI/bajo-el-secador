#!/usr/bin/env python3
"""Hygiene + doorway audit for malecon curation lists."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path("/Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador")
CUR = ROOT / "research/bangers/curation"
PUB = ROOT / "public"

KINGS = {
    "juan luis guerra",
    "juan luis guerra 4.40",
    "aventura",
    "romeo santos",
    "prince royce",
}

NEIGHBOR_DOORS = {
    "silla-ayer": "SEjw5rdyvVg",
    "silla-hoy": "QFs3PIZb3js",
    "secador-ayer": "RgKqxLAhRKE",
    "secador-hoy": "QFs3PIZb3js",
    "colmado-ayer": "_koz_f4mthE",
    "colmado-hoy": "ExCIp6TOnJw",
    "galeria-ayer": "dDEVFQnBTp0",
    "galeria-hoy": "ncByymoHQRI",
    "limpieza-ayer": "E6soE-1p3kw",
    "limpieza-hoy": "hal7rXfJj5o",
}

# Songs that are another room's authored doorway — must not sit as our #1,
# and Galería Tus Besos / Barbería first-four clone should stay off our 15.
HARD_STEALS = {
    "dDEVFQnBTp0",  # Ojalá — Galería AYER #1
    "ncByymoHQRI",  # Tus Besos — Galería HOY #1
    "SEjw5rdyvVg",  # Obsesión — Barbería AYER #1
    "_koz_f4mthE",  # A Pedir Su Mano
    "RgKqxLAhRKE",  # Amor Eterno
    "E6soE-1p3kw",  # Volvió Juanita
    "hal7rXfJj5o",  # Dale Vieja
    "ExCIp6TOnJw",  # Manos de Tijera
}


def lead(artist: str) -> str:
    name = (artist or "").split(",")[0].strip().lower()
    if name.startswith("juan luis guerra"):
        return "juan luis guerra"
    return name


def load(era: str) -> dict:
    return json.loads((CUR / f"malecon-{era}.json").read_text())


def neighbor_first15(era_dir: str, room: str) -> list[str]:
    p = PUB / era_dir / f"{room}.json"
    data = json.loads(p.read_text())
    return [t["id"] for t in data["tracks"][:15]]


def audit(era: str) -> None:
    data = load(era)
    tracks = data["tracks"]
    print(f"\n===== {era} =====")
    assert data["room"] == "malecon"
    assert data["era"] == era
    assert data["count"] == 100
    assert data["introCount"] == 15
    assert len(tracks) == 100, len(tracks)
    ids = [t["id"] for t in tracks]
    assert all(len(i) == 11 for i in ids), [i for i in ids if len(i) != 11]
    assert len(set(ids)) == 100
    intro = [t for t in tracks if t.get("intro")]
    assert len(intro) == 15
    assert all(t.get("intro") for t in tracks[:15])
    assert not any(t.get("intro") for t in tracks[15:])
    years = [t["year"] for t in tracks]
    if era == "ayer":
        assert min(years) >= 1980 and max(years) <= 2010, (min(years), max(years))
    else:
        assert min(years) >= 2011, min(years)
    consec = [
        (i, tracks[i - 1]["artist"], tracks[i]["artist"])
        for i in range(1, 100)
        if lead(tracks[i]["artist"]) == lead(tracks[i - 1]["artist"])
    ]
    assert not consec, consec
    c = Counter(lead(t["artist"]) for t in tracks)
    for name, n in c.items():
        cap = 18 if name in KINGS else 12
        assert n <= cap, (name, n, cap)
    c15 = Counter(lead(t["artist"]) for t in tracks[:15])
    for name, n in c15.items():
        assert n <= 2, (name, n)
    locked = "v0ckuv1xBm0" if era == "ayer" else "QFs3PIZb3js"
    assert tracks[0]["id"] == locked
    forgotten = "uBwk106e3es" if era == "ayer" else "bdOXnTbyk0g"
    forgotten_pos = ids.index(forgotten) + 1
    assert 2 <= forgotten_pos <= 15, forgotten_pos
    steal = [t["id"] for t in tracks[:15] if t["id"] in HARD_STEALS]
    assert not steal, steal
    pub_era = "ayer" if era == "ayer" else "hoy"
    for room in ["silla", "secador", "colmado", "galeria", "limpieza"]:
        theirs = neighbor_first15(pub_era, room)
        overlap = [i for i in ids[:15] if i in theirs]
        print(f"  overlap {room} {pub_era} first15: {len(overlap)} {overlap}")
    print("  count", len(tracks), "unique", len(set(ids)))
    print("  years", min(years), max(years))
    print("  leads", c.most_common(8))
    print("  first15 leads", c15)
    print("  forgotten", forgotten, "at", forgotten_pos)
    print("  locked #1", tracks[0]["title"])


if __name__ == "__main__":
    audit("ayer")
    audit("hoy")
    print("\nAUDIT OK")
