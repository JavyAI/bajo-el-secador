# Esquina AYER / HOY — first 15s

**Room:** En la esquina (`#colmado`)  
**Job:** sidewalk / colmado speaker. AYER = salsa dura + merengue de fiesta through ~2010. HOY = what is still playing now.  
**Date:** 2026-08-16  
**Rule:** culture locks the pool. Virality × sentiment × fame ranks *inside* the lock. Views do **not** pick #1.  
**Forgotten #1:** Elvis Crespo — *Suavemente*. **Not** Son by Four.

Live `public/colmado.json` was **not** edited.

---

## [OBJECTIVE]

Author the two time-rails for this room.

- **AYER** first 15: doorway of the old colmado. *A Pedir Su Mano* stays #1. Include the culturally correct overtaken hit as forgotten #1. Drop story/sensual openers that fail the first-15-seconds test.
- **HOY** first 15: Yiyo / Chiquito first. No *A Puro Dolor*. No *La Gozadera* first. *Vivir Mi Vida* only late. One gated urbano receipt at the back.

Test for both: *would a Dominican on the esquina say wow in the first 15 seconds — in this year?*

---

## Method

1. Split the locked esquina-100 pool at the era cut (`year <= 2010` → AYER; `2011–2026` → HOY). Yiyo / Chiquito leave AYER even if they sit in the live catalog.
2. Hard-ban from AYER: Son by Four, Niche *Cali Pachanguero*, JLG bachata (*Bachata Rosa*, *Burbujas*). Hard-ban from HOY opener: *A Puro Dolor*, *La Gozadera*, *Vivir Mi Vida*, *Despacito*.
3. Score every remaining track  
   **V** = log10(official YouTube views, scrape 2026-08-16)  
   **S** = doorway sentiment 1–5 (first 15 seconds on this speaker)  
   **F** = sidewalk fame 1–5 (does the block already know it)  
   **VSF** = V × S × F. Log-compression is required: raw views × S × F re-creates the Son by Four trap.
4. Lock AYER #1 = *A Pedir Su Mano*. Forgotten #1 = highest VSF among doorway-correct AYER tracks (S≥4 and F≥4). That winner sits at #2 — not instead of #1.
5. Fill 3–15 by VSF with genre interleave (no three merengues on the door), required names, and **no consecutive same artist**. Max 3 JLG.
6. Lock HOY 1–6 as Yiyo / Chiquito alternating. Fill 7–15 by VSF with the same artist-gap rule. Urbano gated to the last third. *Vivir Mi Vida* late. *La Gozadera* stays out.

S and F are expert codes from `esquina-100.md` / `hoy-tab.md`, not a street survey.

---

## [DATA]

- Live catalog `public/colmado.json`: **86** tracks, `introCount` 15.
- AYER pool: **95** pre-2011 locked tracks (Yiyo/Chiquito and the four AYER bans removed).
- Doorway-correct subset (S≥4 and F≥4): **44**.
- HOY candidate set: **16** official clips (Yiyo ×3, Chiquito ×3, revival, 2010s salsa-radio, gated urbano, plus *La Gozadera* as the reject).
- Views: same 2026-08-16 official scrape as esquina-100 + hoy-tab.

[STAT:n] n_AYER = 95; n_doorway = 44; n_HOY_cand = 16; authored = 15 + 15

---

## Score rubric

| S | First 15 seconds on this speaker |
|---|---|
| 5 | Instant shout / piano tumbao / merengue bomb |
| 4 | Dance/fiesta that already swings |
| 3 | Outdoor romántica. Radio-soft open. 100-yes, 15-no |
| 2 | Story / walking-bass / quiet narrative |
| 1 | Bedroom sensual, TV-pop, or wrong room |

| F | Sidewalk fame |
|---|---|
| 5 | National reflex. Everyone on the block sings it |
| 4 | Required corner name / colmado regular |
| 3 | Known and requested |
| 2 | Deep catalog |
| 1 | Thin / specialists |

---

## AYER first 15

True #1 locked. Forgotten #1 at #2. Genre interleaved after two merengue bombs. No consecutive artist. JLG at 1 / 6 / 11 only.

