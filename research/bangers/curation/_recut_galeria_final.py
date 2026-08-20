#!/usr/bin/env python3
"""Recut Galería AYER + HOY. Research write only. Door first."""
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
    "kr2B1RoWrlE",  # Perales Y Cómo Es Él
    "1ddK89KqVe8",  # Myriam El Hombre Que Yo Amo
    "apFqJ49VstY",  # Daniela Romo Yo No Te Pido la Luna
    "td2K3taR3bc",  # Cristian Lloran las Rosas
    "mIszekfGw3Q",  # Yuri Detrás de Mi Ventana
    "VyraXS0iMHw",  # Los Bukis Tu Cárcel
    "g-GBiuujmL8",  # Pausini Se Fue
    "kMIaYXxLnUA",  # Juanes A Dios Le Pido
]

HOY_DOOR = [
    "ncByymoHQRI",  # JLG Tus Besos — locked #1
    "I9cCPQVPv8o",  # Arjona Fuiste Tú — forgotten #1
    "CJ_zRSv3Hr8",  # Vives Volví a Nacer
    "07314LhFag4",  # JLG Todo Tiene Su Hora
    "ea4ovC_B6ow",  # Vicente Carmesí
    "3VmoZrxXbmg",  # Marc Anthony Flor Pálida
    "NAEGTNrfmmo",  # Vicente Loma de Cayenas
    "zLX_GcXt2pI",  # Medrano Bajo El Agua
    "00QVU7voMq8",  # Fonseca Eres Mi Sueño
    "ahtMpUhoj9s",  # Monsieur Periné Nuestra Canción
    "weKJWqw8-3g",  # Fonsi Llegaste Tú
    "S8RmXvxlIzc",  # Santiago Cruz Desde Lejos
    "IKmPci5VXz0",  # Lafourcade Hasta La Raíz
    "MvITnIylaQ8",  # Cepeda Lo Mejor Que Hay En Mi Vida
    "vWtJJRTqVSI",  # Arjona El Amor
]

AYER_ADD = [
    {
        "id": "td2K3taR3bc",
        "artist": "Cristian Castro",
        "title": "Lloran las Rosas",
        "year": 1997,
        "channel": "CristianCastroVEVO",
        "views": 92000000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    }
]
AYER_DROP = {"pCBfCmHQw58"}  # Luismi Ahora Te Puedes Marchar — pop-party, not porch

