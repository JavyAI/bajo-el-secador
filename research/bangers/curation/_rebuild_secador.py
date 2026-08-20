#!/usr/bin/env python3
"""Secador AYER + HOY: dryer-cry doors, 100 + 100, no Romeo dump."""
from __future__ import annotations

import json
import re
import ssl
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path("/Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador")
CUR_DIR = ROOT / "research/bangers/curation"
CTX = ssl.create_default_context()
UA = "Mozilla/5.0 en-el-secador-curator"
ID_RE = re.compile(r"^[\w-]{11}$")

# Authored #1s stay. Forgotten #1 in the 15, never opener.
# Max 2 of a lead in the 15. Kings ≤18 in the 100, anyone else ≤12.

AYER_15 = [
    ("RgKqxLAhRKE", "Juan Gabriel", "Amor Eterno", 1984, "JuanGabrielVEVO", 302103425),
    ("wOjzo02Tmck", "Luis Miguel", "La Incondicional", 1989, "Warner Music México", 376814619),
    ("kkF5eGMxwEQ", "Ana Gabriel", "Simplemente Amigos", 1988, "AnaGabrielVEVO", 141472866),
    ("OkOJGgqcwro", "Olga Tañón", "Como Olvidar", 2001, "Warner Música", 8803115),
    ("FwZTgDjRLM0", "Selena", "Como La Flor", 1995, "SelenaVEVO", 800716067),
    ("b1cbgrcBrY0", "José José", "El Triste", 1970, "JoseJoseVEVO", 23795914),
    ("ApAhB3DRkFE", "Rocío Dúrcal", "La Gata Bajo La Lluvia", 1981, "Rocío Durcal - Topic", 60374784),
    ("Fi6_kgz5vwU", "Amanda Miguel", "Él Me Mintió", 1981, "Amanda Miguel - Topic", 93000000),
    ("0O4CLgXvbjU", "Juan Gabriel", "Así Fue", 1988, "JuanGabrielVEVO", 1050000000),
    ("uMrN1W4ryoE", "Chayanne", "Dejaría Todo", 1998, "ChayanneVEVO", 463000000),
    ("xftFxCYQTdk", "Camila", "Mientes", 2009, "camilaVEVO", 750155274),
    ("QFVkLGqVhbo", "Ana Gabriel", "Quién Como Tú", 1989, "Ana Gabriel - Topic", 142000000),
    ("FCi-Xp2TVoQ", "Selena", "No Me Queda Más", 1994, "SelenaVEVO", 309000000),
    ("ASnkzgvBf0o", "Olga Tañón", "Es Mentiroso", 1994, "Olga Tañón - Topic", 16000000),
    ("tOVHj4zuRTU", "Marco Antonio Solís", "Si No Te Hubieras Ido", 1999, "MarcoAntonioSolisVEVO", 225000000),
]

# Live AYER minus: Limpieza doorway / merengue fiesta, HOY leak, weak-temp.
AYER_DROP = {
    "E6soE-1p3kw",  # Milly Volvió Juanita — Limpieza #1 + merengue de fiesta
    "F0rwOsAteXM",  # Pablo Alborán Solamente Tú — 2011 HOY
    "tExaVNSjQdo",  # Roberto Carlos Amigo — friendship, not dryer-cry
    "ik5vcov1piU",  # Franco De Vita No Basta — social ballad
    "WPbP2GWTtBk",  # Emmanuel Es Mi Mujer — male-gaze pop
}

AYER_ADD = [
    ("Fk5oL0mgI08", "Sin Bandera", "Que Lloro", 2003, "SinBanderaVEVO", 421577237),
    ("nYbcVK2jjXc", "Shakira", "Inevitable", 1998, "shakiraVEVO", 219000000),
    ("ZGsjpuUrKGc", "Shakira", "Antología", 1995, "Shakira - Topic", 259500000),
    ("KstbkZwnTv0", "Camila", "Aléjate De Mí", 2010, "camilaVEVO", 650200000),
]