| # | Artist | Title | Year | Genre | Official id | Catalog id | Views | S | F | VSF | Role |
|---:|---|---|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | Juan Luis Guerra | A Pedir Su Mano | 1990 | merengue | `_koz_f4mthE` | `_koz_f4mthE` | 15.4M | 5 | 5 | 179.7 | **TRUE #1** |
| 2 | Elvis Crespo | Suavemente | 1998 | merengue | `WPiEbYSF9kE` | `WPiEbYSF9kE` | 299.4M | 5 | 5 | 211.9 | **FORGOTTEN #1** |
| 3 | El Gran Combo | Me Liberé | 1988 | salsa | `frsVQWSINAI` | `frsVQWSINAI` | 39.2M | 5 | 5 | 189.8 | Combo piano. Breaks the merengue stack |
| 4 | Los Hermanos Rosario | La Dueña del Swing | 1995 | merengue | `HN6ACmknaiw` | `rOw9UxJyhII` | 158.4M | 5 | 5 | 205.0 | Merengue royalty. Rank on Topic |
| 5 | Joe Arroyo | Rebelión | 1986 | salsa | `oWBf9hfW_4Y` | `oWBf9hfW_4Y` | 33.2M | 5 | 5 | 188.0 | Claimed salsa. Instant wow |
| 6 | Juan Luis Guerra | La Bilirrubina | 1990 | merengue | `McV4pBRb-Sg` | `McV4pBRb-Sg` | 53.7M | 5 | 5 | 193.3 | JLG that moves the block |
| 7 | Héctor Lavoe | El Cantante | 1978 | salsa | `BNo0vkEYWRc` | `BNo0vkEYWRc` | 101.0M | 4 | 5 | 160.1 | Fania prayer. Was live #2 |
| 8 | Wilfrido Vargas | El Africano | 1983 | merengue | `1DbXzlhKS5s` | `1DbXzlhKS5s` | 5.3M | 5 | 5 | 168.1 | THE merengue. Clip undercounts |
| 9 | Oscar D'León | Llorarás | 1975 | salsa | `gxlB1B9emDc` | `gxlB1B9emDc` | 157.9M | 4 | 5 | 164.0 | Colmado singalong |
| 10 | Celia Cruz | La Vida Es Un Carnaval | 1999 | salsa | `AFYJ5axf02o` | `AFYJ5axf02o` | 72.6M | 4 | 5 | 157.2 | Raises a Presidente |
| 11 | Juan Luis Guerra | El Costo de La Vida | 1992 | merengue | `tPTB0TRV3BA` | `tPTB0TRV3BA` | 6.1M | 4 | 5 | 135.8 | Talks on the esquina. Already walked |
| 12 | Cuco Valoy | Juliana | 1983 | salsa | `y08MAPIACBY` | `y08MAPIACBY` | 4.4M | 4 | 5 | 132.9 | Dominican salsa receipt |
| 13 | Frankie Ruiz | Deseándote | 1989 | salsa | `N8kGeGXddxg` | — | 136.0M | 4 | 4 | 130.1 | Frankie the corner streams. Not in live JSON |
| 14 | Willie Colón y Héctor Lavoe | El Día de Mi Suerte | 1973 | salsa | `mXZRB_al3fs` | `mXZRB_al3fs` | 113.3M | 4 | 4 | 128.9 | Willie shout. Not *Gran Varón* |
| 15 | Rubén Blades | Decisiones | 1984 | salsa | `GyhwmZAQB-Y` | `GyhwmZAQB-Y` | 63.2M | 4 | 4 | 124.8 | Blades with body. Not *Pedro Navaja* |

Mix: **6 merengue / 9 salsa**. JLG ×3, never consecutive. Artist-gap scan: **pass**.

[FINDING] *Suavemente* is the forgotten #1: highest VSF in the doorway-correct AYER pool, including the locked true #1.
[STAT:effect_size] VSF Suavemente = 211.9 vs A Pedir Su Mano = 179.7 (ratio 1.18)
[STAT:effect_size] views Suavemente / A Pedir = 19.43× (299.4M / 15.4M)
[STAT:n] n_doorway = 44; Suavemente is rank 1 by VSF, rank 1 by views inside that subset

Dueña del Swing is the runner-up overtaken hit (VSF 205.0). *El Cantante* (160.1) and *Rebelión* (188.0) stay in the 15. They are almost-#1 *candidates*. They lose the slot at #2.

### Why Son by Four is not the forgotten #1

Son by Four — *A Puro Dolor* is the cautionary tale, not the overtaken hit. 746.6M official views. Wrong room (salsa-romántica ballad). Javy already killed a view-rank pass that put it first.

