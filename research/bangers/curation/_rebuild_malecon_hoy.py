#!/usr/bin/env python3
"""Malecón El Presente: couple radio, not a Romeo/Royce album dump."""
from __future__ import annotations

import json
import re
import ssl
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path("/Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador")
PUB = ROOT / "public/hoy/malecon.json"
CUR = ROOT / "research/bangers/curation/malecon-hoy.json"
COVERS = ROOT / "assets/covers"
CTX = ssl.create_default_context()
UA = "Mozilla/5.0 en-el-secador-verify"

# Doorway. Propuesta locked. Darte is the forgotten #1. Other couple voices in the 15.
FIRST15 = [
    ("QFs3PIZb3js", "Romeo Santos", "Propuesta Indecente"),
    ("bdOXnTbyk0g", "Prince Royce", "Darte un Beso"),
    ("XlmaJ-yU46U", "Aventura", "Inmortal"),
    ("8iPcqtHoR3U", "Romeo Santos", "Eres Mía"),
    ("C8FQ4wQXyaE", "Chayanne", "Humanos a Marte"),
    ("ncByymoHQRI", "Juan Luis Guerra", "Tus Besos"),
    ("jk4HYngf65w", "Romeo Santos", "Cancioncitas de Amor"),
    ("hpzT6Wq6pKY", "Prince Royce", "Incondicional"),
    ("I9cCPQVPv8o", "Ricardo Arjona, Gaby Moreno", "Fuiste Tú"),
    ("ROzZSmaxDz8", "Prince Royce", "Las Cosas Pequeñas"),
    ("Z81hsLIY1sQ", "Alejandro Fernández, Christina Aguilera", "Hoy Tengo Ganas de Ti"),
    ("mhHqonzsuoA", "Romeo Santos", "Imitadora"),
    ("P2hM9CLAMu4", "Jesse & Joy", "¡Corre!"),
    ("yUAZxs3qY3Y", "Prince Royce", "Te Robaré"),
    ("Rir_fuLX7HM", "Carlos Rivera", "Te Esperaba"),
]