HOY_15 = [
    ("QFs3PIZb3js", "Romeo Santos", "Propuesta Indecente", 2013, "RomeoSantosVEVO", 2417487182),
    ("Uws510cVia4", "Ha*Ash", "Lo Aprendí de Ti", 2015, "HaAshVEVO", 1844713103),
    ("P2hM9CLAMu4", "Jesse & Joy", "¡Corre!", 2011, "jesseyjoyoficial", 1108738680),
    ("XEvKn-QgAY0", "Prince Royce, Shakira", "Deja Vu", 2017, "PrinceRoyceVEVO", 736017230),
    ("_wL3Pc-EmjA", "Ha*Ash", "Perdón, Perdón", 2014, "HaAshVEVO", 1123900978),
    ("5R1RGl4WQP8", "Mon Laferte", "Tu Falta de Querer", 2015, "MonLaferteVEVO", 1030126162),
    ("jk4HYngf65w", "Romeo Santos", "Cancioncitas de Amor", 2014, "RomeoSantosVEVO", 635000000),
    ("7TWzV05kQ4w", "Reik", "Ya Me Enteré", 2016, "reikVEVO", 709000000),
    ("TMT9MNM-NHg", "Jesse & Joy", "Dueles", 2016, "jesseyjoyoficial", 680000000),
    ("uMLuLLCXXx4", "Yuridia", "Ya Te Olvidé", 2011, "Yuridia", 789600000),
    ("G3diF-5DlAc", "Gloria Trevi", "No Querías Lastimarme", 2013, "GloriaTreviVEVO", 742000000),
    ("gwmWEr67hzQ", "Carla Morrison", "Déjenme Llorar", 2011, "CarlaMorrisonVEVO", 452100000),
    ("TOgCeRQvzoY", "Kany García", "Confieso", 2018, "kanygarciaVEVO", 204802789),
    ("Q8xIa7KcI1A", "Yuridia, Ángela Aguilar", "Qué Agonía", 2022, "Yuridia", 1142956776),
    ("F0rwOsAteXM", "Pablo Alborán", "Solamente Tú", 2011, "PabloAlboranVEVO", 400000000),
]

