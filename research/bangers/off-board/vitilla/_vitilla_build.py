#!/usr/bin/env python3
"""Build and verify Vitilla AYER/HOY curation JSON."""
from __future__ import annotations

import json
import ssl
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

OUT = Path(__file__).resolve().parent
CTX = ssl.create_default_context()

# (id, artist, title, year, intro)
AYER = [
    ("rOw9UxJyhII", "Los Hermanos Rosario", "La Dueña del Swing", 1995, True),
    ("1DbXzlhKS5s", "Wilfrido Vargas", "El Africano", 1983, True),
    ("WPiEbYSF9kE", "Elvis Crespo", "Suavemente", 1998, True),
    ("4Qy0vs80T5M", "Proyecto Uno", "El Tiburón", 1996, True),
    ("eLTvctdHftc", "Kinito Méndez", "Cachamba", 1995, True),
    ("ssOtmdQatGQ", "Toño Rosario", "Kulikitaka", 2003, True),
    ("x6Y3EFLtnFM", "Fulanito", "Guallando", 1997, True),
    ("BT8Afk8HDxY", "Ilegales", "La Morena", 1995, True),
    ("fs1Fg07CsQs", "Wilfrido Vargas", "El Baile del Perrito", 1993, True),
    ("McV4pBRb-Sg", "Juan Luis Guerra", "La Bilirrubina", 1990, True),
    ("m29uPaJ0Deo", "Grupo Manía", "A Que Te Pego Mi Manía", 1995, True),
    ("AJ_OX-w7G_Q", "Sandy y Papo", "Mueve Mueve", 1996, True),
    ("e9vSD4KLM0Y", "Juan Luis Guerra", "La Hormiguita", 1998, True),
    ("OHY_UwId_0M", "Fulanito", "El Cepillo", 1997, True),
    ("vtizic9NnfY", "Kinito Méndez", "El Baile del Sua Sua", 1996, True),
    ("AhGe1rsLuQQ", "Proyecto Uno", "Esta Pega'o", 1993, False),
    ("3CqNeJLqvL0", "Elvis Crespo", "Tu Sonrisa", 1998, False),
    ("JPU1_MNLZ1Y", "Ilegales", "El Taqui Taqui", 1997, False),
    ("3SJwKBxKuoM", "Juan Luis Guerra", "La Cosquillita", 1994, False),
    ("dElUL4hvbJE", "Grupo Manía", "Linda Eh", 1996, False),
    ("Ety4cES6hRQ", "Proyecto Uno", "Brinca", 1991, False),
    ("ipDNOrqLIHU", "Toño Rosario", "Resistiré", 2009, False),
    ("epndigKqzDs", "Wilfrido Vargas", "El Jardinero", 1984, False),
    ("_gGwBmmnYls", "Las Chicas del Can", "Juana la Cubana", 1988, False),
    ("_koz_f4mthE", "Juan Luis Guerra", "A Pedir Su Mano", 1990, False),
    ("hBhIA8lDi2c", "Elvis Crespo", "Píntame", 1999, False),
    ("_u2m43WXQks", "Ramón Orlando", "El Venao", 1992, False),
    ("FChzlYpau0g", "Olga Tañón", "Es Mentiroso", 1994, False),
    ("4iBwipKkX6k", "Proyecto Uno", "25 Horas", 1993, False),
    ("E6soE-1p3kw", "Milly Quezada", "Volvió Juanita", 1984, False),
    ("yWSQxGppcFA", "Eddy Herrera", "Pégame Tu Vicio", 2000, False),
    ("V1jnol6o1kQ", "Bonny Cepeda", "La Asesina", 1987, False),
    ("ihZQAh4jr4M", "Juan Luis Guerra", "Las Avispas", 2004, False),
    ("95Wcl9ucitM", "Sergio Vargas", "La Ventanita", 1991, False),
    ("jaxUyaTc4wo", "La Makina", "Nadie Se Muere", 1997, False),
    ("Q_2rzu1f-eo", "Elvis Crespo", "La Cerveza", 1998, False),
    ("HOrPwEZLhD4", "Kinito Méndez", "El Asilo", 1996, False),
    ("SGy4pmOvKVI", "Olga Tañón", "Bandolero", 1994, False),
    ("lvfQWpvcE30", "Los Hermanos Rosario", "Ella Se Fue", 1995, False),
    ("uWIl86jzQqc", "Johnny Ventura", "El Sueño", 1985, False),
    ("tRpRavSeAac", "Rikarena", "Ay!!", 1994, False),
    ("eotdaHXYV3Y", "Eddy Herrera", "Carolina", 1993, False),
    ("bntQQjEnbPA", "Wilfrido Vargas", "Abusadora", 1981, False),
    ("uwQ-2yfnuRU", "Gisselle y Sergio Vargas", "Perdóname, Olvídalo", 1997, False),
    ("ydz-OjoIyuo", "Los Hermanos Rosario", "Dominicana", 1994, False),
    ("-cI_d6kRF1M", "Olga Tañón", "Muchacho Malo", 1993, False),
    ("qfgWkLAmKCM", "Milly Quezada", "Tengo", 1995, False),
    ("E0f3J0z2SBQ", "Fernandito Villalona", "Cama y Mesa", 1983, False),

    ("NYW9T4D7zLw", "Elvis Crespo", "Nuestra Canción", 1998, False),
    ("M3fdWamxjA0", "Grupo Manía", "Me Miras y Te Miro", 1997, False),
    ("zZTo7FYn0lI", "Eddy Herrera", "Me Sabe A Poco", 2002, False),
    ("9x_Zmt4S01s", "Juan Luis Guerra", "La Guagua", 2010, False),
    ("CokWGmuYduM", "Proyecto Uno", "El Grillero", 1996, False),
    ("jnkLAMVI0so", "Grupo Manía", "Ojitos Bellos", 1995, False),
    ("uzU3x_egiEk", "Eddy Herrera", "Tú Eres Ajena", 1996, False),
    ("tPTB0TRV3BA", "Juan Luis Guerra", "El Costo de La Vida", 1992, False),
    ("8QFzVz8whgQ", "Rubby Pérez", "Volveré", 1987, False),
    ("MwJSpVhqFT0", "Fulanito", "La Novela", 1997, False),
    ("sWF2rtxBs4k", "Omega El Fuerte", "Si Te Vas", 2009, False),
    ("bAqw7qQbbXU", "Grupo Manía", "Adivina", 1999, False),
    ("dDEVFQnBTp0", "Juan Luis Guerra", "Ojalá Que Llueva Café", 1989, False),
    ("3BcFam44YYE", "Oro Sólido", "La Paleta", 1994, False),
    ("f7-vEi-uPB8", "Wilfrido Vargas", "Volveré", 1987, False),
    ("49rim-OQ5p0", "Elvis Crespo, Milly Quezada", "Para Darte Mi Vida", 1998, False),
    ("KMtO-egYiFg", "Los Toros Band", "Mi Primer Millón", 2003, False),
    ("Gu2nonpFNCY", "Johnny Ventura", "¿Pitaste?", 1993, False),
    ("e7snJWtn5WI", "Magic Juan, Eddy Herrera", "La Última Vez", 2004, False),
    ("UzKAmOPS3wE", "Manny Manuel", "Rey de Corazones", 1997, False),
    ("fw9orjqEPOc", "Elvis Crespo, Grupo Manía", "Linda Eh (Live Las Vegas)", 2008, False),
    ("2kR2FrKOyhM", "Toño Rosario", "Mujer De Todos, Mujer De Nadie", 2001, False),
    ("Ksc-jNxOx4c", "La Makina", "No Me Digas Que No", 1999, False),
    ("yZaVBHYzWxU", "Olga Tañón", "Hielo y Fuego", 1998, False),
    ("uxZPwAedgFA", "Los Hermanos Rosario", "Bomba", 1990, False),
    ("mdndTRMvPu0", "Pochy y Su Cocoband", "La Flaca", 2007, False),
    ("DZtWoBZUsJg", "Toño Rosario", "Tú Va Vei", 1999, False),
    ("yGvStabyqIE", "Las Chicas del Can", "El Negro No Puede", 1987, False),
    ("Xvps1fC4z1M", "Eddy Herrera", "Demasiado Romántica", 1998, False),
    ("30LcD8c7jJA", "Kinito Méndez", "La Grúa", 1995, False),
    ("slcQ7-Q-5AU", "Eddy Herrera", "Como Hago", 1997, False),
    ("-ENNz5-rWIs", "Kinito Méndez", "Hony Tú Sí Jony", 2004, False),
    ("r4l2VrWBQ0c", "Fernando Villalona", "Tabaco y Ron", 1982, False),
    ("Hb9V7BI2b1U", "Juan Luis Guerra", "El Farolito", 1994, False),
    ("BtbJhoeopt0", "Eddy Herrera", "La Bailadora", 1994, False),
    ("4XR_X26blYA", "Ilegales", "Fiesta Caliente", 1995, False),
    ("gdbDRfu3cPk", "Sandy y Papo", "El Alacrán", 1997, False),
    ("BHxrn49NjQw", "Ilegales", "A Que Te Pongo", 1995, False),
    ("7zX1yooCylk", "Toño Rosario", "Jenny", 1994, False),
    ("OkOJGgqcwro", "Olga Tañón", "Como Olvidar", 1996, False),
    ("hiXux44IlT4", "Juan Luis Guerra", "La Gallera", 1989, False),
    ("PePGIiVK0wo", "Eddy Herrera", "Como Llora Mi Alma", 2004, False),
    ("dPK_W5GR8lg", "Fernando Villalona", "Sonámbulo", 1986, False),
    ("QNcpohnprEg", "Eddy Herrera", "Un Idiota", 2006, False),
]

