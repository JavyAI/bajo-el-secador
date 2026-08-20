# Fiesta en la marquesina — sourced genre-lock verify

**Date:** 2026-08-16  
**Room:** `#marquesina` — family lot, 15s, carport night  
**Job:** verify the four Marquesina genre rules against official / scholarly / catalog sources. Culture still locks the pool. Views do not pick #1.  
**Live JSON:** not edited. `public/marquesina.json` was not opened for write.

Local locks read first:

- [`GENRE-LOCK.md`](../GENRE-LOCK.md) — Marquesina AYER IN = merengue de fiesta + merenhouse 90s–00s. HOY IN = Chiquito, Manny Cruz remakes, JLG 2019 merengue. OUT = salsa monuments, dryer-cry as the spine, dembow, 90s *Suavemente* padding, Yiyo salsa as the house band. Temperature: *hips + cousins. Not the street. Not the dryer.*
- [`marquesina-ayer-hoy.md`](../marquesina-ayer-hoy.md) — AYER first 15; HOY first 15; *Dueña* stays #1; *El Tiburón* is the missing merenhouse hole; Chiquito is the HOY house band.
- [`ERA-LOCK.md`](../ERA-LOCK.md) — AYER through ~2010. HOY = ~2011–now. Marquesina HOY job: “Chiquito, Manny Cruz remakes, JLG 2019. No 90s padding.”
- [`RESEARCH-SPEC.md`](../RESEARCH-SPEC.md) — Marquesina pool = merengue de fiesta, merenhouse, 90s–00s. Ban = salsa monuments (*Pedro Navaja*); dominó (that’s Esquina); club 2024 dembow.

Firecrawl MCP (`firecrawl_search`) hit the anonymous daily network limit on this pass (`try again in ~84760s`). Fallback was Tavily advanced search / extract plus official page fetches (Wikipedia, UNESCO, ASALE, Diario Libre, AllMusic, Discogs, Dominican Music USA, Billboard, Rolling Stone). Do not treat this file as a Firecrawl-complete crawl. Rerun inputs are at the bottom.

---

## Verdict

| # | Lock claim | Verdict | Confidence |
|---|---|---|---|
| 1 | Marquesina / carport / 15s party = merengue de fiesta + merenhouse (90s–00s) | **HOLD**, with two wording nuances | High on merenhouse + dance merengue as quince / family-lot audio. Medium on the phrase *merengue de fiesta* as a published genre name. |
| 2 | Distinct from colmado street and from dryer | **HOLD** as a product-room split | High that the three *places* are different. Medium that any ethnographic source uses those three names as a music taxonomy. |
| 3 | Proyecto Uno / Ilegales / Fulanito = merenhouse | **HOLD** | High |
| 4 | Chiquito / Manny Cruz remakes = HOY merengue | **SPLIT** | High on Manny remakes as 2020s merengue revival. **Chiquito is salsa**, not merengue. Same label correction as Esquina verify. |

No lock rewrite in this file. No JSON write.

**Do not ship from this pass:** Chiquito as a merengue house band without a second Javy walk. *Kitipun* as “JLG 2019 merengue” — official write-ups call it romantic bachata.

---

## 1. Marquesina / carport / 15s = merengue de fiesta + merenhouse (90s–00s)

**Lock text:** Public = family lot, 15s, carport night. AYER IN = merengue de fiesta + merenhouse 90s–00s (Rosario, Wilfrido, Elvis, Ilegales, Proyecto Uno, Fulanito, Kinito, Manía, Chicas del Can). Temperature = hips + cousins.

### What the sources actually say

**Marquesina is a real Dominican / Puerto Rican room name.** ASALE *Diccionario de americanismos* (2010): *marquesina* II.1. f. *RD*, *PR.* “Lugar de una casa destinado a guardar los automóviles.” That is the carport / covered lot, not a genre.

- https://www.asale.org/damer/marquesina

Remezcla (2008) is the best published “party de marquesina” write-up, but it is **Puerto Rican garage-party nostalgia**, not a Dominican 15s ethnography. Music listed there is mixed: “underground (early reggaeton and dancehall) to boleros (around midnight), to merengue, and English dance hits.” Use it for the *place* (terraza / garage / covered lot), not for the genre lock.

- https://remezcla.com/culture/what-the-f-is-a-party-de-marquesina/

