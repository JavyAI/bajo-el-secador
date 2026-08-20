#!/usr/bin/env python3
"""Recut Barbería (silla) AYER + HOY. Doorway first. Official 11-char only."""
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
UA = "Mozilla/5.0 en-la-barberia-curator"
ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")


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


def artist_of(t) -> str:
    return t["artist"] if isinstance(t, dict) else t[1]


def interleave(tracks: list, protect: int = 15) -> list:
    head = tracks[:protect]
    tail = tracks[protect:]
    last = lead(artist_of(head[-1])) if head else ""
    remaining = list(tail)
    out = list(head)
    while remaining:
        picked = None
        for i, t in enumerate(remaining):
            if lead(artist_of(t)) != last:
                picked = remaining.pop(i)
                break
        if picked is None:
            picked = remaining.pop(0)
        out.append(picked)
        last = lead(artist_of(picked))
    return out


def consec(tracks: list) -> int:
    return sum(
        1
        for i in range(1, len(tracks))
        if lead(tracks[i]["artist"]) == lead(tracks[i - 1]["artist"])
    )


# ---------------------------------------------------------------------------
# AYER — típica first, then Aventura era. Authored #1 Obsesión stays.
# Forgotten #1 Un Beso at #3. Medicina de Amor into the 15.
# ---------------------------------------------------------------------------
AYER_15 = [
    ("SEjw5rdyvVg", "Aventura", "Obsesión", 2002, "Aventura", 74662007),
    ("0mFaIxl1wgQ", "Frank Reyes", "Tú Eres Ajena", 1999, "JN Music Group", 39214996),
    ("uBwk106e3es", "Aventura", "Un Beso", 2005, "Aventura", 190140104),
    ("oVLS7QGWlGw", "Antony Santos", "Voy Pa'llá", 1992, "Anthony Santos - Topic", 7100000),
    ("xA0DBcsfjTE", "Monchy y Alexandra", "Hoja en Blanco", 1999, "JN Music Group", 279212605),
    ("L6YuWb-_R9Q", "Luis Vargas", "Loco de Amor", 1996, "JN Music Group", 2900000),
    ("b2Ig9IPBtRs", "Luis Segura", "Pena", 1982, "Luis Segura", 437264),
    ("kuCDQx9AmI8", "Raulín Rodríguez", "Nereyda", 1993, "Raulin Rodriguez - Topic", 919598),
    ("3hXdIcJ8ZDw", "Yoskar Sarante", "Perdóname", 2004, "Yoskar Sarante", 9882690),
    ("5HirJ6k5yzA", "Alex Bueno", "Que Vuelva", 1996, "JN Music Group", 40977059),
    ("mSQR149bnWg", "Antony Santos", "Por Mi Timidez", 1992, "Anthony Santos", 7778136),
    ("0m5SXO8qK78", "Monchy y Alexandra", "Dos Locos", 2002, "Radial / Orchard", 90281453),
    ("QnGNEn5KYc4", "Frank Reyes", "Nada De Nada", 2004, "JN Music Group", 34132573),
    ("9Vt0NBO37yI", "Raulín Rodríguez", "Medicina de Amor", 1994, "Raulin Rodriguez - Topic", 88300000),
    ("IRZv30Jbcms", "Zacarías Ferreira", "El Triste", 2002, "Zacarias Ferreira - Topic", 14020678),
]

AYER_FALLBACK = {
    "oVLS7QGWlGw": ("7WUL72Vvt-U", "Antony Santos", "Voy Pa'llá", 1992, "Anthony Santos - Topic", 836849),
    "L6YuWb-_R9Q": ("VIQ6cijCBf4", "Luis Vargas", "Loco de Amor", 1996, "Luis Vargas - Topic", 826634),
}