HOY = [
    ("hpkaifThmOs", "Juan Luis Guerra", "Kitipun", 2019, True),
    ("hal7rXfJj5o", "Toño Rosario", "Dale Vieja Dale", 2016, True),
    ("4R7NmEa8s8M", "Manny Cruz, Los Hermanos Rosario", "La Dueña del Swing", 2025, True),
    ("K3S96fUGrEY", "Juan Luis Guerra", "Mambo 23", 2023, True),
    ("SRDkwORUPak", "Toño Rosario", "Vuelve Mami", 2020, True),
    ("cenRb14_sMY", "Manny Cruz, Johnny Ventura", "Qué Rico Es El Merengue", 2021, True),
    ("NAEGTNrfmmo", "Vicente García, Juan Luis Guerra", "Loma de Cayenas", 2018, True),
    ("mksDUrgVBDc", "Ilegales", "Chucucha", 2013, True),
    ("WENJIxEfyaw", "Juan Luis Guerra", "La Noviecita", 2023, True),
    ("zyDjrb5GWr8", "Manny Cruz", "Santo Domingo", 2021, True),
    ("-gCgSXFctOQ", "Ilegales", "Meneo", 2020, True),
    ("dUOC-ryYtQI", "Juan Luis Guerra", "I Love You More", 2019, True),
    ("e1Hp8YaQJHc", "Manny Cruz, Aramis Camilo", "El Motor", 2024, True),
    ("ivz_5RS-ENM", "Grupo Manía", "Guaya", 2025, True),
    ("8HCXYy36RM8", "Manny Cruz, Wilfrido Vargas", "El Hombre Divertido", 2024, True),
    ("qhOPeeZHSWE", "Los Hermanos Rosario", "Nuevecita de Caja", 2015, False),
    ("S3h4xmU-qQM", "Manny Cruz", "All Night Long", 2024, False),
    ("7ddBc_Jxbw0", "Elvis Crespo, Fito Blanko", "Pegaito Suavecito", 2016, False),
    ("P_xKX0NBTeQ", "Eddy Herrera", "Si No Era Yo", 2026, False),
    ("vEDn-xoL4Ss", "Manny Cruz", "OYE", 2025, False),
    ("T2BezGCx9q8", "Eddy Herrera", "Ahora Soy Yo", 2020, False),
    ("388Lm2U9Cy8", "Manny Cruz", "Sabes Enamorarme", 2018, False),
    ("dyM5fHdbowM", "Eddy Herrera", "Si Yo Se Lo Pido", 2022, False),
    ("mMBmpYvJe6E", "Manny Cruz", "Si Tú Me Miras", 2025, False),
    ("CtJzPo-OqnY", "Eddy Herrera", "Y Cómo Te Olvido", 2025, False),
    ("qpcGlvzMtaA", "Manny Cruz", "Tus 15 Primaveras", 2019, False),
    ("zd6YpctrLF8", "Los Hermanos Rosario", "Amor Fallido", 2022, False),
    ("ERlLjPvgDJA", "Ilegales", "Baila Conmigo", 2021, False),
    ("0XTsbCeG-Tk", "Proyecto Uno", "Como Tú No Hay Dos", 2023, False),
    ("kx1hkhvz5v8", "Milly Quezada", "Tu Mundo Cambió", 2018, False),
    ("F2xnLHtz00k", "Proyecto Uno", "Regresa Al Nido", 2025, False),
    ("R2Gl0uDgSX8", "Ilegales", "Dime Que Sí", 2019, False),
    ("DgRGekKhCM0", "Los Hermanos Rosario", "Yo Quiero Que Me Des Un Like", 2016, False),
    ("SRLRCCffvlA", "Juan Luis Guerra", "El Farolito (Live)", 2021, False),
    ("cThHSC-_TK4", "Julián Oro Duro", "Prepárate", 2021, False),
    ("RksYXExb0d0", "Juan Luis Guerra", "Vale La Pena (Live)", 2021, False),
    ("oPxoG9irdqE", "Elvis Crespo, Michael Flores", "Abeja Blanca 2.0", 2024, False),
    ("JSTzS_T-2nE", "Manny Cruz, Fernando Villalona", "Medley Mayimbe", 2024, False),
    ("Daf4icdvGPQ", "Olga Tañón", "Así Yo Soy", 2024, False),
    ("sHRzCQEHpU8", "Manny Cruz", "De Lunes a Lunes", 2021, False),
    ("yfptK2ozc2w", "Olga Tañón, Christian Alicea", "Vamos A Ser Feliz", 2023, False),
    ("ALxQBUFpI1s", "Manny Cruz", "Qué Vamo' A Hacer", 2021, False),
    ("8m48iM1UZWY", "Toño Rosario", "Baby Ven Conmigo", 2023, False),
    ("gqkSXYlKt6s", "Nacho, Manny Cruz, Daniel Santacruz", "Dame Una Noche", 2022, False),
    ("YWVA6iziV5g", "Eddy Herrera", "El Trago", 2023, False),
    ("B2SLbC8fnfs", "Elvis Crespo, Manny Cruz", "Imaginarme Sin Ti", 2020, False),
    ("koUeLdZk4Gc", "Ilegales", "No Guarda Luto", 2024, False),
    ("-Vu9Xe8z1eY", "Eddy Herrera", "Quiero Más", 2024, False),
    ("ZBI5nYDrVUc", "Grupo Manía", "Ziriguidum", 2021, False),
    ("tqCQkWEw_Fs", "Wilfrido Vargas", "El Bebé", 2024, False),
    ("GiQddVUaXxk", "Ilegales", "La Pastilla", 2014, False),
    ("9bUxa_tffZA", "Grupo Manía", "Apaga Fuego", 2022, False),
    ("JMq0HJXIp8o", "Juan Luis Guerra", "Corazón Enamorado", 2019, False),
    ("tWdt2dgxMM0", "Ilegales, El Potro Álvarez", "Pasarla Bien", 2015, False),
    ("lzFe4XMk3R0", "Olga Tañón, Eddy Herrera", "Ya No Soy Ajena", 2023, False),
    ("daZ2aRW7ico", "Juan Luis Guerra", "Señorita (Capitán Avispa)", 2024, False),
    ("oEwFnWCmqQU", "Ilegales", "Open", 2023, False),
    ("Qq0Ih7XKoFM", "Manny Cruz", "Gota de Crystal", 2024, False),
    ("eRuik2VCEW0", "Ilegales", "La Mata", 2026, False),
    ("ysLKq-twqUw", "Eddy Herrera, José Alberto El Canario", "Bailemos Otra Vez", 2023, False),
    ("VolmYSTcUzM", "Ilegales", "Mucho Flow", 2023, False),
    ("dw5AoDr3Gmo", "Kinito Méndez", "Pagando Pa' Sufrir", 2023, False),
    ("SMF9nGExTyk", "Ilegales", "Ganas", 2025, False),
    ("AFykvpZBsVc", "Eddy Herrera, Manny Cruz", "No Me Lo Creo", 2018, False),
    ("02FHzWNLibE", "Ilegales", "De Paso", 2025, False),
]


