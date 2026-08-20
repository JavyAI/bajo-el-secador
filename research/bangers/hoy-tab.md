# HOY tab — time rail, not a fifth place

**Date:** 2026-08-16  
**Rule:** rooms stay **old school** (place + memory). HOY is **time** (last ~10–15 years, official YouTube only). Views rank *inside* a culturally locked pool. Views do **not** pick the first 15. Javy already rejected a view-rank pass that put Son by Four first in Esquina. Do not repeat that error with *La Gozadera* / *Vivir Mi Vida* / *Despacito*.

**This file is research only.** Do not rewrite live `public/*.json`, player JS, or CSS from this pass.

**View counts** pulled 2026-08-16 via YouTube oEmbed (title + channel) + Return YouTube Dislike `viewCount`. Treat them as a resonance signal, not a ranking key. They will rot.

---

## 1. Recommendation

**One global HOY *chip*. Four room-filtered rails. Not a fifth place.**

| Option | Verdict | Why |
|---|---|---|
| One unfiltered HOY mix for the whole site | **No** | Dryer would hear El Alfa / Chiquito street / merengue-revival tambora. Esquina would hear Shakira dryer-cry. That is poisoning by another door. |
| Four new place-tabs (*Hoy en el secador* as a fifth wordmark) | **No** | HOY is a **time** rail. A fifth place-wordmark competes with the plates. Rooms keep their paintings. |
| One **HOY** chip next to room nav; list follows the room you are already in | **Yes** | Matches the product split. `Hoy en la silla` = current bachata. `Hoy en el secador` never plays explicit dembow. Plates and lockups stay. |

### How it behaves

1. User is in a room (`#salon` / `#barberia` / `#colmado` / `#marquesina`).
2. They tap a single **HOY** chip in the same nav row as Secador / Silla / Esquina / Marquesina.
3. The **plate does not change**. The **wordmark does not change**.
4. The kicker becomes the time label for that room.
5. The dock swaps catalog to that room’s HOY first-15, same player, authored order, no shuffle.
6. Tapping a room chip while HOY is on **keeps HOY on** and loads that room’s HOY filter (still one player).
7. Tapping HOY again returns to that room’s old-school catalog at index 0.

Suggested kickers (caps, like today’s genre kickers):

| Room | Old kicker (stays when HOY is off) | HOY kicker |
|---|---|---|
| Secador | Baladas y merengue | Hoy · bajo el secador |
| Silla | Bachata | Hoy · en la silla |
| Esquina | Salsa y merengue | Hoy · en la esquina |
| Marquesina | Merengue de fiesta | Hoy · en la marquesina |

Hash stays the place: `#salon`. HOY is a flag (`?hoy=1` or `data-hoy="1"`), not `#hoy`. A fifth hash would teach people HOY is a fifth room.

### What this is not

- Not a second radio playing under the room (ToS + iOS: one YouTube iframe `PLAYING`).
- Not a live Billboard scrape.
- Not “add Romeo to every old-school first 15.”
- Not permission to merge HOY ids into `salon.json` / `barberia.json` / `colmado.json` / `marquesina.json` intros.

---

## 2. What belongs in HOY

**Window:** roughly **2011-08 → 2026-08** (15 years back from today). 2010 is date-edge. Pre-2011 stays in rooms unless Javy makes a one-song exception.

**Source lock (same as rooms):** VEVO / artist / Topic-by-label / Fania / Warner / Karen / JN / Planet Records. No lyrics rips, karaoke, DJ mixes, sped-up, AI, club edits.

**Job:** *what is still playing now* that would poison the old-school spine if it sat in the room first 15.

| Bucket | In HOY | Not in old-school first 15 |
|---|---|---|
| Romeo 2010s solo (*Fórmula*, *Golden*, *Utopía*, *FV3*) | Yes | Yes — *Obsesión* / *Un Beso* stay in Silla. Solo Romeo is time. |
| Prince Royce | Yes (jóvenes / dryer-romantic) | Yes — típica is the Silla spine. One Royce in old Silla is already a leak. |
| Current bachata (Aventura 2019 *Inmortal*, 2021 *Volví* gated, Royce 2020 *Carita*, Romeo 2022 *Sus Huellas*) | Yes | Yes |
| Merengue revival (Chiquito, Manny Cruz remakes, JLG 2019 *Kitipun*) | Yes — Marquesina + Esquina filters | Original *Dueña del Swing* / *Suavemente* stay in Marquesina room |
| Yiyo / Chiquito as “still playing” | Yes — their **home** is HOY Esquina / Marquesina | Keep **out** of Esquina old first 15 (already correct). Do not bury them at catalog tail if HOY exists. |
| Carefully gated urbano | **Esquina HOY only**, one or two slots, official, not explicit | Never dryer. Never Silla. Never Marquesina family lot. |
| Marc Anthony 2013 *Vivir Mi Vida* | HOY Esquina **late**, time-correct | Old Esquina already banned it as “2013 pop-salsa TV.” That ban stays. |