AYER_TAIL = [
    ("mVYQSAm8hB0", "Aventura", "Hermanita", 2002, "Aventura", 270700000),
    ("6KibGmX6vYY", "Antony Santos", "Corazón Culpable", 1993, "Anthony Santos", 78500000),
    ("CsziEW_gYhU", "Aventura", "Los Infieles", 2006, "Aventura", 443100000),
    ("z2pt4CN4rhc", "Aventura", "Mi Corazoncito", 2005, "Aventura", 179400000),
    ("q79vUDskBGQ", "Frank Reyes", "Princesa", 2005, "JN Music Group", 27800000),
    ("elGZbcpGzdU", "Aventura", "El Perdedor", 2009, "Aventura", 707300000),
    ("8sCWmb8f-BY", "Monchy y Alexandra", "Te Quiero Igual Que Ayer", 2002, "JN Music Group", 12000000),
    ("0XCot42qTvA", "Aventura", "Dile al Amor", 2009, "Aventura", 387300000),
    ("sEDubeD2CKw", "Luis Vargas", "Volvió el Dolor", 1997, "JN Music Group", 25300000),
    ("WllxyZpvVEs", "Aventura", "Angelito", 2002, "Aventura", 172500000),
    ("TUbNP4_TQws", "Joe Veras", "Se Te Nota", 2004, "JN Music Group", 47600000),
    ("6WeMiC-CJHA", "Aventura", "El Malo", 2009, "Aventura", 367300000),
    ("ePtOXORN96A", "Zacarías Ferreira", "Dime Qué Faltó", 2006, "Zacarias Ferreira", 58800000),
    ("hPT2FGoSOr8", "Aventura", "Amor de Madre", 2002, "Aventura", 175100000),
    ("8Ei86cJIWlk", "Raulín Rodríguez", "Esta Noche", 1995, "Planet Records Official", 47000000),
    ("rmerQRm3GJk", "Héctor Acosta", "Me Voy", 2008, "Hector Acosta", 59582698),
    ("ot6wDVHqVNw", "Héctor Acosta", "Sin Perdón", 2009, "Hector Acosta", 34100000),
    ("E1VfIlZQ_Zo", "Frank Reyes", "Déjame Entrar", 2004, "JN Music Group", 20700000),
    ("nZFJmyC8lq4", "Joe Veras", "El Hombre de Tu Vida", 2003, "JN Music Group", 30800000),
    ("ozJ7Edk4s9w", "Aventura", "La Boda", 2002, "Aventura", 48300000),
    ("wNqTWrgZPGE", "Zacarías Ferreira", "El Amor Tuvo La Culpa", 2007, "Zacarias Ferreira", 45500000),
    ("rzUjuMC9IDo", "Raulín Rodríguez", "Si Algún Día La Ves", 1995, "Raulin Rodriguez - Topic", 38700000),
    ("Lg_Pn45gyMs", "Aventura", "Ella y Yo", 2005, "Aventura", 982200000),
    ("iiBztjlX2Pc", "Antony Santos", "Porque Tanto Problema", 1994, "Anthony Santos", 0),
    ("snLLiz8l8IU", "Luis Vargas", "Si Tú Me Dejas", 1998, "Luis Vargas - Topic", 0),
    ("ZN6R4y7qBuw", "Frank Reyes", "Noche de Pasión", 2006, "JN Music Group", 19300000),
    ("GfFnQ2l2FxM", "Monchy y Alexandra", "Polos Opuestos", 2006, "JN Music Group", 0),
    ("j5XBAE8JbQ0", "Zacarías Ferreira", "Amiga Veneno", 2003, "Zacarias Ferreira", 38800000),
    ("OY7SCchuzac", "Alex Bueno", "El Jardín Prohibido", 1997, "JN Music Group", 28200000),
    ("2GXm8TmvEV4", "Raulín Rodríguez", "Amor De Mi Vida", 1996, "Raulin Rodriguez", 0),
    ("lgqkROx_qtI", "Joe Veras", "Me Decidí", 2005, "JN Music Group", 0),
    ("snNSmE7EwiM", "Luis Vargas", "La Mesa del Rincón", 1996, "JN Music Group", 12600000),
    ("5oMZic5Ba0g", "Frank Reyes", "Quién Eres Tú", 2007, "JN Music Group", 13700000),
    ("uURKRlanLb0", "Yoskar Sarante", "No Tengo Suerte En El Amor", 2003, "Yoskar Sarante", 21600000),
    ("M3_4mbL2u4A", "Héctor Acosta", "Con Qué Ojos", 2009, "Hector Acosta", 28500000),
    ("uK3pjjU-E2o", "Antony Santos", "Antología de Caricias", 1993, "Anthony Santos", 6200000),
    ("LwXSrmgPN40", "Luis Vargas", "La Traicionera", 1995, "Luis Vargas - Topic", 12500000),
    ("-6IpHAK5_7E", "Elvis Martínez", "Voy Amarte", 1999, "Elvis Martinez", 0),
    ("xocyXCDo0Nc", "Joe Veras", "Quiéreme", 2006, "JN Music Group", 0),
    ("WC94NQnW3_s", "Monchy y Alexandra", "No Es Una Novela", 2004, "JN Music Group", 0),
    ("3NFpJvs5eqk", "Zacarías Ferreira", "Cuánto Duele", 2004, "Zacarias Ferreira", 9300000),
    ("QcCYesRp53k", "Raulín Rodríguez", "Dame Tu Querer", 1994, "Raulin Rodriguez - Topic", 17600000),
    ("cBWXBseM7mQ", "Alex Bueno", "Con El Alma Desnuda", 1998, "JN Music Group", 16500000),
    ("5QniPGGwI7I", "Frank Reyes", "Se Me Olvidó Que Yo Te Amaba", 2002, "JN Music Group", 0),
    ("lZR4fh507-M", "Yoskar Sarante", "No Te Detengas", 2005, "Yoskar Sarante", 18900000),
    ("VY5zYtdhOCI", "Joe Veras", "Inténtalo Tú", 2005, "JN Music Group", 17500000),
    ("PwYDFbsntN8", "Luis Vargas", "La Mortificadora", 1996, "JN Music Group", 7400000),
    ("Vvg6GYgiq9Q", "Antony Santos", "Florecita", 1994, "Anthony Santos", 2200000),
    ("-XVVZYFvaZY", "Elvis Martínez", "Directo al Corazón", 1998, "Elvis Martinez", 15400000),
    ("UHD3JH67StE", "Luis Miguel del Amargue", "Como Te Quise Te Olvido", 2004, "Luis Miguel del Amargue", 21400000),
    ("RxZ4QlIphRE", "Frank Reyes", "Extraño a Mi Pueblo", 2006, "JN Music Group", 3500000),
    ("ByU6ABQ1cp8", "Monchy y Alexandra", "Perdidos", 2004, "JN Music Group", 5000000),
    ("1fJ9wejYS6c", "Raulín Rodríguez", "Culpable", 1995, "Raulin Rodriguez - Topic", 11300000),
    ("vyvGxPUMcyQ", "Héctor Acosta", "Tu Veneno", 2009, "Hector Acosta", 2100000),
    ("Ahsc80j8in8", "Yoskar Sarante", "Amor a Medio Tiempo", 2002, "Yoskar Sarante", 0),
    ("DVnpFry5HOg", "Zacarías Ferreira", "Es Tan Difícil", 2005, "Zacarias Ferreira", 5300000),
    ("JITSAJu6br4", "Antony Santos", "Ay Ven", 1993, "Anthony Santos", 1000000),
    ("taJTVVDpqcc", "Luis Vargas", "El Engaño", 1996, "Luis Vargas", 1800000),
    ("PswEMY8EXj0", "Frank Reyes", "Amor a Distancia", 2007, "JN Music Group", 3100000),
    ("0jxsmqcHr5o", "Teodoro Reyes", "Los Pobres También Aman", 1994, "Teodoro Reyes", 0),
    ("3rKDf5HOo40", "Elvis Martínez", "Bella Sin Alma", 2000, "Elvis Martinez", 0),
    ("dXbuf2U4rqU", "Monchy y Alexandra", "No Ha Sido Fácil", 2006, "JN Music Group", 0),
    ("WMNAgOIP4Mk", "Raulín Rodríguez", "Y Lloraré", 1996, "Raulin Rodriguez", 0),
    ("3lVgjyOTF00", "Antony Santos", "Ya Te Olvidé", 1995, "Anthony Santos", 1300000),
    ("q9inRooaK6I", "Luis Vargas", "Esa Mujer", 1997, "Luis Vargas", 1100000),
    ("avWqPIRWBvk", "Frank Reyes", "Se Fue de Mí", 2005, "JN Music Group", 1200000),
    ("G4o8lME7Bjc", "Héctor Acosta", "Me Puedo Matar", 2009, "Hector Acosta", 0),
    ("nCOW_Bidclw", "Juan Bautista", "Asesina", 1988, "Juan Bautista", 7400000),
    ("f6-QuSDqcNk", "Yoskar Sarante", "Tú, Él y Yo", 2001, "Yoskar Sarante", 0),
    ("rVgVeR2v08Q", "Teodoro Reyes", "La Quiero y Es Ajena", 1996, "Teodoro Reyes", 5600000),
    ("TOWqUKr-IVo", "Antony Santos", "La Parcela", 1994, "Anthony Santos", 582900),
    ("bt1o-aoHuRQ", "Luis Vargas", "El Maíz", 1995, "Luis Vargas", 1100000),
    ("mZrM2Sd_7tg", "Domenic Marte", "Ven Tú", 2004, "Domenic Marte", 4000000),
    ("QXxFPk6Kcxo", "Frank Reyes", "Ya Te Olvidé", 2006, "JN Music Group", 0),
    ("hyaHY0Dn1ok", "Raulín Rodríguez", "Como Quisiera Olvidarte", 1995, "Raulin Rodriguez", 2200000),
    ("hc1veQR3NMI", "Zacarías Ferreira", "Me Liberé", 2006, "Zacarias Ferreira", 1000000),
    ("pEdSZReW05I", "Antony Santos", "Mátame", 1996, "Anthony Santos", 0),
    ("T37tvBHoPYE", "Blas Durán", "El Total", 1987, "Blas Duran", 0),
    ("on4phFOVwRs", "Luis Segura", "Me Muero por Ella", 1985, "Luis Segura", 0),
    ("dNR1ntnF2wg", "Monchy y Alexandra", "Pasión", 2005, "JN Music Group", 1800000),
    ("Vz4CZOBa2P4", "Blas Durán", "Que Le Compre Su Traguito", 1987, "Blas Duran", 6300),
    ("uwuKYJtVqLM", "Andy Andy", "Qué Ironía", 2005, "Andy Andy", 674400),
    ("ZQzKX4-56dk", "Yoskar Sarante", "Llora Alma Mía", 2000, "Yoskar Sarante", 524100),
    ("qguZmEq3PEk", "Frank Reyes", "Ya Basta", 2008, "JN Music Group", 457600),
    ("FohoNEGLfQQ", "Yoskar Sarante", "Perdido", 2003, "Yoskar Sarante", 0),
]


