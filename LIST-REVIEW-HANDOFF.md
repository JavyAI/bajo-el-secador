# List review thread — first 15 sentimental bangers

You are a **separate agent working with the main Bajo el secador thread**. Founder Javy will go over the first 15 songs in each room with you. Your job is the lists, not the site chrome.

Work in:

`/Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador/`

Live catalogs (source of truth):

- `public/salon.json` — 110 tracks, `introCount: 15`
- `public/barberia.json` — 68 tracks, `introCount: 15`
- `public/colmado.json` — 86 tracks, `introCount: 15`

The first 15 play in authored order. After that the rest of the room mix. Official YouTube embeds only. Keep the name **Bajo el secador**.

---

## What Javy wants

The first 15 in each room must be the **best of the best sentimental bangers** — people should say **wow** in the first seconds. Cultural lock, not YouTube-view charts.

He already rejected a view-rank pass that put Son by Four first in Esquina. Restore feeling, not counts.

Never consecutive same artist (room rule). The current first 15s break that in places — flag it, do not silently “fix” unless Javy asks.

---

## The three rooms

| Room | Hash | Crowd | What the first 15 must feel like |
|---|---|---|---|
| **Bajo el secador** | `#salon` | Women, intimate, tía radio | Baladas + Olga merengue. Amor Eterno energy. Ana Gabriel, Rocío, Juan Gabriel, Luismi, Selena, José José. |
| **En la silla** | `#barberia` | Men, diaspora | Bachata típica + Aventura/Romeo. Obsesión energy. Antony, Luis Vargas, Raulín, Frank Reyes, Monchy. |
| **En la esquina** | `#colmado` | Widest Dominican lock | Salsa + merengue de fiesta. JLG, Lavoe, Celia, Gran Combo, Wilfrido. After opener: Yiyo *Manos de Tijera* / *Que Agonía* / *Mi Todo*; Chiquito *La Llamada De Mi Ex*, *Lejos De Ti*. |

---

## Current first 15 (live JSON)

### Secador — `salon.json`  first: `RgKqxLAhRKE`

1. Juan Gabriel — Amor Eterno  
2. Luis Miguel — Suave  
3. Ana Gabriel — Simplemente Amigos  
4. Olga Tañón — Como Olvidar  
5. Selena — Como La Flor  
6. José José — El Triste  
7. Rocío Dúrcal — La Gata Bajo La Lluvia  
8. Amanda Miguel — El Me Mintio  
9. Thalía — Amor a La Mexicana  
10. Luis Miguel — La Incondicional  
11. Milly Quezada — Volvio Juanita  
12. Ana Gabriel — Evidencias  
13. Chayanne — Dejaria Todo  
14. Selena — Amor Prohibido  
15. Marco Antonio Solís — Si No Te Hubieras Ido  

Same-artist repeats in the 15: Luis Miguel (2, 10), Ana Gabriel (3, 12), Selena (5, 14). None consecutive.

### Silla — `barberia.json`

1. Aventura — Obsesion  
2. Romeo Santos — Propuesta Indecente  
3. Prince Royce — Darte un Beso  
4. Frank Reyes — Tu Eres Ajena  
5. Monchy y Alexandra — Hoja en Blanco  
6. Antony Santos — Voy Pa'lla  
7. Luis Vargas — Loco de Amor  
8. Aventura — Ella y Yo  
9. Romeo Santos — Eres Mia  
10. Prince Royce — Corazon Sin Cara  
11. Raulin Rodriguez — Nereyda  
12. Juan Luis Guerra — Burbujas de Amor  
13. Toby Love — Tengo Un Amor  
14. Alex Bueno — Que Vuelva  
15. Aventura — Dile al Amor  

Repeats: Aventura (1, 8, 15), Romeo (2, 9), Prince Royce (3, 10).

### Esquina — `colmado.json`

1. Juan Luis Guerra — A Pedir Su Mano  
2. Hector Lavoe — El Cantante  
3. Elvis Crespo — Suavemente  
4. Celia Cruz — La Vida Es Un Carnaval  
5. Willie Colon — El Gran Varon  
6. El Gran Combo — Me Libere  
7. Ruben Blades — Pedro Navaja  
8. Juan Luis Guerra — Bachata Rosa  
9. Joe Arroyo — Rebelion  
10. Wilfrido Vargas — El Africano  
11. Los Hermanos Rosario — La Dueña del Swing  
12. Frankie Ruiz — Desnudate Mujer  
13. Oscar D'Leon — Lloraras  
14. Grupo Niche — Cali Pachanguero  
15. Juan Luis Guerra — Burbujas de Amor  

Repeats: JLG (1, 8, 15). Confirm Yiyo + Chiquito sit **after** this 15, not instead of it.

---

## How to work with Javy

- Walk room by room. One opener at a time if he wants.
- Ask: would a Dominican in the chair / under the dryer / on the esquina say **wow** in the first 15 seconds?
- Propose swaps with a reason (feeling, memory, ritual) — never “it has more views.”
- Official YouTube only. Do not drop IDs that still play.
- When a first 15 is agreed, write it into the matching `public/*.json` (`intro: true` on those 15, authored order) and tell the main thread so playlists can be rewritten.

Do not redesign the site, favicon, or player. Lists only.

---

## Paste this to start a new Grok thread

```
Read /Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador/LIST-REVIEW-HANDOFF.md and work with me as the list-review agent. We are going over the first 15 songs in each room so they are the best sentimental bangers — wow in the first seconds. Cultural lock, not charts. Start with Secador.
```
