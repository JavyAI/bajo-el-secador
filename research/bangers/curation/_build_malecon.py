#!/usr/bin/env python3
"""Malecón couple radio — raise both first-15s, keep 100 + 100."""
from __future__ import annotations

import json
import ssl
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path

CTX = ssl.create_default_context()
UA = "Mozilla/5.0 en-el-secador-malecon"

ROOT = Path("/Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador")
CUR = ROOT / "research/bangers/curation"

# (id, artist, title, year, channel, views)
# First 15 authored. Locked #1s stay. Forgotten #1 inside the 15, never opener.
# Door rule: do not open like Barbería (Un Beso / Darte as #2) or steal Galería.

AYER15 = [
    ("v0ckuv1xBm0", "Juan Luis Guerra", "Burbujas de Amor", 1990, "Juan Luis Guerra 4.40 - Topic", 30192375),
    ("iK3BlAZAtPs", "Chayanne", "Completamente Enamorados", 1990, "chayanneVEVO", 65510820),
    ("T_oE3qkbo5s", "Luis Miguel", "No Sé Tú", 1991, "Warner Music México", 201611187),
    ("2LiZyAIVmbs", "Juan Luis Guerra", "Bachata Rosa", 1990, "Karen Records", 47098909),
    ("uBwk106e3es", "Aventura", "Un Beso", 2005, "Aventura", 190142020),
    ("NdKhS4MMCEo", "Luis Miguel", "Somos Novios", 1997, "Warner Music México", 9163309),
    ("0m5SXO8qK78", "Monchy y Alexandra", "Dos Locos", 2002, "Radial by The Orchard", 90285479),
    ("hNDtsPMX7p0", "Franco De Vita", "Te Amo", 1988, "Franco De Vita", 28927344),
    ("j3ObHjm1fAE", "Chayanne", "Tiempo de Vals", 1990, "chayanneVEVO", 142030036),
    ("QTYJkS6bTOQ", "Ricardo Montaner", "Tan Enamorados", 1986, "Ricardo Montaner", 10746709),
    ("8sCWmb8f-BY", "Monchy y Alexandra", "Te Quiero Igual Que Ayer", 2002, "Monchy & Alexandra", 11976138),
    ("p7QYo-9SlP0", "Ricky Martin", "Vuelve", 1998, "RickyMartinVEVO", 146318195),
    ("nYWcy7z0QmU", "Enrique Iglesias", "Enamorado Por Primera Vez", 1997, "Enrique Iglesias", 80646306),
    ("-hoZpSoKAYE", "Sin Bandera", "Entra En Mi Vida", 2001, "SinbanderaVEVO", 316531367),
    ("9oLBY9QqTAQ", "Fonseca", "Te Mando Flores", 2005, "Fonseca", 154700000),
]

