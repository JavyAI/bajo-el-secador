#!/usr/bin/env python3
"""Build galería AYER + HOY 100s and verify mqdefault 200."""
import json
import ssl
import time
import urllib.error
import urllib.request
from pathlib import Path

OUT = Path("/Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador/research/bangers/curation")
CTX = ssl.create_default_context()

def T(id, artist, title, year, channel, views=0, intro=False):
    return {
        "id": id,
        "artist": artist,
        "title": title,
        "year": year,
        "channel": channel,
        "views": views,
        "official": True,
        "artworkOk": True,
        "intro": intro,
    }

AYER = [
    T("dDEVFQnBTp0", "Juan Luis Guerra", "Ojalá Que Llueva Café", 1989, "JuanLuisGuerraVEVO", 35966520, True),
    T("95Wcl9ucitM", "Sergio Vargas", "La Ventanita", 1994, "Sergio Vargas", 8076247, True),
    T("E0f3J0z2SBQ", "Fernandito Villalona", "Cama y Mesa", 1983, "Fania Records", 883457, True),
    T("oADpF--uirA", "Juan Gabriel", "Querida", 1984, "JuanGabrielVEVO", 219291899, True),
    T("kkF5eGMxwEQ", "Ana Gabriel", "Simplemente Amigos", 1988, "AnaGabrielVEVO", 141472866, True),
    T("dpxQbZsXgNw", "Rocío Dúrcal", "Costumbres", 1986, "Rocío Dúrcal", 11745769, True),
    T("9jQJfdQlYUk", "José José", "Gavilán o Paloma", 1977, "JoseJoseVEVO", 18075808, True),
    T("tPTB0TRV3BA", "Juan Luis Guerra", "El Costo de la Vida", 1992, "Karen Records", 6147118, True),
    T("0xyfnlWs9QA", "Camilo Sesto", "Vivir Así Es Morir de Amor", 1978, "CamiloSestoVEVO", 24599567, True),
    T("by4I_10HbX4", "Luis Miguel", "La Incondicional", 1989, "OficialLuisMiguel", 286548801, True),
    T("ugNQ5uIN09Q", "Vicente Fernández", "Volver, Volver", 1972, "vicentefernandez®", 168206692, True),
    T("VyraXS0iMHw", "Los Bukis", "Tu Cárcel", 1987, "Los Bukis Oficial", 1561796, True),
    T("oObpxzkul3k", "José José", "Lo Pasado, Pasado", 1978, "José José Oficial", 44024714, True),
    T("g5rsnxJWNkM", "Juan Gabriel", "Se Me Olvidó Otra Vez", 1974, "JuanGabrielVEVO", 82771521, True),
    T("1ddK89KqVe8", "Myriam Hernández", "El Hombre Que Yo Amo", 1988, "Myriam Hernández", 171479805, True),
    T("py5lONtuw2A", "Juan Luis Guerra", "Visa Para un Sueño", 1989, "JuanLuisGuerraVEVO", 39384369),
    T("6e0XWqAeTwc", "José José", "Y Quién Puede Ser", 1984, "JoseJoseVEVO", 201574111),
    T("LakJahiBl2Y", "Juan Luis Guerra", "Mi Bendición", 2004, "JuanLuisGuerraVEVO", 105544731),
    T("apFqJ49VstY", "Daniela Romo", "Yo No Te Pido la Luna", 1984, "Daniela Romo", 82019516),
    T("gxWexyncaTs", "Juan Luis Guerra", "La Llave de Mi Corazón", 2007, "JuanLuisGuerraVEVO", 22210700),
    T("gr6RzMi4L3o", "Ana Gabriel", "No Te Hago Falta", 1999, "AnaGabrielVEVO", 286415069),
    T("AWozq4Phckc", "Juan Luis Guerra", "La Travesía", 2007, "JuanLuisGuerraVEVO", 20800000),
    T("p7QYo-9SlP0", "Ricky Martin", "Vuelve", 1998, "RickyMartinVEVO", 146298297),
    T("_4NBD3SqBwg", "Juan Luis Guerra", "Bachata en Fukuoka", 2010, "JuanLuisGuerraVEVO", 64486205),
    T("29NM6ySmwfQ", "Cristian Castro", "Azul", 2001, "CristianCastroVEVO", 131575495),
    T("RCZQaFu9pn0", "Juan Luis Guerra", "Que Me Des Tu Cariño", 2007, "JuanLuisGuerraVEVO", 29442123),
    T("Jn1OIkMqpbo", "Sergio Vargas", "La Quiero a Morir", 1994, "Sergio Vargas - Topic", 34179166),
    T("xE8gFafKTWU", "Juan Luis Guerra", "En el Cielo No Hay Hospital", 2004, "JuanLuisGuerraVEVO", 30602077),
    T("4DO8GsIYfhQ", "Enrique Iglesias, Juan Luis Guerra", "Cuando Me Enamoro", 2010, "EnriqueIglesiasVEVO", 982973000),
    T("QFVkLGqVhbo", "Ana Gabriel", "Quién Como Tú", 1989, "Ana Gabriel - Topic", 142316667),
    T("kQgXAn5J7is", "Juan Luis Guerra", "Woman del Callao", 1989, "Karen Records", 9525997),
    T("xaKLn_z9R_k", "Fernandito Villalona", "Tabaco y Ron", 1983, "Fernando Villalona", 3649585),
    T("7mGYSCO6yk0", "Juan Luis Guerra", "Coronita de Flores", 1990, "Karen Records", 1254262),
    T("1pr7Fv-9Z3I", "Ana Gabriel", "Evidencias", 1992, "AnaGabrielVEVO", 65449382),
    T("2LiZyAIVmbs", "Juan Luis Guerra", "Bachata Rosa", 1990, "Karen Records", 47097984),
    T("kr2B1RoWrlE", "José Luis Perales", "Y Cómo Es Él", 1982, "José Luis Perales - Topic", 136067019),
    T("EJ0W5MfRu0s", "Fernandito Villalona", "Soy Dominicano", 1987, "Fernando Villalona - Topic", 1229119),
    T("yDKYK-9yh7o", "Marco Antonio Solís", "Si No Te Hubieras Ido", 1999, "Marco Antonio Solís - Topic", 250043475),
    T("uwQ-2yfnuRU", "Gisselle, Sergio Vargas", "Perdóname, Olvídalo", 1997, "GisselleVEVO", 2528849),
    T("T3WJE1mgZs4", "Joan Sebastian", "Secreto de Amor", 1999, "Discos Musart", 69988398),
    T("g-GBiuujmL8", "Laura Pausini", "Se Fue", 1994, "Laura Pausini - Topic", 100359776),
    T("uLvvtQnQw8s", "Pimpinela", "Olvídame y Pega la Vuelta", 1983, "Pimpinela", 54240485),
    T("2GWftGahyvw", "Daniela Romo", "De Mí Enamórate", 1986, "Daniela Romo", 39558223),
    T("mIszekfGw3Q", "Yuri", "Detrás de Mi Ventana", 1993, "YuriMusicVideos", 15038626),
    T("F07ngnis2ig", "Ana Gabriel", "Es Demasiado Tarde", 1990, "AnaGabrielVEVO", 92231107),
    T("xVDmyuzkiPo", "Camilo Sesto", "Melina", 1975, "CamiloSestoVEVO", 125692114),
    T("ZsOJ_PZjjPI", "Ana Gabriel", "Luna", 1987, "AnaGabrielVEVO", 73130252),
    T("zehTpgLxXBs", "José José", "El Amor Acaba", 1985, "José José Oficial", 21995922),
    T("0O4CLgXvbjU", "Juan Gabriel", "Así Fue", 1988, "JuanGabrielVEVO", 1047999383),
    T("xf6cyDfi8t8", "José José", "La Nave del Olvido", 1970, "José José", 35133869),
    T("ga5Bo4YdgH4", "Juan Gabriel", "Hasta Que Te Conocí", 1986, "JuanGabrielVEVO", 808994332),
    T("RzJ3QjBsqM0", "José José", "Amar y Querer", 1977, "José José", 130067308),
    T("OThKTAVrUMQ", "Luis Miguel", "Tengo Todo Excepto a Ti", 1990, "Warner Music México", 94590689),
    T("mOJTvNKGovo", "José José", "Soy Así", 1987, "JoseJoseVEVO", 74860525),
    T("_tNVEhSelH0", "Juan Gabriel", "Abrázame Muy Fuerte", 2000, "JuanGabrielVEVO", 651208212),
    T("iu1sO4LoLN0", "Camilo Sesto, Carlos Rivera", "Algo de Mí", 1972, "CamiloSestoVEVO", 18510162),
    T("GRo0nnF5OXY", "Juan Gabriel", "Te Sigo Amando", 1997, "JuanGabrielVEVO", 55026774),
    T("dY8MG-Qf7tk", "Luis Miguel", "Entrégate", 1990, "OficialLuisMiguel", 41701800),
    T("mKT_QQmNmhM", "Juan Gabriel", "He Venido a Pedirte Perdón", 1980, "JuanGabrielVEVO", 18752886),
    T("YAMnqeBWKXI", "Ana Gabriel", "Ay Amor", 1987, "AnaGabrielVEVO", 0),
    T("T_oE3qkbo5s", "Luis Miguel", "No Sé Tú", 1991, "Warner Music México", 201597155),
    T("AYIKiWZtNOw", "Camilo Sesto", "Amor Mío, ¿Qué Me Has Hecho?", 1991, "Camilo Sesto", 22225725),
    T("uZtXRgB95T4", "Amanda Miguel", "Ámame Una Vez Más", 1987, "Amanda Miguel", 0),
    T("l6LjNOYvhMk", "Gloria Estefan", "Con Los Años Que Me Quedan", 1993, "Gloria Estefan", 0),
    T("Tu5tt_l_YEw", "Cristian Castro", "Nunca Voy a Olvidarte", 1993, "CristianCastroVEVO", 2498484),
    T("iK3BlAZAtPs", "Chayanne", "Completamente Enamorados", 1990, "chayanneVEVO", 65503886),
    T("QTYJkS6bTOQ", "Ricardo Montaner", "Tan Enamorados", 1986, "Ricardo Montaner", 10745759),
    T("hNDtsPMX7p0", "Franco De Vita", "Te Amo", 1988, "Franco De Vita", 28921531),
    T("jrkNik4AHTU", "Ricardo Montaner", "La Cima del Cielo", 1989, "Ricardo Montaner", 26522816),
    T("XuCd3Qj6C08", "Franco De Vita", "Un Buen Perdedor", 2006, "Franco De Vita", 0),
    T("6N2LEajhs30", "Marco Antonio Solís", "O Me Voy o Te Vas", 2001, "Marco Antonio Solís", 0),
    T("XWr_fhIBeIU", "Rocío Dúrcal", "Como Tu Mujer", 1988, "Rocío Dúrcal", 0),
    T("nYWcy7z0QmU", "Enrique Iglesias", "Enamorado Por Primera Vez", 1997, "EnriqueIglesiasVEVO", 0),
    T("0t5iCwpuD8I", "Jon Secada", "Otro Día Más Sin Verte", 1992, "Jon Secada", 0),
    T("UUWtWljM0YA", "Julio Iglesias", "Lo Mejor de Tu Vida", 1987, "Julio Iglesias", 0),
    T("QF0WLoBawSc", "José Luis Rodríguez", "Y Tú También Llorarás", 1987, "José Luis Rodríguez", 0),
    T("J_YqkxlFdgQ", "Rudy La Scala", "El Cariño Es Como Una Flor", 1990, "Rudy La Scala", 0),
    T("WPbP2GWTtBk", "Emmanuel", "Es Mi Mujer", 1986, "Emmanuel", 0),
    T("dAGMFwsinLM", "Pedro Fernández", "Mi Forma de Sentir", 1994, "Pedro Fernández", 0),
    T("Y3p9OhGjxPI", "Bronco", "Que No Me Olvide", 1990, "Bronco", 0),
    T("I-x9D4wnekI", "Los Temerarios", "Ya Me Voy Para Siempre", 1994, "Los Temerarios", 0),
    T("o5TLALYDkQk", "Isabel Pantoja", "Así Fue", 1989, "Isabel Pantoja", 0),
    T("D1kP-PJL7ww", "Ednita Nazario", "Tú Sin Mí", 1986, "Ednita Nazario", 0),
    T("AzzZgK8BJTk", "Myriam Hernández", "Huele a Peligro", 1998, "Myriam Hernández", 0),
    T("Em1dOC9uyKo", "Ednita Nazario", "Más Grande Que Grande", 1997, "Ednita Nazario", 0),
    T("dCCRVjcYZt0", "Myriam Hernández", "Te Pareces Tanto a Él", 1990, "Myriam Hernández", 0),
    T("bOrQAJM2Has", "Marisela", "Tu Dama de Hierro", 1987, "Marisela - Topic", 0),
    T("-apU2sviHCM", "Ricardo Arjona", "Historia de Taxi", 1994, "Ricardo Arjona", 0),
    T("F0rwOsAteXM", "Pablo Alborán", "Solamente Tú", 2010, "Pablo Alborán", 707900000),
    T("kMIaYXxLnUA", "Juanes", "A Dios Le Pido", 2002, "Juanes", 276235322),
    T("v0ckuv1xBm0", "Juan Luis Guerra", "Burbujas de Amor", 1990, "JuanLuisGuerraVEVO", 0),
    T("-hoZpSoKAYE", "Sin Bandera", "Entra En Mi Vida", 2001, "Sin Bandera", 316600000),
    T("8hRGBcr_gJc", "Luis Fonsi", "No Me Doy Por Vencido", 2008, "Luis Fonsi", 357600000),
    T("Hl5WPB7Xtfo", "Sin Bandera", "Suelta Mi Mano", 2003, "Sin Bandera", 261800000),
    T("8DE4H7bd0vs", "Rocío Dúrcal", "Amor Eterno", 1984, "Rocío Dúrcal", 144000000),
    T("tg7QRlINFgQ", "Sin Bandera", "Mientes Tan Bien", 2003, "Sin Bandera", 240300000),
    T("6r8mlDvfyZI", "Alejandro Fernández", "Me Hace Tanto Bien", 2010, "Alejandro Fernández", 129000000),
    T("uMrN1W4ryoE", "Chayanne", "Dejaría Todo", 1998, "chayanneVEVO", 463000000),
    T("mKOkiRJt1hs", "Juan Gabriel", "Inocente Pobre Amigo", 1980, "JuanGabrielVEVO", 3348171),
    T("pCBfCmHQw58", "Luis Miguel", "Ahora Te Puedes Marchar", 1987, "OficialLuisMiguel", 3511803),
]

