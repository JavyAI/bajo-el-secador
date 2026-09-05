#!/usr/bin/env python3
"""Pad En casa de abuela to 100 unique official tracks per era.

Keeps authored first 15. Drops later title-dups. Fills from YouTube search.
"""
from __future__ import annotations

import json
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PUBLIC = ROOT / "public"

import importlib.util

spec = importlib.util.spec_from_file_location(
    "resolve_official_clips", ROOT / "scripts" / "resolve-official-clips.py"
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
BAD = mod.BAD
fold = mod.fold
lead_artist = mod.lead_artist
oembed = mod.oembed
pick = mod.pick
search = mod.search
title_hits = mod.title_hits
walk_hits = mod.walk_hits


DAY_CANDIDATES = [
    ("Cortijo y su Combo", "Caballero Qué Bomba"),
    ("Cortijo y su Combo", "Oriza"),
    ("Cortijo y su Combo", "El Conde de Loíza"),
    ("Cortijo y su Combo", "Temporal"),
    ("Cortijo y su Combo", "El Yoyo"),
    ("Cortijo y su Combo", "Fuego a la Lata"),
    ("Cortijo y su Combo", "El Platanal de Bartolo"),
    ("Cortijo y su Combo", "Juan José"),
    ("Cortijo y su Combo", "Lo Dejé Llorando"),
    ("Cortijo y su Combo", "Calypso Bomba y Plena"),
    ("Cortijo y su Combo", "Cucala"),
    ("Cortijo y su Combo", "Déjalo Que Suba"),
    ("Cortijo y su Combo", "El Chivo"),
    ("Mon Rivera", "Karakatis-Ki"),
    ("Mon Rivera", "El Gato"),
    ("Mon Rivera", "Peteco"),
    ("Mon Rivera", "Aló Quién Ñaña"),
    ("Mon Rivera", "Ron con Coco"),
    ("Mon Rivera", "Ola de Agua"),
    ("Canario y su Grupo", "Cortaron a Elena"),
    ("Canario y su Grupo", "Santa María"),
    ("Ramito", "La Tierra Mía"),
    ("Ramito", "Te Están Vacilando"),
    ("Ramito", "Buena en Cantidad"),
    ("Ramito", "El Gallo"),
    ("Odilio González", "Sacude Zapato Viejo"),
    ("Odilio González", "Ni de Madera Son Buenas"),
    ("Odilio González", "El Libro de Mi Vida"),
    ("Odilio González", "Las Penas Mías"),
    ("Chuíto el de Bayamón", "El Alma de Puerto Rico"),
    ("La Calandria", "Somos Boricuas"),
    ("Maso Rivera", "El Cuatro"),
    ("Germán Rosario", "Seis Chorreao"),
    ("Andrés Jiménez", "El Jíbaro"),
    ("El Gran Combo", "Ojos Chinos"),
    ("El Gran Combo", "Jala Jala"),
    ("El Gran Combo", "Azuquita Pa'l Café"),
    ("Rafael Hernández", "El Cumbanchero"),
    ("Rafael Hernández", "Cachita"),
    ("Ismael Rivera", "El Nazareno"),
    ("Ismael Rivera", "Las Tumbas"),
    ("Ismael Rivera", "Dime Por Qué"),
    ("Ismael Rivera", "Mi Negrita Me Espera"),
    ("Ismael Rivera", "La Bomba"),
    ("Ismael Rivera", "El Negro"),
    ("Tatico Henríquez", "La Pava"),
    ("Tatico Henríquez", "La Chiflera"),
    ("Tatico Henríquez", "El Pañuelo"),
    ("Tatico Henríquez", "La Porfía"),
    ("Tatico Henríquez", "Desde Que La Vi"),
    ("Tatico Henríquez", "La Mujer Ajena"),
    ("Trío Reynoso", "Juanita Morel"),
    ("Trío Reynoso", "Ay Ombe"),
    ("Trío Reynoso", "La Empaliza"),
    ("Trío Reynoso", "Caña Brava"),
    ("Trío Reynoso", "El Gallo"),
    ("Trío Reynoso", "Juangomero"),
    ("Guandulito", "Bolsillo Pelao"),
    ("Guandulito", "La Soga"),
    ("Guandulito", "El Cuento de la Guinea"),
    ("Guandulito", "La Cariñosa"),
    ("Fefita La Grande", "La Chiflera"),
    ("El Ciego de Nagua", "El Sancocho Prieto"),
    ("El Ciego de Nagua", "La Chiflera"),
    ("Joseíto Mateo", "La Chiva Blanca"),
    ("Joseíto Mateo", "Un Cibaeño en Nueva York"),
    ("Joseíto Mateo", "Los Mangos"),
    ("Luis Kalaff", "El Reloj"),
    ("Ángel Viloria y su Conjunto Típico Cibaeño", "La Empalizá"),
    ("Ángel Viloria y su Conjunto Típico Cibaeño", "Juangomero"),
    ("Johnny Ventura", "El Bochinchero"),
    ("Johnny Ventura", "Patacón Pisao"),
    ("Johnny Ventura", "El Llorón"),
    ("Johnny Ventura", "La Muerte de Martín"),
    ("Cuco Valoy", "Juliana"),
    ("Miguel Aceves Mejía", "Cucurrucucú Paloma"),
    ("Miguel Aceves Mejía", "Cielito Lindo"),
    ("Miguel Aceves Mejía", "La Malagueña"),
    ("Jorge Negrete", "Ay Jalisco No Te Rajes"),
    ("Jorge Negrete", "México Lindo y Querido"),
    ("Pedro Infante", "Allá en el Rancho Grande"),
    ("Pedro Infante", "Amorcito Corazón"),
    ("Antonio Aguilar", "Caballo Prieto Azabache"),
    ("Antonio Aguilar", "Un Puño de Tierra"),
    ("Mariachi Vargas", "El Son de la Negra"),
    ("Mariachi Vargas", "Guadalajara"),
    ("Los Hermanos Rigual", "Cuando Calienta el Sol"),
    ("Celia Cruz", "Químbara"),
    ("Celia Cruz", "Guantanamera"),
    ("Celia Cruz", "La Vida Es Un Carnaval"),
    ("Benny Moré", "Francisco Guayabal"),
    ("Pérez Prado", "Cerezo Rosa"),
    ("Pérez Prado", "Mambo No. 5"),
    ("Xavier Cugat", "El Manicero"),
    ("Trio Matamoros", "Son de la Loma"),
    ("Arsenio Rodríguez", "Bruca Manigua"),
    ("Moncho Leña", "Aló Quién Ñama"),
    ("Baltazar Carrero", "En Órbita"),
    ("Luz Celenia Tirado", "Por Retenerte"),
    ("Juaniquillo", "El Zorzal de Orocovis"),
    ("Chuíto el de Cayey", "Seis Mapeyé"),
    ("Plena Libre", "El León"),
    ("Rafael Cepeda", "El Bombón de Elena"),
    ("Celia Cruz", "Cúcala"),
]

NIGHT_CANDIDATES = [
    ("José José", "Lo Dudo"),
    ("José José", "Volcán"),
    ("José José", "Preso"),
    ("José José", "Buenos Días Amor"),
    ("José José", "Amnesia"),
    ("José José", "El Príncipe"),
    ("José José", "Si Me Dejas Ahora"),
    ("José José", "Vamos a Darnos Tiempo"),
    ("José José", "Lo Pasado Pisado"),
    ("José José", "Gotas de Lluvia"),
    ("José José", "Frente a Frente"),
    ("José José", "El Amor Acaba"),
    ("José José", "Y Quién Puede Ser"),
    ("José José", "Como Tú"),
    ("José José", "Insaciable Amante"),
    ("José José", "Payaso"),
    ("José José", "¿Qué Hay de Malo?"),
    ("José José", "Seré"),
    ("José José", "Me Basta"),
    ("José José", "Mi Destino Fui Tú"),
    ("José Luis Rodríguez", "Culpable Soy Yo"),
    ("José Luis Rodríguez", "Agárrense de las Manos"),
    ("José Luis Rodríguez", "Este Amor Es un Sueño de Locos"),
    ("José Luis Rodríguez", "Camino Verde"),
    ("José Luis Rodríguez", "Tengo"),
    ("José Luis Rodríguez", "La Distancia"),
    ("José Luis Rodríguez", "Recuerdos"),
    ("José Luis Rodríguez", "Atrévete"),
    ("Julio Jaramillo", "Fatalidad"),
    ("Julio Jaramillo", "Ódiame"),
    ("Julio Jaramillo", "Reminiscencias"),
    ("Julio Jaramillo", "Cinco Centavitos"),
    ("Julio Jaramillo", "Rondando Tu Esquina"),
    ("Julio Jaramillo", "Devuélveme el Rosario de Mi Madre"),
    ("Julio Jaramillo", "Te Odio y Te Quiero"),
    ("Julio Jaramillo", "Ya No Sufro"),
    ("Los Panchos", "Historia de un Amor"),
    ("Los Panchos", "Reloj"),
    ("Los Panchos", "La Barca"),
    ("Los Panchos", "Perfidia"),
    ("Los Panchos", "Solamente una Vez"),
    ("Los Panchos", "Aquellos Ojos Verdes"),
    ("Los Panchos", "Piel Canela"),
    ("Los Panchos", "Quién Será"),
    ("Los Panchos", "Una Copa Más"),
    ("Eydie Gormé, Los Panchos", "Historia de un Amor"),
    ("Eydie Gormé, Los Panchos", "Reloj"),
    ("Javier Solís", "Payaso"),
    ("Javier Solís", "Entrega Total"),
    ("Javier Solís", "Media Vuelta"),
    ("Javier Solís", "El Loco"),
    ("Javier Solís", "Cenizas"),
    ("Javier Solís", "Llorarás"),
    ("Javier Solís", "Esclavo y Amo"),
    ("Javier Solís", "Amanecí en Tus Brazos"),
    ("Javier Solís", "Sabrás Que Te Quiero"),
    ("Vicente Fernández", "Volver Volver"),
    ("Vicente Fernández", "Por Tu Maldito Amor"),
    ("Vicente Fernández", "Lástima Que Seas Ajena"),
    ("Vicente Fernández", "Acá Entre Nos"),
    ("José Alfredo Jiménez", "Ella"),
    ("José Alfredo Jiménez", "Un Mundo Raro"),
    ("José Alfredo Jiménez", "Paloma Querida"),
    ("José Alfredo Jiménez", "Si Nos Dejan"),
    ("José Alfredo Jiménez", "Camino de Guanajuato"),
    ("Camilo Sesto", "Vivir Así Es Morir de Amor"),
    ("Camilo Sesto", "Melina"),
    ("Camilo Sesto", "Algo de Mí"),
    ("Raphael", "Yo Soy Aquel"),
    ("Raphael", "Cuando Tú No Estás"),
    ("Nino Bravo", "Un Beso y Una Flor"),
    ("Nino Bravo", "Libre"),
    ("Roberto Carlos", "Amigo"),
    ("Roberto Carlos", "Detalles"),
    ("Sandro", "Rosa Rosa"),
    ("Armando Manzanero", "Somos Novios"),
    ("Armando Manzanero", "Adoro"),
    ("Armando Manzanero", "Esta Tarde Vi Llover"),
    ("Armando Manzanero", "Contigo Aprendí"),
    ("Agustín Lara", "Granada"),
    ("Agustín Lara", "Solamente una vez"),
    ("Agustín Lara", "María Bonita"),
    ("Lucho Gatica", "El Reloj"),
    ("Lucho Gatica", "La Barca"),
    ("Daniel Santos", "Fichas Negras"),
    ("Daniel Santos", "Dos Gardenias"),
    ("Daniel Santos", "El Incomprendido"),
    ("Felipe Rodríguez", "La Copa Rota"),
    ("Felipe Rodríguez", "El Incomprendido"),
    ("Tito Rodríguez", "En la Soledad"),
    ("Tito Rodríguez", "Usted"),
    ("Tito Rodríguez", "Cuando, Cuando"),
    ("Beny Moré", "Santa Isabel de las Lajas"),
    ("Beny Moré", "Y Hoy Como Ayer"),
    ("Beny Moré", "Bonito y Sabroso"),
    ("Gilberto Monroig", "Sin Fe"),
    ("Trio Vegabajeño", "En Mi Viejo San Juan"),
    ("Trio Vegabajeño", "Preciosa"),
    ("Trio Vegabajeño", "Lamento Borincano"),
    ("Rafael Hernández", "Perfume de Gardenias"),
    ("Rafael Hernández", "Campanitas de Cristal"),
    ("Rafael Hernández", "Silencio"),
    ("Rafael Hernández", "Capullito de Alelí"),
    ("Pedro Flores", "Amor Perdido"),
    ("Pedro Flores", "Obsesión"),
    ("Toña la Negra", "Enamorada"),
    ("Los Tres Ases", "La Puerta"),
    ("Los Dandys", "Gema"),
    ("Marco Antonio Muñiz", "El Reloj"),
    ("Marco Antonio Muñiz", "La Mentira"),
    ("Luis Miguel", "La Mentira"),
    ("Luis Miguel", "La Barca"),
    ("Luis Miguel", "El Reloj"),
    ("Luis Miguel", "Inolvidable"),
    ("Chavela Vargas", "Paloma Negra"),
    ("Pedro Infante", "La Que Se Fue"),
    ("Pedro Infante", "Cien Años"),
    ("José José", "El Amar y El Querer"),
    ("José José", "Gavilán o Paloma"),
    ("José José", "Almohada"),
    ("José José", "La Nave del Olvido"),
    ("José José", "Lo Que No Fue No Será"),
    ("Bienvenido Granda", "Nuestro Juramento"),
    ("Bienvenido Granda", "En La Orilla Del Mar"),
    ("Leo Marini", "Sin Un Amor"),
    ("Bobby Capó", "Sin Fe"),
    ("Bobby Capó", "El Bardo"),
    ("Cheo Feliciano", "Mi Triste Problema"),
    ("Ismael Rivera", "El Incomprendido"),
    ("Odilio González", "De Rodillas"),
    ("Odilio González", "Olvídame"),
    ("Luz Celenia Tirado", "Alma Gemela"),
    ("Julio Iglesias", "Hey"),
    ("Julio Iglesias", "Me Olvidé de Vivir"),
    ("Paloma San Basilio", "Juntos"),
    ("Mocedades", "Eres Tú"),
    ("José José", "Como Quieres Que Te Quiera"),
    ("José José", "Lo Que No Fue No Será"),
    ("Los Panchos", "No Me Quieras Tanto"),
    ("Los Tres Diamantes", "Usted"),
    ("Trío Los Panchos", "Sabor a Mí"),
]


def song_key(title: str) -> str:
    return fold(title)


def rec(vid: str, artist: str, title: str, intro: bool = False) -> dict:
    out = {
        "id": vid,
        "artist": artist,
        "title": title,
        "youtube": f"https://www.youtube.com/watch?v={vid}",
        "artwork": f"https://i.ytimg.com/vi/{vid}/mqdefault.jpg",
        "artworkLarge": f"https://i.ytimg.com/vi/{vid}/mqdefault.jpg",
    }
    if intro:
        out["intro"] = True
    return out


def unique_keep(tracks: list[dict], first_n: int = 15) -> list[dict]:
    keep = []
    seen_id = set()
    seen_title = set()
    for i, t in enumerate(tracks):
        vid = t["id"]
        if vid in seen_id:
            continue
        key = song_key(t["title"])
        if i >= first_n and key in seen_title:
            continue
        seen_id.add(vid)
        seen_title.add(key)
        keep.append(t)
    return keep


def find_clip(artist: str, title: str) -> dict | None:
    q = f"{artist} {title}"
    try:
        hits = walk_hits(search(q))
    except Exception as err:
        print("SEARCH FAIL", q, err)
        return None
    chosen = pick(artist, title, hits)
    if not chosen or chosen.get("score", 0) < 0:
        return None
    meta = oembed(chosen["id"])
    if not meta.get("ok"):
        return None
    blob = f"{meta.get('title','')} {meta.get('author','')}"
    if BAD.search(blob) and "VEVO" not in (meta.get("author") or "").upper():
        return None
    if not title_hits(title, meta.get("title") or chosen.get("title") or ""):
        return None
    return rec(chosen["id"], artist, title)


def no_consec(head: list[dict], tail: list[dict], limit: int) -> list[dict]:
    out = list(head)
    unused = list(tail)
    while unused and len(out) < limit:
        prev = lead_artist(out[-1]["artist"]) if out else ""
        pick_i = next((i for i, t in enumerate(unused) if lead_artist(t["artist"]) != prev), 0)
        out.append(unused.pop(pick_i))
    return out[:limit]


def write(era: str, tracks: list[dict]) -> None:
    for i, t in enumerate(tracks):
        if i < 15:
            t["intro"] = True
        else:
            t.pop("intro", None)
    blob = {
        "name": "abuela",
        "room": "abuela",
        "era": era,
        "shuffle": False,
        "loop": True,
        "introCount": 15,
        "count": len(tracks),
        "tracks": tracks,
    }
    path = PUBLIC / era / "abuela.json"
    path.write_text(json.dumps(blob, ensure_ascii=False, indent=2) + "\n")
    print("WROTE", path, "n=", len(tracks))
    for i, t in enumerate(tracks[:15], 1):
        print(f"  {i:2} {t['id']}  {t['artist'][:28]:28}  {t['title']}")


def pad(era: str, candidates: list[tuple[str, str]]) -> None:
    path = PUBLIC / era / "abuela.json"
    data = json.loads(path.read_text())
    tracks = unique_keep(data["tracks"], 15)
    head = tracks[:15]
    rest = tracks[15:]
    have_titles = {song_key(t["title"]) for t in tracks}
    have_ids = {t["id"] for t in tracks}
    need = 100 - len(tracks)
    print(f"{era} unique={len(tracks)} need={need}")
    want = [(a, t) for a, t in candidates if song_key(t) not in have_titles]
    found = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futs = {pool.submit(find_clip, a, t): (a, t) for a, t in want}
        for fut in as_completed(futs):
            a, t = futs[fut]
            try:
                hit = fut.result()
            except Exception as err:
                print("ERR", a, t, err)
                continue
            if not hit:
                print("MISS", a, "—", t)
                continue
            if hit["id"] in have_ids or song_key(hit["title"]) in have_titles:
                print("DUP", a, t, hit["id"])
                continue
            have_ids.add(hit["id"])
            have_titles.add(song_key(hit["title"]))
            found.append(hit)
            print("OK", a, "—", t, hit["id"])
            if len(tracks) + len(found) >= 100:
                break
    packed = no_consec(head, rest + found, 100)
    write(era, packed)


def main() -> None:
    pad("ayer", DAY_CANDIDATES)
    pad("hoy", NIGHT_CANDIDATES)


if __name__ == "__main__":
    main()
