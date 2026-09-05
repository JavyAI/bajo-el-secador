#!/usr/bin/env python3
"""Build En casa de abuela day/night catalogs from official YouTube ids."""
from __future__ import annotations

import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PUBLIC = ROOT / "public"

# De día: La Bamba timing, Orocovis finca, PR jíbaro + DR típico + Mexican dance records.
DAY = [
    ("BycLmWI97Nc", "Ritchie Valens", "La Bamba"),
    ("FYMzEoGi8i4", "Ismael Rivera", "El Negro Bembón"),
    ("59j1m49X2eA", "Ángel Viloria y su Conjunto Típico Cibaeño", "Compadre Pedro Juan"),
    ("AZHmbdQD0nE", "La Sonora Matancera, Alberto Beltrán", "El Negrito del Batey"),
    ("whFKkmjl3ps", "Odilio González", "Celos Sin Motivo"),
    ("LbbEbIiGOuY", "Ramito", "Qué Bonita Bandera"),
    ("87uELF0RYaY", "La Sonora Matancera, Bobby Capó", "Piel Canela"),
    ("-rbE8KxEZd8", "Ismael Rivera", "Quítate de la Vía Perico"),
    ("3dNtHbJGDo0", "Trío Vegabajeño", "El Amor del Jibarito"),
    ("TGmvErNQKWA", "Celia Cruz", "Burundanga"),
    ("NRfpb-Ufh4w", "Guandulito", "El Rebu"),
    ("uHmRhMbq2EE", "La Sonora Matancera, Alberto Beltrán", "Aunque Me Cueste La Vida"),
    ("jXHZyEZveKM", "Chuíto el de Bayamón", "La Vieja Voladora"),
    ("4DdWs1A8UZ0", "Ismael Rivera", "El Chivo de la Campana"),
    ("hV8jxgCesEQ", "Ismael Rivera", "Saoco"),
    ("sHFFQsAXjmw", "Cortijo y su Combo", "El Bombón de Elena"),
    ("35P9hZB6Y_I", "Ismael Rivera", "Maquinolandera"),
    ("Ad4-s5p9bYU", "Joseíto Mateo", "El Negrito del Batey"),
    ("GKhXD1MsEOE", "Odilio González", "Qué Mala Suerte La Mía"),
    ("2-r7CHN3IQc", "Chuíto el de Bayamón", "La Vieja Voladora (Live)"),
    ("NocW20IDmtA", "Alberto Beltrán", "Todo Me Gusta De Ti"),
    ("OF8XC9Tf4rE", "Alberto Beltrán", "Aunque Me Cueste La Vida"),
    ("dEut4R6B6jE", "Cortijo y su Combo", "El Negro Bembón"),
    ("BXBHIpFrFoE", "Trini Lopez", "La Bamba"),
    ("YjAvQ22_05I", "Trini Lopez", "La Bamba (Live)"),
    ("DHISNB0xhKc", "Guandulito", "Candelo Cedife"),
    ("0GGrSaWypAM", "Luis Kalaff y sus Alegres Dominicanos", "Las Auroras"),
    ("wc_itynfgHs", "Luis Kalaff y sus Alegres Dominicanos", "La Cosquillita"),
    ("AGO-Sz4tKlk", "Trío Reynoso", "Compadre Pedro Juan"),
    ("Hzg5DRp5218", "Joseíto Mateo", "Los Algodones"),
    ("Iyr08hYofp4", "Cuco Valoy", "El Brujo"),
    ("V8MeUZS5zUk", "Celia Cruz, La Sonora Matancera", "Burundanga"),
    ("Wm5SkDUsrc0", "Cortijo y su Combo", "Saoco"),
    ("reG-sQb9fP4", "Ismael Rivera", "El Bombón de Elena"),
    ("iqL0bOlgrqE", "Ismael Rivera", "Quítate de la Vía Perico"),
    ("E_X0_kzTKNI", "Ismael Rivera y Cortijo", "Quítate de la Vía Perico"),
    ("IoV6X-Nwsss", "Odilio González", "Canto a Lares"),
    ("AXb7EORZekY", "Odilio González", "Celos Sin Motivo (Live)"),
    ("xAm7GYmgJUY", "Juaniquillo", "Canto a Puerto Rico"),
    ("cO0ryWB5yy4", "Juaniquillo", "Amor al Dinero"),
    ("7lggTJ8qTbA", "Ramito", "Qué Bonita Bandera (Plena)"),
    ("eUOFH0dJ74o", "Ramito", "Dos Caminos"),
    ("MlMMWGYcpKA", "Ramito", "Libertad del Campo"),
    ("gY93BsKMc9k", "Miguelito", "Jíbaro en San Juan"),
    ("Fvpd8XYMti0", "Chuíto y Maso Rivera", "Parranda"),
    ("r_40chgVBSw", "Luz Celenia Tirado", "Flotando Sobre el Caribe"),
    ("6q-F8HTj9wo", "Luz Celenia Tirado", "Alma Gemela"),
    ("uvMqK8FYJlk", "El Jilguero de Cienfuegos", "La Vida Es Una Carcajada"),
    ("VPdGO59k_dU", "El Jilguero de Cienfuegos", "La Vida Es una Carcajada"),
    ("_JISmNABRqU", "Trío Vegabajeño", "Vuelve"),
    ("oKIEjcodFYQ", "Trío Vegabajeño", "Amor Prohibido"),
    ("1wA4Tim43g0", "Bobby Capó", "Piel Canela"),
    ("hhNPzLLv4l8", "La Sonora Matancera, Bobby Capó", "Piel Canela"),
    ("tDi3LAYKr8w", "La Sonora Matancera", "El Negrito del Batey"),
    ("Z9DjdYDvvoM", "Joseíto Mateo", "El Negrito del Batey"),
    ("FK0q79LMgHY", "Ángel Viloria y su Conjunto Típico Cibaeño", "Compadre Pedro Juan"),
    ("ftQUOML41Gc", "Miguel Aceves Mejía", "El Jinete"),
    ("EMzctuQA1xY", "Miguel Aceves Mejía", "El Jinete"),
    ("OEJrCpkobWs", "Miguel Aceves Mejía", "El Jinete"),
    ("bb5K3vpNEvw", "Pedro Infante", "Amorcito Corazón"),
    ("Coy8Hoa1DNw", "Ritchie Valens", "La Bamba"),
    ("Cn5TX3TulA0", "Cortijo y su Combo", "Alegría y Bomba"),
    ("XaU_Fv9bWgk", "Cortijo y su Combo", "El Chivo de la Campana"),
    ("LS49yDGjyZ0", "Johnny Ventura", "La Agarradera"),
    ("BRL-3AaiFlA", "Johnny Ventura", "La Agarradera"),
    ("rM4JMszI8gs", "Cuco Valoy", "El Brujo"),
    ("96wyle5C3Q4", "Ismael Rivera", "El Negro Bembón"),
    ("AHlUnpcUJwM", "Ismael Rivera", "El Negro Bembón"),
    ("wrpNZidqfPs", "Ismael Rivera y Cortijo", "Maquinolandera"),
    ("YtixMYREssg", "Ismael Rivera y Cortijo", "El Bombón de Elena"),
    ("PPRN_DSAvbM", "Odilio González", "Celos Sin Motivos"),
    ("Dn9BNGpU0Mo", "Ramito", "Qué Bonita Bandera"),
    ("Jc7FlRKbXZ4", "Trío Vegabajeño", "El Amor del Jibarito"),
    ("6kyfe4uo4X8", "Trío Reynoso", "Compadre Pedro Juan"),
    ("QfoEGqyK1HY", "Guandulito", "Clásico Mix"),
    ("twsPfTbTaxY", "Johnny Ventura", "La Agarradera (Viña)"),
    ("HwjkTH5xCTw", "Ritchie Valens", "La Bamba (Film)"),
    ("YicJPLT1dWU", "Los Lobos", "La Bamba"),
]

