#!/usr/bin/env python3
"""Recut Malecón El Ayer + El Presente: couple radio, doorway first."""
from __future__ import annotations

import json
import ssl
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path("/Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador")
CUR = ROOT / "research/bangers/curation"
CTX = ssl.create_default_context()
UA = "Mozilla/5.0 en-el-secador-curator"

KINGS = {"juan luis guerra", "aventura", "romeo santos", "prince royce"}
HARD_STEALS = {
    "dDEVFQnBTp0",
    "ncByymoHQRI",
    "SEjw5rdyvVg",
    "_koz_f4mthE",
    "RgKqxLAhRKE",
    "E6soE-1p3kw",
    "hal7rXfJj5o",
    "ExCIp6TOnJw",
}

AYER15 = [
    "v0ckuv1xBm0",  # JLG Burbujas LOCKED
    "uBwk106e3es",  # Aventura Un Beso forgotten
    "T_oE3qkbo5s",  # Luismi No Sé Tú
    "iK3BlAZAtPs",  # Chayanne Completamente Enamorados
    "2LiZyAIVmbs",  # JLG Bachata Rosa
    "NdKhS4MMCEo",  # Luismi Somos Novios
    "0m5SXO8qK78",  # Monchy Dos Locos
    "hNDtsPMX7p0",  # Franco Te Amo
    "j3ObHjm1fAE",  # Chayanne Tiempo de Vals
    "QTYJkS6bTOQ",  # Montaner Tan Enamorados
    "8sCWmb8f-BY",  # Monchy Te Quiero Igual Que Ayer
    "p7QYo-9SlP0",  # Ricky Vuelve
    "nYWcy7z0QmU",  # Enrique Enamorado Por Primera Vez
    "-hoZpSoKAYE",  # Sin Bandera Entra En Mi Vida
    "9oLBY9QqTAQ",  # Fonseca Te Mando Flores
]

HOY15 = [
    "QFs3PIZb3js",  # Romeo Propuesta LOCKED
    "bdOXnTbyk0g",  # Royce Darte forgotten
    "DriCCFRQlj8",  # Camilo/Evaluna Índigo
    "Mtau4v6foHA",  # Vives/Yatra Robarte un Beso
    "zHhza3EgHe8",  # JLG/Romeo Frío Frío
    "8iPcqtHoR3U",  # Romeo Eres Mía
    "jucBuAzuZ0E",  # Sanz/Marc Deja Que Te Bese
    "YwodhCjFbQ8",  # Camilo/Evaluna Por Primera Vez
    "BFaRWXEpFrs",  # Marc Tu Vida en la Mía
    "ghAvJMxE1qo",  # Yatra/Reik Un Año
    "W4AiOKlOO0Q",  # Sanz/Cabello Mi Persona Favorita
    "hpzT6Wq6pKY",  # Royce Incondicional
    "Geqmpq0tjNU",  # Vives/Marc Cuando Nos Volvamos
    "weKJWqw8-3g",  # Fonsi/JLG Llegaste Tú
    "idC5sWB9sC0",  # Río Roma/Fonseca Caminar de Tu Mano
]

NEW = {
    "idC5sWB9sC0": ("Río Roma, Fonseca", "Caminar de Tu Mano", 2016, "RioRomaVEVO", 66300000),
    "krP539YBF7U": ("Camilo", "Millones", 2021, "CamiloVEVO", 203400000),
    "iuTtlb2COtc": ("Camilo, Evaluna Montaner", "Machu Picchu", 2021, "CamiloVEVO", 186700000),
    "ZTmShDv7_og": ("Río Roma", "Contigo", 2016, "RioRomaVEVO", 59700000),
    "Lc5fvUzUpnM": ("Río Roma, Carlos Rivera", "Todavía No Te Olvido", 2017, "RioRomaVEVO", 337800000),
    "9jirj0OjI-M": ("Río Roma", "Por Eso Te Amo", 2012, "RioRomaVEVO", 231200000),
    "36kmCZheR1I": ("Río Roma", "Hoy Es un Buen Día", 2014, "RioRomaVEVO", 111400000),
    "2p_eRTj5s5M": ("Romeo Santos", "Amigo", 2014, "RomeoSantosVEVO", 107700000),
    "Gm3WkRDZ8o4": ("Fonseca", "Entre Mi Vida y la Tuya", 2015, "FonsecaVEVO", 27000000),
    "Dj1MRUkZu6s": ("Pablo Alborán", "Pasos de Cero", 2015, "Pablo Alborán", 125000000),
    "USDX0X-d588": ("Morat", "No Se Va", 2019, "MoratVEVO", 393200000),
    "C8FQ4wQXyaE": ("Chayanne", "Humanos a Marte", 2012, "chayanneVEVO", 430000000),
    "5AkDqm-cEgg": ("Camilo, Pedro Capó", "Tutu", 2019, "CamiloVEVO", 980000000),
}