# Couple / vow / two-person. Not típica spine, not salsa, not merengue de fiesta, not dembow.
TAIL = [
    ("07314LhFag4", "Juan Luis Guerra", "Todo Tiene Su Hora"),
    ("HhgxpYNZxgk", "Jesse & Joy", "¿Con Quién Se Queda El Perro?"),
    ("KsdJEolXHQA", "Juan Luis Guerra", "Muchachita Linda"),
    ("2mY7AFTtYwQ", "Camilo", "Favorito"),
    ("WENJIxEfyaw", "Juan Luis Guerra", "La Noviecita"),
    ("gSJd_J3W6NU", "Fonseca, Juan Luis Guerra", "Si Tú Me Quieres"),
    ("snFhcHHdzT0", "Reik", "Creo en Ti"),
    ("JMq0HJXIp8o", "Juan Luis Guerra", "Corazón Enamorado"),
    ("NE3IkFadCHM", "Sebastián Yatra", "Traicionera"),
    ("zHhza3EgHe8", "Juan Luis Guerra, Romeo Santos", "Frío, Frío"),
    ("5AkDqm-cEgg", "Camilo, Pedro Capó", "Tutu"),
    ("tLcfAnN2QgY", "Enrique Iglesias, Marco Antonio Solís", "El Perdedor"),
    ("_gm5piKnrS4", "Morat", "Cómo Te Atreves"),
    ("TMT9MNM-NHg", "Jesse & Joy", "Dueles"),
    ("jucBuAzuZ0E", "Alejandro Sanz, Marc Anthony", "Deja Que Te Bese"),
    ("N6mShTc40BU", "Carlos Rivera", "El Hubiera No Existe"),
    ("_WHGlEYaBgU", "Jesse & Joy", "Ecos de Amor"),
    ("7TWzV05kQ4w", "Reik", "Ya Me Enteré"),
    ("sD9_l3oDOag", "Sebastián Yatra", "No Hay Nadie Más"),
    ("Geqmpq0tjNU", "Carlos Vives, Marc Anthony", "Cuando Nos Volvamos a Encontrar"),
    ("uXUjhE9MhyU", "Pablo Alborán", "Prometo"),
    ("QBaIMZ8QjcU", "Romeo Santos, Marc Anthony", "Yo También"),
    ("ghAvJMxE1qo", "Sebastián Yatra, Reik", "Un Año"),
    ("0diOZSlLKdg", "Carlos Rivera", "¿Cómo Pagarte?"),
    ("TOgCeRQvzoY", "Kany García", "Confieso"),
    ("_X3PPuF_yOE", "Río Roma", "Me Cambiaste la Vida"),
    ("DriCCFRQlj8", "Camilo, Evaluna Montaner", "Índigo"),
    ("weKJWqw8-3g", "Luis Fonsi, Juan Luis Guerra", "Llegaste Tú"),
    ("sPTn0QEhxds", "Shakira", "Me Enamoré"),
    ("OdaIbTUGmHM", "Prince Royce", "La Carretera"),
    ("XEvKn-QgAY0", "Prince Royce, Shakira", "Deja Vu"),
    ("Mtau4v6foHA", "Carlos Vives, Sebastián Yatra", "Robarte un Beso"),
    ("5R1RGl4WQP8", "Mon Laferte", "Tu Falta de Querer"),
    ("Uws510cVia4", "Ha*Ash", "Lo Aprendí de Ti"),
    ("_wL3Pc-EmjA", "Ha*Ash", "Perdón, Perdón"),
    ("OST41MmjdTQ", "Prince Royce", "El Amor Que Perdimos"),
    ("XNGWDH-6yv8", "Prince Royce", "Corazón Sin Cara"),
    ("-lDsqOsJL7k", "Prince Royce", "Culpa al Corazón"),
    ("4eCL0l9iD5A", "Romeo Santos", "Hilito"),
    ("VafbNsrHnD8", "Romeo Santos", "Llévame Contigo"),
    ("qjkb9_AJCLo", "Prince Royce", "Carita de Inocente"),
    ("DXiXPhvYuNU", "Romeo Santos, Santana", "Necio"),
    ("rvmtQvA_cmM", "Romeo Santos", "Sus Huellas"),
    ("J9QmUNZOh7I", "Daniel Santacruz", "Casablanca"),
    ("Vl7RmqGztbk", "Daniel Santacruz", "Bachata en Nueva York"),
    ("tNw9Rc3GbcE", "Daniel Santacruz", "Desnudos"),
    ("p2YCzaZNRqQ", "Daniel Santacruz", "No Me Sueltes"),
    ("CDv6lGEaWTo", "Henry Santos", "Por Nada"),
    ("R5V-A-iu9dg", "Henry Santos", "Te Di"),
    ("DjEttgmfNCU", "Henry Santos, JFab, Paola Fabre", "Cuando Te Toco"),
    ("g81JtMbrJtw", "Pinto Picasso", "París"),
    ("uUeNpTC7UWI", "Pinto Picasso", "No Me Toca"),
    ("RfTcYeNdZHY", "Héctor Acosta", "Amorcito Enfermito"),
    ("YrN5Z-Aj3QE", "Héctor Acosta", "Me Duele La Cabeza"),
    ("ot6wDVHqVNw", "Héctor Acosta", "Sin Perdón"),
    ("eshFzjIZZzA", "Bachata Heightz, Héctor Acosta", "Me Puedo Matar"),
    ("b0vDALH-CUw", "Kewin Cosmos", "Déjame Tenerte"),
    ("S50Vs_y1W2A", "Kewin Cosmos", "La Vecina"),
    ("Qz9gmiLBVFA", "Sebastián Yatra", "Tacones Rojos"),
    ("z1EB-fI0JDI", "Jesse & Joy", "Un Besito Más"),
    ("jwP1HRmDVII", "Carla Morrison", "Disfruto"),
    ("IKmPci5VXz0", "Natalia Lafourcade", "Hasta La Raíz"),
    ("0U3SkZEBGDY", "Ricky Martin", "Disparo al Corazón"),
    ("PQlG1gznMBE", "Mon Laferte", "Amor Completo"),
    ("OK_KvknlJxA", "Jesse & Joy, Mario Domm", "Llorar"),
    ("NAG98gpC8Hw", "Ha*Ash", "Ex de Verdad"),
    ("8_GGmHkgM-8", "Sin Bandera", "En Ésta No"),
    ("00QVU7voMq8", "Fonseca", "Eres Mi Sueño"),
    ("3VmoZrxXbmg", "Marc Anthony", "Flor Pálida"),
    ("BFaRWXEpFrs", "Marc Anthony", "Tu Vida en la Mía"),
    ("CJ_zRSv3Hr8", "Carlos Vives", "Volví a Nacer"),
    ("Nkloca2M6hU", "Juan Luis Guerra 4.40", "Tú"),
    ("prmzWy98c-I", "Jesse & Joy, Pablo Alborán", "La de la Mala Suerte"),
    ("nvxwiRuFgB0", "Jesse & Joy", "Me Soltaste"),
    ("ridGylKQ0WY", "Jesse & Joy, Luis Fonsi", "Tanto"),
    ("qKp1f7Vn9dM", "Camilo", "Vida de Rico"),
    ("9PCjVwJo3EI", "Prince Royce", "Te Me Vas"),
    ("agnV2YjuzSM", "Prince Royce", "Te Me Vas"),
    ("I_cJxvTQ6RM", "Ha*Ash", "100 Años"),
    ("W4AiOKlOO0Q", "Alejandro Sanz, Camila Cabello", "Mi Persona Favorita"),
    ("6eT6cmIZJAM", "Leslie Grace", "Cómo Duele el Silencio"),
    ("sfV6uwZKQRY", "Beret", "Lo Siento"),
    ("0nBzuG_jWbU", "Daniel Santacruz", "Lento"),
    ("EGJ_XbqC64E", "Alex Bueno", "Pídeme"),
    ("owOJ6L8Fepw", "Henry Santos", "Poquito a Poquito"),
    ("1d0y8h-9AAs", "Juan Luis Guerra", "Lacrimosa"),
    ("XOfM7aNH38s", "Carlos Rivera", "Te Esperaba"),
    ("tUhmwamgDZY", "Ha*Ash", "Te Dejo en Libertad"),
    ("NAG98gpC8Hw", "Ha*Ash", "Ex de Verdad"),
    ("u7rTroCsmCY", "Ha*Ash", "No Pasa Nada"),
    ("PQlG1gznMBE", "Mon Laferte", "Amor Completo"),
    ("fRJ3kh9cnQo", "Mon Laferte", "Antes De Ti"),
    ("BlhSvoMifVk", "Mon Laferte", "Pa' Dónde Se Fue"),
    ("szeA9tvItJY", "Morat", "Cuando Nadie Ve"),
    ("1oeD2m2UQAI", "Morat, Juanes", "Besos En Guerra"),
    ("0U3SkZEBGDY", "Ricky Martin", "Disparo al Corazón"),
    ("IKmPci5VXz0", "Natalia Lafourcade", "Hasta La Raíz"),
    ("jwP1HRmDVII", "Carla Morrison", "Disfruto"),
    ("TOgCeRQvzoY", "Kany García", "Confieso"),
    ("_X3PPuF_yOE", "Río Roma", "Me Cambiaste la Vida"),
    ("8_GGmHkgM-8", "Sin Bandera", "En Ésta No"),
    ("00QVU7voMq8", "Fonseca", "Eres Mi Sueño"),
]