# ---------------------------------------------------------------------------
# HOY — típica-now as LEADS in the 15. Romeo/Royce house pair, not a dump.
# Authored #1 Propuesta. Forgotten #1 Darte un Beso.
# Cut Volví, Deja Vu, Carita, Incondicional from the door.
# Cut 2010 Corazón Sin Cara. No 90s padding.
# ---------------------------------------------------------------------------
HOY_15 = [
    ("QFs3PIZb3js", "Romeo Santos", "Propuesta Indecente", 2013, "RomeoSantosVEVO", 2417540812),
    ("bdOXnTbyk0g", "Prince Royce", "Darte un Beso", 2013, "PrinceRoyceVEVO", 1623973849),
    ("XlmaJ-yU46U", "Aventura", "Inmortal", 2019, "RomeoSantosVEVO", 380923040),
    ("Y2KVvROYQrc", "Zacarías Ferreira", "El Intruso", 2018, "Zacarias Ferreira Oficial", 204000000),
    ("8iPcqtHoR3U", "Romeo Santos", "Eres Mía", 2014, "RomeoSantosVEVO", 1338790899),
    ("iuugCBK3RRI", "Antony Santos", "Creíste", 2013, "Anthony Santos", 11700000),
    ("RfTcYeNdZHY", "Héctor Acosta", "Amorcito Enfermito", 2016, "Hector Acosta", 125000000),
    ("1p0QyZIf93I", "Romeo Santos, Antony Santos, Luis Vargas, Raulín Rodríguez", "Debate de 4", 2011, "RomeoSantosVEVO", 43672764),
    ("AL_Ogy2TTXs", "El Chaval de la Bachata", "Dile A Él", 2019, "El Chaval de la Bachata", 0),
    ("D3qMNNgvsII", "Zacarías Ferreira", "Ya No Te Buscaré", 2017, "Zacarias Ferreira Oficial", 170800000),
    ("yUAZxs3qY3Y", "Prince Royce", "Te Robaré", 2013, "PrinceRoyceVEVO", 214356819),
    ("qurynQHSPhw", "Frank Reyes", "Mejor Que a Ti Me Va", 2024, "Frank Reyes", 33500000),
    ("cOy4siyFp0U", "Romeo Santos, Raulín Rodríguez", "La Demanda", 2019, "RomeoSantosVEVO", 125519187),
    ("ErgETXYYtC4", "Antony Santos", "Se Acabó el Abuso", 2019, "Anthony Santos", 18900000),
    ("TZdV0BvZW6o", "Raulín Rodríguez", "Corazón Con Candado", 2017, "Planet Records Official", 43600000),
]