HOY = [
    T("ncByymoHQRI", "Juan Luis Guerra", "Tus Besos", 2014, "JuanLuisGuerraVEVO", 49307371, True),
    T("I9cCPQVPv8o", "Ricardo Arjona, Gaby Moreno", "Fuiste Tú", 2012, "Ricardo Arjona", 1520000000, True),
    T("CJ_zRSv3Hr8", "Carlos Vives", "Volví a Nacer", 2013, "Carlos Vives", 112700000, True),
    T("07314LhFag4", "Juan Luis Guerra", "Todo Tiene Su Hora", 2015, "JuanLuisGuerraVEVO", 41904591, True),
    T("HhgxpYNZxgk", "Jesse & Joy", "¿Con Quién Se Queda El Perro?", 2012, "jesseyjoyoficial", 54100000, True),
    T("3VmoZrxXbmg", "Marc Anthony", "Flor Pálida", 2015, "Marc Anthony", 1200000000, True),
    T("KsdJEolXHQA", "Juan Luis Guerra", "Muchachita Linda", 2015, "JuanLuisGuerraVEVO", 20826614, True),
    T("ETLoTxVVvjM", "Christian Nodal", "Adiós Amor", 2017, "Christian Nodal", 1696843278, True),
    T("Z81hsLIY1sQ", "Alejandro Fernández, Christina Aguilera", "Hoy Tengo Ganas de Ti", 2013, "Alejandro Fernández", 629900000, True),
    T("2mY7AFTtYwQ", "Camilo", "Favorito", 2020, "Camilo", 0, True),
    T("jk4HYngf65w", "Romeo Santos", "Cancioncitas de Amor", 2014, "RomeoSantosVEVO", 635432039, True),
    T("WENJIxEfyaw", "Juan Luis Guerra", "La Noviecita", 2023, "JuanLuisGuerraVEVO", 7906482, True),
    T("Rir_fuLX7HM", "Carlos Rivera", "Te Esperaba", 2018, "Carlos Rivera", 446966039, True),
    T("ROzZSmaxDz8", "Prince Royce", "Las Cosas Pequeñas", 2012, "Planet Records Official", 83602948, True),
    T("C8FQ4wQXyaE", "Chayanne", "Humanos a Marte", 2014, "Chayanne", 197083426, True),
    T("gSJd_J3W6NU", "Fonseca, Juan Luis Guerra", "Si Tú Me Quieres", 2023, "Fonseca", 33500000),
    T("snFhcHHdzT0", "Reik", "Creo en Ti", 2012, "Reik", 536189390),
    T("JMq0HJXIp8o", "Juan Luis Guerra", "Corazón Enamorado", 2019, "JuanLuisGuerraVEVO", 2695434),
    T("NE3IkFadCHM", "Sebastián Yatra", "Traicionera", 2016, "Sebastián Yatra", 744100000),
    T("zHhza3EgHe8", "Juan Luis Guerra, Romeo Santos", "Frío, Frío", 2013, "JuanLuisGuerraVEVO", 383661488),
    T("CnuoXtaX8q0", "Christian Nodal", "No Te Contaron Mal", 2018, "Christian Nodal", 994703541),
    T("6fm3riUiG2c", "Juan Luis Guerra", "Privé", 2020, "JuanLuisGuerraVEVO", 15904743),
    T("5AkDqm-cEgg", "Camilo, Pedro Capó", "Tutu", 2019, "Camilo", 856800000),
    T("U1zjUFn4fHo", "Juan Luis Guerra", "Gracias", 2020, "JuanLuisGuerraVEVO", 3399937),
    T("tLcfAnN2QgY", "Enrique Iglesias, Marco Antonio Solís", "El Perdedor", 2014, "Enrique Iglesias", 1600000000),
    T("dUOC-ryYtQI", "Juan Luis Guerra", "I Love You More", 2019, "JuanLuisGuerraVEVO", 2514015),
    T("_gm5piKnrS4", "Morat", "Cómo Te Atreves", 2015, "Morat", 334951091),
    T("LNrZ_E1LOnw", "Juan Luis Guerra", "Como Me Enamora", 2023, "JuanLuisGuerraVEVO", 1918014),
    T("TMT9MNM-NHg", "Jesse & Joy", "Dueles", 2016, "jesseyjoyoficial", 680000000),
    T("wsQllPKp344", "Juan Luis Guerra", "Cositas de Amor", 2023, "JuanLuisGuerraVEVO", 1317119),
    T("jucBuAzuZ0E", "Alejandro Sanz, Marc Anthony", "Deja Que Te Bese", 2016, "Alejandro Sanz", 204800000),
    T("ApCIF4NOtec", "Juan Luis Guerra", "Me Preguntas", 2019, "JuanLuisGuerraVEVO", 1368517),
    T("N6mShTc40BU", "Carlos Rivera", "El Hubiera No Existe", 2018, "Carlos Rivera", 0),
    T("qB54Hlyb7v4", "Juan Luis Guerra", "Lámpara Pa' Mis Pies", 2019, "JuanLuisGuerraVEVO", 13627065),
    T("P2zOb0HGdxg", "Natalia Jiménez", "Creo en Mí", 2011, "Natalia Jiménez", 0),
    T("gl3Z28ygq4s", "Juan Luis Guerra, Sting", "Estrellitas y Duendes", 2025, "JuanLuisGuerraVEVO", 6064266),
    T("DXiXPhvYuNU", "Romeo Santos, Santana", "Necio", 2014, "RomeoSantosVEVO", 415826404),
    T("SRLRCCffvlA", "Juan Luis Guerra", "El Farolito", 2021, "JuanLuisGuerraVEVO", 19705271),
    T("_WHGlEYaBgU", "Jesse & Joy", "Ecos de Amor", 2015, "jesseyjoyoficial", 607100000),
    T("VoB9bx2iYGw", "Juan Luis Guerra", "Entre Mar y Palmeras", 2024, "JuanLuisGuerraVEVO", 19821405),
    T("7TWzV05kQ4w", "Reik", "Ya Me Enteré", 2016, "Reik", 0),
    T("sD9_l3oDOag", "Sebastián Yatra", "No Hay Nadie Más", 2018, "Sebastián Yatra", 0),
    T("wNrucsuePOg", "Juan Luis Guerra", "DJ Bachata", 2024, "JuanLuisGuerraVEVO", 8413356),
    T("yUAZxs3qY3Y", "Prince Royce", "Te Robaré", 2013, "PrinceRoyceVEVO", 214356819),
    T("qKp1f7Vn9dM", "Camilo", "Vida de Rico", 2020, "Camilo", 1000000000),
    T("ElU-VcWEhRU", "Romeo Santos", "You", 2011, "RomeoSantosVEVO", 236951876),
    T("VkuRIZ7QyDM", "Chayanne", "Madre Tierra (Oye)", 2015, "Chayanne", 206000000),
    T("XlmaJ-yU46U", "Aventura", "Inmortal", 2019, "RomeoSantosVEVO", 378000000),
    T("Geqmpq0tjNU", "Carlos Vives, Marc Anthony", "Cuando Nos Volvamos a Encontrar", 2014, "Carlos Vives", 0),
    T("4eCL0l9iD5A", "Romeo Santos", "Hilito", 2014, "RomeoSantosVEVO", 357479687),
    T("54cCE5q2NEE", "Jesse & Joy, Gente de Zona", "3 A.M.", 2017, "jesseyjoyoficial", 345399467),
    T("mhHqonzsuoA", "Romeo Santos", "Imitadora", 2017, "RomeoSantosVEVO", 796699405),
    T("uXUjhE9MhyU", "Pablo Alborán", "Prometo", 2017, "Pablo Alborán", 0),
    T("QBaIMZ8QjcU", "Romeo Santos, Marc Anthony", "Yo También", 2015, "RomeoSantosVEVO", 901612309),
    T("VlmZMeqoADI", "Christian Nodal", "De Los Besos Que Te Di", 2019, "Christian Nodal", 0),
    T("qjkb9_AJCLo", "Prince Royce", "Carita de Inocente", 2020, "PrinceRoyceVEVO", 81452853),
    T("ghAvJMxE1qo", "Sebastián Yatra, Reik", "Un Año", 2019, "Sebastián Yatra", 0),
    T("9PCjVwJo3EI", "Prince Royce", "Te Me Vas", 2012, "PrinceRoyceVEVO", 0),
    T("0diOZSlLKdg", "Carlos Rivera", "¿Cómo Pagarte?", 2018, "Carlos Rivera", 0),
    T("VafbNsrHnD8", "Romeo Santos", "Llévame Contigo", 2011, "RomeoSantosVEVO", 0),
    T("r0eIhlsks4s", "Jesse & Joy", "La De La Mala Suerte", 2012, "jesseyjoyoficial", 0),
    T("mLwwyCKZZdk", "Romeo Santos", "Inocente", 2011, "RomeoSantosVEVO", 0),
    T("TOgCeRQvzoY", "Kany García", "Confieso", 2019, "Kany García", 0),
    T("2p_eRTj5s5M", "Romeo Santos", "Amigo", 2014, "RomeoSantosVEVO", 0),
    T("_X3PPuF_yOE", "Río Roma", "Me Cambiaste la Vida", 2011, "Río Roma", 0),
    T("rvmtQvA_cmM", "Romeo Santos", "Sus Huellas", 2022, "RomeoSantosVEVO", 139778614),
    T("7mox58jIAdA", "Ha*Ash", "Te Dejo En Libertad", 2015, "Ha*Ash", 0),
    T("P_xKX0NBTeQ", "Eddy Herrera", "Si No Era Yo", 2014, "Eddy Herrera", 0),
    T("fw8kQxMQ6uc", "Juanes", "La Luz", 2013, "Juanes", 45549376),
    T("dyM5fHdbowM", "Eddy Herrera", "Si Yo Se Lo Pido", 2013, "Eddy Herrera", 0),
    T("nvxwiRuFgB0", "Jesse & Joy", "Me Soltaste", 2015, "jesseyjoyoficial", 0),
    T("0K6ItvTTpe8", "Miriam Cruz", "Me Enamoré De Ti", 2012, "Miriam Cruz", 0),
    T("9vr-xmePIUg", "Reik", "Voy a Olvidarte", 2011, "Reik", 0),
    T("-0eIzemjwaQ", "Miriam Cruz", "Tú No Tienes Alma", 2014, "Miriam Cruz", 0),
    T("8_GGmHkgM-8", "Sin Bandera", "En Ésta No", 2016, "Sin Bandera", 0),
    T("ridGylKQ0WY", "Jesse & Joy, Luis Fonsi", "Tanto", 2014, "jesseyjoyoficial", 0),
    T("DriCCFRQlj8", "Camilo, Evaluna Montaner", "Índigo", 2021, "Camilo", 0),
    T("weKJWqw8-3g", "Luis Fonsi, Juan Luis Guerra", "Llegaste Tú", 2014, "Luis Fonsi", 404481904),
    T("oJZeTxNUSC0", "Romeo Santos, Juan Luis Guerra", "Carmín", 2018, "RomeoSantosVEVO", 105809537),
    T("sPTn0QEhxds", "Shakira", "Me Enamoré", 2017, "Shakira", 0),
    T("OdaIbTUGmHM", "Prince Royce", "La Carretera", 2016, "PrinceRoyceVEVO", 0),
    T("mMBmpYvJe6E", "Manny Cruz", "Si Tú Me Miras", 2018, "Manny Cruz", 0),
    T("-UV0QGLmYys", "Carlos Vives, Shakira", "La Bicicleta", 2016, "Carlos Vives", 1800000000),
    T("ym2clIz5t4A", "Manny Cruz, Milly Quezada", "Llegaste", 2019, "Manny Cruz", 0),
    T("sWGJd26kUOY", "Romeo Santos, ROSALÍA", "El Pañuelo", 2022, "RomeoSantosVEVO", 54265522),
    T("Mtau4v6foHA", "Carlos Vives, Sebastián Yatra", "Robarte un Beso", 2017, "Carlos Vives", 2000000000),
    T("XEvKn-QgAY0", "Prince Royce, Shakira", "Deja Vu", 2017, "PrinceRoyceVEVO", 736017230),
    T("P2hM9CLAMu4", "Jesse & Joy", "¡Corre!", 2011, "jesseyjoyoficial", 0),
    T("8iPcqtHoR3U", "Romeo Santos", "Eres Mía", 2014, "RomeoSantosVEVO", 1338681355),
    T("Uws510cVia4", "Ha*Ash", "Lo Aprendí de Ti", 2015, "Ha*Ash", 0),
    T("QFs3PIZb3js", "Romeo Santos", "Propuesta Indecente", 2013, "RomeoSantosVEVO", 2417487182),
    T("NAG98gpC8Hw", "Ha*Ash", "Ex de Verdad", 2015, "Ha*Ash", 0),
    T("bdOXnTbyk0g", "Prince Royce", "Darte un Beso", 2013, "PrinceRoyceVEVO", 1623815546),
    T("5R1RGl4WQP8", "Mon Laferte", "Tu Falta de Querer", 2015, "Mon Laferte", 0),
    T("hpkaifThmOs", "Juan Luis Guerra", "Kitipun", 2019, "JuanLuisGuerraVEVO", 27093782),
    T("YXnjy5YlDwk", "Marc Anthony", "Vivir Mi Vida", 2013, "Marc Anthony", 1310000000),
    T("K3S96fUGrEY", "Juan Luis Guerra", "Mambo 23", 2023, "JuanLuisGuerraVEVO", 14253298),
    T("_wL3Pc-EmjA", "Ha*Ash", "Perdón, Perdón", 2015, "HaAshVEVO", 0),
    T("RksYXExb0d0", "Juan Luis Guerra", "Vale la Pena", 2021, "JuanLuisGuerraVEVO", 137388449),
    T("u7rTroCsmCY", "Ha*Ash", "No Pasa Nada", 2018, "Ha*Ash", 0),
]