**Merengue is the national party dance.** UNESCO inscribed “Music and dance of the merengue in the Dominican Republic” (No. 01162) in 2016. The listing: merengue “plays an active role in various aspects of people’s daily lives – from their education to social gatherings and celebrations, even political campaigning.” Fast paired dance; accordion, drum, saxophone. Introduced at an early age. North of the country as cradle; influence extends to Puerto Rico, the US, and the Caribbean.

- https://ich.unesco.org/en/RL/music-and-dance-of-the-merengue-in-the-dominican-republic-01162
- Decision: https://ich.unesco.org/en/Decisions/11.COM/10.b.9

**The AYER names are the 80s–90s dance-merengue / merenhouse floor, not dryer-cry.**

| Lock name | What official pages call it | Year / receipt |
|---|---|---|
| Los Hermanos Rosario — *La Dueña del Swing* | “canción de merengue rápido”; first single of *Los dueños del Swing* (1995); attributed as the group’s biggest hit | https://es.wikipedia.org/wiki/La_due%C3%B1a_del_Swing |
| Wilfrido Vargas — *El Africano* | 1980s merengue de orquesta bomb the lock already treats as body memory | (lock catalog; UNESCO + Austerlitz frame the orquesta era) |
| Elvis Crespo — *Suavemente* | 1998 merengue crossover; the lock’s forgotten #1, not the ritual opener | Live About / merengue history: Crespo left Grupo Manía and hit with *Suavemente* (1998). https://www.liveabout.com/merengue-from-the-dr-to-dancehalls-2141568 |
| Ilegales / Proyecto Uno / Fulanito | merenhouse (see §3) | Wikipedia merenhouse + artist pages |
| Fulanito — *Guallando* | first single of *El Hombre Más Famoso De La Tierra* (1997); “household chant”; song of the year in Colombia 1998 | https://en.wikipedia.org/wiki/Fulanito |

**Merenhouse is explicitly quince / wedding / club floor music.** HipLatina (90s merengue-fusion roundup): merenhouse/merenrap “originating in New York by artists from the Dominican Republic”; “This was the music that made you run to the dance floor at quinceneras and weddings.” Ilegales *Fiesta Caliente* (1995): “another danceable cancion played at every quince and wedding.” Fulanito *El Cepillo*: “que comience la fiesta” as the party cue.

- https://hiplatina.com/90s-merengue-fusion-songs

Dominican Music USA (CUNY educational resource): Proyecto Uno “was the first group exclusively dedicated to blending traditional merengue with U.S. genres such as house, hip-hop, and rap” and “ushered in a hemispheric movement of the same name in the 1990s.” Inspired Ilegales, Sandy y Papo, Fulanito.

- https://dominicanmusicusa.com/educational_resources/proyecto-uno/221

### Nuance — “merengue de fiesta” is a product label

No UNESCO, AllMusic, or academic page in this pass defines a published genre called **merengue de fiesta** versus **merengue sentimental**. What the sources *do* distinguish:

- Fast / dance / orquesta merengue (Rosario *Dueña*, Wilfrido, Manía, Chicas del Can) vs romantic / ballad versions of the same singers (Olga *Como Olvidar* exists as both a ballad and a merengue cut — Billboard 2021 on the 20-year remake; Encyclopedia.com notes the 2001 single “was released in ballad and merengue versions”).
  - https://www.billboard.com/music/latin/olga-tanon-como-olvidar-comparison-jay-wheeler-9524257
  - https://www.encyclopedia.com/people/literature-and-arts/music-popular-and-jazz-biographies/olga-tanon
- Merenhouse / merenrap (NYC 90s fusion) vs merengue típico / perico ripiao (accordion countryside).
- UNESCO / Austerlitz *merengue de calle* as urban street merengue (see §2), which is **not** the same as merenhouse.

The lock’s phrase *merengue de fiesta* is the right *temperature* (hips, lot, 15s) for dance merengue + merenhouse. Do not write it as if UNESCO named that subgenre.

Olga *Como Olvidar* is the lock’s own split: Marquesina keeps the **party / merengue** cut; Secador keeps sentimental Olga. That split is product, not a Billboard genre tag.

[FINDING] The carport is a documented RD/PR house-part. Dance merengue + 90s merenhouse are the documented 15s / wedding / lot floor. The phrase *merengue de fiesta* is ours.  
[STAT:n] 3/3 merenhouse acts in the lock (Proyecto Uno, Ilegales, Fulanito) are tagged merenhouse / merengue-house on Wikipedia. Rosario *Dueña* is tagged merengue rápido (1995).