# HOY tail: same-temperature 2011+ dryer-cry. No dembow, no 90s pad.
# Romeo kept to 8 total (2 in 15). No Necio / Yo También / You / English / club.
HOY_TAIL = [
    ("NAG98gpC8Hw", "Ha*Ash", "Ex de Verdad", 2015, "HaAshVEVO", 537000000),
    ("8iPcqtHoR3U", "Romeo Santos", "Eres Mía", 2014, "RomeoSantosVEVO", 1338681355),
    ("N6mShTc40BU", "Carlos Rivera", "El Hubiera No Existe", 2013, "CarlosRiveraVEVO", 110000000),
    ("mhHqonzsuoA", "Romeo Santos", "Imitadora", 2017, "RomeoSantosVEVO", 797000000),
    ("7mox58jIAdA", "Ha*Ash", "Te Dejo En Libertad", 2014, "HaAshVEVO", 519100000),
    ("PQlG1gznMBE", "Mon Laferte", "Amor Completo", 2015, "MonLaferteVEVO", 0),
    ("4eCL0l9iD5A", "Romeo Santos", "Hilito", 2014, "RomeoSantosVEVO", 357000000),
    ("_WHGlEYaBgU", "Jesse & Joy", "Ecos de Amor", 2015, "jesseyjoyoficial", 0),
    ("IKmPci5VXz0", "Natalia Lafourcade", "Hasta La Raíz", 2015, "NataliaLafourcadeVEVO", 0),
    ("VafbNsrHnD8", "Romeo Santos", "Llévame Contigo", 2011, "RomeoSantosVEVO", 185000000),
    ("jwP1HRmDVII", "Carla Morrison", "Disfruto", 2015, "CarlaMorrisonVEVO", 0),
    ("rvmtQvA_cmM", "Romeo Santos", "Sus Huellas", 2022, "RomeoSantosVEVO", 140000000),
    ("prmzWy98c-I", "Jesse & Joy, Pablo Alborán", "La de la Mala Suerte", 2012, "jesseyjoyoficial", 0),
    ("SpXdFTmIlYU", "Yuridia", "Amigos No Por Favor", 2016, "Yuridia", 0),
    ("I9cCPQVPv8o", "Ricardo Arjona, Gaby Moreno", "Fuiste Tú", 2012, "Ricardo Arjona", 1521000000),
    ("eFWUnHJWwCg", "Carla Morrison", "Te Regalo", 2015, "Carla Morrison", 245200000),
    ("yUAZxs3qY3Y", "Prince Royce", "Te Robaré", 2013, "PrinceRoyceVEVO", 214000000),
    ("fRJ3kh9cnQo", "Mon Laferte", "Antes De Ti", 2018, "MonLaferteVEVO", 0),
    ("cX2jwx6sIDU", "Ha*Ash, Matisse", "Sé Que Te Vas", 2016, "HaAshVEVO", 0),
    ("ETLoTxVVvjM", "Christian Nodal", "Adiós Amor", 2017, "ChristianNodalVEVO", 0),
    ("OK_KvknlJxA", "Jesse & Joy, Mario Domm", "Llorar", 2013, "jesseyjoyoficial", 0),
    ("tLcfAnN2QgY", "Enrique Iglesias, Marco Antonio Solís", "El Perdedor", 2013, "EnriqueIglesiasVEVO", 0),
    ("sD9_l3oDOag", "Sebastián Yatra", "No Hay Nadie Más", 2018, "SebastianYatraVEVO", 1109000000),
    ("snFhcHHdzT0", "Reik", "Creo En Ti", 2011, "reikVEVO", 0),
    ("PWmJhh_qTSY", "Shakira", "Acróstico", 2023, "shakiraVEVO", 489700000),
    ("0P8qLKnxq3o", "Ha*Ash", "No Pasa Nada", 2017, "HaAshVEVO", 0),
    ("Rir_fuLX7HM", "Carlos Rivera", "Te Esperaba", 2016, "Carlos Rivera", 0),
    ("whYAfEhWiYE", "Mon Laferte", "Vuelve Por Favor", 2017, "MonLaferteVEVO", 0),
    ("ROzZSmaxDz8", "Prince Royce", "Las Cosas Pequeñas", 2012, "Planet Records Official", 84000000),
    ("mOiWXmeZai8", "Yuridia", "Llévame", 2016, "Yuridia", 0),
    ("_KSyWS8UgA4", "Cali Y El Dandee", "Yo Te Esperaré", 2011, "CaliYElDandeeVEVO", 0),
    ("BlhSvoMifVk", "Mon Laferte", "Pa' Dónde Se Fue", 2015, "MonLaferteVEVO", 0),
    ("oZmXYET4qQU", "Christian Nodal", "Te Fallé", 2018, "ChristianNodalVEVO", 0),
    ("KjMCV5K87U0", "Ha*Ash", "Eso No Va a Suceder", 2018, "HaAshVEVO", 0),
    ("z1EB-fI0JDI", "Jesse & Joy", "Un Besito Más", 2015, "jesseyjoyoficial", 0),
    ("kIynEA-hdgQ", "Christian Nodal", "Probablemente", 2017, "ChristianNodalVEVO", 0),
    ("0U3SkZEBGDY", "Ricky Martin", "Disparo al Corazón", 2015, "RickyMartinVEVO", 0),
    ("13m9v78uNJk", "Mon Laferte, Enrique Bunbury", "Mi Buen Amor", 2017, "MonLaferteVEVO", 0),
    ("qjkb9_AJCLo", "Prince Royce", "Carita de Inocente", 2020, "PrinceRoyceVEVO", 81000000),
    ("qXgIcKFJxVY", "Yuridia, Audri Nix", "Que Nadie Se Entere", 2016, "Yuridia", 0),
    ("C8FQ4wQXyaE", "Chayanne", "Humanos a Marte", 2014, "ChayanneVEVO", 0),
    ("sWGJd26kUOY", "Romeo Santos, ROSALÍA", "El Pañuelo", 2022, "RomeoSantosVEVO", 54000000),
    ("NapNBm0FHA0", "Ha*Ash", "No Fue Lo Que Hiciste", 2022, "HaAshVEVO", 0),
    ("NE3IkFadCHM", "Sebastián Yatra", "Traicionera", 2016, "SebastianYatraVEVO", 0),
    ("HhgxpYNZxgk", "Jesse & Joy", "¿Con Quién Se Queda El Perro?", 2011, "jesseyjoyoficial", 0),
    ("ZGx8SqBW8FM", "Christian Nodal", "Perdóname", 2018, "ChristianNodalVEVO", 0),
    ("cSUEFDZ3p3k", "Pablo Alborán", "Te He Echado de Menos", 2012, "PabloAlboranVEVO", 163000000),
    ("D9W4DLjmoOM", "Melendi, Ha*Ash", "Destino o Casualidad", 2017, "MelendiVEVO", 0),
    ("S5UEoLeza-o", "Banda MS", "Háblame de Ti", 2014, "BandaMSVEVO", 0),
    ("lC0-2XGASGg", "Christian Nodal", "Te Voy A Olvidar", 2018, "ChristianNodalVEVO", 0),
    ("uXUjhE9MhyU", "Pablo Alborán", "Prometo", 2017, "PabloAlboranVEVO", 0),
    ("83ckXYtg52I", "Ha*Ash, Abraham Mateo", "30 de Febrero", 2017, "HaAshVEVO", 0),
    ("ghAvJMxE1qo", "Sebastián Yatra, Reik", "Un Año", 2019, "SebastianYatraVEVO", 0),
    ("FzZS_Lx33Gc", "Yuridia", "Ya Es Muy Tarde", 2015, "Yuridia", 0),
    ("_X3PPuF_yOE", "Río Roma", "Me Cambiaste la Vida", 2011, "RioRomaVEVO", 0),
    ("oDmblhAq3Cw", "Ha*Ash", "Ojalá", 2017, "HaAshVEVO", 0),
    ("XlmaJ-yU46U", "Aventura", "Inmortal", 2019, "Aventura", 0),
    ("lzOlA_EPQ18", "Yuridia", "Sin Llorar", 2016, "Yuridia", 0),
    ("0diOZSlLKdg", "Carlos Rivera", "¿Cómo Pagarte?", 2013, "Carlos Rivera", 0),
    ("_gm5piKnrS4", "Morat", "Cómo Te Atreves", 2016, "MoratVEVO", 0),
    ("Z81hsLIY1sQ", "Alejandro Fernández, Christina Aguilera", "Hoy Tengo Ganas de Ti", 2013, "AlejandroFernandezVEVO", 0),
    ("WuVJMfhpdUk", "Christian Nodal, TINI", "Por el Resto de Tu Vida", 2022, "ChristianNodalVEVO", 0),
    ("410cZw2YI0g", "Natalia Lafourcade", "Nunca Es Suficiente", 2015, "NataliaLafourcadeVEVO", 0),
    ("OdaIbTUGmHM", "Prince Royce", "La Carretera", 2015, "PrinceRoyceVEVO", 0),
    ("szeA9tvItJY", "Morat", "Cuando Nadie Ve", 2018, "MoratVEVO", 0),
    ("-7w9tdzndjc", "Banda MS", "No Me Pidas Perdón", 2014, "BandaMSVEVO", 0),
    ("-lDsqOsJL7k", "Prince Royce", "Culpa al Corazón", 2017, "PrinceRoyceVEVO", 0),
    ("1oeD2m2UQAI", "Morat, Juanes", "Besos En Guerra", 2017, "MoratVEVO", 0),
    ("jucBuAzuZ0E", "Alejandro Sanz, Marc Anthony", "Deja Que Te Bese", 2016, "AlejandroSanzVEVO", 0),
    ("bdOXnTbyk0g", "Prince Royce", "Darte un Beso", 2013, "PrinceRoyceVEVO", 1624000000),
    ("CJ_zRSv3Hr8", "Carlos Vives", "Volví a Nacer", 2012, "CarlosVivesVEVO", 0),
    ("weKJWqw8-3g", "Luis Fonsi, Juan Luis Guerra", "Llegaste Tú", 2014, "LuisFonsiVEVO", 0),
    ("Geqmpq0tjNU", "Carlos Vives, Marc Anthony", "Cuando Nos Volvamos a Encontrar", 2014, "CarlosVivesVEVO", 0),
    ("gSJd_J3W6NU", "Fonseca, Juan Luis Guerra", "Si Tú Me Quieres", 2020, "FonsecaVEVO", 0),
    ("zHhza3EgHe8", "Juan Luis Guerra, Romeo Santos", "Frío, Frío", 2014, "JuanLuisGuerraVEVO", 0),
    ("gG3516BF5_w", "Carin León, Grupo Frontera", "Que Vuelvas", 2022, "Grupo Frontera", 814600000),
    ("Qz9gmiLBVFA", "Sebastián Yatra", "Tacones Rojos", 2021, "SebastianYatraVEVO", 0),
    ("sPTn0QEhxds", "Shakira", "Me Enamoré", 2017, "shakiraVEVO", 0),
    ("5AkDqm-cEgg", "Camilo, Pedro Capó", "Tutu", 2019, "CamiloVEVO", 0),
    ("2mY7AFTtYwQ", "Camilo", "Favorito", 2020, "CamiloVEVO", 0),
    ("DriCCFRQlj8", "Camilo, Evaluna Montaner", "Índigo", 2021, "CamiloVEVO", 0),
    ("Mtau4v6foHA", "Carlos Vives, Sebastián Yatra", "Robarte un Beso", 2017, "CarlosVivesVEVO", 0),
    ("07314LhFag4", "Juan Luis Guerra", "Todo Tiene Su Hora", 2014, "JuanLuisGuerraVEVO", 0),
    ("JMq0HJXIp8o", "Juan Luis Guerra", "Corazón Enamorado", 2012, "JuanLuisGuerraVEVO", 0),
    ("3VmoZrxXbmg", "Marc Anthony", "Flor Pálida", 2013, "MarcAnthonyVEVO", 0),
]


