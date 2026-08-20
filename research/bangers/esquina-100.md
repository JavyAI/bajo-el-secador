# Esquina 100 — old-school bangers

**Room:** En la esquina (`#colmado`)  
**Job:** street / colmado speaker. Salsa dura + merengue de fiesta.  
**Date:** 2026-08-16  
**Rule:** culture locks the pool. Views rank *inside* the pool. Views do **not** pick the first 15.

Live JSON was **not** edited.

---

## [OBJECTIVE]

Build a culturally locked top 100 for the colmado speaker, then sort that pool by official YouTube views as a resonance signal. Prove why a raw view-rank (Son by Four first) is the error Javy already rejected.

Test for the authored 15: *would a Dominican on the esquina say wow in the first 15 seconds?*

---

## Method

1. Lock the pool: salsa dura + merengue de fiesta, mostly pre-2012. Not 2024 dembow. Not silla bachata. Not secador balada.
2. Required names stay: JLG merengue/fiesta (A Pedir Su Mano, Bilirrubina, El Costo, Ojalá), Lavoe, Celia, Gran Combo, Willie (Gran Varón = story, not shout), Blades, Joe Arroyo *Rebelión*, Wilfrido, Hermanos Rosario, Frankie Ruiz, Oscar D'León, Cuco Valoy *Juliana*, Sergio Vargas. Yiyo and Chiquito **after** the opener.
3. Hard-ban as opener / top of list: Son by Four *A Puro Dolor*; Niche *Cali Pachanguero* (pride of Cali); a third JLG bachata as closer (*Burbujas*, *Bachata Rosa*).
4. Attach official YouTube ids (artist / VEVO / Fania / Karen / Codiscos / Fuentes / Topic). When the live-catalog clip undercounts the same official song, rank on the stronger official id and keep the catalog id noted.
5. Sort the locked pool by that view count. Hand-flag story songs, salsa sensual, and after-opener artists.
6. List the 10 high-view tracks a naive sort would promote — including Son by Four as the cautionary tale.

---

## [DATA]

- Live catalog `public/colmado.json`: **86** tracks, `introCount` 15.
- Cultural top 100: **82** live tracks kept + **18** official additions. **4** live tracks moved to rejects (Son by Four, Cali Pachanguero, Bachata Rosa, Burbujas).
- View scrape: YouTube watch pages, 2026-08-16, `viewCount` from official ids. n = 86 catalog + 60 extra/alt/reject ids. **0** missing on the ranked 100.
- Genre after lock: salsa 60 / merengue 40.
- Era: 95/100 pre-2012. The five post-2011 cuts are Yiyo ×3 + Chiquito ×2, all flagged AFTER opener.

[STAT:n] n = 100 ranked tracks  
[STAT:n] official view scrapes on ranked set = 100 (0 missing)

---

## Cultural lock (before any sort)

| In | Out |
|---|---|
| Salsa dura + salsa the corner actually dances | Son by Four as opener |
| Merengue de fiesta (Wilfrido, Rosario, Ventura, Fernandito, Sergio, JLG merengue) | Cali pride salsa as opener / top |
| Joe Arroyo *Rebelión* (Colombian, claimed) | Third JLG bachata as closer |
| Cuco *Juliana* (Dominican salsa receipt) | 2024 dembow / El Alfa |
| Yiyo + Chiquito after the authored 15 | Silla bachata (Aventura, Romeo, Antony) |
| Gran Varón / Pedro Navaja as **story**, not shout | Secador baladas |
| Official / Topic / label ids only | Lyrics rips, karaoke, DJ mixes |

JLG bachata (*Bachata Rosa*, *Burbujas*) can live in Silla. On this speaker they are breathers at best, never the closer.

---

## Authored first 15 — feeling, not views

Live order after the already-applied swaps (Bilirrubina, Juliana, El Costo). `#1` stays A Pedir Su Mano.