### Room-filter temperature

**Hoy en el secador** — women, dryer, tía radio *now*. Sentimental bachata + dryer-cry 2010s. Shakira/Royce *Deja Vu* is dryer gold. No dembow, no club, no Drake, no Bad Bunny verse, no *Bella y Sensual*.

**Hoy en la silla** — men, chair, current bachata. Romeo solo + Royce + Utopía with típica voices (*Debate de 4*, *La Demanda*, *Payasos*, *Canalla*). Aventura *Inmortal* is reunion-now, not 2002 *Obsesión*. *Volví* is gated (Bad Bunny). No English/Spanglish R&B-bachata opener (Toby Love is 2006 and still wrong).

**Hoy en la esquina** — sidewalk speaker *now*. Yiyo + Chiquito first. 2010s salsa-radio that old Esquina correctly refused (*Vivir Mi Vida* late, not opener). One urbano gate. No Cali pride. No Son by Four. No *La Gozadera* as opener (1.75B views, Cuban TV party — the next Son by Four).

**Hoy en la marquesina** — family lot at night, merengue that is **new or newly cut**. Chiquito house band. Manny Cruz remakes with Ventura / Rosario. JLG *Literal* (2019). Not salsa monuments. Not 2024 club dembow. Not the 1990s originals already on the Marquesina plate.

---

## 3. Never under the dryer vs allowed in Hoy en la esquina

### NEVER in Hoy en el secador (hard ban)

| Class | Examples | Why |
|---|---|---|
| Explicit dembow | El Alfa *La Mamá de la Mamá* (`s5yRZOQ3EWI`), Tokischa *Linda*, Rochy RD, dirty Chimbala | Wrong body, wrong room, wrong speaker. Tía under the hood does not say wow. |
| Club edits / DJ mixes / sped-up / karaoke | Farruko *Pepas* edits, Alofoke rips, “dembow mix 2024” | Not official audio. Player rule. |
| Chart sludge | Luis Fonsi *Despacito*, Karol G *Tusa*, Bad Bunny *Tití* / *Dákiti*, Enrique *Bailando* | Views without dryer-cry. Same failure mode as Son by Four. |
| Urbano-bachata sex features | Romeo *Bella y Sensual* (Daddy Yankee / Nicky Jam), *Sobredosis* (Ozuna), Aventura *Volví* (Bad Bunny) | Recognition, not dryer. First seconds are club, not lump-in-throat. |
| English / crossover as opener | Romeo *Promise* ft. Usher, *Odio* ft. Drake, Royce *Stand by Me* | Diaspora-chart, not tía radio. *Promise* official `Y3XyWhrZnqE` is 383M and still wrong lock for this filter. |
| Street merengue-urbano | Omega *Si Te Vas*, merengue electrónico | Different street. Marquesina/Esquina question, never dryer. |

### Can live in Hoy en la esquina (gated)

| Track | Gate | Why esquina, not dryer |
|---|---|---|
| Yiyo *Manos de Tijera* / *Qué Agonía* / *Mi Todo* | Full yes | Current colmado salsa. Too new for old Esquina spine. |
| Chiquito *La Llamada De Mi Ex* / *Tengo Que Colgar* / *Lejos De Ti* | Full yes | Same. House band of “still playing.” |
| Romeo *Yo También* ft. Marc Anthony | Yes | 2015 salsa-bachata that actually hits a sidewalk speaker. |
| Marc Anthony *Vivir Mi Vida* | Late in the 15, never opener | Time-correct. Old Esquina ban was about **place**, not existence. |
| Aventura *Volví* ft. Bad Bunny | One slot, not opener | Reunion is time. Bad Bunny verse is urbano. Esquina can hold one. |
| Romeo *Bella y Sensual* | One slot, last third | Urbano-bachata the corner actually plays. Not dryer. |
| El Alfa *La Mamá de la Mamá* | **One slot max**, last third, official only | The one dembow receipt that a real esquina speaker has played since 2021. Not a dembow takeover. No Tokischa. No Rochy. No club remix. |

### Marquesina vs Esquina (HOY)

Marquesina HOY = family lot. Chiquito + Manny Cruz remakes + JLG 2019.  
**Not** El Alfa. **Not** *Volví*. **Not** *Bella y Sensual*.  
If a kid puts dembow on the marquesina Bluetooth, that is not this radio.

---

## 4. First 15 example HOY lists

Authored. Culture first. No consecutive same artist. Official id preferred over the site’s weaker twin. Views = signal only.

**Do not paste these into live JSON until Javy walks them.**

### Hoy en el secador

Dryer-cry 2010s. No dembow. No Drake. No Bad Bunny.