def lead(artist: str) -> str:
    return artist.split(",")[0].strip()


def row(t, intro: bool) -> dict:
    vid, artist, title, year, channel, views = t
    return {
        "id": vid,
        "artist": artist,
        "title": title,
        "year": year,
        "channel": channel,
        "views": views,
        "official": True,
        "artworkOk": True,
        "intro": intro,
    }


def load_meta() -> dict:
    meta = {}
    for name in ("secador-ayer.json", "secador-hoy.json"):
        path = CUR_DIR / name
        if not path.exists():
            continue
        data = json.loads(path.read_text())
        for tr in data.get("tracks", []):
            meta[tr["id"]] = tr
    live_ayer = json.loads((ROOT / "public/ayer/secador.json").read_text())
    live_hoy = json.loads((ROOT / "public/hoy/secador.json").read_text())
    for tr in live_ayer["tracks"] + live_hoy["tracks"]:
        meta.setdefault(tr["id"], tr)
    return meta


def live_ayer_pool(meta: dict) -> list:
    live = json.loads((ROOT / "public/ayer/secador.json").read_text())
    intro_ids = {t[0] for t in AYER_15}
    add_ids = {t[0] for t in AYER_ADD}
    out = []
    for tr in live["tracks"]:
        vid = tr["id"]
        if vid in AYER_DROP or vid in intro_ids or vid in add_ids:
            continue
        prev = meta.get(vid, tr)
        out.append(
            (
                vid,
                tr.get("artist") or prev.get("artist"),
                tr.get("title") or prev.get("title"),
                prev.get("year") or 1990,
                prev.get("channel") or "",
                prev.get("views") or 0,
            )
        )
    return out