| # | Artist | Title | Catalog id | Official views | View-rank in the 100 | Verdict |
|---|---|---|---|---:|---:|---|
| 1 | Juan Luis Guerra | A Pedir Su Mano | `_koz_f4mthE` | 15.4M | view-rank **51** | **KEEP** |
| 2 | Hector Lavoe | El Cantante | `BNo0vkEYWRc` | 101.0M | view-rank **17** | **KEEP** |
| 3 | Elvis Crespo | Suavemente | `WPiEbYSF9kE` | 299.4M | view-rank **4** | **KEEP** |
| 4 | Celia Cruz | La Vida Es Un Carnaval | `AFYJ5axf02o` | 72.6M | view-rank **24** | **KEEP** |
| 5 | Willie Colon | El Gran Varon | `US0GbUpQ9VU` | 73.3M | view-rank **23** | **FLAG** |
| 6 | El Gran Combo | Me Libere | `frsVQWSINAI` | 39.2M | view-rank **35** | **KEEP** |
| 7 | Ruben Blades | Pedro Navaja | `k62zZBeevWQ` | 36.6M | view-rank **38** | **FLAG** |
| 8 | Juan Luis Guerra | La Bilirrubina | `McV4pBRb-Sg` | 53.7M | view-rank **31** | **KEEP** |
| 9 | Joe Arroyo | Rebelion | `oWBf9hfW_4Y` | 33.2M | view-rank **43** | **KEEP** |
| 10 | Wilfrido Vargas | El Africano | `1DbXzlhKS5s` | 5.3M | view-rank **68** | **KEEP** |
| 11 | Los Hermanos Rosario | La Dueña del Swing | `rOw9UxJyhII` | 158.4M | view-rank **10** | **KEEP** |
| 12 | Frankie Ruiz | Desnudate Mujer | `H5gxKL5pmI4` | 4.5M | view-rank **72** | **FLAG** |
| 13 | Oscar D'Leon | Lloraras | `gxlB1B9emDc` | 157.9M | view-rank **11** | **KEEP** |
| 14 | Cuco Valoy | Juliana | `y08MAPIACBY` | 4.4M | view-rank **74** | **KEEP** |
| 15 | Juan Luis Guerra | El Costo de La Vida | `tPTB0TRV3BA` | 6.1M | view-rank **64** | **KEEP** |

**3 of 15** authored openers sit inside the view top 15.

[FINDING] Views inside the locked pool still do not reconstruct the authored 15.
[STAT:n] overlap = 3/15 = 20%
[STAT:n] A Pedir Su Mano view-rank = 51 of 100
[STAT:effect_size] A Pedir Su Mano views = 15.4M vs pool median 15.5M (ratio 1.00)

Yiyo *Manos de Tijera* is view-rank **3** (357.2M). That is why the brief says AFTER opener. A view-sort of the *correct* pool would still open like a 2010s salsa-romántica radio, not a colmado doorway.

---

## What a naive view-rank would have done

| If you sort… | #1 | Why it is wrong |
|---|---|---|
| All Latin YouTube | Despacito 9.10B | Not a room |
| Tropical + salsa tags | Son by Four *A Puro Dolor* **746.6M** | The pass Javy already killed |
| Locked pool, no after-opener flag | Marc Anthony *Valió la Pena* 410M / Jerry *Qué Hay de Malo* 406M / **Yiyo 357M** | Romántica + Yiyo, not the doorway |
| Locked + authored 15 | **JLG A Pedir Su Mano** 15.4M | Correct. Views only pick the official clip. |

[FINDING] Son by Four official views are **48.5×** the correct opener.
[STAT:effect_size] 746.6M / 15.4M = 48.5 (log10 = 1.69)
[STAT:n] two official clips, same scrape window
[STAT:ci] not a sample CI — this is a ratio of two observed view counts

That ratio is the whole product lesson: **views sort the pool after the lock. They do not pick the door.**

---

## Top 100 — views inside the lock

Best official id for ranking. Catalog id kept in the JSON dump when it differs (Dueña, Pedro Navaja, Brujería, Cachamba, Fuego en el 23).