| Track | Room? | Views | S | F | VSF |
|---|---|---:|---:|---:|---:|
| Suavemente | Yes. Merengue bomb | 299.4M | 5 | 5 | **211.9** |
| Dueña del Swing | Yes. Dominican royalty | 158.4M | 5 | 5 | 205.0 |
| A Pedir Su Mano | Yes. True doorway | 15.4M | 5 | 5 | 179.7 |
| El Cantante | Yes. Fania prayer | 101.0M | 4 | 5 | 160.1 |
| Rebelión | Yes. Claimed salsa | 33.2M | 5 | 5 | 188.0 |
| **Son by Four — A Puro Dolor** | **No** | **746.6M** | **1** | **2** | **17.7** |

[FINDING] Son by Four has 48.5× the views of the true #1 and 2.49× the views of the forgotten #1, and still finishes last on VSF.
[STAT:effect_size] views Son / A Pedir = 48.47×
[STAT:effect_size] VSF Suavemente / Son = 11.94× (211.9 / 17.7)
[STAT:n] two official clips, same scrape window

Sensitivity: treat Son as romántica (S=3, F=3) → VSF = 79.9, still below the AYER-pool median (90.8) and far below Suavemente. Son only “wins” if you illegally give it S=5 F=5 (VSF 221.8). That is the product failure mode. Do not.

### Live 15 → this 15

| Live # | Track | Action |
|---:|---|---|
| 1 | A Pedir Su Mano | **KEEP** #1 |
| 2 | El Cantante | KEEP, slide to #7 |
| 3 | Suavemente | **PROMOTE** to #2 (forgotten #1) |
| 4 | Carnaval | KEEP, slide to #10 |
| 5 | El Gran Varón | **OUT** — story, VSF 78.7 |
| 6 | Me Liberé | KEEP, promote to #3 |
| 7 | Pedro Navaja | **OUT** — story, VSF 75.6 |
| 8 | Bilirrubina | KEEP #6 |
| 9 | Rebelión | KEEP #5 |
| 10 | El Africano | KEEP #8 |
| 11 | Dueña del Swing | KEEP, promote to #4 |
| 12 | Desnúdate Mujer | **OUT** — sensual, VSF 20.0 |
| 13 | Llorarás | KEEP #9 |
| 14 | Juliana | KEEP #12 |
| 15 | El Costo | KEEP #11 |

**In:** *Deseándote* (not in live JSON), *El Día de Mi Suerte* (live catalog after the 15), *Decisiones* (live catalog after the 15).

[FINDING] Replacing the three FLAG live openers lifts mean VSF of the 15 from 150.7 to 164.6.
[STAT:effect_size] mean VSF +13.97 (+9.3%)
[STAT:n] n = 15 vs 15
[STAT:ci] authored-15 median VSF = 164.0; bootstrap 95% CI [135.8, 189.8] (2000 resamples)

### Views still do not reconstruct the 15

Naive view-sort of the AYER pool opens Valió la Pena (410M) / Qué Hay de Malo (406M) / Suavemente / Fabricando Fantasías / Yo No Sé Mañana. Romántica radio. Not a doorway.

[FINDING] View-top-15 overlap with this authored AYER 15 is 6/15.
[STAT:n] overlap = 6/15 = 40%
[STAT:effect_size] Spearman ρ(views, VSF) = 0.42 on n = 95. Related, not the same ranking.

Authored 15 vs the other 80 AYER tracks: Mann–Whitney U = 26, z = −5.86, p = 4.7×10⁻⁹, rank-biserial r = 0.96. The 15 sits in the VSF tail on purpose. That is selection, not a claim that VSF “discovered” a hidden 15.

### Greedy VSF (not the walk list)

If you ignore genre interleave and required-name coverage after locking #1 and forgotten #1, greedy VSF opens *A Pedir / Suavemente / Dueña* (three merengues) and swaps *El Costo* for *Ojalá*. It also stacks extra Celia (*Quimbara*, *La Negra*) and drops Frankie / Willie-shout / Blades-body.

**Do not ship the greedy list.** Combo at #3 is the authored break: piano tumbao after two merengue bombs. *El Costo* stays because it was already walked into the live 15 and it talks on this corner. *Ojalá*, *Quimbara*, *Che Che Colé*, Sergio *La Quiero a Morir* (VSF 120.5) are the first cuts after the 15.

---

## HOY first 15

Yiyo / Chiquito first. Then VSF inside the HOY lock. Urbano last third. No *A Puro Dolor*. No *La Gozadera*. *Vivir Mi Vida* at #10.