| # | Artist | Title | Year | Official id | Channel | Views 2026-08-16 | Notes |
|---|---|---|---:|---|---|---:|---|
| 1 | Romeo Santos | Propuesta Indecente | 2013 | `QFs3PIZb3js` | RomeoSantosVEVO | 2,417,487,182 | Already Silla #2. **Move here.** First seconds are the violin. Dryer and silla both know it; dryer HOY can open on it. |
| 2 | Prince Royce | Darte un Beso | 2013 | `bdOXnTbyk0g` | PrinceRoyceVEVO | 1,623,815,546 | Already Silla #3. **Move here.** Romantic, not típica. |
| 3 | Romeo Santos | Eres Mía | 2014 | `8iPcqtHoR3U` | RomeoSantosVEVO | 1,338,681,355 | **Do not use site id `vY_3YrKtUUE`** (1.02M “Eres Mía Audio”). Official MV is this. |
| 4 | Romeo Santos ft. Marc Anthony | Yo También | 2015 | `QBaIMZ8QjcU` | RomeoSantosVEVO | 901,612,309 | Dryer + salsa-voice. Not consecutive Romeo if #3 is Romeo — **swap needed.** See order fix below. |
| 5 | Romeo Santos | Imitadora | 2017 | `mhHqonzsuoA` | RomeoSantosVEVO | 796,699,405 | Official **lyric** video, same channel as the MV (`FAq4OIRDo68`, 253M). Lyric has the resonance. Either is legal. |
| 6 | Prince Royce, Shakira | Deja Vu | 2017 | `XEvKn-QgAY0` | PrinceRoyceVEVO | 736,017,230 | Dryer gold. Shakira is tía-radio now. |
| 7 | Romeo Santos | Cancioncitas de Amor | 2014 | `jk4HYngf65w` | RomeoSantosVEVO | 635,432,039 | The sentimental Romeo LIST-REVIEW already preferred over *Eres Mía* in old Silla. |
| 8 | Romeo Santos ft. Santana | Necio | 2014 | `DXiXPhvYuNU` | RomeoSantosVEVO | 415,826,404 | Official audio. Lump-in-throat. |
| 9 | Romeo Santos | Hilito | 2014 | `4eCL0l9iD5A` | RomeoSantosVEVO | 357,479,687 | Already in Silla catalog after the 15. HOY home. |
| 10 | Romeo Santos | You | 2011 | `ElU-VcWEhRU` | RomeoSantosVEVO | 236,951,876 | Solo-debut English title, Spanish body. Allowed as mid-15, not opener. |
| 11 | Prince Royce | Te Robaré | 2013 | `yUAZxs3qY3Y` | PrinceRoyceVEVO | 214,356,819 | Romantic jóvenes. Breaks Romeo stack. |
| 12 | Romeo Santos | Sus Huellas | 2022 | `rvmtQvA_cmM` | RomeoSantosVEVO | 139,778,614 | FV3. Still playing now. |
| 13 | Prince Royce | Carita de Inocente (ALTER EGO) | 2020 | `qjkb9_AJCLo` | PrinceRoyceVEVO | 81,452,853 | Official MV. Lyric `Ys589P0vLU4` is 40.9M. Remix ft. Myke Towers `VSFL8UpeUvM` is urbano — skip for dryer. |
| 14 | Romeo Santos, ROSALÍA | El Pañuelo | 2022 | `sWGJd26kUOY` | RomeoSantosVEVO | 54,265,522 | Recent dryer-romantic. Not chart sludge. |
| 15 | Prince Royce | Las Cosas Pequeñas | 2012 | `ROzZSmaxDz8` | Planet Records Official | 83,602,948 | Official HD. Site id `UHC7ITw9wPY` is VEVO **audio** at 5.25M — use Planet HD here. |

**Order fix (no consecutive Romeo):** the table above still stacks Romeo at 3–5 and 7–10. **Play this order instead:**

1 Propuesta → 2 Darte un Beso → 3 Eres Mía → 4 Deja Vu → 5 Yo También → 6 Te Robaré → 7 Imitadora → 8 Las Cosas Pequeñas → 9 Cancioncitas → 10 Carita → 11 Necio → 12 Sus Huellas → 13 Hilito → 14 El Pañuelo → 15 You  

*You* last, not first. *Yo También* after Shakira, not after *Eres Mía*.

**Out of this 15 on purpose:** *Promise* Usher, *Odio* Drake, *Sobredosis* Ozuna, *Bella y Sensual*, *Volví*, *Vivir Mi Vida*, *Corazón Sin Cara* (teen-pop + 2010 date-edge).

### Hoy en la silla

Current bachata. Utopía guests earn slots even when views are smaller than *Propuesta*.