| Rank | Artist | Title | Era | Genre | Official id | Views | Verdict | Note |
|---:|---|---|---:|---|---|---:|---|---|
| 1 | Marc Anthony | Valio La Pena (Salsa) | 2004 | salsa | `Ns9YYSqLxyI` | 410.1M | **KEEP** | 2004 salsa version. Not Vivir Mi Vida. Old-school-adjacent Marc. |
| 2 | Jerry Rivera | Que Hay de Malo | 1992 | salsa | `SUgQHe902yQ` | 405.5M | **KEEP** | Jerry romántica megahit. After opener, not first 15 unless walked. |
| 3 | Yiyo Sarante | Manos de Tijera | 2015 | salsa | `ExCIp6TOnJw` | 357.2M | **FLAG** | AFTER opener. Views would put this #3. Do not open. |
| 4 | Elvis Crespo | Suavemente | 1998 | merengue | `WPiEbYSF9kE` | 299.4M | **KEEP** | Merengue bomb. National reflex. |
| 5 | Tito Nieves | Fabricando Fantasias | 2004 | salsa | `s3fcKFQukbY` | 296.9M | **KEEP** | Salsa romántica megahit. Outdoor dance, not opener. |
| 6 | Luis Enrique | Yo No Sé Mañana | 2009 | salsa | `2PVi95J-FMo` | 292.4M | **KEEP** | Salsa romántica 2009. Pre-2012 lock. Not an opener. |
| 7 | Gilberto Santa Rosa | Conciencia | 1990 | salsa | `7kbjKCj-rMQ` | 258.3M | **KEEP** | Santa Rosa romántica. Official video. After opener. |
| 8 | Rey Ruiz | Mi Media Mitad | 1992 | salsa | `wQUcaSEuob0` | 237.5M | **KEEP** | Salsa romántica the corner knows. |
| 9 | Celia Cruz | La Negra Tiene Tumbao | 2001 | salsa | `imeXSRNRMeg` | 169.5M | **KEEP** | Dancing Celia. Stronger sidewalk than Carnaval for some. |
| 10 | Los Hermanos Rosario | La Dueña del Swing | 1995 | merengue | `HN6ACmknaiw` | 158.4M | **KEEP** | Dominican merengue royalty. Rank on Topic official. Topic official 158M; catalog clip 1.66M |
| 11 | Oscar D'Leon | Lloraras | 1975 | salsa | `gxlB1B9emDc` | 157.9M | **KEEP** | Sonero the island adopted. Colmado singalong. |
| 12 | Gilberto Santa Rosa | Que Alguien Me Diga | 1999 | salsa | `0ZfwT6lHahk` | 149.6M | **KEEP** | Santa Rosa romántica. High views, later in mix. |
| 13 | Frankie Ruiz | Deseandote | 1989 | salsa | `N8kGeGXddxg` | 136.0M | **KEEP** | Frankie the corner actually streams. Better than Desnúdate for wow. |
| 14 | Yiyo Sarante | Que Agonia | 2015 | salsa | `eHsR140M2no` | 117.8M | **FLAG** | AFTER opener. Second Yiyo. |
| 15 | Willie Colon y Hector Lavoe | El Dia de Mi Suerte | 1973 | salsa | `mXZRB_al3fs` | 113.3M | **KEEP** | Lavoe/Willie body-move alternative to Gran Varón. |
| 16 | Fruko y sus Tesos | El Preso | 1975 | salsa | `FN5oLBXiNvM` | 109.4M | **KEEP** | Colombian salsa Dominicans claimed, same family as Rebelión. |
| 17 | Hector Lavoe | El Cantante | 1978 | salsa | `BNo0vkEYWRc` | 101.0M | **KEEP** | Fania prayer. First piano/horn is the corner. |
| 18 | Eddy Herrera | Tu Eres Ajena | 1997 | merengue | `uzU3x_egiEk` | 99.5M | **KEEP** | Merengue de fiesta of a bachata. Esquina hips, not silla guitar. |
| 19 | Bonny Cepeda | Una Fotografia | 1985 | merengue | `1crMUfqH6i0` | 90.9M | **KEEP** | Classic merengue de fiesta. |
| 20 | Yiyo Sarante | Mi Todo | 2016 | salsa | `JXLNr85yoKk` | 87.5M | **FLAG** | AFTER opener. Third Yiyo. |
| 21 | Grupo Niche | Una Aventura | 1984 | salsa | `UwnmzIgNzyU` | 76.9M | **KEEP** | The Niche Dominicans request. Not Cali pride. |
| 22 | Jerry Rivera | Amores Como el Nuestro | 1992 | salsa | `sJqDmVekMWU` | 74.8M | **KEEP** | Jerry romántica. Outdoor dance. |
| 23 | Willie Colon | El Gran Varon | 1989 | salsa | `US0GbUpQ9VU` | 73.3M | **FLAG** | Story not shout. Masterpiece; first 15s go quiet. |
| 24 | Celia Cruz | La Vida Es Un Carnaval | 1999 | salsa | `AFYJ5axf02o` | 72.6M | **KEEP** | Celia that raises a Presidente. Stadium-adjacent but wow is real. |
| 25 | Chiquito Team Band | La Llamada De Mi Ex | 2015 | merengue | `u6Q5Lu0Sq3g` | 70.5M | **FLAG** | AFTER opener. Do not bury at tail; do not open. |
| 26 | Ruben Blades | Decisiones | 1984 | salsa | `GyhwmZAQB-Y` | 63.2M | **KEEP** | Blades. More body than Pedro Navaja. |
| 27 | Juan Luis Guerra | El Niagara en Bicicleta (Live) | 1998 | merengue | `xhpJqdZgF5U` | 62.2M | **KEEP** | JLG merengue/fiesta. Best official is VEVO live 62M. |
| 28 | El Gran Combo | Brujeria | 1970 | salsa | `0xT7maXs-UU` | 58.9M | **KEEP** | Combo. Rank on Topic official. Combo Topic 58.9M; catalog clip 8.0M |
| 29 | El Gran Combo | Ojos Chinos | 1970 | salsa | `hLKwsJHspCw` | 58.2M | **KEEP** | Combo classic. High official views. |
| 30 | Hector Lavoe | Periodico de Ayer | 1976 | salsa | `qYkpURie5cU` | 53.8M | **KEEP** | First seconds already hurt and swing. |
| 31 | Juan Luis Guerra | La Bilirrubina | 1990 | merengue | `McV4pBRb-Sg` | 53.7M | **KEEP** | JLG merengue that moves the block. |
| 32 | La India | Ese Hombre | 1994 | salsa | `B3R-0yOXrGY` | 52.1M | **KEEP** | La India. Salsa the corner shouts. |
| 33 | El Gran Combo | Un Verano en Nueva York | 1975 | salsa | `HBkZRS8gTdg` | 46.2M | **KEEP** | Combo classic. Diaspora lock. |
| 34 | Victor Manuelle | He Tratado | 1996 | salsa | `7wpVJvRIKYQ` | 43.8M | **KEEP** | Victor Manuelle romántica. |
| 35 | El Gran Combo | Me Libere | 1988 | salsa | `frsVQWSINAI` | 39.2M | **KEEP** | Combo anthem. Piano tumbao = wow. |
| 36 | Joe Arroyo | En Barranquilla Me Quedo | 1988 | salsa | `j8ElCh65bzk` | 39.1M | **KEEP** | Joe Arroyo. Claimed like Rebelión. |
| 37 | Willie Colon y Hector Lavoe | Juanito Alimana | 1983 | salsa | `xaJUMcmTFpE` | 36.7M | **KEEP** | Salsa dura story with a shout. Fania official lyrics. |
| 38 | Ruben Blades | Pedro Navaja | 1978 | salsa | `ERVhkEtdrPY` | 36.6M | **FLAG** | Story not shout. Walking-bass first 15s. Willie official 36.6M; catalog clip 5.4M |
| 39 | Juan Luis Guerra | Ojala que Llueva Cafe | 1989 | merengue | `dDEVFQnBTp0` | 36.0M | **KEEP** | JLG merengue/fiesta. National body memory. |
| 40 | Joe Arroyo | La Noche | 1988 | salsa | `ISvXRDB8iwE` | 35.2M | **KEEP** | Joe Arroyo. Claimed. |
| 41 | Sergio Vargas | La Quiero a Morir | 1990 | merengue | `Jn1OIkMqpbo` | 34.2M | **KEEP** | Sergio merengue. Second Sergio after Ventanita. |
| 42 | El Gran Combo | Y No Hago Mas Na | 1983 | salsa | `bgSpdgL9lkQ` | 33.6M | **KEEP** | Combo dura missing from live JSON. Official Topic. |
| 43 | Joe Arroyo | Rebelion | 1986 | salsa | `oWBf9hfW_4Y` | 33.2M | **KEEP** | Colombian salsa Dominicans claimed. Instant wow. |
| 44 | Grupo Niche | Gotas de Lluvia | 1989 | salsa | `pE6HUa6Q3b8` | 31.6M | **KEEP** | Niche that is not Cali pride. |
| 45 | Cheo Feliciano | Anacaona | 1971 | salsa | `OvQArMzHt90` | 28.6M | **KEEP** | Cheo. Older blood. |
| 46 | Grupo Mania | Linda Eh | 1996 | merengue | `dElUL4hvbJE` | 21.9M | **KEEP** | Merengue de fiesta. Official Topic 21.9M. |
| 47 | Ismael Rivera | El Nazareno | 1973 | salsa | `fDj-CSQDbsY` | 21.1M | **KEEP** | Ismael. Older blood inside the salsa. |
| 48 | Hector Lavoe | Todo Tiene Su Final | 1974 | salsa | `uTXP8VB52-I` | 20.6M | **KEEP** | Lavoe. Body + story. |
| 49 | Chiquito Team Band | Lejos De Ti | 2016 | merengue | `8820jXsE4kQ` | 16.9M | **FLAG** | AFTER opener. Second Chiquito. |
| 50 | Bonny Cepeda | La Asesina | 1985 | merengue | `V1jnol6o1kQ` | 15.5M | **KEEP** | Bonny merengue de fiesta. |
| 51 | Juan Luis Guerra | A Pedir Su Mano | 1990 | merengue | `_koz_f4mthE` | 15.4M | **KEEP** | JLG merengue/fiesta. Correct opener. Do not bury under views. |
| 52 | Celia Cruz | Quimbara | 1974 | salsa | `MAq9y0bxTX0` | 14.2M | **KEEP** | Dancing Celia. Catalog notes preferred this over Carnaval. |
| 53 | Wilfrido Vargas | El Baile del Perrito | 1993 | merengue | `fs1Fg07CsQs` | 13.7M | **KEEP** | Wilfrido fiesta. Colmado speaker classic. |
| 54 | Willie Colon | Idilio | 1993 | salsa | `pXPVxwaXtV0` | 13.3M | **KEEP** | Willie romántica the corner knows. |
| 55 | Wilfrido Vargas | El Jardinero | 1984 | merengue | `epndigKqzDs` | 12.1M | **KEEP** | Wilfrido merengue de fiesta. |
| 56 | Fulanito | Guallando | 1997 | merengue | `x6Y3EFLtnFM` | 11.2M | **KEEP** | Merenhouse 90s. Marquesina overlap OK. |
| 57 | Rubby Perez | Volvere | 1990 | merengue | `8QFzVz8whgQ` | 11.1M | **KEEP** | Rubby merengue de fiesta. |
| 58 | Willie Colon | Che Che Cole | 1969 | salsa | `-X92muXeN-s` | 9.0M | **KEEP** | Che Che Colé. Early Willie/Lavoe shout. |
| 59 | Ismael Rivera | Las Tumbas | 1973 | salsa | `ptb09sCuMTo` | 8.1M | **KEEP** | Ismael. Older blood. |
| 60 | Sergio Vargas | La Ventanita | 1994 | merengue | `95Wcl9ucitM` | 8.1M | **KEEP** | Sergio. Merengue the block owns. |
| 61 | Bonny Cepeda | Ay Doctor | 1985 | merengue | `cg7pyBPSEwE` | 6.6M | **KEEP** | Bonny official Topic. Cleaner ID than some Fotografía rips. |
| 62 | Johnny Ventura | Patacon Pisao | 1985 | merengue | `zN138OU1qws` | 6.2M | **KEEP** | Official Topic. Do not use unofficial lyrics rips. |
| 63 | Lalo Rodriguez | Ven Devorame Otra Vez | 1987 | salsa | `e494zPaEc6A` | 6.2M | **KEEP** | Lalo romántica. Bedroom-leaning; still outdoor dance. |
| 64 | Juan Luis Guerra | El Costo de La Vida | 1992 | merengue | `tPTB0TRV3BA` | 6.1M | **KEEP** | JLG merengue/fiesta that talks on the esquina. |
| 65 | Los Hermanos Rosario | Ella Se Fue | 1990 | merengue | `lvfQWpvcE30` | 6.0M | **KEEP** | Hermanos Rosario. |
| 66 | Willie Colon y Hector Lavoe | Aguanile | 1972 | salsa | `5BPYFIWNehg` | 5.8M | **KEEP** | Salsa dura. Fania official. Official clip undercounts the song. |
| 67 | Jossie Esteban y la Patrulla 15 | El Cantinero | 1987 | merengue | `hwv_-V5LsHk` | 5.5M | **KEEP** | Merengue de fiesta. Doorway speaker. |
| 68 | Wilfrido Vargas | El Africano | 1983 | merengue | `1DbXzlhKS5s` | 5.3M | **KEEP** | THE merengue de fiesta. Official clip undercounts the song. |
| 69 | Kinito Mendez | El Baile del Sua Sua | 1997 | merengue | `vtizic9NnfY` | 5.1M | **KEEP** | Kinito fiesta. |
| 70 | Ramon Orlando | El Venao | 1993 | merengue | `_u2m43WXQks` | 4.8M | **KEEP** | Merengue de fiesta the block owns. |
| 71 | Toño Rosario | Kulikitaka | 2003 | merengue | `ssOtmdQatGQ` | 4.7M | **KEEP** | Fiesta merengue. Later than 1988 plate; real speakers play it. |
| 72 | Frankie Ruiz | Desnudate Mujer | 1988 | salsa | `H5gxKL5pmI4` | 4.5M | **FLAG** | Salsa sensual. Bedroom grin, not esquina shout. |
| 73 | Tito Rojas | Sensual | 1992 | salsa | `Rh2YCjhZnYk` | 4.4M | **KEEP** | Tito Rojas romántica. |
| 74 | Cuco Valoy | Juliana | 1983 | salsa | `y08MAPIACBY` | 4.4M | **KEEP** | Dominican salsa receipt. Not the DLG cover. |
| 75 | Fernando Villalona | Tabaco y Ron | 1983 | merengue | `xaKLn_z9R_k` | 3.7M | **KEEP** | Fernandito colmado merengue. Sister to Cama y Mesa. |
| 76 | Willie Colon | Oh Que Sera | 1993 | salsa | `DJfU0ZfFidY` | 3.6M | **KEEP** | Willie. Outdoor salsa. |
| 77 | Elvis Crespo | Tu Sonrisa | 1998 | merengue | `yy52Zkzm4pY` | 3.2M | **KEEP** | Elvis. Second merengue after Suavemente. |
| 78 | Los Hermanos Rosario | Dominicana | 1990 | merengue | `ydz-OjoIyuo` | 3.1M | **KEEP** | Hermanos Rosario. Dominican lock. |
| 79 | Ilegales | La Morena | 1995 | merengue | `BT8Afk8HDxY` | 3.0M | **KEEP** | Merenhouse 90s. Marquesina overlap OK. |
| 80 | Kinito Mendez | Cachamba | 1996 | merengue | `XtQ6QxGF0PM` | 3.0M | **KEEP** | Cachamba. Rank on JN official. JN lyric video 3.03M; catalog clip 1.02M |
| 81 | Sonora Poncena | Fuego en el 23 | 1972 | salsa | `jqg5n6TtO-U` | 2.8M | **KEEP** | Ponceña dura. Rank on Fania official. Fania official 2.76M; catalog clip 1.02M |
| 82 | Johnny Ventura | El Sueno | 1974 | merengue | `uWIl86jzQqc` | 2.7M | **KEEP** | Johnny. Door-opener merengue family. |
| 83 | Gisselle y Sergio Vargas | Perdoname, Olvidalo | 1997 | merengue | `uwQ-2yfnuRU` | 2.5M | **KEEP** | Sergio/Gisselle merengue duet. |
| 84 | Grupo Mania | A Que Te Pego Mi Mania | 1996 | merengue | `m29uPaJ0Deo` | 2.5M | **KEEP** | Grupo Manía merengue de fiesta. |
| 85 | Wilfrido Vargas | Abusadora | 1981 | merengue | `bntQQjEnbPA` | 2.3M | **KEEP** | Wilfrido merengue de fiesta. |
| 86 | Marc Anthony | Hasta Ayer | 1997 | salsa | `bibVirPrCD4` | 2.0M | **KEEP** | Marc salsa period. Official clip undercounts. |
| 87 | Hector Lavoe | Mi Gente | 1974 | salsa | `af9gVqE9-E8` | 2.0M | **KEEP** | Mi Gente. Official clip undercounts; song is a shout. |
| 88 | Marc Anthony | Y Hubo Alguien | 1997 | salsa | `zLu1z5Cg59w` | 1.8M | **KEEP** | Marc salsa period. Official clip undercounts the song. |
| 89 | Eddie Santiago | Tu Me Quemas | 1986 | salsa | `tvX9xwHCPmg` | 1.6M | **KEEP** | Eddie romántica. Official clip undercounts. |
| 90 | Kinito Mendez | El Asilo | 1998 | merengue | `HOrPwEZLhD4` | 1.6M | **KEEP** | Kinito fiesta. |
| 91 | Frankie Ruiz | Mi Libertad | 1992 | salsa | `-VuPAychkn8` | 1.4M | **KEEP** | Frankie freedom anthem. More corner than mattress. |
| 92 | Eddie Santiago | Que Locura Enamorarme de Ti | 1988 | salsa | `fJ_Rsda2chU` | 1.4M | **KEEP** | Eddie romántica. Official clip undercounts. |
| 93 | Frankie Ruiz | La Cura | 1989 | salsa | `PmXJKVjhbqI` | 1.3M | **KEEP** | The Frankie people shout. Better 15s than Desnúdate. |
| 94 | Eddy Herrera | Me Sabe A Poco | 1997 | merengue | `zZTo7FYn0lI` | 1.3M | **KEEP** | Eddy Herrera merengue. |
| 95 | Eddie Santiago | Lluvia | 1988 | salsa | `KFhdezcPhGA` | 1.2M | **KEEP** | Eddie romántica. Official clip undercounts. |
| 96 | Willie Colon | El Malo | 1967 | salsa | `KP_TJdAiGLE` | 995.5K | **KEEP** | Willie origin myth. Official clip undercounts. |
| 97 | Fernandito Villalona | Cama y Mesa | 1983 | merengue | `E0f3J0z2SBQ` | 883.6K | **KEEP** | Fernandito colmado merengue. Official clip undercounts. |
| 98 | Oscar D'Leon | Detalles | 1986 | salsa | `1yvoPyqaOCA` | 864.8K | **KEEP** | Oscar. Official clip undercounts. |
| 99 | Las Chicas del Can | El Negro No Puede | 1987 | merengue | `yGvStabyqIE` | 473.8K | **KEEP** | Merengue de fiesta. Official clip undercounts. |
| 100 | Richie Ray | Sonido Bestial | 1971 | salsa | `s_U6G68NYec` | 246.9K | **KEEP** | Richie Ray. Salsa dura monument. Official clip tiny. |

