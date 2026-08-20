# Curator loop — doorway first

One curator per live room. Both eras. Loop until the door is close to 100.

## Live rooms only

Colmado · Secador · Barbería · Limpieza · Galería · Malecón.

Vitilla and Marquesina stay off. Do not stand them up.

On disk Barbería is still `silla.json` / `silla-ayer.json` / `silla-hoy.json`. Hash is `#barberia`.

## Counts

El Ayer **100**. El Presente **100**. Same number. No short HOY. If the era is thin, look **sideways** (same temperature, official 2011+) — do not pad El Presente with 90s hits.

## Doorway = first 15

The first 15 are the 15 best bangers for **this room × this era**. Wow in 15 seconds. Not view-rank. Views only pick the official clip.

After the 15, tracks 16–100 are still bangers. They are not the throne.

## Kings

Some voices own a genre. They may appear more than once.

- Never consecutive same **lead** artist (name before the comma).
- First 15: at most **two** of the same lead, unless the lock names a house pair (Yiyo / Chiquito alternate on Colmado El Presente; JLG may appear twice on Galería; Romeo / Royce may alternate on Barbería / Malecón El Presente).
- In the 100: a king may go to **18**. Anyone else stays ≤ **12**. A dump (Romeo 40) is a fail.

## Authored #1s — do not move

| Room | El Ayer | El Presente |
|---|---|---|
| Colmado | Juan Luis Guerra — *A Pedir Su Mano* `_koz_f4mthE` | Yiyo Sarante — *Manos de Tijera* `ExCIp6TOnJw` |
| Secador | Juan Gabriel — *Amor Eterno* `RgKqxLAhRKE` | Ha*Ash — *Lo Aprendí de Ti* `Uws510cVia4` |
| Barbería | Aventura — *Obsesión* `SEjw5rdyvVg` | Romeo Santos — *Propuesta Indecente* `QFs3PIZb3js` |
| Limpieza | Milly Quezada — *Volvió Juanita* `E6soE-1p3kw` | Toño Rosario — *Dale Vieja Dale* `hal7rXfJj5o` |
| Galería | Juan Luis Guerra — *Ojalá Que Llueva Café* `dDEVFQnBTp0` | Juan Luis Guerra — *Tus Besos* `ncByymoHQRI` |
| Malecón | Juan Luis Guerra — *Burbujas de Amor* `v0ckuv1xBm0` | Camilo, Evaluna Montaner — *Índigo* `DriCCFRQlj8` |

Forgotten / overtaken #1 sits **in** the 15, never as opener.

**No shared doorway:** a song id may appear in the **first 5** of only one live list (any room, any era). *Propuesta* lives in Barbería El Presente. *Darte un Beso* lives there too. Other rooms may keep those songs after slot 5.

## Official only

11-char YouTube id. VEVO / artist / label Topic / Fania / Warner / Karen / JN / Planet. No lyrics, karaoke, DJ mixes, AI, sped-up. Artwork `mqdefault` 200 or `assets/covers/{id}.jpg`.

## Research

Read the locks first: `GENRE-LOCK.md`, `ERA-LOCK.md`, `TITLE-LOCK.md`, `CURATION-SPEC.md`, `SCORECARD.md`, live `public/ayer/{file}.json` and `public/hoy/{file}.json`.

Then look sideways: web search, X/Twitter if the tool is there, YouTube official channels, what a Dominican in **this room** actually hears. Do not copy another room’s first 15.

## Write

Research only: `research/bangers/curation/{file}-ayer.json` and `{file}-hoy.json`. Do not write `public/` unless a later promote step says so.

Score the door 0–40 before you stop. Target **36+** on both eras. Hygiene 30. Identity 30.