def get(url: str, timeout: int = 20):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (vitilla-curation)"},
    )
    with urllib.request.urlopen(req, context=CTX, timeout=timeout) as r:
        return r.status, r.read(), dict(r.headers)


def oembed(vid: str):
    url = "https://www.youtube.com/oembed?url=" + urllib.parse.quote(
        f"https://www.youtube.com/watch?v={vid}", safe=""
    ) + "&format=json"
    try:
        status, body, _ = get(url)
        if status != 200:
            return None
        return json.loads(body.decode("utf-8"))
    except Exception:
        return None


def mq_ok(vid: str) -> bool:
    url = f"https://i.ytimg.com/vi/{vid}/mqdefault.jpg"
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=CTX, timeout=15) as r:
            if r.status != 200:
                return False
            cl = r.headers.get("Content-Length")
            # YouTube 404 placeholder is a tiny gray image (~1000-1200 bytes).
            if cl and int(cl) < 2000:
                return False
            return True
    except Exception:
        try:
            status, body, _ = get(url)
            return status == 200 and len(body) > 2000
        except Exception:
            return False


def views_of(vid: str) -> int:
    url = f"https://returnyoutubedislikeapi.com/votes?videoId={vid}"
    try:
        status, body, _ = get(url)
        if status != 200:
            return 0
        data = json.loads(body.decode("utf-8"))
        return int(data.get("viewCount") or 0)
    except Exception:
        return 0