| # | Artist | Title | Year | Official id | Channel | Views 2026-08-16 | Notes |
|---|---|---|---:|---|---|---:|---|
| 1 | Romeo Santos | Propuesta Indecente | 2013 | `QFs3PIZb3js` | RomeoSantosVEVO | 2,417,487,182 | Leaves old Silla first 15. HOY opener. |
| 2 | Prince Royce | Darte un Beso | 2013 | `bdOXnTbyk0g` | PrinceRoyceVEVO | 1,623,815,546 | Leaves old Silla first 15. |
| 3 | Aventura | Inmortal | 2019 | `XlmaJ-yU46U` | RomeoSantosVEVO | 380,923,040 | Reunion. HOY, not 2002 *Obsesión*. |
| 4 | Romeo Santos | Eres Mía | 2014 | `8iPcqtHoR3U` | RomeoSantosVEVO | 1,338,681,355 | Official MV only. |
| 5 | Prince Royce | Te Robaré | 2014 | `yUAZxs3qY3Y` | PrinceRoyceVEVO | 214,356,819 | |
| 6 | Romeo, Antony Santos, Luis Vargas, Raulín Rodríguez | Debate de 4 | 2011/2015 | `1p0QyZIf93I` | RomeoSantosVEVO | 43,672,081 | **Keep despite 44M.** Típica still playing *now*. This is the silla-HOY lock. |
| 7 | Prince Royce | Carita de Inocente (ALTER EGO) | 2020 | `qjkb9_AJCLo` | PrinceRoyceVEVO | 81,452,853 | |
| 8 | Romeo Santos, Raulín Rodríguez | La Demanda | 2019 | `cOy4siyFp0U` | RomeoSantosVEVO | 125,519,187 | Cacique in HOY, not a third Raulín in old Silla. |
| 9 | Prince Royce | Las Cosas Pequeñas | 2012 | `ROzZSmaxDz8` | Planet Records Official | 83,602,948 | |
| 10 | Romeo Santos, Frank Reyes | Payasos | 2019 | `CkNSGnekpBA` | RomeoSantosVEVO | 113,381,249 | Príncipe still playing. |
| 11 | Prince Royce | Corazón Sin Cara | 2010/2014 | `XNGWDH-6yv8` | PrinceRoyceVEVO | 281,969,595 | **Date-edge** (song 2010, VEVO 2014). Jóvenes only. **Do not use site `ZNN7NTl83cI`** (Planet, 54M). If Javy cuts 2010, swap to *Deja Vu*. |
| 12 | Romeo Santos, El Chaval | Canalla | 2019 | `8zcZC4HVr68` | RomeoSantosVEVO | 185,676,188 | Official MV. Topic `aQ9ZDQI4svc` is only 24M. |
| 13 | Aventura, Bad Bunny | Volví | 2021 | `ayd3yWr4tqU` | Romeo Santos | 693,619,409 | **Gated.** One urbano slot. Official video, not the Topic `NQrgT3cJR2Y` (131M). |
| 14 | Romeo Santos | You | 2011 | `ElU-VcWEhRU` | RomeoSantosVEVO | 236,951,876 | |
| 15 | Romeo Santos | Llévame Contigo | 2011 | `VafbNsrHnD8` | RomeoSantosVEVO | 185,175,148 | Official audio. MSG live `_uqZYZxleqA` is 118M — audio is cleaner for the dock. |

14–15 are both Romeo. **Swap 15 to *Sus Huellas* only if 14 changes**, or put *Sus Huellas* at 15 after a Royce. Cleaner close: **15 Prince Royce *Deja Vu*** (`XEvKn-QgAY0`) if Javy will share it with dryer HOY. Duplicate-across-filters is allowed. Consecutive-same-artist is not.

**Out of Silla HOY:** Toby Love (2006 + English R&B), *Odio* Drake, *Stand by Me* (2010 English, site `PPgQ4nDLh0s` is Planet not VEVO), *Promise* Usher as opener, Antony *Celoso* 2026 until an official id is walked, Zacarías 2024/25 until official ids beat the old *El Triste* / *Amiga Veneno* already in the room.

### Hoy en la esquina

Street now. Yiyo/Chiquito first. Urbano gated at the back. **Do not open on view-rank salsa-TV.**

