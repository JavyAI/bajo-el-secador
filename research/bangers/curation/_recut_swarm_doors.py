#!/usr/bin/env python3
"""Apply 2026-08-17 swarm recuts. Reorder first 15 from existing 100s only."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path("/Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador")
CUR = ROOT / "research/bangers/curation"
PUB = ROOT / "public"

DOORS: dict[tuple[str, str], list[str]] = {
    ("colmado", "ayer"): [
        "_koz_f4mthE",  # JLG — A Pedir Su Mano
        "WPiEbYSF9kE",  # Elvis — Suavemente (forgotten #1, one patio guest)
        "frsVQWSINAI",  # Gran Combo — Me Liberé
        "1DbXzlhKS5s",  # Wilfrido — El Africano
        "oWBf9hfW_4Y",  # Arroyo — Rebelión
        "McV4pBRb-Sg",  # JLG — La Bilirrubina
        "y08MAPIACBY",  # Cuco — Juliana
        "uzU3x_egiEk",  # Eddy — Tú Eres Ajena
        "imeXSRNRMeg",  # Celia — La Negra Tiene Tumbao
        "PmXJKVjhbqI",  # Frankie — La Cura
        "UwnmzIgNzyU",  # Niche — Una Aventura
        "_u2m43WXQks",  # Los Cantantes — El Venao
        "BNo0vkEYWRc",  # Lavoe — El Cantante (one Fania prayer, late)
        "SUgQHe902yQ",  # Jerry — Qué Hay de Malo
        "7wpVJvRIKYQ",  # Víctor Manuelle — He Tratado
    ],
    ("colmado", "hoy"): [
        "ExCIp6TOnJw",  # Yiyo — Manos de Tijera
        "u6Q5Lu0Sq3g",  # Chiquito — La Llamada De Mi Ex
        "eHsR140M2no",  # Yiyo — Qué Agonía
        "A0f-FDFpPZE",  # Chiquito — Tengo Que Colgar
        "JXLNr85yoKk",  # Yiyo — Mi Todo
        "8820jXsE4kQ",  # Chiquito — Lejos De Ti
        "K3S96fUGrEY",  # JLG — Mambo 23 (merengue de calle now)
        "QBaIMZ8QjcU",  # Romeo / Marc — Yo También (late)
        "AsCnKFzhFSA",  # Marc — Parecen Viernes
        "WENJIxEfyaw",  # JLG — La Noviecita
        "YH6DvXUuYJk",  # Yiyo — Corazón de Acero (forgotten viral)
        "1EarnVR8_Og",  # Marc — Pa'lla Voy
        "8HCXYy36RM8",  # Manny / Wilfrido — El Hombre Divertido
        "h6sbZalmiu4",  # Elvis — Abracadabra
        "zyDjrb5GWr8",  # Manny — Santo Domingo
    ],
    ("secador", "ayer"): [
        "RgKqxLAhRKE",
        "wOjzo02Tmck",
        "kkF5eGMxwEQ",
        "OkOJGgqcwro",
        "FwZTgDjRLM0",
        "b1cbgrcBrY0",
        "ApAhB3DRkFE",
        "Fi6_kgz5vwU",
        "0O4CLgXvbjU",
        "uMrN1W4ryoE",
        "ga5Bo4YdgH4",  # Hasta Que Te Conocí (kills Mientes)
        "QFVkLGqVhbo",
        "FCi-Xp2TVoQ",
        "ASnkzgvBf0o",
        "tOVHj4zuRTU",
    ],
    ("secador", "hoy"): [
        "Uws510cVia4",  # Ha*Ash — Lo Aprendí de Ti
        "XEvKn-QgAY0",  # Royce / Shakira — Deja Vu
        "P2hM9CLAMu4",  # J&J — Corre
        "jk4HYngf65w",  # Romeo — Cancioncitas de Amor
        "_wL3Pc-EmjA",  # Ha*Ash — Perdón, Perdón
        "5R1RGl4WQP8",  # Mon Laferte — Tu Falta de Querer
        "7TWzV05kQ4w",  # Reik — Ya Me Enteré
        "4eCL0l9iD5A",  # Romeo — Hilito (yields Propuesta)
        "TMT9MNM-NHg",  # J&J — Dueles
        "7mox58jIAdA",  # Ha*Ash — Te Dejo En Libertad
        "snFhcHHdzT0",  # Reik — Creo En Ti
        "N6mShTc40BU",  # Rivera — El Hubiera No Existe
        "_WHGlEYaBgU",  # J&J — Ecos de Amor
        "tLcfAnN2QgY",  # Enrique / Marco — El Perdedor
        "Rir_fuLX7HM",  # Rivera — Te Esperaba
    ],
    ("silla", "ayer"): [
        "SEjw5rdyvVg",
        "0mFaIxl1wgQ",
        "uBwk106e3es",
        "oVLS7QGWlGw",
        "xA0DBcsfjTE",
        "L6YuWb-_R9Q",
        "b2Ig9IPBtRs",
        "9Vt0NBO37yI",
        "3hXdIcJ8ZDw",
        "5HirJ6k5yzA",
        "6KibGmX6vYY",
        "0m5SXO8qK78",
        "QnGNEn5KYc4",
        "rmerQRm3GJk",
        "ePtOXORN96A",
    ],
    ("silla", "hoy"): [
        "QFs3PIZb3js",  # Propuesta
        "bdOXnTbyk0g",  # Darte
        "XlmaJ-yU46U",  # Inmortal
        "MB23TtaeiQY",  # La Asesina
        "8iPcqtHoR3U",  # Eres Mía
        "iuugCBK3RRI",  # Creíste (Mayimbe before more Royce)
        "yUAZxs3qY3Y",  # Te Robaré
        "Y2KVvROYQrc",  # El Intruso
        "mhHqonzsuoA",  # Imitadora
        "AL_Ogy2TTXs",  # Dile A Él
        "cOy4siyFp0U",  # La Demanda (Utopía; kills 2010 Royce)
        "qurynQHSPhw",  # Mejor Que a Ti Me Va
        "1p0QyZIf93I",  # Debate de 4
        "Bbu6K6DWQAA",  # Corazón Con Candado
        "RfTcYeNdZHY",  # Amorcito Enfermito
    ],
    ("limpieza", "ayer"): [
        "E6soE-1p3kw",
        "yWSQxGppcFA",
        "GRo0nnF5OXY",
        "S5tcXtlhmF8",
        "1pr7Fv-9Z3I",
        "f7-vEi-uPB8",
        "CwfCO_CRKqw",
        "1crMUfqH6i0",
        "48SWXqe1K-8",
        "3LCEzvkwWwI",  # Kulikitaka contained late
        "qfgWkLAmKCM",
        "lvfQWpvcE30",
        "wit3kfPhXqE",
        "zZTo7FYn0lI",
        "ipDNOrqLIHU",
    ],
    ("limpieza", "hoy"): [
        "hal7rXfJj5o",
        "vqEdCsOgy9E",
        "dyM5fHdbowM",
        "B2SLbC8fnfs",
        "SRDkwORUPak",  # Vuelve Mami (kills Madre Tierra)
        "ym2clIz5t4A",
        "bWTfpdD4nRM",
        "qhOPeeZHSWE",
        "0K6ItvTTpe8",
        "sHRzCQEHpU8",
        "P_xKX0NBTeQ",
        "dUOC-ryYtQI",
        "yfptK2ozc2w",
        "SagA6H4LWjI",
        "-_fCguTGj88",
    ],
    ("galeria", "ayer"): [
        "dDEVFQnBTp0",
        "95Wcl9ucitM",
        "E0f3J0z2SBQ",
        "oADpF--uirA",
        "xhpJqdZgF5U",
        "-apU2sviHCM",
        "xaKLn_z9R_k",
        "kr2B1RoWrlE",
        "1ddK89KqVe8",
        "apFqJ49VstY",
        "td2K3taR3bc",
        "mIszekfGw3Q",
        "VyraXS0iMHw",
        "g-GBiuujmL8",
        "l6LjNOYvhMk",
    ],
    ("galeria", "hoy"): [
        "ncByymoHQRI",
        "I9cCPQVPv8o",
        "ea4ovC_B6ow",  # Carmesí up
        "07314LhFag4",
        "vVbYpOdAOgU",  # Mi Balcón up
        "ZpWRU0H5dmA",
        "zLX_GcXt2pI",
        "ahtMpUhoj9s",
        "C8JJxmVQ9KI",  # Te Guardo
        "IKmPci5VXz0",
        "S8RmXvxlIzc",
        "MvITnIylaQ8",
        "1KZ9osr-a8I",  # Sabor a Mí
        "410cZw2YI0g",  # Nunca Es Suficiente
        "7Mk-8TR7vg0",  # En Otra Vida
    ],
    ("malecon", "ayer"): [
        "v0ckuv1xBm0",
        "iK3BlAZAtPs",
        "T_oE3qkbo5s",
        "2LiZyAIVmbs",
        "NdKhS4MMCEo",
        "8sCWmb8f-BY",
        "9oLBY9QqTAQ",
        "j3ObHjm1fAE",
        "QTYJkS6bTOQ",
        "XFRfrPkfghY",  # La Boda (yields Un Beso)
        "QGQTLN_RCmI",
        "NPo0gfThXeA",
        "ohumtiwSo9E",
        "00QVU7voMq8",
        "v6aicYYG59I",
    ],
    ("malecon", "hoy"): [
        "DriCCFRQlj8",  # Índigo — authored #1 stays
        "idC5sWB9sC0",  # Caminar de Tu Mano
        "hpzT6Wq6pKY",  # Incondicional
        "zHhza3EgHe8",  # Frío, Frío
        "Mtau4v6foHA",  # Robarte un Beso
        "ghAvJMxE1qo",  # Un Año
        "JMq0HJXIp8o",  # Corazón Enamorado
        "YwodhCjFbQ8",  # Por Primera Vez
        "uXUjhE9MhyU",  # Prometo
        "ZTmShDv7_og",  # Contigo
        "J9QmUNZOh7I",  # Casablanca
        "gSJd_J3W6NU",  # Si Tú Me Quieres
        "p2YCzaZNRqQ",  # No Me Sueltes
        "W4AiOKlOO0Q",  # Mi Persona Favorita
        "ROzZSmaxDz8",  # Las Cosas Pequeñas (forgotten couple-bachata)
    ],
}


def lead(artist: str) -> str:
    a = (artist or "").split(",")[0]
    for sep in (" feat", " ft", " Feat", " Ft"):
        a = a.split(sep)[0]
    return a.strip().lower()


def reorder(tracks: list[dict], door: list[str]) -> list[dict]:
    by_id = {t["id"]: t for t in tracks}
    missing = [i for i in door if i not in by_id]
    if missing:
        raise SystemExit(f"missing ids: {missing}")
    used = set(door)
    rest = [t for t in tracks if t["id"] not in used]
    out = [by_id[i] for i in door] + rest
    if len(out) != 100 or len({t["id"] for t in out}) != 100:
        raise SystemExit(f"count/unique fail {len(out)} {len({t['id'] for t in out})}")
    for i, t in enumerate(out):
        t["intro"] = i < 15
    return out


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    for (room, era), door in DOORS.items():
        if len(door) != 15 or len(set(door)) != 15:
            raise SystemExit(f"bad door {room} {era}")
        cur_path = CUR / f"{room}-{era}.json"
        pub_path = PUB / era / f"{room}.json"
        cur = json.loads(cur_path.read_text())
        pub = json.loads(pub_path.read_text())
        cur["tracks"] = reorder(cur["tracks"], door)
        pub["tracks"] = reorder(pub["tracks"], door)
        write_json(cur_path, cur)
        write_json(pub_path, pub)

    # verify
    rooms = ["colmado", "secador", "silla", "limpieza", "galeria", "malecon"]
    labels = {
        "colmado": "Colmado",
        "secador": "Secador",
        "silla": "Barbería",
        "limpieza": "Limpieza",
        "galeria": "Galería",
        "malecon": "Malecón",
    }
    all15: dict[tuple[str, str], list[tuple[str, str, str]]] = {}
    print("LIVE FIRST 15 AFTER RECUT")
    for era in ("ayer", "hoy"):
        print(f"\n######## {era.upper()} ########")
        for room in rooms:
            pub = json.loads((PUB / era / f"{room}.json").read_text())
            t = pub["tracks"]
            cons = []
            prev = None
            for i, x in enumerate(t):
                ld = lead(x.get("artist", ""))
                if prev and ld and ld == prev:
                    cons.append(i + 1)
                prev = ld
            print(f"\n--- {labels[room]} {era} n={len(t)} unique={len({x['id'] for x in t})} consec={cons or 'ok'} ---")
            first = []
            for i, x in enumerate(t[:15], 1):
                print(f"  {i:2d}. {x['artist']} — {x['title']}  [{x['id']}]")
                first.append((x["id"], x["artist"], x["title"]))
            all15[(era, room)] = first

    print("\nIDENTICAL SEQUENCES")
    seqs: dict[tuple[str, ...], list] = {}
    for k, v in all15.items():
        seqs.setdefault(tuple(x[0] for x in v), []).append(k)
    ident = {s: rs for s, rs in seqs.items() if len(rs) > 1}
    print("  none" if not ident else ident)

    print("\nFIRST-15 ID OVERLAPS (same era)")
    for era in ("ayer", "hoy"):
        print(f"-- {era} --")
        sets = {room: {x[0] for x in all15[(era, room)]} for room in rooms}
        found = False
        for i, a in enumerate(rooms):
            for b in rooms[i + 1 :]:
                inter = sets[a] & sets[b]
                if inter:
                    found = True
                    print(f"  {labels[a]} ∩ {labels[b]}: {inter}")
        if not found:
            print("  none")

    print("\nFIRST-5 UNIQUENESS (all 12)")
    f5: dict[str, list[str]] = {}
    for (era, room), lst in all15.items():
        for i, x in enumerate(lst[:5], 1):
            f5.setdefault(x[0], []).append(f"{labels[room]} {era}#{i}")
    dups = {k: v for k, v in f5.items() if len(v) > 1}
    print("  all unique" if not dups else dups)

    thrones = {
        "QFs3PIZb3js": "Propuesta",
        "bdOXnTbyk0g": "Darte",
        "8iPcqtHoR3U": "Eres Mía",
        "uBwk106e3es": "Un Beso",
    }
    print("\nBARBERÍA THRONES IN OTHER FIRST-15s")
    for vid, name in thrones.items():
        homes = []
        for (era, room), lst in all15.items():
            for i, x in enumerate(lst, 1):
                if x[0] == vid:
                    homes.append(f"{labels[room]} {era}#{i}")
        print(f"  {name}: {homes}")


if __name__ == "__main__":
    main()