AYER_TAIL = [
    ("kAKVT1HWNsg", "Son by Four", "A Puro Dolor", 2000, "SonByFourVEVO", 746667910),
    ("z2pt4CN4rhc", "Aventura", "Mi Corazoncito", 2005, "Aventura", 179443704),
    ("giAE7Yz7gHI", "Luis Miguel", "Por Debajo de la Mesa", 1997, "Warner Music México", 185838650),
    ("XFRfrPkfghY", "Aventura", "La Boda", 2002, "Aventura", 599100304),
    ("kCv8ipMi-BE", "Luis Miguel", "Hasta Que Me Olvides", 1993, "Luis Miguel - Topic", 185546302),
    ("KYZlT2iYRh8", "Chayanne", "Un Siglo Sin Ti", 2002, "chayanneVEVO", 525015141),
    ("xA0DBcsfjTE", "Monchy y Alexandra", "Hoja en Blanco", 1999, "JN Music Group", 279258163),
    ("elGZbcpGzdU", "Aventura", "El Perdedor", 2009, "Aventura", 707327647),
    ("wOjzo02Tmck", "Luis Miguel", "La Incondicional", 1989, "Warner Music México", 376857718),
    ("ByU6ABQ1cp8", "Monchy y Alexandra", "Perdidos", 2004, "JN Music Group", 5028208),
    ("29NM6ySmwfQ", "Cristian Castro", "Azul", 2001, "CristianCastroVEVO", 131622379),
    ("0t5iCwpuD8I", "Jon Secada", "Otro Día Más Sin Verte", 1992, "JON SECADA - Latin Crossover King LCK", 119194491),
    ("XuCd3Qj6C08", "Franco De Vita", "Un Buen Perdedor", 2006, "FrancodeVitaVEVO", 112522693),
    ("l6LjNOYvhMk", "Gloria Estefan", "Con Los Años Que Me Quedan", 1993, "GloriaEstefanVEVO", 106999134),
    ("_4NBD3SqBwg", "Juan Luis Guerra", "Bachata en Fukuoka", 2010, "JuanLuisGuerraVEVO", 64498844),
    ("uLvvtQnQw8s", "Pimpinela", "Olvídame y Pega la Vuelta", 1983, "Pimpinela", 54247251),
    ("QGQTLN_RCmI", "Ricardo Montaner", "Castillo Azul", 1989, "Ricardo Montaner", 30371052),
    ("Spz1YgguUOM", "Xtreme", "Te Extraño", 2006, "XtremeVEVO", 23181500),
    ("L_xc4YBmtOQ", "Alex Ubago", "Aunque No Te Pueda Ver", 2001, "Warner Música", 20357272),
    ("u3wrqH2dXL0", "Alejandro Fernández", "Me Dediqué a Perderte", 2004, "AFernandezVEVO", 11306973),
    ("AtRjy0iB_1M", "Daniel Santacruz", "Adónde Va El Amor", 2008, "Daniel Santacruz", 8583503),
    ("mZrM2Sd_7tg", "Domenic Marte", "Ven Tú", 2004, "Domenic Marte", 4001576),
    ("0ZcfOkrbUkI", "Charlie Zaa", "Un Disco Más", 1996, "Charlie Zaa Catalogo", 1628583),
    ("aW13iWEktsA", "Alejandro Sanz", "Corazón Partío", 1997, "Warner Música", 140300000),
    ("2MjvxB1_lmo", "Sin Bandera", "Kilómetros", 2001, "SinbanderaVEVO", 196899431),
    ("uwuKYJtVqLM", "Andy Andy", "Qué Ironía", 2005, "Andy Andy - Topic", 674438),
    ("E4B8I2M0y-Y", "Reik", "Noviembre Sin Ti", 2005, "reikVEVO", 499663),
    ("iajZ1R5dIXU", "Cristian Castro", "Por Amarte Así", 1999, "Cristian Castro - Topic", 363400000),
    ("uMrN1W4ryoE", "Chayanne", "Dejaría Todo", 1998, "chayanneVEVO", 462950023),
    ("GfFnQ2l2FxM", "Monchy y Alexandra", "Polos Opuestos", 2005, "Radial by The Orchard", 16735415),
    ("sLqg5DXeQxc", "Ricky Martin", "Perdido Sin Ti", 1998, "Ricky Martin - Topic", 1526274),
    ("Tu5tt_l_YEw", "Cristian Castro", "Nunca Voy a Olvidarte", 1993, "CristianCastroVEVO", 2498850),
    ("3DV57Y4tEAM", "Enrique Iglesias", "Experiencia Religiosa", 1995, "Enrique Iglesias", 89500000),
    ("LvgEpio1-kA", "Juan Luis Guerra", "Como Abeja al Panal", 1990, "Karen Records", 17268406),
    ("jrkNik4AHTU", "Ricardo Montaner", "La Cima del Cielo", 1989, "Ricardo Montaner", 26527636),
    ("z0T-7j_pt6w", "Alex Ubago", "Sin Miedo a Nada", 2003, "Warner Music México", 7272931),
    ("Fk5oL0mgI08", "Sin Bandera", "Que Lloro", 2003, "SinbanderaVEVO", 422264656),
    ("DaDuJhparw8", "Reik", "Inolvidable", 2008, "reikVEVO", 203637938),
    ("YkVbgpXXR0M", "Chayanne", "Yo Te Amo", 2000, "chayanneVEVO", 240452578),
    ("OThKTAVrUMQ", "Luis Miguel", "Tengo Todo Excepto a Ti", 1990, "Warner Music México", 94597722),
    ("dNR1ntnF2wg", "Monchy y Alexandra", "Pasión", 2001, "JN Music Group", 1778088),
    ("pRrjt4htXlE", "Enrique Iglesias", "Nunca Te Olvidaré", 1998, "Enrique Iglesias", 635139830),
    ("sxbKoqz9bNM", "Juan Luis Guerra", "Estrellitas y Duendes", 1990, "Karen Records", 13368763),
    ("jamgjQ-CTI8", "Ricardo Montaner", "Bésame", 1994, "Ricardo Montaner", 21411126),
    ("0i7-nNOCjiM", "Reik", "Me Duele Amarte", 2006, "reikVEVO", 164376719),
    ("Ubxb1u3izeM", "Chayanne", "Atado a Tu Amor", 1998, "chayanneVEVO", 226607365),
    ("wEF19rvbH3I", "Luis Miguel", "El Reloj", 1997, "Warner Music México", 38548696),
    ("B-4LuFAOMKQ", "Monchy y Alexandra", "No Es Una Novela", 2006, "JN Music Group", 619587),
    ("jRxebPzoiMo", "Juan Luis Guerra", "Frío Frío", 1991, "Karen Records", 5503512),
    ("AJXGjG9_ENI", "Ricardo Montaner", "Me Va a Extrañar", 1988, "Ricardo Montaner", 14400000),
    ("tg7QRlINFgQ", "Sin Bandera", "Mientes Tan Bien", 2006, "SinbanderaVEVO", 240269880),
    ("lLiPh6kmFoU", "Luis Miguel", "Contigo en la Distancia", 1991, "Warner Música", 35957064),
    ("ohumtiwSo9E", "Monchy y Alexandra", "Hasta El Fin", 2004, "JN Music Group", 458812),
    ("bqvBxdO0B1s", "Juan Luis Guerra", "Quisiera", 1998, "Karen Records", 2642507),
    ("GsI6V_DToHg", "Chayanne", "Y Tú Te Vas", 2002, "chayanneVEVO", 327200000),
    ("3fJkFcw7CZ4", "Luis Miguel", "O Tú o Ninguna", 1999, "Warner Música", 28759578),
    ("dY8MG-Qf7tk", "Luis Miguel", "Entrégate", 1990, "OficialLuisMiguel", 41703874),
    ("ZM2KoVO0NSs", "Juan Luis Guerra", "Si Tú Te Vas", 1990, "Karen Records", 2496587),
    ("wTZ7A-h8yTs", "Shakira", "Tú", 1998, "shakiraVEVO", 112400000),
    ("zZBLqpRoE_E", "Luis Miguel", "Amarte Es Un Placer", 1999, "Warner Music México", 7457462),
    ("5dNxsyvuYho", "Juan Luis Guerra", "Cuando Te Beso", 2007, "Karen Records", 234564),
    ("n0xjCC4-RwI", "Luis Miguel", "Te Necesito", 2003, "Warner Music México", 3485599),
    ("QZKrLIoMyxY", "Reik", "Yo Quisiera", 2005, "reikVEVO", 499935282),
    ("gO8-9OWzPOQ", "Camila", "Todo Cambió", 2006, "camilaVEVO", 323843798),
    ("xftFxCYQTdk", "Camila", "Mientes", 2009, "camilaVEVO", 742000000),
    ("EsfSuL-VFBw", "Luis Fonsi, Aleks Syntek, Noel Schajris, David Bisbal", "Aquí Estoy Yo", 2008, "LuisFonsiVEVO", 522000000),
    ("jlySoaI0DGI", "Camila", "Coleccionista de Canciones", 2006, "camilaVEVO", 349016223),
    ("00QVU7voMq8", "Fonseca", "Eres Mi Sueño", 2008, "FonsecaVEVO", 180000000),
    ("XNGWDH-6yv8", "Prince Royce", "Corazón Sin Cara", 2010, "PrinceRoyceVEVO", 282100000),
    ("foyH-TEs9D0", "Prince Royce", "Stand by Me", 2010, "PrinceRoyceVEVO", 112000000),
    ("WllxyZpvVEs", "Aventura", "Angelito", 2002, "Aventura", 172550334),
    ("uPCZm2Tvjpo", "Aventura", "Enséñame a Olvidar", 2002, "Aventura", 307940605),
    ("fY36BMNDqbg", "Aventura", "Su Veneno", 2009, "Aventura", 355485085),
    ("GHLVjriwzFg", "Aventura", "Por Un Segundo", 2009, "Aventura", 355026262),
    ("kADoBrj4934", "Aventura", "Todavía Me Amas", 2009, "Aventura", 156910480),
    ("v6aicYYG59I", "Aventura", "Te Invito", 2008, "Aventura", 72278134),
    ("TviYVNPCs2c", "Aventura", "Cuando Volverás", 1999, "Aventura", 64287840),
    ("KstbkZwnTv0", "Camila", "Aléjate de Mí", 2010, "camilaVEVO", 649633745),
    ("fge78Gv0f1E", "Enrique Iglesias", "Si Tú Te Vas", 1995, "Enrique Iglesias", 45000000),
    ("OY7SCchuzac", "Alex Bueno", "El Jardín Prohibido", 1996, "Alex Bueno - Topic", 28184350),
    ("q79vUDskBGQ", "Frank Reyes", "Princesa", 2002, "JN Music Group", 27797617),
    ("ZN6R4y7qBuw", "Frank Reyes", "Noche de Pasión", 2004, "Radial by The Orchard", 19334328),
    ("-XVVZYFvaZY", "Elvis Martínez", "Directo al Corazón", 1998, "Elvis Martinez", 15379813),
    ("zo-r93kzotA", "Elvis Martínez", "Hoy", 1999, "Elvis Martinez", 502170),
    ("rmerQRm3GJk", "Héctor Acosta", "Me Voy", 2008, "Hector Acosta", 59590745),
    ("uZtXRgB95T4", "Amanda Miguel", "Ámame Una Vez Más", 1987, "Amanda Miguel TV - Canal Oficial", 23427393),
    ("QcRscK_S0Ic", "Juan Luis Guerra", "Razones", 1990, "Juan Luis Guerra 4.40 - Topic", 560537),
    ("X3rdR2vlii4", "Sin Bandera", "Suelta Mi Mano", 2005, "SinbanderaVEVO", 80000000),
    ("Aa6MmoSKOdo", "Enrique Iglesias", "Hero", 2001, "EnriqueIglesiasVEVO", 250000000),
    ("8hRGBcr_gJc", "Luis Fonsi", "No Me Doy Por Vencido", 2008, "LuisFonsiVEVO", 890000000),
    ("av3wkasS-WQ", "Maná", "Mariposa Traicionera", 2002, "ManaVEVO", 180000000),
    ("Em1dOC9uyKo", "Ednita Nazario", "Más Grande Que Grande", 1994, "EdnitaNazarioVEVO", 12000000),
    ("dr32e5ms9Go", "Marc Anthony", "Hasta Ayer", 1997, "marcanthonyVEVO", 45000000),
    ("FLYbAHFW5SY", "Monchy y Alexandra", "Corazón Prendido", 2003, "JN Music Group", 800000),
]