def weave(fixed: list, rest: list, king: str, king_cap: int = 18, other_cap: int = 12) -> list:
    counts = Counter(lead(t[1]) for t in fixed)
    last = lead(fixed[-1][1]) if fixed else ""
    leftover = list(rest)
    ordered = []
    while leftover:
        picked = None
        for i, t in enumerate(leftover):
            name = lead(t[1])
            cap = king_cap if name == king else other_cap
            if name == last:
                continue
            if counts[name] >= cap:
                continue
            picked = i
            break
        if picked is None:
            for i, t in enumerate(leftover):
                name = lead(t[1])
                cap = king_cap if name == king else other_cap
                if counts[name] < cap:
                    picked = i
                    break
        if picked is None:
            raise SystemExit(f"cannot place remaining {len(leftover)} tracks: {[lead(t[1]) for t in leftover[:8]]}")
        t = leftover.pop(picked)
        ordered.append(t)
        last = lead(t[1])
        counts[last] += 1
    return ordered


def check_list(era: str, tracks: list[dict], king: str) -> None:
    assert len(tracks) == 100, f"{era} count {len(tracks)}"
    ids = [t["id"] for t in tracks]
    assert len(ids) == len(set(ids)), f"{era} duplicate ids"
    assert all(ID_RE.match(i) for i in ids), f"{era} bad id"
    intro = [t for t in tracks if t["intro"]]
    assert len(intro) == 15, f"{era} intro {len(intro)}"
    assert tracks[0]["intro"] and all(tracks[i]["intro"] for i in range(15))
    assert all(not tracks[i]["intro"] for i in range(15, 100))
    leads = [lead(t["artist"]) for t in tracks]
    for a, b in zip(leads, leads[1:]):
        if a == b:
            raise SystemExit(f"{era} consecutive lead {a}")
    intro_leads = Counter(leads[:15])
    for name, n in intro_leads.items():
        if n > 2:
            raise SystemExit(f"{era} intro lead {name}={n} > 2")
    all_leads = Counter(leads)
    for name, n in all_leads.items():
        cap = 18 if name == king else 12
        if n > cap:
            raise SystemExit(f"{era} {name}={n} > {cap}")
    print(f"{era} hygiene OK. top leads: {all_leads.most_common(8)}")
    print(f"{era} intro: " + " → ".join(f"{t['artist'].split(',')[0]} {t['title']}" for t in intro))


