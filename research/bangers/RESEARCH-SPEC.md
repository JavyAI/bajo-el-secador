# Bangers research spec — old school rooms + optional HOY

**Started:** 2026-08-16  
**Rule:** rooms stay **old school**. Views rank *inside* the cultural pool. Views do **not** pick the first 15. Javy already rejected a view-rank pass that put Son by Four first in Esquina.

## Product split

| Rail | Time | Job |
|---|---|---|
| Room (Secador / Silla / Esquina / Marquesina) | Mostly pre-2012, típico, tía/barbero/esquina/15s memory | Place + feeling. Authored first 15. |
| **HOY** (proposed tab) | Last ~10–15 years, still official YT | *What’s playing now* without poisoning the rooms. |

HOY is a **time** rail, not a fifth place. One HOY tab, optionally filtered by the room you’re in (`Hoy en la silla` = current bachata, not dembow under the dryer).

## Room locks

| Room | Crowd | Old-school pool | Ban from first 15 / core 100 |
|---|---|---|---|
| Secador | Women, dryer, tía radio | Baladas, bolero, Olga merengue sentimental | Club Luismi as #2; Mexican fiesta (Amor a La Mexicana); chart ballads that aren’t dryer-cry |
| Silla | Men, barbería, diaspora | Bachata típica first, then Aventura/Romeo | English/Spanglish R&B-bachata (Toby Love); Don Omar-led Aventura as opener; teen-pop Royce stacking |
| Esquina | Street / colmado | Salsa dura + merengue de fiesta | Son by Four as opener; Cali pride salsa; third JLG bachata as closer |
| Marquesina | Family lot, 15s, night | Merengue de fiesta, merenhouse, 90s–00s | Salsa monuments (Pedro Navaja); dominó (that’s Esquina); club 2024 dembow |

## Ranking method (research only)

1. Build a culturally correct candidate pool (memory, radio, ritual).
2. Attach official YouTube ids when found.
3. Sort that pool by **view count** as a resonance signal.
4. Hand-check: would this body say wow in 15 seconds *in this room*?
5. Deliver **top 100** with era, views (if known), official id, keep/flag.

Do not rewrite live JSON in this pass. Research files only.

## Outputs

- `secador-100.md`
- `silla-100.md`
- `esquina-100.md`
- `marquesina-100.md`
- `hoy-tab.md`