HOY15 = [
    ("QFs3PIZb3js", "Romeo Santos", "Propuesta Indecente", 2013, "RomeoSantosVEVO", 2420000000),
    ("DriCCFRQlj8", "Camilo, Evaluna Montaner", "Índigo", 2021, "CamiloVEVO", 228400000),
    ("Mtau4v6foHA", "Carlos Vives, Sebastián Yatra", "Robarte un Beso", 2017, "CarlosVivesVEVO", 1900000000),
    ("8iPcqtHoR3U", "Romeo Santos", "Eres Mía", 2014, "RomeoSantosVEVO", 1340000000),
    ("bdOXnTbyk0g", "Prince Royce", "Darte un Beso", 2013, "PrinceRoyceVEVO", 1620000000),
    ("ghAvJMxE1qo", "Sebastián Yatra, Reik", "Un Año", 2019, "SebastianYatraVEVO", 856000000),
    ("zHhza3EgHe8", "Juan Luis Guerra, Romeo Santos", "Frío, Frío", 2014, "JuanLuisGuerraVEVO", 383700000),
    ("jucBuAzuZ0E", "Alejandro Sanz, Marc Anthony", "Deja Que Te Bese", 2016, "AlejandroSanzVEVO", 204800000),
    ("BFaRWXEpFrs", "Marc Anthony", "Tu Vida en la Mía", 2019, "marcanthonyVEVO", 198100000),
    ("hpzT6Wq6pKY", "Prince Royce", "Incondicional", 2012, "PrinceRoyceVEVO", 210800000),
    ("sPTn0QEhxds", "Shakira", "Me Enamoré", 2017, "shakiraVEVO", 983800000),
    ("YwodhCjFbQ8", "Camilo, Evaluna Montaner", "Por Primera Vez", 2020, "CamiloVEVO", 608300000),
    ("sD9_l3oDOag", "Sebastián Yatra", "No Hay Nadie Más", 2018, "SebastianYatraVEVO", 980000000),
    ("W4AiOKlOO0Q", "Alejandro Sanz, Camila Cabello", "Mi Persona Favorita", 2019, "AlejandroSanzVEVO", 310000000),
    ("Geqmpq0tjNU", "Carlos Vives, Marc Anthony", "Cuando Nos Volvamos a Encontrar", 2014, "CarlosVivesVEVO", 890000000),
]