HOY_ADD = [
    {
        "id": "vWtJJRTqVSI",
        "artist": "Ricardo Arjona",
        "title": "El Amor",
        "year": 2011,
        "channel": "Ricardo Arjona",
        "views": 241000000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "PBNon8saBmo",
        "artist": "Ricardo Arjona",
        "title": "El Amor Que Me Tenía",
        "year": 2020,
        "channel": "Ricardo Arjona",
        "views": 83000000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "410cZw2YI0g",
        "artist": "Natalia Lafourcade",
        "title": "Nunca Es Suficiente",
        "year": 2015,
        "channel": "NLaFourcadeVEVO",
        "views": 183000000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "YDJsjfwFPes",
        "artist": "Andrés Cepeda, Morat",
        "title": "Déjame Ir",
        "year": 2019,
        "channel": "Andrés Cepeda",
        "views": 105000000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "Gzh-mH2lhog",
        "artist": "Juanes",
        "title": "Es Tarde",
        "year": 2017,
        "channel": "JuanesVEVO",
        "views": 31000000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "cSUEFDZ3p3k",
        "artist": "Pablo Alborán",
        "title": "Te He Echado de Menos",
        "year": 2012,
        "channel": "Pablo Alborán",
        "views": 163000000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "Dj1MRUkZu6s",
        "artist": "Pablo Alborán",
        "title": "Pasos de Cero",
        "year": 2015,
        "channel": "Pablo Alborán",
        "views": 124000000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "nA2Cm4uaj64",
        "artist": "Santiago Cruz",
        "title": "No Te Necesito",
        "year": 2012,
        "channel": "SantiagocruzVEVO",
        "views": 99100000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "eyCpzmchaqk",
        "artist": "Fonseca",
        "title": "Por Toda la Vida",
        "year": 2024,
        "channel": "Fonseca",
        "views": 4500000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "-u6w90uQhTI",
        "artist": "Marc Anthony",
        "title": "Cambio de Piel",
        "year": 2013,
        "channel": "Marc Anthony",
        "views": 129000000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
]

# JLG album dump + dryer/silla/colmado leaks off the porch
HOY_DROP = {
    "dUOC-ryYtQI",  # JLG I Love You More
    "U1zjUFn4fHo",  # JLG Gracias
    "LNrZ_E1LOnw",  # JLG Como Me Enamora
    "WENJIxEfyaw",  # JLG La Noviecita
    "wNrucsuePOg",  # JLG DJ Bachata
    "6fm3riUiG2c",  # JLG Privé
    "gl3Z28ygq4s",  # JLG/Sting Estrellitas remake
    "7mox58jIAdA",  # Ha*Ash Te Dejo En Libertad — secador
    "NAG98gpC8Hw",  # Ha*Ash Ex de Verdad — secador
    "u7rTroCsmCY",  # Ha*Ash No Pasa Nada — secador
}

ALIASES = (
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
    "andrés cepeda",
    "santiago cruz",
    "pablo alborán",
    "natalia lafourcade",
    "manuel medrano",
    "cristian castro",
)


def lead(artist):
    a = artist.split(",")[0].strip().lower()
    for pref in ALIASES:
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
            pick = 0
        t = pool.pop(pick)
        out.append(t)
        last = lead(t["artist"])
    return out


def recut(src_tracks, door_ids, extras, drop):
    by_id = {t["id"]: dict(t) for t in src_tracks}
    for t in extras:
        if t["id"] not in by_id:
            by_id[t["id"]] = dict(t)
    missing = [i for i in door_ids if i not in by_id]
    if missing:
        raise SystemExit(f"missing door ids {missing}")
    door = []
    for vid in door_ids:
        t = dict(by_id[vid])
        t["intro"] = True
        door.append(t)
    used = set(door_ids) | set(drop)
    rest = []
    for t in src_tracks:
        if t["id"] in used:
            continue
        nt = dict(t)
        nt["intro"] = False
        rest.append(nt)
    extra_ids = {t["id"] for t in extras} - used
    for vid in extra_ids:
        nt = dict(by_id[vid])
        nt["intro"] = False
        rest.append(nt)
    rest = interleave(rest, lead(door[-1]["artist"]))
    tracks = door + rest
    if len(tracks) != 100:
        raise SystemExit(f"count {len(tracks)} after recut (door {len(door)} rest {len(rest)})")
    return tracks


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
        if t.get("official") is not True:
            errs.append(f"{name} unofficial {t['id']}")
    for i in range(1, len(tracks)):
        if lead(tracks[i]["artist"]) == lead(tracks[i - 1]["artist"]):
            errs.append(
                f"{name} consec {i}/{i+1} {tracks[i-1]['artist']} -> {tracks[i]['artist']}"
            )
    for i, t in enumerate(tracks[:15], 1):
        if not t.get("intro"):
            errs.append(f"{name} #{i} missing intro")
    for i, t in enumerate(tracks[15:], 16):
        if t.get("intro"):
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
    years = [t.get("year") or 0 for t in tracks]
    print(f"{name} lead top", counts.most_common(10))
    print(f"{name} door leads", door_counts.most_common())
    print(f"{name} years {min(years)}-{max(years)}")
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


def ryd(vid):
    url = f"https://returnyoutubedislikeapi.com/votes?videoId={vid}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=12, context=CTX) as r:
        return json.loads(r.read().decode())


def main():
    ayer_src = json.loads((OUT / "galeria-ayer.json").read_text())["tracks"]
    hoy_src = json.loads((OUT / "galeria-hoy.json").read_text())["tracks"]
    ayer = recut(ayer_src, AYER_DOOR, AYER_ADD, AYER_DROP)
    hoy = recut(hoy_src, HOY_DOOR, HOY_ADD, HOY_DROP)
    errs = checks("ayer", ayer) + checks("hoy", hoy)
    for e in errs:
        print("ERR", e)
    if errs:
        raise SystemExit("hygiene failed")

    new_ids = [t["id"] for t in AYER_ADD + HOY_ADD] + [
        vid for vid in AYER_DOOR + HOY_DOOR
    ]
    # verify door + new
    verify = []
    seen = set()
    for vid in new_ids:
        if vid not in seen:
            verify.append(vid)
            seen.add(vid)
    bad = []
    for vid in verify:
        try:
            st = mq(vid)
            oe = oembed(vid)
            views = None
            try:
                views = ryd(vid).get("viewCount")
            except Exception:
                pass
            ok = st == 200 and bool(oe.get("title"))
            print(
                f"{'OK' if ok else 'FAIL'} {vid} mq={st} views={views} | {oe.get('author_name')} | {oe.get('title')}",
                flush=True,
            )
            if not ok:
                bad.append(vid)
            # stamp views if we got them
            for tracks in (ayer, hoy):
                for t in tracks:
                    if t["id"] == vid and views:
                        t["views"] = int(views)
        except Exception as e:
            print(f"FAIL {vid} {e}", flush=True)
            bad.append(vid)
        time.sleep(0.08)
    if bad:
        raise SystemExit(f"verify failed {bad}")

    dump("galeria", "ayer", ayer, OUT / "galeria-ayer.json")
    dump("galeria", "hoy", hoy, OUT / "galeria-hoy.json")
    print("AYER door:")
    for i, t in enumerate(ayer[:15], 1):
        print(f"  {i:2d} {t['artist']} — {t['title']} ({t['year']}) {t['id']}")
    print("HOY door:")
    for i, t in enumerate(hoy[:15], 1):
        print(f"  {i:2d} {t['artist']} — {t['title']} ({t['year']}) {t['id']}")
    print("DONE", len(ayer), len(hoy))


if __name__ == "__main__":
    main()