| # | Artist | Title | Year | Official id | Channel | Views 2026-08-16 | Notes |
|---|---|---|---:|---|---|---:|---|
| 1 | Yiyo Sarante | Manos de Tijera | 2021 | `ExCIp6TOnJw` | Yiyo Sarante | 357,150,375 | Official. This is the esquina-HOY opener. Already in `colmado.json` after the 15. |
| 2 | Chiquito Team Band | La Llamada De Mi Ex | 2016 | `u6Q5Lu0Sq3g` | Chiquito Team Band | 70,446,183 | Official. Buried at Esquina #85 today. HOY home. |
| 3 | Yiyo Sarante | Qué Agonía | 2021 | `eHsR140M2no` | Yiyo Sarante | 117,766,533 | Official. |
| 4 | Chiquito Team Band | Tengo Que Colgar | 2017 | `A0f-FDFpPZE` | Chiquito Team Band | 23,069,258 | Official. |
| 5 | Yiyo Sarante | Mi Todo | 2021 | `JXLNr85yoKk` | Yiyo Sarante | 87,510,416 | Official. |
| 6 | Chiquito Team Band | Lejos De Ti | 2014 | `8820jXsE4kQ` | Planet Records Official | 16,880,543 | Official HD. Same id already in Esquina/Marquesina catalogs. |
| 7 | Juan Luis Guerra 4.40 | Kitipun | 2019 | `hpkaifThmOs` | JuanLuisGuerraVEVO | 27,100,061 | Dominican poet *now*. Not *A Pedir Su Mano*. |
| 8 | Romeo Santos ft. Marc Anthony | Yo También | 2015 | `QBaIMZ8QjcU` | RomeoSantosVEVO | 901,612,309 | Time-correct salsa-bachata. |
| 9 | Manny Cruz, Los Hermanos Rosario | La Dueña del Swing | 2025 | `4R7NmEa8s8M` | Manny Cruz | 1,704,510 | **Remake.** Original 90s cut stays in Marquesina room. Low views, correct lock. |
| 10 | Marc Anthony | Vivir Mi Vida | 2013 | `YXnjy5YlDwk` | marcanthonyVEVO | 1,312,641,595 | **Late, not opener.** Old Esquina ban stands for the room. HOY can hold the time. |
| 11 | Juan Luis Guerra 4.40 | I Love You More | 2019 | `dUOC-ryYtQI` | JuanLuisGuerraVEVO | 2,513,369 | Official. Small views, correct decade. |
| 12 | Aventura, Bad Bunny | Volví | 2021 | `ayd3yWr4tqU` | Romeo Santos | 693,619,409 | Gated urbano. One slot. |
| 13 | Romeo, Daddy Yankee, Nicky Jam | Bella y Sensual | 2017 | `RSRzIrOqaN4` | RomeoSantosVEVO | 827,105,085 | Gated. Last third. |
| 14 | Manny Cruz, Johnny Ventura | Qué Rico Es El Merengue | 2021 | `cenRb14_sMY` | Manny Cruz | 1,420,925 | Revival with the old voice. Family-safe enough for esquina *and* marquesina. |
| 15 | El Alfa, CJ, El Cherry Scom | La Mamá de la Mamá | 2021 | `s5yRZOQ3EWI` | ElAlfaElJefeTV | 246,403,408 | **One dembow receipt. Last. Official only.** Never copy into dryer/silla/marquesina HOY. |

**Out of Esquina HOY opener:** Gente de Zona *La Gozadera* (`VMp55KH_3wo`, 1,754,757,037, GenteDeZonaVEVO). That is the Son by Four trap — 1.75B, Cuban TV carnival, not a Dominican colmado. If Javy wants one party-salsa now-cut, put it after #10, never first.

**Out entirely:** Tokischa, Rochy RD, Farruko *Pepas*, *Despacito*, salsa monuments already in the room (*Pedro Navaja*, *El Cantante*).

### Hoy en la marquesina

Family lot. New merengue / new cuts of old merengue. **Honest gap:** revival does not have billion-view official clips. Do not pad with 1998 *Suavemente*.

| # | Artist | Title | Year | Official id | Channel | Views 2026-08-16 | Notes |
|---|---|---|---:|---|---|---:|---|
| 1 | Chiquito Team Band | La Llamada De Mi Ex | 2016 | `u6Q5Lu0Sq3g` | Chiquito Team Band | 70,446,183 | Already in `marquesina.json` after the 15. HOY opener. |
| 2 | Juan Luis Guerra 4.40 | Kitipun | 2019 | `hpkaifThmOs` | JuanLuisGuerraVEVO | 27,100,061 | |
| 3 | Chiquito Team Band | Tengo Que Colgar | 2017 | `A0f-FDFpPZE` | Chiquito Team Band | 23,069,258 | |
| 4 | Manny Cruz, Los Hermanos Rosario | La Dueña del Swing | 2025 | `4R7NmEa8s8M` | Manny Cruz | 1,704,510 | Remake. Original stays on the room plate. |
| 5 | Chiquito Team Band | Lejos De Ti | 2014 | `8820jXsE4kQ` | Planet Records Official | 16,880,543 | |
| 6 | Manny Cruz, Johnny Ventura | Qué Rico Es El Merengue | 2021 | `cenRb14_sMY` | Manny Cruz | 1,420,925 | Dead maestro + living revival. Marquesina lock. |
| 7 | Juan Luis Guerra 4.40 | I Love You More | 2019 | `dUOC-ryYtQI` | JuanLuisGuerraVEVO | 2,513,369 | |
| 8 | Manny Cruz | All Night Long | 2024 | `S3h4xmU-qQM` | Manny Cruz | 2,859,828 | Official merengue 2024. English title, merengue body. Mid-15 only. |
| 9 | Manny Cruz | OYE | 2025 | `vEDn-xoL4Ss` | Manny Cruz | 1,094,193 | Official. Thin views, correct lock. |
| 10 | Ilegales | Meneo | 2020 | `-gCgSXFctOQ` | ILEGALES | ~1.3M (search; re-verify before JSON) | Official 2020 merenhouse. **Re-oembed before ship.** |
| 11 | Ilegales | Baila Conmigo | 2021 | `ERlLjPvgDJA` | ILEGALES | ~277K (search; weak) | Official but small. Swap if a stronger official merengue-revival id appears. |
| 12 | Yiyo Sarante | Manos de Tijera | 2021 | `ExCIp6TOnJw` | Yiyo Sarante | 357,150,375 | Allowed as “still playing” guest, not a salsa-monument takeover. One Yiyo max here. |
| 13–15 | **OPEN** | Official merengue revival only | 2011–2026 | — | artist / VEVO / Planet | — | Need walked official ids for: Eddy Herrera 2010s, Toño Rosario later, Grupo Manía later, Vakeró merengue, Miriam Cruz later (Chiquito *Tu Recuerdo* `PDUBTtive2A` is only 117k — too thin). **Do not fill with Omega mixes or 90s originals.** |