# De noche: bolero, trío, José José, El Puma — after-dark radio in the house.
NIGHT = [
    ("b1cbgrcBrY0", "José José", "El Triste"),
    ("Gb1FrnjlXoo", "Eydie Gormé, Los Panchos", "Sabor a Mí"),
    ("UasiMOoMz1o", "Javier Solís", "Sombras Nada Más"),
    ("sodp4caaGC0", "Los Panchos", "Sin Ti"),
    ("fVDed_ORGdY", "Julio Jaramillo", "Nuestro Juramento"),
    ("86FCW0GRRcc", "José José", "40 y 20"),
    ("pOi9LLVcFBo", "Javier Solís", "En Mi Viejo San Juan"),
    ("jhx3hYS__JI", "Los Panchos", "Contigo"),
    ("y96olukMtfg", "José Luis Rodríguez", "Dueño de Nada"),
    ("LR7F45paOVc", "José José", "Gavilán o Paloma"),
    ("1Y9Sy1e2CFY", "Pedro Infante", "Cien Años"),
    ("ZipzeNiBe_E", "José Alfredo Jiménez", "El Rey"),
    ("TXRW9FdZcZA", "Tito Rodríguez", "Inolvidable"),
    ("1LYZ6sGmq-U", "Beny Moré", "Cómo Fue"),
    ("tDM0Oi9YdKM", "José José", "La Nave del Olvido"),
    ("lCUnsPvJMWg", "José José", "Lo Que No Fue No Será"),
    ("-I8ERJNhHAQ", "José José", "Almohada"),
    ("RzJ3QjBsqM0", "José José", "El Amar y El Querer"),
    ("xRK33-dd7nI", "José Luis Rodríguez", "Pavo Real"),
    ("QX44fC9MszA", "José Luis Rodríguez", "Voy a Perder la Cabeza por Tu Amor"),
    ("2BYody7JX_w", "Los Panchos", "Rayito de Luna"),
    ("Qg_L54DW69U", "Los Panchos", "Sabor a Mí"),
    ("tqKCXJaSr60", "Los Panchos", "Sin Ti"),
    ("_YKWaS3HUAc", "Los Panchos", "Contigo"),
    ("sPStjGfwC9k", "Julio Jaramillo", "Nuestro Juramento"),
    ("b4pa2-kF51c", "Julio Jaramillo", "Nuestro Juramento"),
    ("yiATSi7Gcik", "Javier Solís", "Si Dios Me Quita la Vida"),
    ("bb5K3vpNEvw", "Pedro Infante", "Amorcito Corazón"),
    ("1Y9Sy1e2CFY", "Pedro Infante", "Cien Años"),
    ("diSAz7xfpvE", "Pedro Infante", "Cien Años"),
    ("bxf59VB_TLI", "Felipe Rodríguez", "La Última Copa"),
    ("PtUjx-edL3E", "Felipe Rodríguez", "La Última Copa"),
    ("Ru9QRh25X7A", "Daniel Santos", "Lamento Borincano"),
    ("HI07Kq7z5lc", "Daniel Santos", "Lamento Borincano"),
    ("ZOLMn06UwYw", "Daniel Santos", "Lamento Borincano"),
    ("2remXMDCx3U", "Bienvenido Granda", "Total"),
    ("TDN6V_0Se3k", "Bienvenido Granda", "Quisiera Que El Mundo Acabase"),
    ("NQhnqBsgwoA", "Bienvenido Granda", "Egoísmo"),
    ("Ojytcx7cabQ", "Beny Moré", "Cómo Fue"),
    ("p4GggYWjRao", "Beny Moré", "Cómo Fue"),
    ("87sX9HkpErw", "Tito Rodríguez", "Inolvidable"),
    ("WEeI205f0WI", "Tito Rodríguez", "Inolvidable"),
    ("YTyBE-bvJ1M", "Gilberto Monroig", "Qué Falta Tú Me Haces"),
    ("dsH4i71crIc", "Gilberto Monroig", "Un Imposible Amor"),
    ("w336St83jos", "José José", "Almohada"),
    ("lflKe1W-6Rg", "José José", "Lo Que No Fue No Será"),
    ("ZxMbfrfbChU", "José José", "El Amar y el Querer"),
    ("2UijpO1rGnA", "José José", "El Triste"),
    ("Dp7duGuhAqw", "José José", "La Nave del Olvido"),
    ("GyasWUdWRG0", "José Luis Rodríguez", "Dueño de Nada"),
    ("HtdFtKOO7uI", "José Luis Rodríguez", "Dueño de Nada"),
    ("bNQg2N9Ifsk", "José Luis Rodríguez", "Voy a Perder la Cabeza por Tu Amor"),
    ("BEAAuDvukaY", "José Luis Rodríguez", "Voy a Perder la Cabeza por Tu Amor"),
    ("SdT4TLGJU4s", "José Luis Rodríguez", "Pavo Real"),
    ("e-a2iqX-ZfY", "Los Panchos", "Bésame Mucho"),
    ("pwRiKDcrjz0", "Los Panchos", "Bésame Mucho"),
    ("kjbCePqcb_4", "Los Panchos", "Rayito de Luna"),
    ("8vvivqjmmFY", "Los Panchos", "Rayito de Luna"),
    ("JC3z7XQXCm8", "Marco Antonio Muñiz", "Si Dios Me Quita la Vida"),
    ("UHAwnbE7sYk", "Javier Solís", "Sombras Nada Más"),
    ("CmOC-K-YU2Y", "Javier Solís", "Sombras Nada Más"),
    ("PC1B1n5C174", "Javier Solís", "En Mi Viejo San Juan"),
    ("PoKZ9MfnkBM", "José Alfredo Jiménez", "El Rey"),
    ("EdqLGTZd3NA", "Pedro Infante", "Amorcito Corazón"),
    ("N-GAVyBzNX0", "Felipe Rodríguez", "La Última Copa"),
    ("Rn4KOurlsYQ", "Lucho Gatica", "Contigo En La Distancia"),
    ("5wNIjmlC7Z0", "Lucho Gatica", "Contigo En La Distancia"),
    ("S9tzfMHYKcs", "Marc Anthony", "Lamento Borincano"),
    ("ggUlpfchOwk", "Joe Valle", "Preciosa"),
    ("vDzO8jrDT08", "José José", "Gavilán o Paloma"),
    ("Kc0ZZC9Z0Yw", "José José", "40 y 20"),
    ("mUGTXjSmtUA", "Eydie Gormé, Los Panchos", "Sabor a Mí"),
    ("QbedopuXdW4", "Eydie Gormé, Los Panchos", "Sabor a Mí"),
    ("eMA7MtCGlaU", "Los Panchos", "Rayito de Luna"),
    ("GiNTj7tso9g", "Los Panchos", "Sin Ti"),
    ("F1COh7t3el4", "Los Panchos", "Contigo"),
]