| # | Artist | Title | Year | Genre | Official id | Views | S | F | VSF | Role |
|---:|---|---|---:|---|---|---:|---:|---:|---:|---|
| 1 | Yiyo Sarante | Manos de Tijera | 2021 | salsa | `ExCIp6TOnJw` | 357.2M | 5 | 5 | 213.8 | **HOY opener.** Already in live catalog after the 15 |
| 2 | Chiquito Team Band | La Llamada De Mi Ex | 2016 | merengue | `u6Q5Lu0Sq3g` | 70.4M | 5 | 4 | 157.0 | House band. Buried at live #85 today |
| 3 | Yiyo Sarante | Qué Agonía | 2021 | salsa | `eHsR140M2no` | 117.8M | 4 | 4 | 129.1 | Second Yiyo |
| 4 | Chiquito Team Band | Tengo Que Colgar | 2017 | merengue | `A0f-FDFpPZE` | 23.1M | 4 | 4 | 117.8 | Official. Not in live JSON |
| 5 | Yiyo Sarante | Mi Todo | 2021 | salsa | `JXLNr85yoKk` | 87.5M | 4 | 4 | 127.1 | Third Yiyo |
| 6 | Chiquito Team Band | Lejos De Ti | 2014 | merengue | `8820jXsE4kQ` | 16.9M | 4 | 4 | 115.6 | Official HD. Already in catalogs |
| 7 | Romeo Santos ft. Marc Anthony | Yo También | 2015 | salsa | `QBaIMZ8QjcU` | 901.6M | 4 | 4 | 143.3 | Sidewalk salsa-bachata. Highest VSF after the house band |
| 8 | Juan Luis Guerra 4.40 | Kitipun | 2019 | merengue | `hpkaifThmOs` | 27.1M | 4 | 4 | 118.9 | Dominican poet *now*. Not *A Pedir* |
| 9 | Manny Cruz, Los Hermanos Rosario | La Dueña del Swing | 2025 | merengue | `4R7NmEa8s8M` | 1.70M | 4 | 3 | 74.8 | **Remake.** 1995 original stays AYER #4 |
| 10 | Marc Anthony | Vivir Mi Vida | 2013 | salsa | `YXnjy5YlDwk` | 1,313M | 2 | 4 | 72.9 | **Late, not opener.** Old-room ban stands |
| 11 | Juan Luis Guerra 4.40 | I Love You More | 2019 | merengue | `dUOC-ryYtQI` | 2.51M | 3 | 3 | 57.6 | Thin views, correct decade |
| 12 | Romeo, Daddy Yankee, Nicky Jam | Bella y Sensual | 2017 | bachata | `RSRzIrOqaN4` | 827.1M | 2 | 3 | 53.5 | Gated. Last third |
| 13 | Aventura, Bad Bunny | Volví | 2021 | bachata | `ayd3yWr4tqU` | 693.6M | 2 | 3 | 53.0 | Gated urbano. One slot |
| 14 | Manny Cruz, Johnny Ventura | Qué Rico Es El Merengue | 2021 | merengue | `cenRb14_sMY` | 1.42M | 4 | 3 | 73.8 | Revival with the old voice |
| 15 | El Alfa, CJ, El Cherry Scom | La Mamá de la Mamá | 2021 | dembow | `s5yRZOQ3EWI` | 246.4M | 2 | 3 | 50.3 | **One dembow receipt. Last. Official only** |

Artist-gap scan: **pass**. Yiyo at 1/3/5, Chiquito at 2/4/6, Romeo at 7/12, JLG at 8/11, Manny at 9/14. *Yo También* (Romeo + Marc) and *Vivir Mi Vida* (Marc) are not adjacent.

[FINDING] Yiyo — *Manos de Tijera* is the HOY opener on VSF, not on a view-rank of tropical YouTube.
[STAT:effect_size] VSF Yiyo = 213.8 vs La Gozadera = 27.7 (ratio 7.71)
[STAT:effect_size] views La Gozadera / Yiyo = 4.91× (1.75B / 357M)
[STAT:n] two official clips

[FINDING] *Vivir Mi Vida* has 3.68× Yiyo’s views and still scores 72.9 vs 213.8 because S=2 (2013 pop-salsa TV). Late is the lock, not a slight.
[STAT:effect_size] VSF Yiyo / Vivir = 2.93
[STAT:n] n = 2 official clips

### Out of HOY on purpose

| Track | Views | VSF | Why |
|---|---:|---:|---|
| Gente de Zona — *La Gozadera* `VMp55KH_3wo` | 1.75B | 27.7 | Next Son by Four. Cuban TV carnival. If Javy wants one party-salsa now-cut, after #10, never first |
| Son by Four — *A Puro Dolor* | 746.6M | 17.7 | 2000, wrong room, wrong rail |
| *Despacito*, Tokischa, Rochy, Farruko *Pepas* | — | — | Chart sludge / explicit / club |
| AYER monuments (*Pedro Navaja*, *El Cantante*, *A Pedir*) | — | — | Place + memory. Stay on the old plate |