HOY_TAIL = [
    ("mhHqonzsuoA", "Romeo Santos", "Imitadora", 2017, "RomeoSantosVEVO", 796700000),
    ("ROzZSmaxDz8", "Prince Royce", "Las Cosas Pequeñas", 2012, "Planet Records Official", 83600000),
    ("0w1eAAmOU4k", "Antony Santos, Romeo Santos", "Bellas", 2019, "Anthony Santos", 0),
    ("jk4HYngf65w", "Romeo Santos", "Cancioncitas de Amor", 2014, "RomeoSantosVEVO", 635500000),
    ("kCcljqz-wEY", "Zacarías Ferreira", "Si Pudiera", 2016, "Zacarias Ferreira Oficial", 52500000),
    ("CkNSGnekpBA", "Romeo Santos, Frank Reyes", "Payasos", 2019, "RomeoSantosVEVO", 113381249),
    ("cKtdb8ttsg4", "El Chaval de la Bachata", "El Último Golpe", 2018, "El Chaval de la Bachata", 28200000),
    ("4eCL0l9iD5A", "Romeo Santos", "Hilito", 2014, "RomeoSantosVEVO", 357600000),
    ("YrN5Z-Aj3QE", "Héctor Acosta", "Me Duele La Cabeza", 2015, "Hector Acosta", 41000000),
    ("8zcZC4HVr68", "Romeo Santos, El Chaval de la Bachata", "Canalla", 2019, "RomeoSantosVEVO", 185676188),
    ("PFMXOl3AQF0", "Frank Reyes", "Egoísta", 2021, "Frank Reyes", 41800000),
    ("rvmtQvA_cmM", "Romeo Santos", "Sus Huellas", 2022, "RomeoSantosVEVO", 139778614),
    ("E01fpwK9zZo", "Raulín Rodríguez", "Cómo Serás Tú", 2016, "Planet Records Official", 6700000),
    ("hpzT6Wq6pKY", "Prince Royce", "Incondicional", 2012, "Planet Records Official", 210810374),
    ("OuVhfYqb2fs", "Zacarías Ferreira", "La Mejor de Todas", 2015, "Zacarias Ferreira Oficial", 34300000),
    ("Ktq4zATPFsI", "Romeo Santos", "Héroe Favorito", 2017, "RomeoSantosVEVO", 331300000),
    ("ntOjtjk7qTo", "Frank Reyes", "Aventurero", 2021, "Frank Reyes", 1400000),
    ("OST41MmjdTQ", "Prince Royce", "El Amor Que Perdimos", 2012, "PrinceRoyceVEVO", 481620642),
    ("kKuBFuDFS_4", "Antony Santos", "El Eco de Tu Adiós", 2018, "Anthony Santos", 0),
    ("MkcXU_kn8dw", "Romeo Santos", "7 Días", 2011, "RomeoSantosVEVO", 259500000),
    ("1Tg_xhYHqpQ", "El Chaval de la Bachata", "Se Te Hizo Tarde", 2018, "El Chaval de la Bachata", 9900000),
    ("VafbNsrHnD8", "Romeo Santos", "Llévame Contigo", 2011, "RomeoSantosVEVO", 185200000),
    ("TF7DZgRM_cw", "Luis Vargas", "Yo Tengo Un Ángel", 2022, "Luis Vargas", 0),
    ("qjkb9_AJCLo", "Prince Royce", "Carita de Inocente (ALTER EGO)", 2020, "PrinceRoyceVEVO", 81452853),
    ("2aZeb5709TE", "Romeo Santos, Luis Vargas", "Los Últimos", 2019, "RomeoSantosVEVO", 0),
    ("mclq1x1Q7FM", "Zacarías Ferreira", "En Peligro de Extinción", 2014, "Zacarias Ferreira Oficial", 0),
    ("OdaIbTUGmHM", "Prince Royce", "La Carretera", 2016, "PrinceRoyceVEVO", 503023136),
    ("0-M3MkMCSso", "Antony Santos", "A Fuerza de Dolor", 2017, "Anthony Santos", 0),
    ("oLBTkf7jm0Q", "Romeo Santos, Zacarías Ferreira", "Me Quedo", 2019, "RomeoSantosVEVO", 0),
    ("7ZCa6wELRVc", "Raulín Rodríguez", "Mi Gran Amor", 2018, "Raulin Rodriguez", 0),
    ("-lDsqOsJL7k", "Prince Royce", "Culpa al Corazón", 2017, "PrinceRoyceVEVO", 0),
    ("FdDaPzhTIQs", "Luis Vargas", "Mal Herido", 2019, "Luis Vargas", 0),
    ("3ZcgUPwyhuI", "Romeo Santos", "Bebo", 2022, "RomeoSantosVEVO", 187500000),
    ("iZMOccjasnE", "Frank Reyes", "Quién Te Dio El Derecho", 2025, "Frank Reyes", 0),
    ("kVtfXd_WdkA", "Prince Royce", "Rechazame", 2012, "PrinceRoyceVEVO", 142100000),
    ("5MjbxCOy1Bo", "El Chaval de la Bachata", "La Locura de Tu Amor", 2023, "El Chaval de la Bachata", 5900000),
    ("DXiXPhvYuNU", "Romeo Santos, Santana", "Necio", 2014, "RomeoSantosVEVO", 415800000),
    ("ZB7mMiILVmQ", "Frank Reyes", "El Tubi", 2025, "Frank Reyes", 0),
    ("9PCjVwJo3EI", "Prince Royce", "Te Me Vas", 2012, "Planet Records Official", 14700000),
    ("COh7Al7hpPA", "Luis Segura, Romeo Santos", "Como Yo", 2019, "Luis Segura", 0),
    ("ed6XePWlMPY", "Luis Vargas", "Tarde Te Arrepientes", 2018, "Luis Vargas", 0),
    ("2wHa_op488g", "Frank Reyes", "Como Hojas al Viento", 2024, "Frank Reyes", 0),
    ("yUu6bxxRUGI", "Zacarías Ferreira", "Todos Juntos", 2019, "JN Music Group", 0),
    ("T4tGJ4MISNw", "Zacarías Ferreira", "10 Segundos", 2017, "Zacarias Ferreira Oficial", 16300000),
    ("0tAWnSebr_8", "Raulín Rodríguez", "Hablamos En La Cama", 2015, "Raulin Rodriguez", 0),
    ("FAL0qiSuH0Q", "Luis Miguel del Amargue", "A Un Milímetro de Ti", 2024, "Luis Miguel del Amargue", 0),
    ("Sq4In2ZvhTw", "Frank Reyes", "Me Haces Mucha Falta Amor", 2016, "Frank Reyes", 0),
    ("1-K9OwST2ZU", "Antony Santos, Los Sufridos", "Lleno Contigo", 2024, "Anthony Santos", 0),
    ("mp-g0oAGrOw", "Héctor Acosta", "Si No Me Falla El Corazón", 2014, "EL TORITO OFICIAL", 0),
    ("17fGLPG4Wtw", "Antony Santos", "Ay Chichi", 2023, "Anthony Santos - Topic", 0),
    ("F_l_I-QlcyE", "Héctor Acosta", "Ya Fue Bastante", 2022, "EL TORITO OFICIAL", 0),
    ("66qBzWshc_w", "Kiko Rodríguez", "Hoy Te Vi Pasar", 2015, "Kiko Rodriguez - Topic", 52300000),
    ("eshFzjIZZzA", "Bachata Heightz, Héctor Acosta", "Me Puedo Matar", 2011, "Bachata Heightz", 0),
    ("J9tC0cPsz3g", "Kiko Rodríguez", "Yo Fui el Primero", 2016, "Kiko Rodriguez - Topic", 9800000),
    ("hiFrZxa78tM", "Joe Veras", "Todo Cansa", 2023, "Joe Veras Oficial", 12400000),
    ("xm-Z_2XpPFY", "Kiko Rodríguez", "La Boda (Me Arrepentí)", 2025, "Kiko Rodriguez", 0),
    ("L48Mw2W6v6Q", "Joe Veras", "Tu Excusa", 2025, "JoeVerasVEVO", 0),
    ("Ra5xGEPlIjw", "Kiko Rodríguez", "Usted No Sabe", 2025, "Kiko Rodriguez", 0),
    ("I68EMkzz3jI", "Joe Veras", "Aunque No Sea Conmigo", 2025, "JoeVerasVEVO", 0),
    ("Xr_jslGVFvo", "Grupo Extra", "Me Emborracharé", 2014, "Urban Latin Records", 0),
    ("tP_XZ0teEno", "Yoskar Sarante, El Chaval de la Bachata", "Tres Veces", 2015, "JN Music Group", 0),
    ("IFfLjoKsHX0", "Grupo Extra", "Qué Mal Te Hice Yo", 2015, "Urban Latin Records", 0),
    ("CDv6lGEaWTo", "Henry Santos", "Por Nada", 2012, "HenrySantosVEVO", 2400000),
    ("W1_7r-7D74I", "Grupo Extra", "Te Vas", 2013, "Urban Latin Records", 0),
    ("DiZEZg93U1E", "Elvis Martínez", "Ambición", 2012, "Elvis Martinez", 0),
    ("nKN8tTN-_O0", "Grupo Extra", "Tengo Una Necesidad", 2014, "Urban Latin Records", 0),
    ("R5V-A-iu9dg", "Henry Santos, Pavel Núñez", "Te Di", 2015, "Henry Santos", 0),
    ("9kbFdKX1rJw", "Grupo Extra", "Lejos de Ti", 2016, "Urban Latin Records", 0),
    ("1S7SJcEKfuY", "Elvis Martínez", "Tú Sabes Bien", 2017, "Elvis Martinez", 0),
    ("Q2HftVyi6wc", "Grupo Extra, Lirow", "Cuando Te Vuelva a Ver", 2018, "Urban Latin Records", 0),
    ("DjEttgmfNCU", "Henry Santos, JFab, Paola Fabre", "Cuando Te Toco", 2020, "Henry Santos", 0),
    ("uXLkI5Lknpo", "Grupo Extra", "Dile a Él", 2014, "Urban Latin Records", 0),
    ("2Y6uAa6Jnpw", "Henry Santos", "Poquito A Poquito", 2011, "HenrySantosVEVO", 4900000),
    ("m9Xxk7pXE3s", "Elvis Martínez", "Rica", 2016, "Elvis Martinez", 0),
    ("J9QmUNZOh7I", "Daniel Santacruz", "Casablanca", 2013, "Daniel Santacruz", 0),
    ("VJSBbSlykM8", "Teodoro Reyes", "El Huequito", 2016, "Teodoro Reyes", 0),
    ("Vl7RmqGztbk", "Daniel Santacruz", "Bachata en Nueva York", 2015, "Daniel Santacruz", 0),
    ("4GU0sTsIpzo", "Teodoro Reyes", "Mis Dos Estrellas", 2014, "Teodoro Reyes", 0),
    ("p2YCzaZNRqQ", "Daniel Santacruz", "No Me Sueltes", 2018, "Daniel Santacruz", 0),
    ("z285rG7DkhA", "Teodoro Reyes", "Me Dejó Por Otro", 2015, "Teodoro Reyes", 0),
    ("tNw9Rc3GbcE", "Daniel Santacruz", "Desnudos", 2017, "Daniel Santacruz", 0),
    ("uUeNpTC7UWI", "Pinto Picasso", "No Me Toca", 2018, "BCHTA RECORDS", 0),
    ("b0vDALH-CUw", "Kewin Cosmos", "Déjame Tenerte", 2018, "Kewin Cosmos", 0),
    ("g81JtMbrJtw", "Pinto Picasso", "París", 2019, "Pinto Picasso", 0),
    ("S50Vs_y1W2A", "Kewin Cosmos", "La Vecina", 2019, "Kewin Cosmos", 0),
]