def oembed(vid: str) -> dict | None:
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    try:
        with urllib.request.urlopen(url, timeout=12) as r:
            return json.loads(r.read().decode())
    except Exception:
        return None


def pack(era: str, rows: list[tuple[str, str, str]]) -> list[dict]:
    locked = set(Path("/tmp/locked-first5.txt").read_text().split()) if Path("/tmp/locked-first5.txt").exists() else set()
    out = []
    seen = set()
    for vid, artist, title in rows:
        if vid in seen:
            continue
        seen.add(vid)
        meta = oembed(vid)
        if not meta:
            print("DROP", vid, title)
            continue
        if len(out) < 5 and vid in locked:
            print("FIRST5 LOCK", vid, title)
            continue
        rec = {
            "id": vid,
            "artist": artist,
            "title": title,
            "youtube": f"https://www.youtube.com/watch?v={vid}",
            "artwork": f"https://i.ytimg.com/vi/{vid}/mqdefault.jpg",
            "artworkLarge": f"https://i.ytimg.com/vi/{vid}/mqdefault.jpg",
        }
        if len(out) < 15:
            rec["intro"] = True
        out.append(rec)
        if len(out) >= 100:
            break
    return out


def write(era: str, tracks: list[dict]) -> None:
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
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(blob, ensure_ascii=False, indent=2) + "\n")
    print("WROTE", path, "n=", len(tracks))
    for i, t in enumerate(tracks[:15], 1):
        print(f"  {i:2} {t['id']}  {t['artist'][:28]:28}  {t['title']}")


def main() -> None:
    print("=== DAY ===")
    day = pack("ayer", DAY)
    write("ayer", day)
    print("=== NIGHT ===")
    night = pack("hoy", NIGHT)
    write("hoy", night)


if __name__ == "__main__":
    main()