HOY_TAIL = [
    ("ROzZSmaxDz8", "Prince Royce", "Las Cosas Pequeñas", 2012, "PrinceRoyceVEVO", 83600000),
    ("uXUjhE9MhyU", "Pablo Alborán", "Prometo", 2017, "Pablo Alborán", 55300000),
    ("2mY7AFTtYwQ", "Camilo", "Favorito", 2020, "CamiloVEVO", 520000000),
    ("jk4HYngf65w", "Romeo Santos", "Cancioncitas de Amor", 2014, "RomeoSantosVEVO", 635500000),
    ("XlmaJ-yU46U", "Aventura", "Inmortal", 2019, "Aventura", 381000000),
    ("ncByymoHQRI", "Juan Luis Guerra", "Tus Besos", 2014, "JuanLuisGuerraVEVO", 210000000),
    ("I9cCPQVPv8o", "Ricardo Arjona, Gaby Moreno", "Fuiste Tú", 2012, "RicardoArjonaVEVO", 890000000),
    ("Z81hsLIY1sQ", "Alejandro Fernández, Christina Aguilera", "Hoy Tengo Ganas de Ti", 2013, "AFernandezVEVO", 980000000),
    ("Rir_fuLX7HM", "Carlos Rivera", "Te Esperaba", 2018, "CarlosRiveraVEVO", 180000000),
    ("07314LhFag4", "Juan Luis Guerra", "Todo Tiene Su Hora", 2014, "JuanLuisGuerraVEVO", 160000000),
    ("gSJd_J3W6NU", "Fonseca, Juan Luis Guerra", "Si Tú Me Quieres", 2021, "FonsecaVEVO", 90000000),
    ("JMq0HJXIp8o", "Juan Luis Guerra", "Corazón Enamorado", 2014, "JuanLuisGuerraVEVO", 25000000),
    ("NE3IkFadCHM", "Sebastián Yatra", "Traicionera", 2016, "SebastianYatraVEVO", 1300000000),
    ("_gm5piKnrS4", "Morat", "Cómo Te Atreves", 2016, "MoratVEVO", 430000000),
    ("TMT9MNM-NHg", "Jesse & Joy", "Dueles", 2014, "JesseyJoyVEVO", 210000000),
    ("N6mShTc40BU", "Carlos Rivera", "El Hubiera No Existe", 2018, "CarlosRiveraVEVO", 120000000),
    ("_WHGlEYaBgU", "Jesse & Joy", "Ecos de Amor", 2015, "JesseyJoyVEVO", 190000000),
    ("7TWzV05kQ4w", "Reik", "Ya Me Enteré", 2016, "reikVEVO", 620000000),
    ("Geqmpq0tjNU", "Carlos Vives, Marc Anthony", "Cuando Nos Volvamos a Encontrar", 2014, "CarlosVivesVEVO", 890000000),
    ("QBaIMZ8QjcU", "Romeo Santos, Marc Anthony", "Yo También", 2014, "RomeoSantosVEVO", 410000000),
    ("0diOZSlLKdg", "Carlos Rivera", "¿Cómo Pagarte?", 2013, "CarlosRiveraVEVO", 140000000),
    ("TOgCeRQvzoY", "Kany García", "Confieso", 2019, "KanyGarciaVEVO", 180000000),
    ("_X3PPuF_yOE", "Río Roma", "Me Cambiaste la Vida", 2012, "RioRomaVEVO", 320000000),
    ("weKJWqw8-3g", "Luis Fonsi, Juan Luis Guerra", "Llegaste Tú", 2014, "LuisFonsiVEVO", 110000000),
    ("OdaIbTUGmHM", "Prince Royce", "La Carretera", 2016, "PrinceRoyceVEVO", 502000000),
    ("XEvKn-QgAY0", "Prince Royce, Shakira", "Deja Vu", 2017, "PrinceRoyceVEVO", 890000000),
    ("OST41MmjdTQ", "Prince Royce", "El Amor Que Perdimos", 2011, "PrinceRoyceVEVO", 482500000),
    ("-lDsqOsJL7k", "Prince Royce", "Culpa al Corazón", 2017, "PrinceRoyceVEVO", 210000000),
    ("4eCL0l9iD5A", "Romeo Santos", "Hilito", 2014, "RomeoSantosVEVO", 357600000),
    ("VafbNsrHnD8", "Romeo Santos", "Llévame Contigo", 2011, "RomeoSantosVEVO", 185200000),
    ("qjkb9_AJCLo", "Prince Royce", "Carita de Inocente", 2020, "PrinceRoyceVEVO", 81500000),
    ("DXiXPhvYuNU", "Romeo Santos, Santana", "Necio", 2014, "RomeoSantosVEVO", 415800000),
    ("J9QmUNZOh7I", "Daniel Santacruz", "Casablanca", 2015, "Daniel Santacruz", 12000000),
    ("rvmtQvA_cmM", "Romeo Santos", "Sus Huellas", 2022, "RomeoSantosVEVO", 190000000),
    ("Vl7RmqGztbk", "Daniel Santacruz", "Bachata en Nueva York", 2014, "Daniel Santacruz", 8000000),
    ("CDv6lGEaWTo", "Henry Santos", "Por Nada", 2013, "HenrySantosVEVO", 15000000),
    ("tNw9Rc3GbcE", "Daniel Santacruz", "Desnudos", 2018, "Daniel Santacruz", 9000000),
    ("R5V-A-iu9dg", "Henry Santos", "Te Di", 2015, "HenrySantosVEVO", 8000000),
    ("p2YCzaZNRqQ", "Daniel Santacruz", "No Me Sueltes", 2017, "Daniel Santacruz", 6000000),
    ("g81JtMbrJtw", "Pinto Picasso", "París", 2016, "Pinto Picasso", 12000000),
    ("RfTcYeNdZHY", "Héctor Acosta", "Amorcito Enfermito", 2015, "Hector Acosta", 85000000),
    ("uUeNpTC7UWI", "Pinto Picasso", "No Me Toca", 2017, "Pinto Picasso", 4000000),
    ("ot6wDVHqVNw", "Héctor Acosta", "Sin Perdón", 2013, "Hector Acosta", 18000000),
    ("eshFzjIZZzA", "Bachata Heightz, Héctor Acosta", "Me Puedo Matar", 2012, "Bachata Heightz", 25000000),
    ("b0vDALH-CUw", "Kewin Cosmos", "Déjame Tenerte", 2016, "Kewin Cosmos", 8000000),
    ("z1EB-fI0JDI", "Jesse & Joy", "Un Besito Más", 2016, "JesseyJoyVEVO", 140000000),
    ("0U3SkZEBGDY", "Ricky Martin", "Disparo al Corazón", 2015, "RickyMartinVEVO", 180000000),
    ("PQlG1gznMBE", "Mon Laferte", "Amor Completo", 2015, "MonLaferteVEVO", 160000000),
    ("OK_KvknlJxA", "Jesse & Joy, Mario Domm", "Llorar", 2011, "JesseyJoyVEVO", 210000000),
    ("8_GGmHkgM-8", "Sin Bandera", "En Ésta No", 2016, "SinbanderaVEVO", 45000000),
    ("Nkloca2M6hU", "Juan Luis Guerra 4.40", "Tú", 2014, "JuanLuisGuerraVEVO", 20000000),
    ("prmzWy98c-I", "Jesse & Joy, Pablo Alborán", "La de la Mala Suerte", 2012, "JesseyJoyVEVO", 90000000),
    ("qKp1f7Vn9dM", "Camilo", "Vida de Rico", 2020, "CamiloVEVO", 680000000),
    ("nvxwiRuFgB0", "Jesse & Joy", "Me Soltaste", 2015, "JesseyJoyVEVO", 80000000),
    ("I_cJxvTQ6RM", "Ha*Ash", "100 Años", 2017, "HaAshVEVO", 320000000),
    ("ridGylKQ0WY", "Jesse & Joy, Luis Fonsi", "Tanto", 2017, "JesseyJoyVEVO", 110000000),
    ("6eT6cmIZJAM", "Leslie Grace", "Cómo Duele el Silencio", 2015, "LeslieGraceVEVO", 45000000),
    ("0nBzuG_jWbU", "Daniel Santacruz", "Lento", 2019, "Daniel Santacruz", 4000000),
    ("EGJ_XbqC64E", "Alex Bueno", "Pídeme", 2015, "Alex Bueno", 12000000),
    ("owOJ6L8Fepw", "Henry Santos", "Poquito a Poquito", 2012, "HenrySantosVEVO", 8000000),
    ("yUAZxs3qY3Y", "Prince Royce", "Te Robaré", 2013, "PrinceRoyceVEVO", 214400000),
    ("mhHqonzsuoA", "Romeo Santos", "Imitadora", 2017, "RomeoSantosVEVO", 796700000),
    ("69ppp5Ipook", "Romeo Santos", "Solo Conmigo", 2022, "RomeoSantosVEVO", 164300000),
    ("mjBH8FHVjO8", "Grupo Extra", "Es Amor", 2017, "Urban Latin Records", 13000000),
    ("9PCjVwJo3EI", "Prince Royce", "Te Me Vas", 2012, "Planet Records Official", 14000000),
    ("szeA9tvItJY", "Morat", "Cuando Nadie Ve", 2018, "MoratVEVO", 380000000),
    ("1oeD2m2UQAI", "Morat, Juanes", "Besos En Guerra", 2018, "MoratVEVO", 720000000),
    ("8DdKe4bPELU", "Prince Royce, Manuel Turizo", "Cúrame", 2019, "PrinceRoyceVEVO", 176700000),
    ("KsdJEolXHQA", "Juan Luis Guerra", "Muchachita Linda", 2014, "JuanLuisGuerraVEVO", 40000000),
    ("WENJIxEfyaw", "Juan Luis Guerra", "La Noviecita", 2022, "JuanLuisGuerraVEVO", 25000000),
    ("5R1RGl4WQP8", "Mon Laferte", "Tu Falta de Querer", 2015, "MonLaferteVEVO", 890000000),
    ("Uws510cVia4", "Ha*Ash", "Lo Aprendí de Ti", 2014, "HaAshVEVO", 980000000),
    ("jwP1HRmDVII", "Carla Morrison", "Disfruto", 2012, "CarlaMorrisonVEVO", 210000000),
    ("IKmPci5VXz0", "Natalia Lafourcade", "Hasta La Raíz", 2015, "NataliaLafourcadeVEVO", 430000000),
    ("NAG98gpC8Hw", "Ha*Ash", "Ex de Verdad", 2015, "HaAshVEVO", 280000000),
    ("sfV6uwZKQRY", "Beret", "Lo Siento", 2018, "BeretVEVO", 190000000),
    ("tUhmwamgDZY", "Ha*Ash", "Te Dejo en Libertad", 2011, "HaAshVEVO", 410000000),
    ("fRJ3kh9cnQo", "Mon Laferte", "Antes De Ti", 2018, "MonLaferteVEVO", 90000000),
    ("ZrUrwUwSHR0", "Camilo", "KESI", 2021, "CamiloVEVO", 128700000),
    ("HhgxpYNZxgk", "Jesse & Joy", "¿Con Quién Se Queda El Perro?", 2011, "JesseyJoyVEVO", 410000000),
    ("P2hM9CLAMu4", "Jesse & Joy", "¡Corre!", 2011, "JesseyJoyVEVO", 1108738680),
    ("snFhcHHdzT0", "Reik", "Creo en Ti", 2011, "reikVEVO", 310000000),
    ("tLcfAnN2QgY", "Enrique Iglesias, Marco Antonio Solís", "El Perdedor", 2013, "EnriqueIglesiasVEVO", 1600000000),
    ("Qz9gmiLBVFA", "Sebastián Yatra", "Tacones Rojos", 2021, "SebastianYatraVEVO", 690000000),
    ("3VmoZrxXbmg", "Marc Anthony", "Flor Pálida", 2013, "marcanthonyVEVO", 1200000000),
    ("CJ_zRSv3Hr8", "Carlos Vives", "Volví a Nacer", 2012, "CarlosVivesVEVO", 112700000),
    ("5AkDqm-cEgg", "Camilo, Pedro Capó", "Tutu", 2019, "CamiloVEVO", 856800000),
    ("YwodhCjFbQ8", "Camilo, Evaluna Montaner", "Por Primera Vez", 2020, "CamiloVEVO", 608300000),
    ("VjfGWTeSWF0", "Camilo, Evaluna Montaner", "PLIS", 2024, "CamiloVEVO", 67400000),
    ("iuTtlb2COtc", "Camilo, Evaluna Montaner", "Machu Picchu", 2021, "CamiloVEVO", 186700000),
    ("OukQDrJ7QRQ", "Morat", "Aprender A Quererte", 2016, "MoratVEVO", 323800000),
    ("sWGJd26kUOY", "Romeo Santos, ROSALÍA", "El Pañuelo", 2022, "RomeoSantosVEVO", 54300000),
    ("DjEttgmfNCU", "Henry Santos, JFab, Paola Fabre", "Cuando Te Toco", 2018, "HenrySantosVEVO", 5000000),
    ("S50Vs_y1W2A", "Kewin Cosmos", "La Vecina", 2014, "Kewin Cosmos", 5000000),
    ("YrN5Z-Aj3QE", "Héctor Acosta", "Me Duele La Cabeza", 2012, "Hector Acosta", 20000000),
    ("1d0y8h-9AAs", "Juan Luis Guerra", "Lacrimosa", 2021, "JuanLuisGuerraVEVO", 15000000),
    ("_wL3Pc-EmjA", "Ha*Ash", "Perdón, Perdón", 2014, "HaAshVEVO", 1123900978),
]