[FINDING] Median official views in the locked 100 are 15.5M (bootstrap 95% CI 7.4M–34.7M).
[STAT:ci] 95% bootstrap CI of the median, 2000 resamples: [7.4M, 34.7M]
[STAT:n] n = 100
[STAT:effect_size] IQR = 3.6M–68.6M; mean 56.3M (right-skewed by romántica megahits)

[FINDING] Pool is salsa-majority, merengue-strong — a pillar mix, not a token merengue plate.
[STAT:n] salsa 60 / merengue 40 (salsa 60%)
[STAT:n] pre-2012 = 95/100

---

## Ten high-view rejects

Include Son by Four as the cautionary tale. These are tracks a view-first pass would promote into this room.

| # | Artist | Title | Era | Official id | Views | Why out |
|---|---|---|---:|---|---:|---|
| R1 | Luis Fonsi ft. Daddy Yankee | Despacito | 2017 | `kJQP7kiw5Fk` | 9.10B | Global pop. Views without a room. Not salsa dura, not merengue de fiesta. |
| R2 | Romeo Santos | Propuesta Indecente | 2013 | `QFs3PIZb3js` | 2.42B | Silla / headphones bachata-pop. Wrong chair. |
| R3 | Marc Anthony | Vivir Mi Vida | 2013 | `YXnjy5YlDwk` | 1.31B | 2013 pop-salsa TV. Colmado notes already banned it. Valió la Pena (2004 salsa) is the Marc that stays. |
| R4 | Son by Four | A Puro Dolor | 2000 | `kAKVT1HWNsg` | 746.6M | CAUTIONARY TALE. Javy already rejected a view-rank pass that put this first. Salsa-romántica ballad. 747M official views would win any naive sort. Hard-ban as opener / top of list. |
| R5 | El Alfa x CJ x El Cherry Scom | La Mama de la Mama | 2021 | `s5yRZOQ3EWI` | 246.5M | 2021 dembow. A different street. HOY rail if anywhere. |
| R6 | Daddy Yankee | Gasolina | 2004 | `CCF1_jI8Prk` | 167.5M | Reggaeton monument. Not colmado salsa/merengue. |
| R7 | Grupo Niche | Cali Pachanguero | 1984 | `7KxkMLAZlzw` | 124.7M | Pride of Cali. Official Codiscos 125M. Dominicans know it from salsa night; first lyric is still Cali. Hard-ban as opener / top. Una Aventura / Gotas stay. |
| R8 | Juan Luis Guerra | Burbujas de Amor | 1990 | `G6fJreMyIks` | 76.0M | Third JLG bachata as closer. Silla-coded slow dance. Best official 76M. Hard-ban as closer. Already lives in Silla. |
| R9 | Aventura | Obsesion | 2002 | `SEjw5rdyvVg` | 74.7M | Silla opener. Not esquina salsa/merengue. Cross-room leakage. |
| R10 | Juan Luis Guerra | Bachata Rosa | 1990 | `2LiZyAIVmbs` | 47.1M | JLG bachata, pretty radio, not esquina shout. Swapped out of the live 15 for Bilirrubina. Not a closer. |

