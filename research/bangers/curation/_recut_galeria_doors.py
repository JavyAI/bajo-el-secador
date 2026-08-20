#!/usr/bin/env python3
"""Recut Galería AYER + HOY doors. Research write only."""
import json
import ssl
import time
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path

OUT = Path("/Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador/research/bangers/curation")
CTX = ssl.create_default_context()

AYER_DOOR = [
    "dDEVFQnBTp0",  # JLG Ojalá — locked #1
    "95Wcl9ucitM",  # Sergio La Ventanita
    "E0f3J0z2SBQ",  # Villalona Cama y Mesa
    "oADpF--uirA",  # JuanGa Querida
    "xhpJqdZgF5U",  # JLG El Niágara — forgotten #1
    "-apU2sviHCM",  # Arjona Historia de Taxi
    "xaKLn_z9R_k",  # Villalona Tabaco y Ron
    "VyraXS0iMHw",  # Los Bukis Tu Cárcel
    "1ddK89KqVe8",  # Myriam El Hombre Que Yo Amo
    "dpxQbZsXgNw",  # Dúrcal Costumbres
    "kr2B1RoWrlE",  # Perales Y Cómo Es Él
    "apFqJ49VstY",  # Daniela Romo Yo No Te Pido la Luna
    "mIszekfGw3Q",  # Yuri Detrás de Mi Ventana
    "29NM6ySmwfQ",  # Cristian Azul
    "kMIaYXxLnUA",  # Juanes A Dios Le Pido
]

HOY_DOOR = [
    "ncByymoHQRI",  # JLG Tus Besos — locked #1
    "I9cCPQVPv8o",  # Arjona Fuiste Tú — forgotten #1
    "CJ_zRSv3Hr8",  # Vives Volví a Nacer
    "07314LhFag4",  # JLG Todo Tiene Su Hora
    "HhgxpYNZxgk",  # Jesse & Joy ¿Con Quién Se Queda El Perro?
    "3VmoZrxXbmg",  # Marc Anthony Flor Pálida
    "NAEGTNrfmmo",  # Vicente García Loma de Cayenas
    "zLX_GcXt2pI",  # Medrano Bajo El Agua
    "ZpWRU0H5dmA",  # Arjona Mi Novia Se Me Está Poniendo Vieja
    "ea4ovC_B6ow",  # Vicente García Carmesí
    "00QVU7voMq8",  # Fonseca Eres Mi Sueño
    "ahtMpUhoj9s",  # Monsieur Periné Nuestra Canción
    "weKJWqw8-3g",  # Fonsi Llegaste Tú
    "S8RmXvxlIzc",  # Santiago Cruz Desde Lejos
    "BFaRWXEpFrs",  # Marc Anthony Tu Vida en la Mía
]

VIEW_FIX = {
    "-apU2sviHCM": 1300000000,
    "ea4ovC_B6ow": 82100000,
    "00QVU7voMq8": 469000000,
    "ahtMpUhoj9s": 42600000,
    "S8RmXvxlIzc": 212000000,
    "BFaRWXEpFrs": 198000000,
    "kMIaYXxLnUA": 276000000,
}


def lead(artist):
    a = artist.split(",")[0].strip().lower()
    aliases = (
        "juan luis guerra",
        "camilo sesto",
        "jesse & joy",
        "ha*ash",
        "prince royce",
        "romeo santos",
        "carlos vives",
        "camilo",
        "reik",
        "sebastián yatra",
        "christian nodal",
        "fernandito villalona",
        "fernando villalona",
        "sergio vargas",
        "josé josé",
        "juan gabriel",
        "ana gabriel",
        "rocío dúrcal",
        "luis miguel",
        "myriam hernández",
        "sin bandera",
        "eddy herrera",
        "manny cruz",
        "miriam cruz",
        "vicente garcía",
        "ricardo arjona",
        "marc anthony",
        "fonseca",
        "monsieur periné",
    )
    for pref in aliases:
        if a.startswith(pref) or pref in a:
            return pref
    return a


def interleave(rest, prev_lead):
    pool = list(rest)
    out = []
    last = prev_lead
    while pool:
        pick = None
        for i, t in enumerate(pool):
            if lead(t["artist"]) != last:
                pick = i
                break
        if pick is None:
            # last resort: take first and we'll fail hygiene if still stuck
            pick = 0
        t = pool.pop(pick)
        out.append(t)
        last = lead(t["artist"])
    return out