def official_enough(channel: str) -> bool:
    c = (channel or "").lower()
    needles = [
        "vevo", "topic", "jn music", "karen", "warner", "planet", "fania",
        "universal", "sony", "cutting records", "elviscrespo", "elvis crespo", "juan luis",
        "oreja",
        "hermanos rosario", "wilfrido", "toño rosario", "tono rosario",
        "fulanito", "ilegales", "proyecto uno", "kinito", "grupo mania",
        "cantantes", "vecinos", "pochy", "makina", "toros",
        "manía", "manny cruz", "eddy herrera", "milly", "olga", "chicas del can",
        "sandy", "oro solido", "oro sólido", "johnny ventura", "sergio vargas",
        "fernandito", "villalona", "bonny", "rubby", "rikarena", "gisselle",
        "vicente garcía", "vicente garcia", "omega", "julian oro", "julián oro",
        "los toros", "banda gorda", "pochy", "jossie", "alex bueno",
        "manny manuel", "cuco valoy", "ramón orlando", "ramon orlando",
        "caña brava", "sabrosos", "festivaldevina", "symphonic",
    ]
    return any(n in c for n in needles)


def probe(row):
    vid, artist, title, year, intro = row
    info = oembed(vid)
    art = mq_ok(vid)
    views = views_of(vid)
    channel = (info or {}).get("author_name") or ""
    official = bool(info) and official_enough(channel)
    return {
        "id": vid,
        "artist": artist,
        "title": title,
        "year": year,
        "channel": channel,
        "views": views,
        "official": official,
        "artworkOk": bool(art),
        "intro": bool(intro),
        "oembed": bool(info),
    }