HOY_DROP = {
    "00QVU7voMq8",
    "5R1RGl4WQP8",
    "IKmPci5VXz0",
    "jwP1HRmDVII",
    "sfV6uwZKQRY",
    "P2hM9CLAMu4",
    "NAG98gpC8Hw",
    "tUhmwamgDZY",
    "Uws510cVia4",
    "fRJ3kh9cnQo",
    "HhgxpYNZxgk",
    "3VmoZrxXbmg",
    "CJ_zRSv3Hr8",
    "eshFzjIZZzA",
}

HOY_EXTRA = [
    "XlmaJ-yU46U",
    "C8FQ4wQXyaE",
    "I9cCPQVPv8o",
    "Z81hsLIY1sQ",
    "Rir_fuLX7HM",
    "5AkDqm-cEgg",
    "krP539YBF7U",
    "iuTtlb2COtc",
    "ZTmShDv7_og",
    "Lc5fvUzUpnM",
    "9jirj0OjI-M",
    "36kmCZheR1I",
    "2p_eRTj5s5M",
    "Gm3WkRDZ8o4",
    "Dj1MRUkZu6s",
    "USDX0X-d588",
]


def lead(artist: str) -> str:
    name = (artist or "").split(",")[0].strip().lower()
    if name.startswith("juan luis guerra"):
        return "juan luis guerra"
    return name


def load_pool(*paths: Path) -> dict:
    pool: dict = {}
    for p in paths:
        data = json.loads(p.read_text())
        for t in data["tracks"]:
            cur = pool.get(t["id"], {})
            year = int(t.get("year") or 0) or int(cur.get("year") or 0)
            views = int(t.get("views") or 0) or int(cur.get("views") or 0)
            pool[t["id"]] = {
                "id": t["id"],
                "artist": t.get("artist") or cur.get("artist") or "",
                "title": t.get("title") or cur.get("title") or "",
                "year": year,
                "channel": t.get("channel") or cur.get("channel") or "",
                "views": views,
            }
    return pool


def track(tid: str, pool: dict, intro: bool) -> dict:
    if tid in NEW:
        artist, title, year, channel, views = NEW[tid]
        src = {
            "artist": artist,
            "title": title,
            "year": year,
            "channel": channel,
            "views": views,
        }
    else:
        src = dict(pool[tid])
        if tid in NEW:
            artist, title, year, channel, views = NEW[tid]
            src.update({"artist": artist, "title": title, "year": year, "channel": channel, "views": views})
    if not src.get("year") and tid in pool and pool[tid].get("year"):
        src["year"] = pool[tid]["year"]
    assert src.get("artist") and src.get("title") and src.get("year"), (tid, src)
    return {
        "id": tid,
        "artist": src["artist"],
        "title": src["title"],
        "year": int(src["year"]),
        "channel": src.get("channel") or "",
        "views": int(src.get("views") or 0),
        "official": True,
        "artworkOk": True,
        "intro": intro,
    }


def cap_for(ld: str) -> int:
    return 18 if ld in KINGS else 12


def interleave(head: list, tail: list) -> list:
    used = Counter(lead(t["artist"]) for t in head)
    out = list(head)
    remaining = list(tail)
    while remaining:
        prev = lead(out[-1]["artist"])
        picked = None
        for i, t in enumerate(remaining):
            ld = lead(t["artist"])
            if ld != prev and used[ld] < cap_for(ld):
                picked = i
                break
        if picked is None:
            raise RuntimeError(
                f"stuck n={len(out)} prev={prev} left={[lead(t['artist'])+':'+t['id'] for t in remaining[:10]]}"
            )
        t = remaining.pop(picked)
        out.append(t)
        used[lead(t["artist"])] += 1
    return out