def recut(src_path, door_ids):
    data = json.loads(src_path.read_text())
    by_id = {t["id"]: t for t in data["tracks"]}
    missing = [i for i in door_ids if i not in by_id]
    if missing:
        raise SystemExit(f"{src_path.name} missing {missing}")
    door = []
    for vid in door_ids:
        t = dict(by_id[vid])
        t["intro"] = True
        if vid in VIEW_FIX and (t.get("views") or 0) < VIEW_FIX[vid]:
            t["views"] = VIEW_FIX[vid]
        door.append(t)
    rest = []
    for t in data["tracks"]:
        if t["id"] in set(door_ids):
            continue
        nt = dict(t)
        nt["intro"] = False
        rest.append(nt)
    rest = interleave(rest, lead(door[-1]["artist"]))
    return door + rest


def checks(name, tracks):
    errs = []
    if len(tracks) != 100:
        errs.append(f"{name} count {len(tracks)}")
    ids = [t["id"] for t in tracks]
    if len(ids) != len(set(ids)):
        dups = [i for i, c in Counter(ids).items() if c > 1]
        errs.append(f"{name} dups {dups}")
    for t in tracks:
        if len(t["id"]) != 11:
            errs.append(f"bad id {t['id']}")
    for i in range(1, len(tracks)):
        if lead(tracks[i]["artist"]) == lead(tracks[i - 1]["artist"]):
            errs.append(
                f"{name} consec {i}/{i+1} {tracks[i-1]['artist']} -> {tracks[i]['artist']}"
            )
    for i, t in enumerate(tracks[:15], 1):
        if not t["intro"]:
            errs.append(f"{name} #{i} missing intro")
    for i, t in enumerate(tracks[15:], 16):
        if t["intro"]:
            errs.append(f"{name} #{i} extra intro")
    counts = Counter(lead(t["artist"]) for t in tracks)
    door_counts = Counter(lead(t["artist"]) for t in tracks[:15])
    kings = {"juan luis guerra"}
    for artist, n in counts.most_common():
        cap = 18 if artist in kings else 12
        if n > cap:
            errs.append(f"{name} {artist} {n} > {cap}")
    for artist, n in door_counts.items():
        if n > 2:
            errs.append(f"{name} door {artist} {n} > 2")
    print(f"{name} lead top", counts.most_common(8))
    print(f"{name} door leads", door_counts.most_common())
    return errs


def dump(room, era, tracks, path):
    payload = {
        "room": room,
        "era": era,
        "count": len(tracks),
        "introCount": 15,
        "tracks": tracks,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def mq(vid):
    url = f"https://i.ytimg.com/vi/{vid}/mqdefault.jpg"
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=12, context=CTX) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code


def oembed(vid):
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=12, context=CTX) as r:
        return json.loads(r.read().decode())


def main():
    ayer = recut(OUT / "galeria-ayer.json", AYER_DOOR)
    hoy = recut(OUT / "galeria-hoy.json", HOY_DOOR)
    errs = checks("ayer", ayer) + checks("hoy", hoy)
    for e in errs:
        print("ERR", e)
    if errs:
        raise SystemExit("hygiene failed")
    dump("galeria", "ayer", ayer, OUT / "galeria-ayer.json")
    dump("galeria", "hoy", hoy, OUT / "galeria-hoy.json")
    print("AYER door:")
    for i, t in enumerate(ayer[:15], 1):
        print(f"  {i:2d} {t['artist']} — {t['title']} ({t['year']}) {t['id']}")
    print("HOY door:")
    for i, t in enumerate(hoy[:15], 1):
        print(f"  {i:2d} {t['artist']} — {t['title']} ({t['year']}) {t['id']}")
    bad = []
    for era, tracks in (("ayer", ayer), ("hoy", hoy)):
        for t in tracks[:15]:
            vid = t["id"]
            try:
                st = mq(vid)
                oe = oembed(vid)
                ok = st == 200 and bool(oe.get("title"))
                print(
                    f"{era} {'OK' if ok else 'FAIL'} {vid} mq={st} | {oe.get('author_name')} | {oe.get('title')}",
                    flush=True,
                )
                if not ok:
                    bad.append(vid)
            except Exception as e:
                print(f"{era} FAIL {vid} {e}", flush=True)
                bad.append(vid)
            time.sleep(0.08)
    print("BAD", bad)
    print("DONE")


if __name__ == "__main__":
    main()