def verify_list(rows, room, era):
    probed = {}
    with ThreadPoolExecutor(max_workers=12) as pool:
        futs = {pool.submit(probe, row): row[0] for row in rows}
        for fut in as_completed(futs):
            track = fut.result()
            probed[track["id"]] = track
            print(
                f"{era} {track['id']} art={track['artworkOk']} off={track['official']} "
                f"views={track['views']} ch={track['channel']!r} {track['artist']} — {track['title']}",
                flush=True,
            )
    tracks = []
    seen = set()
    prev_artist = None
    fails = []
    for vid, artist, title, year, intro in rows:
        if vid in seen:
            fails.append((vid, title, "duplicate id"))
            continue
        if len(vid) != 11:
            fails.append((vid, title, "bad id length"))
            continue
        lead = artist.split(",")[0].strip().lower()
        if prev_artist and lead == prev_artist:
            fails.append((vid, title, "consecutive artist"))
        track = probed[vid]
        if not track["oembed"]:
            fails.append((vid, title, "oembed fail"))
        if not track["artworkOk"]:
            fails.append((vid, title, "mqdefault fail"))
        if not track["official"]:
            fails.append((vid, title, f"unofficial:{track['channel']}"))
        tracks.append({k: track[k] for k in (
            "id", "artist", "title", "year", "channel", "views", "official", "artworkOk", "intro"
        )})
        seen.add(vid)
        prev_artist = lead
    payload = {
        "room": room,
        "era": era,
        "count": len(tracks),
        "introCount": 15,
        "tracks": tracks,
    }
    return payload, fails


def main():
    ayer, af = verify_list(AYER, "vitilla", "ayer")
    hoy, hf = verify_list(HOY, "vitilla", "hoy")
    (OUT / "vitilla-ayer.json").write_text(
        json.dumps(ayer, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (OUT / "vitilla-hoy.json").write_text(
        json.dumps(hoy, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print("AYER count", ayer["count"], "fails", len(af))
    for row in af:
        print("  AYER FAIL", row)
    print("HOY count", hoy["count"], "fails", len(hf))
    for row in hf:
        print("  HOY FAIL", row)


if __name__ == "__main__":
    main()