def pack(row, intro: bool) -> dict:
    vid, artist, title, year, channel, views = row
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


def verify_rows(rows: list) -> dict:
    ids = [r[0] for r in rows]
    out = {}
    with ThreadPoolExecutor(max_workers=12) as pool:
        futs = {pool.submit(check, vid): vid for vid in ids}
        for fut in as_completed(futs):
            out[futs[fut]] = fut.result()
    return out


def apply_fallbacks(rows: list, recs: dict, fallbacks: dict) -> list:
    fixed = []
    for row in rows:
        vid = row[0]
        rec = recs.get(vid, {})
        if rec.get("ok"):
            fixed.append(row)
            continue
        alt = fallbacks.get(vid)
        if alt:
            print(f" FALLBACK {vid} → {alt[0]} ({row[2]}) err={rec.get('err')}")
            fixed.append(alt)
        else:
            print(f" FAIL drop {vid} {row[1]} — {row[2]} err={rec.get('err')} author={rec.get('author')}")
    return fixed


def hygiene(tracks: list, era: str) -> None:
    n = len(tracks)
    ids = [t["id"] for t in tracks]
    print(f"\n=== {era} n={n} unique={len(set(ids))} consec={consec(tracks)} ===")
    print("first15:")
    for i, t in enumerate(tracks[:15], 1):
        print(f"  {i:2d}. {t['artist'].split(',')[0]} — {t['title']} [{t['id']}] {t['year']}")
    print("leads:", Counter(lead(t["artist"]) for t in tracks).most_common(12))
    romeo = sum(1 for t in tracks if lead(t["artist"]) == "romeo santos")
    aventura = sum(1 for t in tracks if lead(t["artist"]) == "aventura")
    royce = sum(1 for t in tracks if lead(t["artist"]) == "prince royce")
    print(f"romeo-lead={romeo} aventura-lead={aventura} royce-lead={royce}")
    dups = [i for i, c in Counter(ids).items() if c > 1]
    if dups:
        print("DUP IDS", dups)
    over = [(a, c) for a, c in Counter(lead(t["artist"]) for t in tracks).items() if c > 18]
    mid = [(a, c) for a, c in Counter(lead(t["artist"]) for t in tracks).items() if 13 <= c <= 18]
    print("over18", over, "kings13-18", mid)
    years = [t["year"] for t in tracks]
    print(f"year min={min(years)} max={max(years)}")