def lead(artist: str) -> str:
    return (artist or "").split(",")[0].strip().lower()


def interleave(tracks: list, protect: int = 15) -> list:
    head, tail = tracks[:protect], tracks[protect:]
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
        "name": "malecon",
        "room": "malecon",
        "era": "hoy",
        "shuffle": False,
        "loop": True,
        "introCount": 15,
        "count": len(pub),
        "tracks": pub,
    }


def main() -> None:
    used = set()
    tracks = []
    for vid, artist, title in FIRST15:
        tracks.append({"id": vid, "artist": artist, "title": title})
        used.add(vid)

    romeo = sum(1 for t in tracks if lead(t["artist"]) == "romeo santos")
    royce = sum(1 for t in tracks if lead(t["artist"]) == "prince royce")
    for vid, artist, title in TAIL:
        if vid in used:
            continue
        ld = lead(artist)
        if ld == "romeo santos" and romeo >= 12:
            continue
        if ld == "prince royce" and royce >= 10:
            continue
        tracks.append({"id": vid, "artist": artist, "title": title})
        used.add(vid)
        if ld == "romeo santos":
            romeo += 1
        if ld == "prince royce":
            royce += 1
        if len(tracks) >= 100:
            break

    if len(tracks) < 100:
        raise SystemExit(f"only {len(tracks)}")
    tracks = interleave(tracks[:100], 15)
    c = Counter(lead(t["artist"]) for t in tracks)
    consec = sum(
        1
        for i in range(1, len(tracks))
        if lead(tracks[i]["artist"]) == lead(tracks[i - 1]["artist"])
    )
    print("n", len(tracks), "consec", consec)
    print("leads", c.most_common(12))
    print("romeo", c.get("romeo santos", 0), "royce", c.get("prince royce", 0))
    print("first15", [t["title"] for t in tracks[:15]])
    CUR.write_text(
        json.dumps(
            {
                "room": "malecon",
                "era": "hoy",
                "count": 100,
                "introCount": 15,
                "tracks": [{**t, "official": True, "intro": i < 15} for i, t in enumerate(tracks)],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n"
    )
    PUB.write_text(json.dumps(to_public(tracks), ensure_ascii=False, indent=2) + "\n")
    print("wrote", PUB)


if __name__ == "__main__":
    main()
