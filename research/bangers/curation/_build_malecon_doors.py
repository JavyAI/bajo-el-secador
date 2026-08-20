#!/usr/bin/env python3
"""Recut Malecón El Ayer + El Presente: couple radio, doorway first."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

CUR = Path("/Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador/research/bangers/curation")

KINGS = {
    "juan luis guerra",
    "juan luis guerra 4.40",
    "aventura",
    "romeo santos",
    "prince royce",
}

AYER15 = [
    "v0ckuv1xBm0",  # JLG Burbujas LOCKED
    "iK3BlAZAtPs",  # Chayanne Completamente Enamorados — the room
    "T_oE3qkbo5s",  # Luismi No Sé Tú — two-person, named in lock
    "2LiZyAIVmbs",  # JLG Bachata Rosa
    "NdKhS4MMCEo",  # Luismi Somos Novios — Los novios
    "8sCWmb8f-BY",  # Monchy Te Quiero Igual Que Ayer
    "9oLBY9QqTAQ",  # Fonseca Te Mando Flores
    "j3ObHjm1fAE",  # Chayanne Tiempo de Vals
    "QTYJkS6bTOQ",  # Montaner Tan Enamorados
    "uBwk106e3es",  # Aventura Un Beso forgotten — in 15, not the throne
    "XFRfrPkfghY",  # Aventura La Boda
    "-hoZpSoKAYE",  # Sin Bandera Entra En Mi Vida
    "hNDtsPMX7p0",  # Franco Te Amo
    "nYWcy7z0QmU",  # Enrique Enamorado Por Primera Vez
    "-zgDXIi1uYw",  # Bacilos Caraluna — waterfront couple
]

HOY15 = [
    "QFs3PIZb3js",  # Romeo Propuesta LOCKED
    "DriCCFRQlj8",  # Camilo/Evaluna Índigo — the 2020s couple
    "Mtau4v6foHA",  # Vives/Yatra Robarte un Beso
    "bdOXnTbyk0g",  # Royce Darte un Beso forgotten
    "idC5sWB9sC0",  # Río Roma/Fonseca Caminar de Tu Mano — X register
    "8iPcqtHoR3U",  # Romeo Eres Mía
    "jucBuAzuZ0E",  # Sanz/Marc Deja Que Te Bese
    "hpzT6Wq6pKY",  # Royce Incondicional
    "BFaRWXEpFrs",  # Marc Tu Vida en la Mía
    "YwodhCjFbQ8",  # Camilo/Evaluna Por Primera Vez
    "ghAvJMxE1qo",  # Yatra/Reik Un Año
    "W4AiOKlOO0Q",  # Sanz/Cabello Mi Persona Favorita
    "zHhza3EgHe8",  # JLG/Romeo Frío Frío
    "sD9_l3oDOag",  # Yatra No Hay Nadie Más
    "Z81hsLIY1sQ",  # Fernández/Xtina Hoy Tengo Ganas de Ti
]

AYER_PREF = [
    "giAE7Yz7gHI",  # Por Debajo de la Mesa — dinner couple, 3rd Luismi so not 15
    "iajZ1R5dIXU",  # Por Amarte Así
    "p7QYo-9SlP0",  # Vuelve
    "KYZlT2iYRh8",  # Un Siglo Sin Ti
    "LvgEpio1-kA",  # Como Abeja al Panal
    "0m5SXO8qK78",  # Dos Locos
    "2MjvxB1_lmo",  # Kilómetros
    "29NM6ySmwfQ",  # Azul
    "QGQTLN_RCmI",  # Castillo Azul
    "YkVbgpXXR0M",  # Yo Te Amo
    "sxbKoqz9bNM",  # Estrellitas y Duendes
    "jamgjQ-CTI8",  # Bésame
    "dY8MG-Qf7tk",  # Entrégate
    "jRxebPzoiMo",  # Frío Frío original
    "wTZ7A-h8yTs",  # Shakira Tú
    "kAKVT1HWNsg",  # A Puro Dolor
    "7IPVe1oywh0",  # Te Extraño, Te Olvido, Te Amo
    "6hRlvcy3V9k",  # Tú De Qué Vas
    "NPo0gfThXeA",  # Bailar Pegados
    "kVtfXd_WdkA",  # Rechazame 2010
    "z2pt4CN4rhc",  # Mi Corazoncito
    "Ubxb1u3izeM",  # Atado a Tu Amor
    "xA0DBcsfjTE",  # Hoja en Blanco
    "OThKTAVrUMQ",  # Tengo Todo Excepto a Ti
    "ByU6ABQ1cp8",  # Perdidos
    "3DV57Y4tEAM",  # Experiencia Religiosa
    "jrkNik4AHTU",  # La Cima del Cielo
    "WllxyZpvVEs",  # Angelito
    "lLiPh6kmFoU",  # Contigo en la Distancia
    "GsI6V_DToHg",  # Y Tú Te Vas
    "_4NBD3SqBwg",  # Bachata en Fukuoka
    "XNGWDH-6yv8",  # Corazón Sin Cara
    "foyH-TEs9D0",  # Stand by Me
    "gO8-9OWzPOQ",  # Todo Cambió
    "DaDuJhparw8",  # Inolvidable Reik
    "z0T-7j_pt6w",  # Sin Miedo a Nada
    "0t5iCwpuD8I",  # Otro Día Más Sin Verte
    "u3wrqH2dXL0",  # Me Dediqué a Perderte
    "aW13iWEktsA",  # Corazón Partío
    "Fk5oL0mgI08",  # Que Lloro
    "tg7QRlINFgQ",  # Mientes Tan Bien
    "X3rdR2vlii4",  # Suelta Mi Mano
    "bqvBxdO0B1s",  # Quisiera
    "3fJkFcw7CZ4",  # O Tú o Ninguna
    "wEF19rvbH3I",  # El Reloj
    "kCv8ipMi-BE",  # Hasta Que Me Olvides
    "uMrN1W4ryoE",  # Dejaría Todo
    "elGZbcpGzdU",  # El Perdedor
    "XuCd3Qj6C08",  # Un Buen Perdedor
    "L_xc4YBmtOQ",  # Aunque No Te Pueda Ver
    "GfFnQ2l2FxM",  # Polos Opuestos
    "dNR1ntnF2wg",  # Pasión
    "B-4LuFAOMKQ",  # No Es Una Novela
    "ohumtiwSo9E",  # Hasta El Fin
    "FLYbAHFW5SY",  # Corazón Prendido
    "fY36BMNDqbg",  # Su Veneno
    "GHLVjriwzFg",  # Por Un Segundo
    "kADoBrj4934",  # Todavía Me Amas
    "v6aicYYG59I",  # Te Invito
    "uPCZm2Tvjpo",  # Enséñame a Olvidar
    "TviYVNPCs2c",  # Cuando Volverás
    "ZM2KoVO0NSs",  # Si Tú Te Vas JLG
    "QcRscK_S0Ic",  # Razones — DROPPED
]

HOY_PREF = [
    "_kxz7WX4mLU",  # Por Fin Te Encontré
    "Geqmpq0tjNU",  # Cuando Nos Volvamos a Encontrar
    "sPTn0QEhxds",  # Me Enamoré
    "KIBeny5wq6M",  # Canción Bonita
    "Rir_fuLX7HM",  # Te Esperaba
    "ROzZSmaxDz8",  # Las Cosas Pequeñas
    "uXUjhE9MhyU",  # Prometo
    "5AkDqm-cEgg",  # Tutu
    "9jirj0OjI-M",  # Por Eso Te Amo
    "2mY7AFTtYwQ",  # Favorito
    "ZTmShDv7_og",  # Contigo
    "_X3PPuF_yOE",  # Me Cambiaste la Vida
    "JMq0HJXIp8o",  # Corazón Enamorado
    "Nkloca2M6hU",  # Tú
    "WENJIxEfyaw",  # La Noviecita
    "weKJWqw8-3g",  # Llegaste Tú — Galería 15 guest, not our door
    "TYrcdhots80",  # A Dónde Vamos
    "VebVifKv3UM",  # Juramento eterno de sal
    "krP539YBF7U",  # Millones
    "iuTtlb2COtc",  # Machu Picchu
    "qKp1f7Vn9dM",  # Vida de Rico
    "Lc5fvUzUpnM",  # Todavía No Te Olvido
    "36kmCZheR1I",  # Hoy Es un Buen Día
    "gSJd_J3W6NU",  # Si Tú Me Quieres
    "07314LhFag4",  # Todo Tiene Su Hora
    "K8q5boZdKuU",  # Diez Mil Maneras
    "Gm3WkRDZ8o4",  # Entre Mi Vida y la Tuya
    "0diOZSlLKdg",  # Cómo Pagarte
    "snFhcHHdzT0",  # Creo en Ti
    "z1EB-fI0JDI",  # Un Besito Más
    "W4AiOKlOO0Q",  # already 15
    "jk4HYngf65w",  # Cancioncitas
    "C8FQ4wQXyaE",  # Humanos a Marte — Limpieza 15 guest
    "I9cCPQVPv8o",  # Fuiste Tú — Galería #2 guest
    "ncByymoHQRI",  # Tus Besos — Galería #1 guest
    "XlmaJ-yU46U",  # Inmortal
    "OdaIbTUGmHM",  # La Carretera
    "XEvKn-QgAY0",  # Deja Vu
    "OST41MmjdTQ",  # El Amor Que Perdimos
    "qjkb9_AJCLo",  # Carita de Inocente
    "4eCL0l9iD5A",  # Hilito
    "VafbNsrHnD8",  # Llévame Contigo
    "2p_eRTj5s5M",  # Amigo
    "69ppp5Ipook",  # Solo Conmigo
    "rvmtQvA_cmM",  # Sus Huellas
    "-lDsqOsJL7k",  # Culpa al Corazón
    "yUAZxs3qY3Y",  # Te Robaré
    "mhHqonzsuoA",  # Imitadora
    "QBaIMZ8QjcU",  # Yo También
    "DXiXPhvYuNU",  # Necio
    "J9QmUNZOh7I",  # Casablanca
    "Vl7RmqGztbk",  # Bachata en Nueva York
    "tNw9Rc3GbcE",  # Desnudos
    "p2YCzaZNRqQ",  # No Me Sueltes
    "0nBzuG_jWbU",  # Lento
    "CDv6lGEaWTo",  # Por Nada
    "R5V-A-iu9dg",  # Te Di
    "owOJ6L8Fepw",  # Poquito a Poquito
    "g81JtMbrJtw",  # París
    "KsdJEolXHQA",  # Muchachita Linda
    "1d0y8h-9AAs",  # Lacrimosa
]

AYER_DROP = {
    "Aa6MmoSKOdo",  # Hero — English
    "5dNxsyvuYho",  # Cuando Te Beso — 234k, not wow
    "QcRscK_S0Ic",  # Razones — 560k
    "uZtXRgB95T4",  # Amanda Miguel — dryer
    "8hRGBcr_gJc",  # No Me Doy Por Vencido — pop-radio, not couple walk
}

HOY_DROP = {
    "TOgCeRQvzoY",  # Confieso — dryer
    "I_cJxvTQ6RM",  # 100 Años — dryer
}

NEW = {
    "-zgDXIi1uYw": ("Bacilos", "Caraluna", 2002, "Warner Música", 395300000),
    "7IPVe1oywh0": ("Ricky Martin", "Te Extraño, Te Olvido, Te Amo", 1995, "RickyMartinVEVO", 75800000),
    "6hRlvcy3V9k": ("Franco De Vita", "Tú De Qué Vas", 2004, "FrancodeVitaVEVO", 375400000),
    "kVtfXd_WdkA": ("Prince Royce", "Rechazame", 2010, "PrinceRoyceVEVO", 141000000),
    "NPo0gfThXeA": ("Sergio Dalma", "Bailar Pegados", 1991, "SergioDalmaVEVO", 4600000),
    "TYrcdhots80": ("Morat", "A Dónde Vamos", 2019, "MoratVEVO", 122300000),
    "VebVifKv3UM": ("Álvaro de Luna", "Juramento Eterno de Sal", 2020, "Álvaro De Luna", 35300000),
}

CHANNEL_FIX = {
    "9oLBY9QqTAQ": "FonsecaVEVO",
}


def lead(artist: str) -> str:
    name = (artist or "").split(",")[0].strip().lower()
    if name.startswith("juan luis guerra"):
        return "juan luis guerra"
    return name


def load_pool(path: Path) -> dict:
    data = json.loads(path.read_text())
    pool = {}
    for t in data["tracks"]:
        pool[t["id"]] = {
            "id": t["id"],
            "artist": t["artist"],
            "title": t["title"],
            "year": int(t["year"]),
            "channel": t.get("channel") or "",
            "views": int(t.get("views") or 0),
        }
    return pool


def make_track(tid: str, pool: dict, intro: bool) -> dict:
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
        src = pool[tid]
    return {
        "id": tid,
        "artist": src["artist"],
        "title": src["title"],
        "year": int(src["year"]),
        "channel": CHANNEL_FIX.get(tid, src.get("channel") or ""),
        "views": int(src.get("views") or 0),
        "official": True,
        "artworkOk": True,
        "intro": intro,
    }


def interleave(tracks: list[dict]) -> list[dict]:
    remaining = tracks[:]
    out: list[dict] = []
    while remaining:
        last = lead(out[-1]["artist"]) if out else None
        pick = None
        for i, t in enumerate(remaining):
            if last is None or lead(t["artist"]) != last:
                pick = i
                break
        if pick is None:
            # swap last with an earlier different-lead slot if possible
            stuck = remaining[0]
            swapped = False
            for j in range(len(out) - 2, -1, -1):
                if (
                    lead(out[j]["artist"]) != last
                    and (j == 0 or lead(out[j - 1]["artist"]) != last)
                    and lead(out[j + 1]["artist"]) != lead(stuck["artist"])
                    and (j == 0 or lead(out[j - 1]["artist"]) != lead(stuck["artist"]))
                ):
                    out[j], remaining[0] = remaining[0], out[j]
                    swapped = True
                    break
            if not swapped:
                raise RuntimeError(f"consecutive lock: {out[-1]['artist']} / {stuck['artist']}")
            continue
        out.append(remaining.pop(pick))
    return out


def build(era: str, door: list[str], pref: list[str], drop: set[str]) -> dict:
    pool = load_pool(CUR / f"malecon-{era}.json")
    for tid, meta in NEW.items():
        year = meta[2]
        if era == "ayer" and 1980 <= year <= 2010:
            pool.setdefault(tid, {})
        if era == "hoy" and year >= 2011:
            pool.setdefault(tid, {})
    used = set(door)
    rest_ids: list[str] = []
    for tid in pref:
        if tid in used or tid in drop:
            continue
        if tid in pool or tid in NEW:
            rest_ids.append(tid)
            used.add(tid)
    for tid in list(pool):
        if tid in used or tid in drop:
            continue
        year = int(pool[tid]["year"])
        if era == "ayer" and not (1980 <= year <= 2010):
            continue
        if era == "hoy" and year < 2011:
            continue
        rest_ids.append(tid)
        used.add(tid)
    # new ids not already consumed
    for tid, meta in NEW.items():
        year = meta[2]
        if tid in used or tid in drop:
            continue
        if era == "ayer" and 1980 <= year <= 2010:
            rest_ids.append(tid)
            used.add(tid)
        if era == "hoy" and year >= 2011:
            rest_ids.append(tid)
            used.add(tid)
    rest = [make_track(tid, pool, False) for tid in rest_ids]
    rest = interleave(rest)
    tracks = [make_track(tid, pool, True) for tid in door] + rest
    if len(tracks) < 100:
        raise RuntimeError(f"{era} short {len(tracks)}")
    tracks = tracks[:100]
    # final consecutive pass on the 100
    for i in range(1, 100):
        if lead(tracks[i]["artist"]) == lead(tracks[i - 1]["artist"]):
            swapped = False
            for j in range(i + 1, 100):
                if (
                    lead(tracks[j]["artist"]) != lead(tracks[i - 1]["artist"])
                    and (j == 99 or lead(tracks[j]["artist"]) != lead(tracks[j + 1]["artist"]))
                    and lead(tracks[i]["artist"]) != lead(tracks[j - 1]["artist"])
                    and (j == 99 or lead(tracks[i]["artist"]) != lead(tracks[j + 1]["artist"]))
                ):
                    tracks[i], tracks[j] = tracks[j], tracks[i]
                    swapped = True
                    break
            if not swapped:
                raise RuntimeError(f"{era} consec at {i}: {tracks[i-1]['artist']} / {tracks[i]['artist']}")
    assert all(t["intro"] for t in tracks[:15])
    assert not any(t["intro"] for t in tracks[15:])
    return {
        "room": "malecon",
        "era": era,
        "count": 100,
        "introCount": 15,
        "tracks": tracks,
    }


def validate(data: dict) -> None:
    tracks = data["tracks"]
    era = data["era"]
    assert len(tracks) == 100
    ids = [t["id"] for t in tracks]
    assert len(set(ids)) == 100
    assert all(len(i) == 11 for i in ids)
    years = [t["year"] for t in tracks]
    if era == "ayer":
        assert min(years) >= 1980 and max(years) <= 2010, (min(years), max(years))
        assert ids[0] == "v0ckuv1xBm0"
        assert 2 <= ids.index("uBwk106e3es") + 1 <= 15
    else:
        assert min(years) >= 2011, min(years)
        assert ids[0] == "QFs3PIZb3js"
        assert 2 <= ids.index("bdOXnTbyk0g") + 1 <= 15
    consec = [
        (i + 1, tracks[i - 1]["artist"], tracks[i]["artist"])
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
    steals = {"dDEVFQnBTp0", "ncByymoHQRI", "SEjw5rdyvVg", "_koz_f4mthE", "RgKqxLAhRKE", "E6soE-1p3kw", "hal7rXfJj5o", "ExCIp6TOnJw"}
    assert not [i for i in ids[:15] if i in steals]
    print(f"{era}: 100 ok | years {min(years)}-{max(years)} | leads {c.most_common(6)}")
    print(f"  first15: {[(t['artist'].split(',')[0], t['title']) for t in tracks[:15]]}")
    print(f"  first15 leads {dict(c15)}")


def main() -> None:
    ayer = build("ayer", AYER15, AYER_PREF, AYER_DROP)
    hoy = build("hoy", HOY15, HOY_PREF, HOY_DROP)
    validate(ayer)
    validate(hoy)
    (CUR / "malecon-ayer.json").write_text(json.dumps(ayer, ensure_ascii=False, indent=2) + "\n")
    (CUR / "malecon-hoy.json").write_text(json.dumps(hoy, ensure_ascii=False, indent=2) + "\n")
    print("WROTE malecon-ayer.json + malecon-hoy.json")


if __name__ == "__main__":
    main()
