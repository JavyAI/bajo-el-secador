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
    "l6LjNOYvhMk",  # Gloria Con Los Años Que Me Quedan
]

HOY_DOOR = [
    "ncByymoHQRI",  # JLG Tus Besos — locked #1
    "I9cCPQVPv8o",  # Arjona Fuiste Tú — forgotten #1
    "CJ_zRSv3Hr8",  # Vives Volví a Nacer
    "07314LhFag4",  # JLG Todo Tiene Su Hora
    "ea4ovC_B6ow",  # Vicente Carmesí
    "3VmoZrxXbmg",  # Marc Anthony Flor Pálida
    "vVbYpOdAOgU",  # Vicente Mi Balcón — the balcony
    "ZpWRU0H5dmA",  # Arjona Mi Novia Se Me Está Poniendo Vieja
    "zLX_GcXt2pI",  # Medrano Bajo El Agua
    "00QVU7voMq8",  # Fonseca Eres Mi Sueño
    "ahtMpUhoj9s",  # Monsieur Periné Nuestra Canción
    "weKJWqw8-3g",  # Fonsi Llegaste Tú
    "IKmPci5VXz0",  # Lafourcade Hasta La Raíz
    "S8RmXvxlIzc",  # Santiago Cruz Desde Lejos
    "MvITnIylaQ8",  # Cepeda Lo Mejor Que Hay En Mi Vida
]

HOY_ADD = [
    {
        "id": "vVbYpOdAOgU",
        "artist": "Vicente García, Cultura Profética",
        "title": "Mi Balcón",
        "year": 2011,
        "channel": "Vicente García",
        "views": 58900000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "RS6CRP_OoQA",
        "artist": "Natalia Lafourcade",
        "title": "Lo Que Construimos",
        "year": 2015,
        "channel": "NLaFourcadeVEVO",
        "views": 30900000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "cfzmjgpx-VE",
        "artist": "Carlos Rivera",
        "title": "Recuérdame",
        "year": 2017,
        "channel": "DisneyMusicLAVEVO",
        "views": 209100000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "wsQllPKp344",
        "artist": "Juan Luis Guerra",
        "title": "Cositas de Amor",
        "year": 2023,
        "channel": "JuanLuisGuerraVEVO",
        "views": 1310000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "ApCIF4NOtec",
        "artist": "Juan Luis Guerra",
        "title": "Me Preguntas",
        "year": 2014,
        "channel": "JuanLuisGuerraVEVO",
        "views": 12000000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "JMq0HJXIp8o",
        "artist": "Juan Luis Guerra",
        "title": "Corazón Enamorado",
        "year": 2019,
        "channel": "JuanLuisGuerraVEVO",
        "views": 2690000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "C8JJxmVQ9KI",
        "artist": "Silvana Estrada",
        "title": "Te Guardo",
        "year": 2018,
        "channel": "Silvana Estrada",
        "views": 23800000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "7Mk-8TR7vg0",
        "artist": "Andrés Cepeda",
        "title": "En Otra Vida",
        "year": 2023,
        "channel": "Andrés Cepeda",
        "views": 15000000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "1KZ9osr-a8I",
        "artist": "Monsieur Periné",
        "title": "Sabor a Mí",
        "year": 2012,
        "channel": "Monsieur Periné",
        "views": 8900000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "HyBu2KEe2pI",
        "artist": "Jorge Drexler",
        "title": "Silencio",
        "year": 2017,
        "channel": "Jorge Drexler Oficial",
        "views": 8000000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "yBAx5nBdJqU",
        "artist": "Pablo Alborán",
        "title": "Saturno",
        "year": 2017,
        "channel": "Pablo Alborán",
        "views": 651000000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "gYyKuLV8A_c",
        "artist": "Rozalén",
        "title": "La Puerta Violeta",
        "year": 2017,
        "channel": "Rozalén",
        "views": 34200000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "WENJIxEfyaw",
        "artist": "Juan Luis Guerra",
        "title": "La Noviecita",
        "year": 2023,
        "channel": "JuanLuisGuerraVEVO",
        "views": 7900000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
    {
        "id": "wyJd8xYuyyQ",
        "artist": "Jorge Drexler, Mon Laferte",
        "title": "Asilo",
        "year": 2018,
        "channel": "Jorge Drexler Oficial",
        "views": 25000000,
        "official": True,
        "artworkOk": True,
        "intro": False,
    },
]

HOY_DROP = {
    "ETLoTxVVvjM",  # Nodal Adiós Amor — ranchera, not porch
    "VlmZMeqoADI",  # Nodal De Los Besos
    "CnuoXtaX8q0",  # Nodal No Te Contaron Mal
    "2mY7AFTtYwQ",  # Camilo Favorito — kids pop
    "qKp1f7Vn9dM",  # Camilo Vida de Rico
    "QBaIMZ8QjcU",  # Romeo Yo También — colmado door
    "DXiXPhvYuNU",  # Romeo Necio — secador leak
    "mhHqonzsuoA",  # Romeo Imitadora — silla/malecon door
    "bdOXnTbyk0g",  # Royce Darte un Beso — silla/malecon door
    "P2hM9CLAMu4",  # J&J Corre — secador/limpieza/malecon door
    "ym2clIz5t4A",  # Manny Cruz Llegaste — merengue fiesta
    "P_xKX0NBTeQ",  # Eddy Si No Era Yo
    "K3S96fUGrEY",  # JLG Mambo 23 — dance
    "RksYXExb0d0",  # JLG Vale la Pena — colmado door
}

ALIASES = (
    "juan luis guerra",
    "camilo sesto",
    "jesse & joy",
    "ha*ash",
    "prince royce",
    "romeo santos",
    "carlos vives",
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
    "carlos rivera",
    "jorge drexler",
    "silvana estrada",
    "rozalén",
    "reik",
    "camilo",
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
    print(f"{name} lead top", counts.most_common(12))
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
    ayer = recut(ayer_src, AYER_DOOR, [], set())
    hoy = recut(hoy_src, HOY_DOOR, HOY_ADD, HOY_DROP)
    errs = checks("ayer", ayer) + checks("hoy", hoy)
    for e in errs:
        print("ERR", e)
    if errs:
        raise SystemExit("hygiene failed")

    verify = []
    seen = set()
    for vid in AYER_DOOR + HOY_DOOR + [t["id"] for t in HOY_ADD]:
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