KINGS = {
    "juan luis guerra",
    "juan luis guerra 4.40",
    "aventura",
    "romeo santos",
    "prince royce",
}


def lead(artist: str) -> str:
    name = (artist or "").split(",")[0].strip().lower()
    if name.startswith("juan luis guerra"):
        return "juan luis guerra"
    return name


def to_track(row, intro: bool) -> dict:
    vid, artist, title, year, channel, views = row
    return {
        "id": vid,
        "artist": artist,
        "title": title,
        "year": year,
        "channel": channel,
        "views": int(views),
        "official": True,
        "artworkOk": True,
        "intro": intro,
    }


def interleave(tracks: list[dict], protect: int = 15) -> list[dict]:
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
    for i in range(protect, len(out)):
        if lead(out[i]["artist"]) != lead(out[i - 1]["artist"]):
            continue
        for j in range(i + 1, len(out)):
            if lead(out[j]["artist"]) == lead(out[i - 1]["artist"]):
                continue
            if j + 1 < len(out) and lead(out[i]["artist"]) == lead(out[j + 1]["artist"]):
                continue
            if lead(out[i]["artist"]) == lead(out[j - 1]["artist"]):
                continue
            out[i], out[j] = out[j], out[i]
            break
    return out


def build(era: str, first15, tail) -> list[dict]:
    used: set[str] = set()
    tracks: list[dict] = []
    counts: Counter[str] = Counter()

    for row in first15:
        t = to_track(row, True)
        if t["id"] in used:
            raise SystemExit(f"dup in 15: {t['id']}")
        if len(t["id"]) != 11:
            raise SystemExit(f"bad id in 15: {t['id']}")
        used.add(t["id"])
        tracks.append(t)
        counts[lead(t["artist"])] += 1

    for row in tail:
        t = to_track(row, False)
        if t["id"] in used:
            continue
        if len(t["id"]) != 11:
            raise SystemExit(f"bad id in tail: {t['id']}")
        ld = lead(t["artist"])
        cap = 18 if ld in KINGS else 12
        if counts[ld] >= cap:
            continue
        if not (1980 <= t["year"] <= 2010) and era == "ayer":
            raise SystemExit(f"AYER year fail {t}")
        if t["year"] < 2011 and era == "hoy":
            raise SystemExit(f"HOY year fail {t}")
        tracks.append(t)
        used.add(t["id"])
        counts[ld] += 1
        if len(tracks) >= 100:
            break

    if len(tracks) < 100:
        raise SystemExit(f"{era} only {len(tracks)}")
    tracks = interleave(tracks[:100], 15)
    return tracks