Also close, not tabled: Buena Vista *Chan Chan* official HD `tGbRZ73NvlY` (61.9M) — tourist son. Raulín *Medicina de Amor* (46.0M) and Luis Vargas *Ceniza Fría* (18.0M) — silla típica.

[FINDING] The cautionary tale still has **746.6M** official views — more than every track in the locked 100 (next is Valió la Pena at 410.1M).
[STAT:n] 10 rejects scraped
[STAT:effect_size] Son by Four / pool median = 48×; Son by Four / #1-in-pool = 1.82×

---

## Flags to walk with Javy (do not auto-edit JSON)

**Story, not shout** — keep in the 100, do not treat as doorway bombs:

- Willie Colón — *El Gran Varón* (view-rank 23)
- Rubén Blades — *Pedro Navaja* (view-rank 38)

**Salsa sensual** — Frankie *Desnúdate Mujer*. If the 15 needs a Frankie shout, *La Cura* / *Mi Libertad* / *Deseándote* hit harder.

**After opener, not inside the 15:**

| Artist | Title | View-rank | Views |
|---|---|---:|---:|
| Yiyo Sarante | Manos de Tijera | 3 | 357.2M |
| Yiyo Sarante | Que Agonia | 14 | 117.8M |
| Yiyo Sarante | Mi Todo | 20 | 87.5M |
| Chiquito Team Band | La Llamada De Mi Ex | 25 | 70.5M |
| Chiquito Team Band | Lejos De Ti | 49 | 16.9M |