**Omega:** *Si Te Vas* is 2009 (outside the 15-year window). Official Topic uploads are 0.5–1.5M. The heat lives on unofficial mixes. **Hold Omega** until a clean official single-track id inside the window beats a mix. Do not use DJ merengue-electrónico rips.

**Rubby Pérez later work:** do not use as a marquesina-HOY party cut without Javy. Jet Set, 2025.

---

## 5. UX

**One chip. Four rooms keep their plates.**

```
[ Secador ] [ Silla ] [ Esquina ] [ Marquesina ]   [ HOY ]
```

- HOY sits in the **same** `.rooms` nav, last, as a chip — not a second wordmark, not a fifth painted place.
- Visual difference: same caps/weight as room chips, plus a small time mark (dot, or the letters HOY only). Do not invent a fifth color plate.
- `h1.wordmark` stays `Bajo el / secador` (or the room you are in).
- `p.kicker` is the only chrome that changes (see §1).
- Heroes stay `assets/{salon,barberia,colmado,marquesina}.jpg`. HOY does **not** get a DSA plate.
- Dock, vinyl, authored order, no shuffle — same bones.
- YT Music pill: when HOY is on, point at the HOY playlist for **that filter**, not the old-school room list. Marquesina still has no room playlist (`music.youtube.com/` empty) — do not ship HOY Marquesina pill until a list exists.
- Hash: `#salon` + `data-hoy="1"`. Not `#hoy`. Not `#hoy-secador` as a place.
- Room change after first gesture starts **that filter’s** HOY index 0 if HOY is on.
- Same dual-host player. Fade room→HOY like room→room. **Never two iframes PLAYING.**

### What not to build

- A fifth wordmark “Hoy en el / secador”.
- A live “what’s hot on YouTube” scrape.
- HOY as a global mix that ignores the room.
- Two radios (HOY audio under old-school audio).
- Spotify.

---

## 6. Risks

| Risk | How it shows up | Prevention |
|---|---|---|
| **Chart sludge** | *La Gozadera* (1.75B), *Vivir Mi Vida* (1.31B), *Despacito* jump the first 15 | Same rule as rooms: views rank *inside* the pool. Never pick the opener. Ban the sludge class in §3. |
| **Date rot** | 2011 Romeo is 15 years old in 2026; in 2028 it is old-school by this spec | Pin the window in data (`year: 2013`). Re-walk HOY every 2–3 years. 2010 Royce is already date-edge. |
| **ToS / two radios** | HOY + room both `PLAYING`; iOS + YouTube RMF | One queue. Catalog swap. Existing 1.1s/1.3s fade. Do not bring back overlapping playback. |
| **Two radios (product)** | User thinks HOY is a fifth station and the room died | Chip + kicker only. Plate stays. Copy: HOY is *lo de ahora* in this room, not a new place. |
| **Poisoning the old rooms** | HOY ids get merged into `barberia.json` intros “because they’re official” | Hard split: HOY JSON is separate. Old first 15 may **lose** 2013 Romeo/Royce; they may not **gain** Yiyo. |
| **Wrong twin ids** | Site *Eres Mía* `vY_3YrKtUUE` is 1.02M audio; official is `8iPcqtHoR3U` at 1.34B | HOY uses the oEmbed-checked id. Audit table below. |
| **Romeo stack** | 8/15 Romeo because he *is* the 2010s | Interleave Royce / Utopía guests / Aventura reunion. Same “no consecutive artist” room rule. |
| **Marquesina thinness** | Revival official clips are 1–3M, not 1B | Do not pad with 90s merengue. Leave slots 13–15 open rather than fake them. |
| **Urbano creep** | El Alfa #15 becomes El Alfa #3 next pass | Hard cap: ≤1 explicit dembow, Esquina HOY only, last third. |
| **Marquesina pill** | HOY on Marquesina opens a blank `music.youtube.com/` | No pill until a real unlisted HOY playlist exists. |

### Site id vs official twin (do not copy these site ids into HOY)