def hygiene(tracks: list[dict], era: str) -> None:
    ids = [t["id"] for t in tracks]
    if len(ids) != 100 or len(set(ids)) != 100:
        raise SystemExit(f"{era} id fail {len(ids)} unique {len(set(ids))}")
    bad = [i for i in ids if len(i) != 11]
    if bad:
        raise SystemExit(f"{era} bad id len {bad}")
    consec = [
        (tracks[i - 1]["artist"], tracks[i]["artist"])
        for i in range(1, len(tracks))
        if lead(tracks[i]["artist"]) == lead(tracks[i - 1]["artist"])
    ]
    if consec:
        raise SystemExit(f"{era} consecutive {consec}")
    c = Counter(lead(t["artist"]) for t in tracks)
    for name, n in c.items():
        cap = 18 if name in KINGS else 12
        if n > cap:
            raise SystemExit(f"{era} cap fail {name} {n}>{cap}")
    intro = [t for t in tracks if t["intro"]]
    if len(intro) != 15:
        raise SystemExit(f"{era} intro {len(intro)}")
    c15 = Counter(lead(t["artist"]) for t in intro)
    for name, n in c15.items():
        if n > 2:
            raise SystemExit(f"{era} first15 lead {name}={n}")
    years = [t["year"] for t in tracks]
    if era == "ayer" and (min(years) < 1980 or max(years) > 2010):
        raise SystemExit(f"AYER year window {min(years)}-{max(years)}")
    if era == "hoy" and min(years) < 2011:
        raise SystemExit(f"HOY year window {min(years)}")