def oembed(vid: str) -> dict | None:
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=20) as resp:
            return json.loads(resp.read().decode())
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return None


def thumb_ok(vid: str) -> bool:
    url = f"https://i.ytimg.com/vi/{vid}/mqdefault.jpg"
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method="HEAD")
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=15) as resp:
            length = int(resp.headers.get("Content-Length") or 0)
            return resp.status == 200 and length != 1097
    except urllib.error.URLError:
        return False


def verify(tracks: list[dict], label: str, all_ids: bool = False) -> None:
    subset = tracks if all_ids else tracks[:15]
    bad = []
    for t in subset:
        info = oembed(t["id"])
        art = thumb_ok(t["id"])
        t["artworkOk"] = bool(art)
        if not info:
            bad.append((t["id"], t["title"], "no-oembed"))
            continue
        author = info.get("author_name", "")
        if not t.get("channel"):
            t["channel"] = author
        print(f"  OK {t['id']} {t['artist']} — {t['title']} | {author} | art={art}")
    if bad:
        raise SystemExit(f"{label} verify fail: {bad}")


def write(room_era: str, era: str, tracks: list[dict]) -> Path:
    payload = {
        "room": "secador",
        "era": era,
        "count": 100,
        "introCount": 15,
        "tracks": tracks,
    }
    path = CUR_DIR / f"{room_era}.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    return path