def norm_artist(a):
    a = a.split(",")[0].strip().lower()
    for pref in ("juan luis guerra", "jesse & joy", "ha*ash", "prince royce", "romeo santos",
                 "carlos vives", "camilo", "reik", "sebastián yatra", "christian nodal",
                 "fernandito villalona", "sergio vargas", "josé josé", "juan gabriel",
                 "ana gabriel", "rocío dúrcal", "luis miguel", "camilo sesto",
                 "myriam hernández", "sin bandera", "eddy herrera", "manny cruz",
                 "miriam cruz"):
        if a.startswith(pref) or pref in a:
            return pref
    return a

def checks(name, tracks):
    errs = []
    if len(tracks) != 100:
        errs.append(f"{name} count {len(tracks)}")
    ids = [t["id"] for t in tracks]
    if len(ids) != len(set(ids)):
        from collections import Counter
        dups = [i for i, c in Counter(ids).items() if c > 1]
        errs.append(f"{name} dups {dups}")
    for t in tracks:
        if len(t["id"]) != 11:
            errs.append(f"bad id {t['id']}")
    for i in range(1, len(tracks)):
        if norm_artist(tracks[i]["artist"]) == norm_artist(tracks[i-1]["artist"]):
            errs.append(f"{name} consec {i}/{i+1} {tracks[i-1]['artist']} -> {tracks[i]['artist']}")
    for i, t in enumerate(tracks[:15], 1):
        if not t["intro"]:
            errs.append(f"{name} #{i} missing intro")
    for i, t in enumerate(tracks[15:], 16):
        if t["intro"]:
            errs.append(f"{name} #{i} extra intro")
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

def main():
    print("AYER", len(AYER), "HOY", len(HOY))
    errs = checks("ayer", AYER) + checks("hoy", HOY)
    for e in errs:
        print("ERR", e)
    dump("galeria", "ayer", AYER, OUT / "galeria-ayer.json")
    dump("galeria", "hoy", HOY, OUT / "galeria-hoy.json")
    ids = [t["id"] for t in AYER + HOY]
    bad = []
    for i, vid in enumerate(ids, 1):
        try:
            st = mq(vid)
            oe = oembed(vid)
            ok = st == 200 and bool(oe.get("title"))
            print(f"{i:03d} {'OK' if ok else 'FAIL'} {vid} mq={st} | {oe.get('author_name')} | {oe.get('title')}", flush=True)
            if not ok:
                bad.append(vid)
        except Exception as e:
            print(f"{i:03d} FAIL {vid} {e}", flush=True)
            bad.append(vid)
        time.sleep(0.08)
    print("BAD", bad)
    print("DONE bad", len(bad))

if __name__ == "__main__":
    main()