def oembed_ok(vid: str) -> tuple[bool, str]:
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=20) as r:
            data = json.loads(r.read().decode())
        title = data.get("title") or ""
        author = data.get("author_name") or ""
        return True, f"{author} | {title}"
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError) as exc:
        return False, str(exc)


def art_ok(vid: str) -> tuple[bool, int]:
    url = f"https://i.ytimg.com/vi/{vid}/mqdefault.jpg"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=20) as r:
            payload = r.read()
            status = r.status
        return status == 200 and len(payload) > 2000, len(payload)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
        return False, 0


def verify_door(tracks: list[dict], era: str) -> None:
    fails = []
    for t in tracks[:15]:
        ok, info = oembed_ok(t["id"])
        art, nbytes = art_ok(t["id"])
        t["artworkOk"] = bool(art)
        print(f"  {era} {t['id']} oembed={ok} art={art}({nbytes}) {info}")
        if not ok:
            fails.append(t["id"])
        if not art:
            fails.append(f"art:{t['id']}")
    if fails:
        raise SystemExit(f"{era} door verify fail {fails}")


def write_list(era: str, tracks: list[dict]) -> None:
    payload = {
        "room": "malecon",
        "era": era,
        "count": 100,
        "introCount": 15,
        "tracks": tracks,
    }
    path = CUR / f"malecon-{era}.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    c = Counter(lead(t["artist"]) for t in tracks)
    print(f"=== {era} n={len(tracks)} ===")
    print("first15:")
    for i, t in enumerate(tracks[:15], 1):
        print(f"  {i:2} {t['artist']} — {t['title']} ({t['year']}) {t['id']}")
    print("leads", c.most_common(12))
    print("wrote", path)


def main() -> None:
    ayer = build("ayer", AYER15, AYER_TAIL)
    hoy = build("hoy", HOY15, HOY_TAIL)
    hygiene(ayer, "ayer")
    hygiene(hoy, "hoy")
    print("verifying AYER door")
    verify_door(ayer, "ayer")
    print("verifying HOY door")
    verify_door(hoy, "hoy")
    write_list("ayer", ayer)
    write_list("hoy", hoy)


if __name__ == "__main__":
    main()