| Song | Site id | Site signal | Official HOY id | Official views |
|---|---|---|---|---:|
| Romeo — Eres Mía | `vY_3YrKtUUE` | 1,024,433 · “Eres Mía Audio” | `8iPcqtHoR3U` | 1,338,681,355 |
| Romeo — Promise | `yUTlRzOkOX4` | 6,723,576 · Walmart Acceso Total | `Y3XyWhrZnqE` | 382,796,772 |
| Romeo — Odio | `ka58yy5Sd0Q` | 1,107,161 · live | `W8r-eIhp4j0` | 500,993,453 |
| Royce — Corazón Sin Cara | `ZNN7NTl83cI` | 54,394,899 · Planet | `XNGWDH-6yv8` | 281,969,595 |
| Royce — Las Cosas Pequeñas | `UHC7ITw9wPY` | 5,249,199 · VEVO audio | `ROzZSmaxDz8` | 83,602,948 |

*Promise* / *Odio* official twins are listed for completeness. They stay **out** of dryer HOY even with the better id.

---

## 7. What to do to the old rooms (not in this pass)

When HOY ships, old-school first 15s should lose the time-layer that is already leaking:

| Room | Currently leaking into old first 15 / catalog | HOY destination |
|---|---|---|
| Silla | #2 *Propuesta*, #3 *Darte un Beso*, #9 *Eres Mía* (live JSON; LIST-REVIEW already questioned Royce/Romeo weight) | Silla HOY + Secador HOY |
| Silla catalog | *Imitadora*, *Cancioncitas*, *Hilito*, *Promise*, *Odio*, extra Royce | Silla HOY (except *Promise*/*Odio*) |
| Esquina | Yiyo 17/23/26, Chiquito 85/86 | Esquina HOY first 15. Optional: keep one deep in the room catalog, not the intro. |
| Marquesina | Chiquito after the 15 | Marquesina HOY opener |

Aventura *Obsesión*, Antony *Voy Pa’llá*, Luis Vargas, Raulín *Nereyda*, JLG *A Pedir Su Mano*, Rosario *Dueña* (original), *Suavemente* — **stay**. Those are place + memory.

---

## 8. Implementability notes (for planner, not this pass)

- New files, not edits to room intros: `public/hoy-salon.json`, `hoy-barberia.json`, `hoy-colmado.json`, `hoy-marquesina.json` (or one `hoy.json` keyed by room).
- `intro: true` on each authored 15. `shuffle: false`. Official `youtube` urls.
- Player: `data-hoy` flag; `loadHoy(room)` fetches HOY JSON; `buildQueue()` unchanged (catalog order).
- Do not add a `ROOMS.hoy` place object with its own plate/theme.
- Covers: reuse `assets/covers/{id}.jpg` when the id already exists; fetch iTunes/Deezer squares for new ids. No `maxresdefault` on the vinyl.
- YouTube playlists: four unlisted HOY lists, sync with `scripts/sync-youtube-playlists.py` after Javy signs in. Marquesina room list is still empty — do not block HOY research on that.

---

## Analyst Review: HOY tab

### Missing Questions

1. Does Javy want *Propuesta Indecente* **removed** from old Silla #2 the day HOY ships, or left as the one 2010s bridge? — Decides whether Silla stays típica-first or keeps a diaspora-wow leak.
2. Is El Alfa *La Mamá de la Mamá* allowed as Esquina HOY #15, or is “carefully gated urbano” = Romeo-urbano only (no dembow at all)? — This is the only explicit dembow in the four lists.
3. Are duplicate ids across filters OK (*Propuesta* in dryer HOY and silla HOY)? — Affects playlist sync and “did I already hear this.”
4. Who re-walks HOY when 2011 ages out — Javy, or a dated review every 24 months? — Date rot is guaranteed.
5. Marquesina HOY slots 13–15: wait for official merengue-revival ids, or ship a 12-song list? — Shipping a fake 15 will pad with 90s cuts and poison the room.

### Undefined Guardrails

1. Time window — **Suggested:** `releaseYear >= 2011` inclusive, review in 2028. 2010 Royce is opt-in only.
2. Urbano cap — **Suggested:** 0 on Secador / Silla / Marquesina HOY. ≤1 on Esquina HOY, last third, official, not Tokischa/Rochy/club edit.
3. Artist gap — **Suggested:** same as rooms, no consecutive same artist, min ~7 in the full HOY catalog.
4. View floor — **Suggested:** none for Utopía guests / Manny Cruz remakes. Floor only as a *warning* under 1M (re-check official).
5. Two-player — **Suggested:** existing fade; forbid overlapping `PLAYING`. HOY is not a second station.

### Scope Risks

1. HOY becomes a fifth painted room — Prevent: no plate, no `#hoy` place, chip + kicker only.
2. Chart-sludge first 15 — Prevent: authored lists in this file; ban *La Gozadera* as opener; views are a column, not a sort.
3. Merging HOY into room JSON “to keep one catalog” — Prevent: separate files. Rooms may lose 2013 hits; they do not gain Yiyo in the intro.
4. Urbano creep on the next pass — Prevent: write the cap into the HOY JSON header comment / kicker copy.
5. Building live YouTube search — Prevent: static authored JSON, same as rooms.

### Unvalidated Assumptions

1. Javy agrees rooms = place + memory and HOY = time — Validate: he already wrote that split in `RESEARCH-SPEC.md`; confirm the Silla *Propuesta* move.
2. Official lyric/audio VEVO counts as “official YouTube” (Imitadora lyric 797M vs MV 253M) — Validate: rooms already use official audio/Topic. Same rule.
3. A real esquina speaker in 2026 still plays Yiyo/Chiquito more than El Alfa — Validate: street listen + Javy walk, not Billboard Tropical.
4. Marquesina families will accept Chiquito as “today’s merengue” — Validate: Javy walk of #1–6 only.
5. RYD view counts match what YouTube shows in Chrome — Validate: spot-check 3 ids in signed-in Chrome before any JSON write.

### Missing Acceptance Criteria

1. HOY chip visible next to room nav, not a fifth wordmark — Pass: one control labeled HOY; `h1` unchanged when toggled.
2. Plate unchanged when HOY turns on — Pass: `data-scene` / hero asset still the current room.
3. Secador HOY first 15 contains zero dembow / *Pepas* / *Volví* / *Bella y Sensual* / *Odio* / *Promise* — Pass: list match.
4. Esquina HOY opens on Yiyo or Chiquito, not *La Gozadera* / *Vivir Mi Vida* — Pass: index 0 is `ExCIp6TOnJw` or `u6Q5Lu0Sq3g`.
5. Old room intros do not gain HOY ids in this research pass — Pass: no `public/*.json` edits.
6. One YouTube player `PLAYING` after room↔HOY fade — Pass: Shift+D shows a single `yt:playing`.
7. Every shipped HOY id oEmbeds to VEVO / artist / Planet / label Topic — Pass: script + hand check.
8. No consecutive same artist in each HOY 15 — Pass: scan.

### Edge Cases

1. User lands on `#salon?hoy=1` cold — Load Secador plate + Secador HOY catalog; do not autoplay (browser rule).
2. HOY on, user taps Esquina — Stay in HOY, swap to Esquina HOY, index 0, same fade.
3. HOY id embed-blocked (error 150/153) — Same as rooms: retry same id 3×, then skip. Do not fail-forward into a room track.
4. Marquesina HOY with empty YT Music pill — Hide pill or keep it disabled; do not open a blank Music homepage.
5. Same id in dryer HOY and silla HOY — Allowed. Queue is per filter. Do not dedupe across rooms.
6. 2011 track on 2028 revisit — Year field flags it; do not auto-promote into the old room.
7. Chiquito/Yiyo still sitting in old Esquina catalog after HOY ships — Allowed after the intro. Not in the old first 15.

### Recommendations

1. **Lock the architecture:** one HOY chip, four filtered JSON rails, plates stay.
2. **Walk Silla first:** moving *Propuesta* / *Darte un Beso* / *Eres Mía* off the old first 15 is the whole point. If Javy keeps *Propuesta* in old Silla, HOY still exists but the poison remains.
3. **Walk Esquina HOY opener as Yiyo**, not Marc Anthony, not *La Gozadera*.
4. **Hard-ban dryer:** explicit dembow, club edits, Drake, Bad Bunny verse, *Bella y Sensual*.
5. **Gate Esquina #15 El Alfa** as an explicit Javy yes/no before planning.
6. **Do not ship Marquesina HOY 15** until slots 13–15 have official merengue-revival ids, or ship 12.
7. **Replace weak site twins** when HOY is implemented (`Eres Mía`, *Corazón Sin Cara*, *Las Cosas Pequeñas*).
8. **Planner next:** HOY JSON shape + chip UX + catalog split. Not live JSON edits in this pass.

---

## Open Questions

- [ ] Remove *Propuesta Indecente* / *Darte un Beso* / *Eres Mía* from old Silla first 15 when HOY ships, or keep one 2010s bridge? — Decides whether the time/place split is real.
- [ ] El Alfa *La Mamá de la Mamá* as Esquina HOY last slot: yes, no, or “Romeo-urbano only”? — Only explicit dembow proposed.
- [ ] Duplicate the same official id across HOY filters (*Propuesta* in dryer + silla)? — Playlist and listening-repeat implications.
- [ ] Ship Marquesina HOY as 12 songs, or wait for 3 more official merengue-revival ids? — Prevents padding with 90s room cuts.
- [ ] Confirm official lyric/audio VEVO (*Imitadora* lyric, *Necio* audio, *Llévame Contigo* audio) is acceptable when the MV is weaker or missing. — Player already allows official audio in rooms.
- [ ] Who owns the 24-month date-rot review, and is 2010 Royce in or out? — *Corazón Sin Cara* is the test case.