Live JSON already has them after the 15 (Yiyo 16/22/25, Chiquito 26/27). Keep that. Do not promote. Do not bury Chiquito at the tail again.

**Official clip undercounts** (song is bigger than the live id): Dueña del Swing, Pedro Navaja, Brujería, El Africano, Juliana, Cama y Mesa, Mi Gente, Quimbara, El Negro No Puede. Rank used the stronger official id when one was verified.

---

## 18 additions (not in live JSON)

Research only. Do not write these into `public/colmado.json` in this pass.

Valió la Pena (salsa 2004), Qué Hay de Malo, Conciencia, Deseándote, El Preso, Tú Eres Ajena (Eddy merengue), El Niágara (JLG merengue), Juanito Alimaña, La Quiero a Morir, Y No Hago Más Na, Linda Eh, El Baile del Perrito, Volveré, Ay Doctor, Patacón Pisao, Aguanile, El Cantinero, Tabaco y Ron.

Honorable, not in the 100: JLG *La Cosquillita* Topic `rBlmzy2gINk` (4.6M, típico accordion = silla-adjacent), *Calle Luna Calle Sol* Fania `Phy-i5oPJJ0` (4.1M), Pochy *La Peliona* (2.3M), Elvis *Píntame* live (2.7M).

---

## [LIMITATION]

