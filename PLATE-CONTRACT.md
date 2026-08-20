# Plate contract — one artist, six rooms

Source of truth: Saloon → Salón grammar
(`prompts/salon-grammar/style-guide.html` + Deluxe Saloon source plate).
The eight laws stay. Only Dominican vocabulary swaps.

This file is the house look for En el secador. Every Ayer and Presente plate
must pass it. The live wordmark and player are HTML. They are never painted.

## Size and export

| Item | Rule |
|---|---|
| Design grid | 2560 × 1435, ~16:9 |
| Generate | Same grammar as Deluxe Saloon. Full STYLE block, not a summary |
| Export | Centered resample to 2560×1435. No re-crop, no reframe |
| Phone | Cover crop of the wide. Portrait plate later |

## Artist look — Salón D'Lujo

One imaginary Dominican illustrator. Not a photograph. Not oil.
Grammar is saloon.wtf. Vocabulary is our six rooms.

1. Flat shapes, hard edges. No outlines. No gradients inside a shape.
2. Faceless figures. Mustache and hair only. No eyes, no mouths.
3. Stage-set camera. Frontal elevation. Zero vanishing point.
4. One cream diagonal beam, upper-left → lower-right.
5. Uniform grain over the whole image as a final pass.
6. Horizontal bands: road · sidewalk · shop · hillside · sky.
7. Focal action at ~55% x, lower-middle.
8. Warm light, cool teal-black shade `#14211E`.

Palette: turquoise `#1B9E96`, coral `#E8503A`, mango `#F2A21B`,
rosa `#F0A8A0`, palma `#3E6B34`, mar `#2277B9`, zinc `#9AA3A8`,
cream `#F2E6CC`.

- Use the full STYLE paragraph from the Deluxe Saloon prompt. Do not shorten it
- Presente is the same canvas with clothes updated. Paint does not change
- No gadget dump. One analog radio or one bocina only
- No painted words, no fake player, no UI
- Barrio Tuesday, not a brochure

Reject: oil, photoreal, clip-art faces, neon, resort props, painted titles, a second artist.

## Hard zones (1536×1024)

| Zone | Pixels | What may live there |
|---|---|---|
| Title reserve | x544–992, y143–445 | Quiet sky, painted wall, or open air. No face, head, hand, tool, roof edge, sun disk, post, wire, seam, or hard contrast |
| Live text inner | x576–960, y175–413 | Empty of story. HTML wordmark sits here |
| Player reserve | x384–1152, y840–983 | Low-detail street, floor, dirt, or promenade. No person, foot, chair, curb, animal, vehicle, tool, or hard shadow |
| Live player inner | x420–1116, y856–967 | Empty of story. HTML player sits here |
| Top-left calm | x32–160, y32–160 | Calm sky/wall for the clock |
| Top-right calm | x1376–1504, y32–160 | Calm sky/wall for YT Music |
| 3:4 crop | x384–1152, full height | Complete ritual + both reserves |
| Action floor | everything important above y825 | |

Do not paint a blank UI rectangle. Both reserves stay part of the world.

## Camera and skyline

Straight-on or gently oblique, adult eye height, level horizon.
Central roof / eave / zinc ridge stays **below y465** so the title field is sky or quiet wall.
All people, chairs, and ritual stay **below the title reserve** and **above the player reserve**.
Camera, horizon, and architecture do not move between Ayer and Presente.

## Room scripts (Ayer)

| Room | Place / year | Camera | Ritual | Cast |
|---|---|---|---|---|
| Colmado | SD corner shop, ~1994 | Across the street, intimate asymmetry | Four-man dominó, one tile being placed | 9: 4 players, clerk, 2 women, 2 children |
| Secador | Yamasá timber salon, ~1994 | Across the street, 40–50 mm | One blower + round-brush blowout through the open door | 6: stylist, client, 2 abuelas, 2 girls |
| Barbería | Dajabón storefront, ~1998 | Across the street, 10–12 m, 50 mm | Scissor-over-comb at the left temple | 6 inside, child far from blades |
| Limpieza | Las Caobas house, ~1992 | Across a thin street | Cleaning is done; two adults at rest, dog settled | 2 adults + 1 dog. No mop, no wet floor |
| Galería | Salcedo–Tenares campo, ~1994 | Across the yard | Abuela and granddaughter listen to one cream transistor | 2 people, 1 radio, 1 distant burro |
| Malecón | Av. George Washington, 1991 | Rear-track, road left, sea right, horizon ~y569 | Couple walk inland on the promenade | 8 people, 4 period cars in the road only |

One analog radio is the only visible audio device. Packages are mute color blocks.

## Presente

Same camera, same architecture, same painter, same reserves.
Only the era moves: clothes, one small speaker in the radio’s place, quieter modern street life.
No LED carnival, no giant phones, no brand walls, no photoreal jump.

## Pass / reject

Fail the plate if any one is true:

- Anything readable is painted in
- Title or player reserve is invaded
- Count is wrong
- It reads as a photo, CGI, vector poster, or resort
- The ritual is not complete inside the centered 3:4
- Ayer and Presente look like two different painters