def validate(era: str, tracks: list, locked: str, forgotten: str, ymin: int, ymax: int) -> None:
    ids = [t["id"] for t in tracks]
    assert len(tracks) == 100, len(tracks)
    assert len(set(ids)) == 100
    assert all(len(i) == 11 for i in ids), [i for i in ids if len(i) != 11]
    assert all(t["intro"] for t in tracks[:15])
    assert not any(t["intro"] for t in tracks[15:])
    assert tracks[0]["id"] == locked
    assert 2 <= ids.index(forgotten) + 1 <= 15
    years = [t["year"] for t in tracks]
    bad_year = [t for t in tracks if t["year"] < ymin or t["year"] > ymax]
    assert not bad_year, [(t["id"], t["title"], t["year"]) for t in bad_year]
    consec = [
        (i + 1, tracks[i - 1]["artist"], tracks[i]["artist"])
        for i in range(1, 100)
        if lead(tracks[i]["artist"]) == lead(tracks[i - 1]["artist"])
    ]
    assert not consec, consec
    counts = Counter(lead(t["artist"]) for t in tracks)
    for name, n in counts.items():
        assert n <= cap_for(name), (name, n)
    c15 = Counter(lead(t["artist"]) for t in tracks[:15])
    for name, n in c15.items():
        assert n <= 2, (name, n)
    steal = [t["id"] for t in tracks[:15] if t["id"] in HARD_STEALS]
    assert not steal, steal
    print(f"{era} OK years {min(years)}-{max(years)}")
    print("  leads", counts.most_common(8))
    print("  first15", dict(c15))


def oembed(vid: str) -> tuple[bool, str, str]:
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=12) as r:
            data = json.loads(r.read().decode())
        return True, data.get("author_name", ""), data.get("title", "")
    except Exception as exc:
        return False, str(exc), ""


def dump(path: Path, era: str, tracks: list) -> None:
    obj = {"room": "malecon", "era": era, "count": 100, "introCount": 15, "tracks": tracks}
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")
    print("wrote", path)


def main() -> None:
    ayer_pool = load_pool(CUR / "malecon-ayer.json", ROOT / "public/ayer/malecon.json")
    hoy_pool = load_pool(CUR / "malecon-hoy.json", ROOT / "public/hoy/malecon.json")

    ayer_head = [track(tid, ayer_pool, True) for tid in AYER15]
    ayer_tail = [
        track(t["id"], ayer_pool, False)
        for t in json.loads((CUR / "malecon-ayer.json").read_text())["tracks"]
        if t["id"] not in set(AYER15)
    ]
    ayer = interleave(ayer_head, ayer_tail)
    validate("ayer", ayer, "v0ckuv1xBm0", "uBwk106e3es", 1980, 2010)

    existing = [
        t["id"]
        for t in json.loads((CUR / "malecon-hoy.json").read_text())["tracks"]
        if t["id"] not in HOY_DROP
    ]
    for tid in HOY_EXTRA:
        if tid not in existing and tid not in HOY15:
            existing.append(tid)
    tail_ids = [i for i in existing if i not in set(HOY15)]
    print("hoy tail candidates", len(tail_ids))
    if len(tail_ids) < 85:
        raise SystemExit(f"hoy tail short {len(tail_ids)}")
    tail_ids = tail_ids[:85]

    hoy_head = [track(tid, hoy_pool, True) for tid in HOY15]
    hoy_tail = [track(tid, hoy_pool, False) for tid in tail_ids]
    hoy = interleave(hoy_head, hoy_tail)
    validate("hoy", hoy, "QFs3PIZb3js", "bdOXnTbyk0g", 2011, 2026)

    print("\nAYER 15")
    for i, t in enumerate(ayer[:15], 1):
        print(f"  {i:2}. {t['id']} {t['year']} {t['artist']} — {t['title']}")
    print("\nHOY 15")
    for i, t in enumerate(hoy[:15], 1):
        print(f"  {i:2}. {t['id']} {t['year']} {t['artist']} — {t['title']}")

    print("\nNeighbor overlap first15")
    for era, tracks in (("ayer", ayer), ("hoy", hoy)):
        ids = {t["id"] for t in tracks[:15]}
        for room in ["silla", "secador", "colmado", "galeria", "limpieza"]:
            pub = json.loads((ROOT / f"public/{era}/{room}.json").read_text())
            theirs = [t["id"] for t in pub["tracks"][:15]]
            hit = [i for i in theirs if i in ids]
            print(f"  {era} vs {room}: {len(hit)} {hit}")

    print("\noEmbed first 15")
    bad = []
    for t in ayer[:15] + hoy[:15]:
        ok, author, title = oembed(t["id"])
        mark = "OK" if ok else "FAIL"
        print(f"  {mark} {t['id']} {t['title']} -> {author} | {title[:70]}")
        if not ok:
            bad.append(t["id"])
    if bad:
        raise SystemExit(f"oEmbed fail {bad}")

    dump(CUR / "malecon-ayer.json", "ayer", ayer)
    dump(CUR / "malecon-hoy.json", "hoy", hoy)


if __name__ == "__main__":
    main()