**Source:** https://www.asale.org/damer/marquesina  
**Source:** https://ich.unesco.org/en/RL/music-and-dance-of-the-merengue-in-the-dominican-republic-01162  
**Source:** https://en.wikipedia.org/wiki/Merenhouse  
**Source:** https://hiplatina.com/90s-merengue-fusion-songs  
**Source:** https://es.wikipedia.org/wiki/La_due%C3%B1a_del_Swing

---

## 2. Distinct from colmado street and from dryer

**Lock text:** Temperature = hips + cousins. *Not the street. Not the dryer.* Esquina owns salsa dura + merengue de fiesta on the sidewalk speaker. Secador owns balada / merengue sentimental. Cross-room: *Dueña* / *El Tiburón* / *La Morena* home = Marquesina. *El Africano* is listed as Esquina home in the ownership table (and as Marquesina AYER #2 in the authored 15) — that overlap is already a product walk, not a source problem.

### What the sources actually say

**Three different social rooms exist. No source maps them with the product’s three names.**

| Product room | Place the sources describe | Typical audio the sources name | Why it is not Marquesina |
|---|---|---|---|
| Esquina / colmado | Corner store with speakers angled at the sidewalk; everyday, not a booked party | Merengue, bachata, salsa, later dembow on motos | Public / street / dominó. Esquina verify already holds salsa + merengue de fiesta as *doorway temperature*, not a monopoly. |
| Secador / dryer | Product room (women, hood dryer, tía radio). No academic “secador genre.” Closest published audio = romantic balada / merengue-ballad dual cuts | Olga ballad *Como Olvidar*; dryer-cry | Alone-with-the-song. Lump in the throat, not hips first. |
| Marquesina | ASALE carport; Remezcla garage / terraza party; UNESCO “social gatherings and celebrations”; HipLatina quince / wedding merenhouse | Dance merengue + merenhouse | Private lot, cousins, 15s. Booked night, not the sidewalk. |

Colmado as street speaker (not a party):

- Punta Cana / visitor guide: “The colmado (small corner store) with bachata playing as the older customers chat about politics. The wedding next door where the band plays until 4:00 AM.” Everyday vs booked celebration in the same paragraph.
  - https://puntacana-excursions.com/blog/merengue-bachata-dominican-music-guide
- Las Terrenas lifestyle: “a tiny colmado in El Limón blasting Merengue.”
  - https://realestatelasterrenas.com/republic-dominican-music
- Esquina verify already collected the sidewalk-speaker ethnography: https://knycxjourneying.com/dominican-rhythms-how-merengue-and-bachata-define-a-nation/

UNESCO’s own 2016 video transcript distinguishes **merengue de calle** as “a strictly urban merengue that arose in popular areas, in marginalized urban neighborhoods… public settings, in the streets.” That is Esquina temperature (street / barrio), not the family lot.

- https://ich.unesco.org/en/video/38864
- YouTube mirror of the same UNESCO film: https://www.youtube.com/watch?v=fautemcgU48

Dryer / tía radio has **no** official genre page. It is a product listening place, same class as Silla’s “barbershop” (see silla verify: scholarship locates típica in campo / cabaret / colmado, not the chair). Do not write “merengue sentimental was born under the dryer.” Write: Secador is the *listening place* for weep / balada / sentimental merengue; Marquesina is the *listening place* for hips.

### What official sources do **not** support

- A published taxonomy “colmado vs marquesina vs secador.”
- A rule that merengue never plays in a colmado (it does) or that salsa never plays at a family party (it does).
- Yiyo as marquesina house band. Lock already parks Yiyo *Manos de Tijera* as Esquina HOY salsa. Hold that.

[FINDING] The split is a **place lock**, not a genre monopoly. Merengue lives in all three rooms. Marquesina owns the *booked family lot / 15s* cut of dance merengue + merenhouse. Esquina owns the sidewalk shout. Secador owns the weep.  
[STAT:n] ASALE marks marquesina as RD+PR carport. UNESCO marks merengue as both everyday life *and* celebrations. HipLatina marks merenhouse as quince/wedding floor.

**Source:** https://www.asale.org/damer/marquesina  
**Source:** https://ich.unesco.org/en/RL/music-and-dance-of-the-merengue-in-the-dominican-republic-01162  
**Source:** https://ich.unesco.org/en/video/38864  
**Source:** https://puntacana-excursions.com/blog/merengue-bachata-dominican-music-guide  
**Source:** https://hiplatina.com/90s-merengue-fusion-songs  
**Cross-file:** [`verify/esquina-deep-research.md`](esquina-deep-research.md) already holds the colmado as sidewalk speaker and warns Chiquito off Marquesina.

---

## 3. Proyecto Uno / Ilegales / Fulanito = merenhouse

**Lock text:** AYER IN names Ilegales, Proyecto Uno, Fulanito as the merenhouse floor. *La Morena*, *El Tiburón*, *Guallando* are the authored 15’s merenhouse body. *El Tiburón* is “the hole” vs live JSON.

**Answer:** Yes. All three acts are merenhouse / merengue-house / merenrap. Not salsa. Not bachata. Not merengue típico.

### Genre definition

Wikipedia *Merenhouse* (also merenrap, merengue house, electronic merengue): “a style of Dominican Merengue music derived by blending it with dancehall, hip hop and house, particularly latin house.” Cultural origin: **1990s, New York City.** Stylistic origins: hip hop, dancehall, merengue, Latin house. Influential artists listed on the same page: **Fulanito**, **Proyecto Uno**, **Ilegales**.

- https://en.wikipedia.org/wiki/Merenhouse

Sandy & Papo Wikipedia: “The group was part of the merenhouse (called also ‘house-merengue’ or ‘merengue-hip hop’) style movement that emerged in New York City in the 1990s. Groups such as Proyecto Uno, Fulanito, Ilegales and El Cartel were part of this movement.”

- https://en.wikipedia.org/wiki/Sandy_%26_Papo

Remezcla: “Throughout the 90s, merenhouse swept Latin American and Latino spaces. Artists like Ilegales, Lisa M, Sandy & Papo, and Fransheska… And there was no act that transcended the genre more other than the originators, Proyecto Uno.” Formed 1989 by Nelson Zapata and Ricky Echevarría; producer Pavel de Jesús at Quad Studios with Frankie Knuckles / David Morales. Hits: *Está Pega’o*, *Brinca*, *El Tiburón*.

- https://remezcla.com/lists/music/5-songs-african-american-proyecto-uno-merenhouse

Deborah Pacini Hernandez, *Oye Como Va!* (Temple, 2009), p. 102, is the scholarly cite on Proyecto Uno’s Wikipedia page for the merengue-house blend.

- https://archive.org/details/oyecomovahybridi00paci/page/102

### Per-act receipts

| Act | Official genre tag | Key lock track | Year notes |
|---|---|---|---|
| **Proyecto Uno** | Wikipedia: “Dominican American hip-hop and merengue house group.” Founded NYC Lower East Side, 1989. Originally a traditional merengue cover band, then the fusion. | *El Tiburón* — Rolling Stone (2018) #24 of 50 greatest Latin pop songs. Wikipedia singles list dates the song **1993**. Discogs European pressings **1995** (Electronic / House / Merengue). Local authored 15 says **1996** (*New Era* album year). Treat 1993–96 as the window; do not pin a single year without the release you ship. | https://en.wikipedia.org/wiki/Proyecto_Uno · https://www.rollingstone.com/music/music-latin-lists/50-greatest-latin-pop-songs-695776/ · https://www.discogs.com/release/1140875-Proyecto-Uno-El-Tibur%C3%B3n · https://dominicanmusicusa.com/educational_resources/proyecto-uno/221 · https://musicbrainz.org/artist/3c22f531-e3fd-4422-8700-c8daea85b996 |
| **Ilegales** | Wikipedia infobox genre = **Merengue house**. “Grammy-nominated Dominican merenhouse group… one of the main exponents that helped to introduce and establish the merenhouse to the mainstream.” Founded 1993. Debut 1995. | *La Morena* — “massive hit” 1996; peaked #6 RPM Dance (Canada); Gold Mexico / Gold Venezuela / Platinum US. Discogs single: Electronic / Latin / House / Merengue. Live album nominated Best Merengue Album, 43rd Grammys. | https://en.wikipedia.org/wiki/Ilegales · https://www.discogs.com/release/988305-Ilegales-La-Morena · https://www.discogs.com/artist/120848-Ilegales |
| **Fulanito** | Wikipedia: Washington Heights; “combines traditional merengue with elements of other genres such as house, hip hop, and bachata.” Merenhouse page: “one of the first groups to combine merengue and house music.” Founded 1996. AllMusic styles include Merenhouse / Latin Dance. | *Guallando* — first single of *El Hombre Más Famoso De La Tierra* (**1997**). Discogs: Electronic / Latin / House / Merengue. | https://en.wikipedia.org/wiki/Fulanito · https://en.wikipedia.org/wiki/Merenhouse · https://www.allmusic.com/artist/fulanito-mn0000153109 · https://www.discogs.com/release/2480707-Fulanito-Guallando |

[FINDING] The lock’s three merenhouse names are the textbook trio. Putting *El Tiburón* into the AYER 15 is genre-correct. It is not salsa, not bachata, not dryer.  
[STAT:n] 3/3 acts appear on Wikipedia *Merenhouse* as exemplars. *La Morena* 1995–96, *Guallando* 1997, *El Tiburón* 1993–96 — all inside AYER (through ~2010).

### Date conflict to flag, not to “fix” in JSON

Local `marquesina-ayer-hoy.md` dates *El Tiburón* **1996**. Wikipedia singles list **1993**. Discogs EU **1995**. *New Era* (the album most associated with the later hit cycle) is 1996. All three years are AYER. Re-pin the year against the official id `4Qy0vs80T5M` when JSON is allowed to move.

**Source:** https://en.wikipedia.org/wiki/Merenhouse  
**Source:** https://en.wikipedia.org/wiki/Proyecto_Uno  
**Source:** https://en.wikipedia.org/wiki/Ilegales  
**Source:** https://en.wikipedia.org/wiki/Fulanito  
**Source:** https://dominicanmusicusa.com/educational_resources/proyecto-uno/221  
**Source:** https://remezcla.com/lists/music/5-songs-african-american-proyecto-uno-merenhouse  
**Source:** https://hiplatina.com/90s-merengue-fusion-songs

---

## 4. Chiquito / Manny Cruz remakes = HOY merengue

**Lock text:** HOY IN = Chiquito, Manny Cruz remakes, JLG 2019 merengue. Chiquito = “house band of still playing.” Manny = remakes with Rosario / Ventura / Wilfrido. Zero 90s originals. Yiyo salsa is Esquina, not this lot.

### 4a. Manny Cruz remakes — **HOLD**

Manny is a 2010s–2020s merenguero whose current catalog is explicitly revival / tribute merengue, not 90s originals.

Diario Libre (23 Oct 2024), Severo Rivera: Manny presents *2080* at Jet Set as “un tributo a relevantes intérpretes del género.” Guests who “tuvieron una presencia destacada en la década de los 80”: Aramis Camilo, Fernando Villalona, Wilfrido Vargas, Sergio Vargas, Dioni Fernández, Rasputín (tribute), **Los Hermanos Rosario**. Cruz: “Es un disco tributo a la música de los 80… Por eso el nombre ‘2080’: es la esencia de los 80, pero con un toque ligero de los años 2000.” He says he recorded *La Dueña del Swing* with Los Hermanos Rosario — “la única canción de los 80 que quise incluir” (his wording; the original is 1995). Planned video drop on 26 Nov, Día Nacional del Merengue. Genesis was *Qué Rico Es El Merengue* with Johnny Ventura, “hace tres años, justo antes de su partida” (Ventura died 28 Jul 2021).

- https://www.diariolibre.com/revista/musica/2024/10/23/manny-cruz-presenta-album-2080/2888828

Diario Libre (5 Mar 2024): *El Hombre Divertido* with Wilfrido Vargas is “una nueva versión del éxito popularizado en 1983.” Wilfrido on Cruz: “El merengue como género rejuvenece con el trabajo que él está realizando.”

- https://www.diariolibre.com/revista/musica/2024/03/05/asi-suena-la-version-de-el-hombre-divertido-con-manny-cruz-y-wilfrido/2633300

Catalog matches the authored HOY 15:

| Lock slot | Recording | Official year | URL |
|---|---|---|---|
| Manny + Rosario — *La Dueña del Swing* | *2080* | album 22 Oct 2024; official video posted 23 Jan 2025 (`4R7NmEa8s8M`) | https://open.spotify.com/track/6rfOydvpGRFEPumMLCsbS7 · https://music.apple.com/mx/song/la-due%C3%B1a-del-swing/1772153255 · https://www.youtube.com/watch?v=4R7NmEa8s8M |
| Manny + Johnny Ventura — *Qué Rico Es El Merengue* | written by Cruz; video as posthumous tribute | 2021 | https://www.youtube.com/watch?v=cenRb14_sMY · Diario Libre 2080 piece |
| Manny + Wilfrido — *El Hombre Divertido* | remake of 1983 | 2024 | https://www.diariolibre.com/revista/musica/2024/03/05/asi-suena-la-version-de-el-hombre-divertido-con-manny-cruz-y-wilfrido/2633300 |
| Manny + Aramis Camilo — *El Motor* | *2080* lead promo | 2024 | same 2080 article |
| Manny — *Santo Domingo* | original city merengue | 2021 | named in Diario Libre live-album piece https://www.diariolibre.com/revista/musica/2022/06/08/manny-cruz-estrena-album/1877488 |

[FINDING] Manny remakes are the correct HOY merengue spine. Original 1995 *Dueña* stays AYER #1. The 2024/25 cut is a new recording with the old voices.  
[STAT:n] *2080* names 7 80s merengue figures. 3 of the lock’s HOY remake slots (Rosario, Wilfrido, Ventura) are documented in Diario Libre 2024.

### 4b. Chiquito Team Band — **DO NOT CALL THIS MERENGUE**

Official bios, album titles, and the door hit itself are **salsa**.

- AllMusic: “Dominican salsa vocal quintet… who call their genre ‘La Industria Salsera.’” Formed 12 Jun 2012. Styles: Salsa, Dominican Traditions, Tropical, Sonero. *Llamada de Mi Ex* listed as a 2015 single after the 2014 debut *La Industria Salsera*.
  - https://www.allmusic.com/artist/chiquito-team-band-mn0003220418
- Apple Music: “a quintet of salseros… ‘La Industria Salsera.’”
  - https://music.apple.com/us/artist/chiquito-team-band/762759011
- Spotify artist copy: “una de las agrupaciones de **salsa** más influyentes… Fundada en Santo Domingo en el año 2012.” Hits named include *La Llamada de Mi Ex*, *Tengo Que Colgar*, *Lejos de Ti* — “himnos dentro de la nueva ola **salsera**.”
  - https://open.spotify.com/artist/0vEYOFlkqy2FUy1UOF7RiV
- Deezer: 2018 Latin Grammy nomination **Best Salsa Album**; Billboard Latin Music Award noms as Tropical Artist; multiple Soberano / Conga awards for **Best Salsa Orchestra**.
  - https://www.deezer.com/mx/artist/5372016
- *La Llamada De Mi Ex* appears on Planet Records’ *Hot Salsa 2016* compilation (℗ 2015). SoundCloud rip titled “La Llamada de Mi Ex (Salsa 2015).” Official video © 2015 Chiquito Team Band (`u6Q5Lu0Sq3g`).
  - https://www.youtube.com/watch?v=fdwnuuN5d3Q
  - https://www.youtube.com/watch?v=u6Q5Lu0Sq3g

Esquina verify already wrote the same correction: “`esquina-ayer-hoy.md` tags the three Chiquito door tracks as merengue. Official bios… tag them as salsa. They still belong on HOY Esquina. They do **not** belong on Marquesina as a merengue house band without a second walk.”

Local `marquesina-ayer-hoy.md` already flags the conflict in its limitation: “Chiquito’s catalog is salsa-labeled in some bios; the room lock already treats them as the HOY house band.” This pass upgrades that from a parenthetical to a **hold-and-walk**: salsa-labeled in *all* official bios checked, not “some.”

**What still makes Chiquito HOY-legal as a *guest after the merengue 15*:** formed 2012; door hits 2014–2017; they play the family lot *now*. That is a **place** argument, not a genre argument. GENRE-LOCK already splits them: “Yiyo / Chiquito | HOY Esquina / HOY Marquesina.” If Marquesina HOY is merengue-only, Chiquito as opener is the same error as putting Yiyo *Manos de Tijera* in this 15 — which the lock already refuses.

[FINDING] Chiquito = 2012 salsa orquesta. *La Llamada* (2015) is salsa. Using them as Marquesina HOY *opener / house band* contradicts the merengue lock. Using them as HOY Esquina house band matches the bios.  
[STAT:n] 4/4 official bios checked (AllMusic, Apple, Spotify, Deezer) say salsa. 0/4 say merengue as primary genre.

### 4c. JLG 2019 / 2023 — **HOLD the decade, correct the track tags**

ERA-LOCK / GENRE-LOCK: “JLG 2019 merengue.” Authored HOY 15 puts four JLG cuts: *Kitipun*, *I Love You More* (*Literal*, 2019); *Mambo 23*, *La Noviecita* (*Radio Güira*, 2023).

*Literal* (31 May 2019, Universal Music Latin) is a mixed tropical album (merengue, salsa, bachata). Wikipedia track notes:

| Track | Official tag on the *Literal* page | Lock use |
|---|---|---|
| **Kitipun** (5 Apr 2019) | “a romantic **bachata** with innovative sound.” Rolling Stone review is titled “**Bachata** Legend… *Literal*.” | HOY #2 as “Dominican poet *now*.” **Wrong body if Marquesina is merengue-only.** |
| **I Love You More** | “a celebratory **merengue** that interpolates Liszt’s Hungarian Rhapsody No. 2.” | HOY #10. Genre-correct. |
| *Lámpara Pa’ Mis Pies* | merengue with township-jive / highlife choruses | Not in this 15; merengue-legal if needed. |
| *Merengue de Cuna* | merengue dedicated to his son | Not in this 15. |

- https://en.wikipedia.org/wiki/Literal_(album)
- https://www.rollingstone.com/music/music-latin/juan-luis-guerra-new-album-literal-844282/
- https://www.billboard.com/music/latin/juan-luis-guerra-new-album-literal-8512678/

*Radio Güira* (3 Nov 2023, Rimas): merengue / bachata / Latin pop / blues. Latin Grammy 2024: Album of the Year + Best Merengue/Bachata Album; *Mambo 23* won Record of the Year + Best Tropical Song.

| Track | Official tag | Lock use |
|---|---|---|
| **Mambo 23** (22 Sep 2023) | “merengue-mambo (**merengue de calle**)”; first time Guerra ventured into mambo. Soberano 2024 nominee **Merengue del Año**. | HOY #6 as “Merengue *now*.” Genre-correct, but *merengue de calle* is the UNESCO/Esquina street term — walk the temperature. |
| **La Noviecita** (6 Dec 2023) | “a folk **merengue** with influences of jazz and rock.” | HOY #14. Genre-correct. |
| *DJ Bachata* | bachata | Not in this 15. Correct omit. |

- https://en.wikipedia.org/wiki/Radio_Güira

[FINDING] JLG 2019–2023 is the right HOY *name*. *Kitipun* is the wrong *body* for a merengue-only lot (it is bachata). *I Love You More*, *La Noviecita*, and (with a street-temperature caveat) *Mambo 23* are merengue.  
[STAT:n] 1/4 authored JLG HOY slots (*Kitipun*) is officially bachata. 2/4 are merengue. 1/4 (*Mambo 23*) is merengue-mambo / merengue de calle.

---

## Cross-checks against the other rooms

| If it is… | Home | Why this pass agrees |
|---|---|---|
| Rosario *Dueña* 1995 | Marquesina AYER #1 | Merengue rápido, lot swing. |
| Proyecto Uno *El Tiburón* | Marquesina AYER merenhouse hole | Textbook merenhouse. Rolling Stone Latin-pop monument. |
| Ilegales *La Morena* | Marquesina AYER | Merenhouse; quince floor. |
| Fulanito *Guallando* | Marquesina AYER | Merenhouse 1997. |
| Elvis *Suavemente* 1998 | Marquesina AYER forgotten #1, never opener | 90s merengue bomb. HOY padding = forbidden. |
| Olga merengue *Como Olvidar* | Marquesina party cut / Secador sentimental cut | Dual-version receipt exists (ballad + merengue). |
| JLG *Burbujas* / *Bachata Rosa* | Not Marquesina (Love Birds / Silla leak) | Couple radio, not lot merengue. |
| *Pedro Navaja* / *Gran Varón* | Esquina catalog, never Marquesina first 15 | Salsa monuments. |
| Yiyo *Manos de Tijera* | Esquina HOY | Salsa. 357M is the trap. |
| Chiquito *La Llamada* | **Esquina HOY** on official genre; Marquesina only if Javy walks a salsa guest | Salsa orquesta 2012–. |
| Manny *2080* remakes | Marquesina HOY | Documented 2024 merengue tribute. |
| Dembow / *Pepas* / *Despacito* | OUT | Family lot lock. UNESCO merengue ≠ dembow. |

---

## Conflicts and version notes

1. **Firecrawl quota.** This file is Tavily + official-page fallback. Re-run Firecrawl when the anonymous cap resets (~24h from this pass).
2. **Chiquito salsa vs lock “merengue house band.”** Highest-severity conflict. Matches Esquina verify. Walk before JSON.
3. **Kitipun = bachata.** Second-severity conflict with “JLG 2019 merengue.”
4. **Mambo 23 = merengue de calle / mambo.** Legal merengue *now*, street-adjacent temperature. Optional Esquina leak.
5. **El Tiburón year** 1993 / 1995 / 1996. All AYER. Re-pin to the shipped id.
6. **Manny *Dueña* year.** Local HOY table says 2025 (video date). Spotify/Apple album *2080* is **22 Oct 2024**. Video `4R7NmEa8s8M` posted 23 Jan 2025. Both are HOY.
7. **“Merengue de fiesta”** is not a published UNESCO/AllMusic term. Keep it as product temperature.
8. **Remezcla 2008 marquesina** is Puerto Rican garage-party, mixed playlist. Do not cite it as proof that Dominican 15s = merenhouse-only.
9. **Olga *Como Olvidar*** exists as ballad + merengue (2001). Marquesina wants the merengue body; Secador wants the weep. Dual-home is already in GENRE-LOCK’s spirit.
10. Wikipedia *Merenhouse* carries July 2020 “excessively detailed / style / unsourced” banners. Cross-checked against Dominican Music USA, Remezcla, Pacini Hernandez, Discogs, AllMusic, and the three artist pages. The trio identification holds without relying on the unsourced sales claims.

Older than two years, still standard (flagged, not discarded): UNESCO 2016 listing; Pacini Hernandez 2009; Austerlitz 1997 (via Esquina verify); Remezcla 2008 place-piece; ASALE 2010 dictionary; HipLatina 90s roundup (undated; content is historical). Current (2023–2025): Diario Libre *2080*, *Radio Güira* Latin Grammys, Manny/Wilfrido remake.

---

## What not to do

1. Do not rewrite `public/marquesina.json` from this file.
2. Do not call Chiquito a merengue act in copy, chips, or liner notes.
3. Do not open HOY on *Suavemente* or original *Dueña*.
4. Do not treat *Kitipun* as merengue without a second walk.
5. Do not put Yiyo, *Pedro Navaja*, or El Alfa on this lot.
6. Do not cite Remezcla’s PR garage party as a Dominican 15s genre survey.
7. Do not treat YT Music *plays* (Fulanito *Guallando* 231M) as watch-page views — already in the authored file.

---

## Recommended next step

Walk two lock questions with Javy before any JSON move:

1. **Chiquito on Marquesina HOY** — keep as house-band *place* guest after a merengue-only 15 (Manny / JLG merengue / Toño *Dale Vieja*), or move the opener to Esquina-only?
2. **Kitipun** — keep as HOY poet/name, or swap for a *Literal* merengue (*I Love You More* is already #10; *Lámpara Pa’ Mis Pies* is unused merengue)?

Then, if Firecrawl quota is back, run the rerun pack below and append any new official URLs. Still no live JSON until the list is walked.

---

## Firecrawl rerun pack

When the MCP cap resets, run these searches then scrape the official hits:

```
marquesina fiesta merengue quinceañera carport Dominican
merenhouse Proyecto Uno Ilegales Fulanito 1990s
"La Morena" Ilegales merengue house
"El Tiburón" Proyecto Uno merenhouse
Fulanito Guallando 1997
Chiquito Team Band salsa OR merengue "La Llamada de Mi Ex"
Manny Cruz 2080 "Dueña del Swing" Wilfrido Ventura
Juan Luis Guerra Kitipun bachata OR merengue Literal 2019
UNESCO merengue Dominican Republic 01162
colmado speaker merengue salsa Dominican
```

Priority scrapes: UNESCO 01162, ASALE marquesina, Wikipedia Merenhouse / Proyecto Uno / Ilegales / Fulanito / Literal / Radio Güira, Dominican Music USA Proyecto Uno, Diario Libre 2080, AllMusic Chiquito, Discogs *La Morena* / *El Tiburón* / *Guallando*.