def write_list(path: Path, room: str, era: str, tracks: list) -> None:
    payload = {
        "room": room,
        "era": era,
        "count": len(tracks),
        "introCount": 15,
        "tracks": tracks,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print("wrote", path, "n=", len(tracks))


def main() -> None:
    print("verifying AYER ids")
    ayer_all = AYER_15 + AYER_TAIL
    ayer_recs = verify_rows(ayer_all)
    ayer_15 = apply_fallbacks(AYER_15, ayer_recs, AYER_FALLBACK)
    need = [r for r in ayer_15 if r[0] not in ayer_recs or not ayer_recs[r[0]].get("ok")]
    if need:
        extra = verify_rows(need)
        ayer_recs.update(extra)
        ayer_15 = apply_fallbacks(ayer_15, ayer_recs, {})
    ayer_tail = apply_fallbacks(AYER_TAIL, ayer_recs, {})
    used = {r[0] for r in ayer_15}
    ayer_tail = [r for r in ayer_tail if r[0] not in used]
    ayer_rows = interleave(ayer_15 + ayer_tail, 15)[:100]
    ayer_tracks = [pack(r, i < 15) for i, r in enumerate(ayer_rows)]
    hygiene(ayer_tracks, "AYER")

    print("\nverifying HOY ids")
    hoy_all = HOY_15 + HOY_TAIL
    hoy_recs = verify_rows(hoy_all)
    for vid, rec in sorted(hoy_recs.items()):
        if not rec.get("ok"):
            print(" HOY FAIL", vid, rec.get("err"), rec.get("author"), rec.get("title"))
    hoy_15 = apply_fallbacks(HOY_15, hoy_recs, {})
    hoy_tail = apply_fallbacks(HOY_TAIL, hoy_recs, {})
    used = {r[0] for r in hoy_15}
    hoy_tail = [r for r in hoy_tail if r[0] not in used]
    hoy_rows = interleave(hoy_15 + hoy_tail, 15)
    print(f"HOY assembled {len(hoy_rows)}")
    if len(hoy_rows) < 100:
        print(f"HOY SHORT {len(hoy_rows)}")
    hoy_rows = hoy_rows[:100]
    hoy_tracks = [pack(r, i < 15) for i, r in enumerate(hoy_rows)]
    hygiene(hoy_tracks, "HOY")

    if len(ayer_tracks) != 100:
        raise SystemExit(f"AYER not 100: {len(ayer_tracks)}")
    if len(hoy_tracks) != 100:
        raise SystemExit(f"HOY not 100: {len(hoy_tracks)}")
    if consec(ayer_tracks):
        raise SystemExit("AYER consecutive leads")
    if consec(hoy_tracks):
        raise SystemExit("HOY consecutive leads")
    if ayer_tracks[0]["id"] != "SEjw5rdyvVg":
        raise SystemExit("AYER #1 moved")
    if hoy_tracks[0]["id"] != "QFs3PIZb3js":
        raise SystemExit("HOY #1 moved")

    write_list(CUR / "silla-ayer.json", "silla", "ayer", ayer_tracks)
    write_list(CUR / "silla-hoy.json", "silla", "hoy", hoy_tracks)


if __name__ == "__main__":
    main()