Sensitivity: treat *La Gozadera* as romántica (S=3, F=3) → VSF = 83.2, still below every Yiyo/Chiquito cut in slots 1–6.

*Qué Rico Es El Merengue* (VSF 73.8) outscores the gated urbano on purpose. It sits at #14 so the last third can hold the urbano receipts without opening on them. Open Javy question from `hoy-tab.md`: El Alfa at #15 — yes, no, or Romeo-urbano only.

---

## What a naive view-rank would have done

| If you sort… | AYER #1 | HOY #1 | Why it is wrong |
|---|---|---|---|
| All Latin YouTube | *Despacito* 9.10B | *Despacito* | Not a room |
| Tropical / salsa tags | Son by Four 746.6M | *La Gozadera* 1.75B | The two cautionary tales |
| Locked pool, views only | Valió la Pena 410M | Yiyo 357M *or* *Vivir* 1.31B if HOY is unfiltered | Romántica / TV, not the doorway |
| Locked + VSF + authored | **A Pedir Su Mano** | **Manos de Tijera** | Correct |

The HOY trap is the same shape as the AYER trap. *La Gozadera* is to HOY what Son by Four was to AYER: billion-view, wrong room, first-in-line if you sort the spreadsheet.

---

## Flags to walk with Javy

Do not auto-edit `public/colmado.json`.

1. **Forgotten #1 = Suavemente at AYER #2.** Confirm. Dueña as #2 is the Dominican-royalty alternate (VSF 205.0 vs 211.9).
2. **Drop Gran Varón / Pedro Navaja / Desnúdate from the old first 15.** They stay in the catalog after the 15. Replacements are *El Día de Mi Suerte*, *Decisiones*, *Deseándote*.
3. **Deseándote `N8kGeGXddxg` is not in live JSON.** Need a cover fetch if it ships. *La Cura* (`PmXJKVjhbqI`, VSF 122.3) is the shout alternate already on the plate.
4. **Dueña official id.** Rank on Topic `HN6ACmknaiw` (158M). Live catalog still uses `rOw9UxJyhII` (1.66M). Swap the twin when JSON is walked.
5. **HOY El Alfa #15:** yes / no / Romeo-urbano only. Only explicit dembow proposed.
6. **HOY *I Love You More*** is 2.51M. Keep for decade-lock, or swap to a stronger official 2010s merengue if one is walked.
7. **Sergio Vargas *La Quiero a Morir*** (VSF 120.5) and **Ojalá** (VSF 151.1) sit just outside AYER 15. First adds if a slot opens.

---

## [LIMITATION]

- S and F are expert codes from the room notes, not a sampled sidewalk study. A ±1 fame miss on Suavemente (F=4 instead of 5) would hand forgotten-#1 to Dueña. Both remain culturally correct. Son by Four still loses.
- Official view counts measure upload resonance, not colmado play. *El Africano* (5.3M) and *Juliana* (4.4M) are saved by S×F because the official clip undercounts the song. Topic vs video vs live can differ by 10–100× (Dueña 1.66M catalog vs 158M Topic).
- Yiyo *Manos de Tijera* is dated 2015 in the ranked dump and 2021 in `hoy-tab.md` (official video). Either year is HOY. Same for Chiquito *Lejos De Ti* (2014/2016).
- Mann–Whitney on authored-vs-rest is descriptive of the selection, not independent discovery.
- Bootstrap CIs describe this pool only (n = 95 / 15, 2000 resamples). Not a super-population of all salsa/merengue.
- HOY date-rot is guaranteed. 2014 Chiquito is already 12 years old in 2026. Re-walk every 24 months.
- This file does not rewrite live JSON.

---

## Figures

- `.omc/scientist/figures/esquina-ayer-vsf-vs-views.png`
- `.omc/scientist/figures/esquina-ayer-15-vsf.png`
- `.omc/scientist/figures/esquina-ayer-forgotten-1.png`
- `.omc/scientist/figures/esquina-hoy-vsf-vs-views.png`
- `.omc/scientist/figures/esquina-hoy-15-vsf.png`
- `.omc/scientist/figures/esquina-ayer-hoy-mix.png`

## Data

- `.omc/scientist/data/esquina-ayer-hoy-stats.json`
- `.omc/scientist/data/esquina-100-ranked.json` (AYER views)
- `.omc/scientist/analyze_esquina_ayer_hoy.py`