def main() -> None:
    meta = load_meta()

    ayer_rest = live_ayer_pool(meta) + AYER_ADD
    # de-dupe adds vs live
    seen = {t[0] for t in AYER_15}
    ayer_rest_u = []
    for t in ayer_rest:
        if t[0] in seen:
            continue
        seen.add(t[0])
        ayer_rest_u.append(t)
    ayer_tail = weave(AYER_15, ayer_rest_u, king="Juan Gabriel")
    if len(AYER_15) + len(ayer_tail) != 100:
        raise SystemExit(f"AYER assembled {len(AYER_15)+len(ayer_tail)} (tail {len(ayer_tail)})")
    ayer_tracks = [row(t, True) for t in AYER_15] + [row(t, False) for t in ayer_tail]
    check_list("ayer", ayer_tracks, "Juan Gabriel")

    hoy_seen = {t[0] for t in HOY_15}
    hoy_rest = []
    for t in HOY_TAIL:
        if t[0] in hoy_seen:
            continue
        # 2010 date-edge Royce stays out of HOY
        if t[0] in {"hpzT6Wq6pKY", "OST41MmjdTQ", "XNGWDH-6yv8"}:
            continue
        hoy_seen.add(t[0])
        hoy_rest.append(t)
    if len(HOY_15) + len(hoy_rest) < 100:
        raise SystemExit(f"HOY short: {len(HOY_15)+len(hoy_rest)}")
    hoy_rest = hoy_rest[:85]
    hoy_tail = weave(HOY_15, hoy_rest, king="Romeo Santos")
    if len(HOY_15) + len(hoy_tail) != 100:
        raise SystemExit(f"HOY assembled {len(HOY_15)+len(hoy_tail)}")
    hoy_tracks = [row(t, True) for t in HOY_15] + [row(t, False) for t in hoy_tail]
    check_list("hoy", hoy_tracks, "Romeo Santos")

    print("\nVerifying AYER first 15 + new ids…")
    verify(ayer_tracks[:15], "ayer-15")
    new_ayer = [t for t in ayer_tracks if t["id"] in {x[0] for x in AYER_ADD} | {"xftFxCYQTdk"}]
    verify(new_ayer, "ayer-new", all_ids=True)

    print("\nVerifying HOY first 15 + new ids…")
    verify(hoy_tracks[:15], "hoy-15")
    new_hoy_ids = {
        "TOgCeRQvzoY",
        "F0rwOsAteXM",
        "gwmWEr67hzQ",
        "eFWUnHJWwCg",
        "PWmJhh_qTSY",
        "cSUEFDZ3p3k",
        "gG3516BF5_w",
        "gSJd_J3W6NU",
        "zHhza3EgHe8",
        "_X3PPuF_yOE",
        "0diOZSlLKdg",
        "Z81hsLIY1sQ",
        "uXUjhE9MhyU",
        "OdaIbTUGmHM",
        "-lDsqOsJL7k",
        "weKJWqw8-3g",
        "CJ_zRSv3Hr8",
        "jucBuAzuZ0E",
        "Geqmpq0tjNU",
    }
    verify([t for t in hoy_tracks if t["id"] in new_hoy_ids], "hoy-new", all_ids=True)

    p1 = write("secador-ayer", "ayer", ayer_tracks)
    p2 = write("secador-hoy", "hoy", hoy_tracks)
    print(f"\nWrote {p1}")
    print(f"Wrote {p2}")


if __name__ == "__main__":
    main()