- YouTube view counts are a resonance signal, not listenership on a Dominican sidewalk. Official Topic vs video vs live can differ by 10–100× for the same song (Dueña del Swing 1.66M catalog vs 158M Topic).
- Some Fania-era monuments (Sonido Bestial 0.25M, El Malo 1.0M, Mi Gente 2.0M on the catalog clip) are culturally heavier than their official upload. Views underrate salsa dura that lived on vinyl and radio.
- Yiyo / Chiquito are post-2012. They stay in the 100 because the brief placed them after the opener, not because they are 1988-plate music.
- Salsa romántica megahits (Valió la Pena, Qué Hay de Malo, Fabricando Fantasías, Yo No Sé Mañana) pass the genre lock and fail the doorway test. They belong in the 100, not the first 15.
- Joe Arroyo *Rebelión* catalog id `oWBf9hfW_4Y` (33.2M) is not the Discos Fuentes video (`W8PTWqE2SVw` is only 0.65M). Other unofficial Rebelión uploads are larger and were ignored.
- Scrape date 2026-08-16. Counts move. Channels replace Topic uploads.
- Bootstrap CI is for the *median of this 100*, not for a super-population of all salsa/merengue.
- This file does not rewrite live JSON.

---

## Figures

- `.omc/scientist/figures/esquina-view-rank-trap.png`
- `.omc/scientist/figures/esquina-authored15-vs-views.png`
- `.omc/scientist/figures/esquina-100-mix.png`
- `.omc/scientist/figures/esquina-10-rejects.png`

## Data

- `.omc/scientist/data/esquina-100-ranked.json`
- `.omc/scientist/data/colmado-views.json`
- `.omc/scientist/data/extra-views.json`
- `.omc/scientist/data/extra-views-2.json`
