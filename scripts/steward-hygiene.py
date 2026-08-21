#!/usr/bin/env python3
"""Report-only hygiene for the 12 live Sopita lists. Never writes JSON."""

from __future__ import annotations

import collections
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"

ROOMS = [
    ("colmado", "ayer/colmado.json", "hoy/colmado.json"),
    ("secador", "ayer/secador.json", "hoy/secador.json"),
    ("barberia", "ayer/silla.json", "hoy/silla.json"),
    ("limpieza", "ayer/limpieza.json", "hoy/limpieza.json"),
    ("galeria", "ayer/galeria.json", "hoy/galeria.json"),
    ("malecon", "ayer/malecon.json", "hoy/malecon.json"),
]

AUTHED = {
    ("colmado", "ayer"): "McV4pBRb-Sg",
    ("colmado", "hoy"): "u6Q5Lu0Sq3g",
    ("secador", "ayer"): "FwZTgDjRLM0",
    ("secador", "hoy"): "XEvKn-QgAY0",
    ("barberia", "ayer"): "oVLS7QGWlGw",
    ("barberia", "hoy"): "MB23TtaeiQY",
    ("limpieza", "ayer"): "3LCEzvkwWwI",
    ("limpieza", "hoy"): "SagA6H4LWjI",
    ("galeria", "ayer"): "95Wcl9ucitM",
    ("galeria", "hoy"): "ea4ovC_B6ow",
    ("malecon", "ayer"): "iK3BlAZAtPs",
    ("malecon", "hoy"): "Mtau4v6foHA",
}


def lead(artist: str) -> str:
    a = (artist or "").strip()
    return re.split(r"\s*(?:,| feat\.| ft\.| featuring)\s*", a, flags=re.I)[0].strip()


def load_lists() -> dict:
    out = {}
    for room, ayer, hoy in ROOMS:
        for era, rel in (("ayer", ayer), ("hoy", hoy)):
            data = json.loads((PUBLIC / rel).read_text())
            out[(room, era)] = data.get("tracks") or []
    return out


def main() -> None:
    lists = load_lists()
    print("=== COUNTS ===")
    for (room, era), tracks in lists.items():
        print(f"{room:10} {era:4} n={len(tracks):3}")

    print("\n=== AUTHORED #1 ===")
    for key, want in AUTHED.items():
        tracks = lists[key]
        got = tracks[0]["id"] if tracks else ""
        mark = "HOLD" if got == want else f"MOVED (now {got})"
        print(f"{key[0]}/{key[1]}: {mark}")

    print("\n=== FIRST-5 ID COLLISIONS ===")
    owners: dict[str, list[str]] = collections.defaultdict(list)
    for (room, era), tracks in lists.items():
        for i, t in enumerate(tracks[:5], 1):
            owners[t["id"]].append(f"{room}/{era}#{i} {t.get('artist')} — {t.get('title')}")
    hits = {i: o for i, o in owners.items() if len(o) > 1}
    if not hits:
        print("none")
    else:
        for i, o in hits.items():
            print(i)
            for line in o:
                print("  ", line)

    print("\n=== CONSECUTIVE SAME LEAD ===")
    dirty = False
    for (room, era), tracks in lists.items():
        prev = None
        for i, t in enumerate(tracks):
            a = lead(t.get("artist", ""))
            if prev and a.lower() == prev.lower():
                dirty = True
                print(f"{room}/{era} slots {i}-{i+1} {a}")
            prev = a
    if not dirty:
        print("clean")

    print("\n=== FIRST 15 LEAD REPEATS (>2) ===")
    for (room, era), tracks in lists.items():
        cnt = collections.Counter(lead(t.get("artist", "")) for t in tracks[:15])
        reps = [(a, n) for a, n in cnt.items() if n > 2]
        if reps:
            print(f"{room}/{era}: " + ", ".join(f"{a}×{n}" for a, n in reps))

    print("\n=== KING SHARE IN 100 (≥12) ===")
    for (room, era), tracks in lists.items():
        n = len(tracks) or 1
        cnt = collections.Counter(lead(t.get("artist", "")) for t in tracks)
        heavy = [(a, c) for a, c in cnt.most_common(8) if c >= 12]
        if heavy:
            print(
                f"{room}/{era}: "
                + ", ".join(f"{a} {c} ({round(100 * c / n)}%)" for a, c in heavy)
            )


if __name__ == "__main__":
    main()
