# Codex handoff — Bajo el secador

Finish the three-room Dominican listening site. Static HTML. Clone **saloon.wtf mechanisms**, not its art, logo, or music.

Founder is Javy. Talk to him in product language. Do not invent a new concept.

**Today:** 2026-08-15  
**Git:** local only, `main` at `5121685` (`Initial snapshot of the three-room listening site.`). No GitHub remote. Commit before risky player/playlist edits so Javy can reset.

---

## Run it

```bash
cd /Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador
python3 -m http.server 8876 --bind 127.0.0.1
```

Live: http://127.0.0.1:8876/  
Rooms: `#salon` `#barberia` `#colmado`  
A server on `:8876` may already be running.

Hard-refresh after JS/CSS/JSON edits (`Cmd+Shift+R`). The tab caches `player.js` hard.

Debug overlay: **Shift+D** or `?debug=1`. Shows wanted vs YouTube state, nudges, fake-end, skips. Off by default (`localStorage bes-debug`).

---

## What this is

Three rooms, one page, saloon.wtf layout:

| Hash | Wordmark | Kicker | Crowd | Radio |
|---|---|---|---|---|
| `#salon` | Bajo el / secador | Baladas y merengue | Women / intimate | Tía radio (Ana Gabriel, Rocío, Juan Gabriel, Luismi, Olga merengue) |
| `#barberia` | En la / silla | Bachata | Men / diaspora | Bachata típica + Aventura/Romeo |
| `#colmado` | En la / esquina | Salsa y merengue | Widest Dominican lock | JLG, Lavoe, Celia, merengue de fiesta |

**Keep the name `Bajo el secador`.** Do **not** rename to “En la secadora” — that is a clothes dryer. The hood is *el secador*; you sit *bajo* it. Parallel “En la…” would be **En el secador**, which is weaker. Founder was advised to keep Bajo.

No Spotify unless Javy gets a real affiliate deal. He does not want a free-tier signup. YouTube official embeds only.

Monetize later via the room/brand, not by stealing ads off the videos.

---

## Tree

```
/Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador/
  index.html
  css/styles.css
  js/player.js
  public/salon.json          110 tracks  first: Juan Gabriel — Amor Eterno
  public/barberia.json        70 tracks  first: Aventura — Obsesión
  public/colmado.json         81 tracks  first: Juan Luis Guerra — A Pedir Su Mano
  public/tracks.json          STALE 42-track leftover. Site does not load this.
  assets/salon.jpg            Codex DSA-3 plate (~2400×1600 jpeg)
  assets/barberia.jpg
  assets/colmado.jpg
  assets/covers/{youtubeId}.jpg   259 square catalog covers
```

Source playlists + scripts (do not treat as live player input):

`/Users/javyai/Documents/CODEX/2026-08-15/dominican-saloon-clean-room/outputs/dsa5-grok-salon/playlist/`

- `bajo-el-secador.json` / `barberia-en-la-silla.json` / `colmado-en-la-esquina.json`
- `salon-ids.json` / `barberia-ids.json` / `colmado-ids.json`
- `PLAYLIST-URLS.md`
- `resolve-official.py`, `expand-and-mix.py`, `chart-gaps.py`

Style lock (do not feed saloon.wtf rasters into image gen):

`~/.codex/skills/direct-dominican-scene-art/`

Live plates came from:

- `.../outputs/scenes/dsa3/02-dominican-salon-interior-circa-1988-dsa3-v3.png` → `assets/salon.jpg` object-position `50% 36%` theme `#1a3538`
- `.../01-dominican-colmado-corner-circa-1988-dsa3-v4.png` → `assets/colmado.jpg` `50% 24%` `#4e5540`
- `.../03-dominican-barberia-inside-out-circa-1988-dsa3-v4.png` → `assets/barberia.jpg` `68% 30%` `#102848`

---

## What already works

- Full-bleed CSS `background-size: cover` (not `<img>`). Dual `.hero` layers, 0.7s opacity crossfade.
- Safari `theme-color` + `apple-mobile-web-app-status-bar-style: black-translucent` updates per room.
- Center Fraunces wordmark, two-line lockup, **currently all-caps upright** (`BAJO EL` / `SECADOR`). Room chips + kicker already uppercase.
- Clock: local TZ greeting (`buenos días` / `tardes` / `noches`) + time + long `es-DO` date.
- YouTube pill with play icon + up-right arrow (saloon.wtf pattern). No Spotify pill.
- Glass dock: 80×80 spinning vinyl, title, artist, seek, prev/play/next.
- Hidden official YouTube IFrame API. Dual hosts `#yt-player-a` / `#yt-player-b`.
- Authored mix order (`shuffle: false`). `buildQueue()` is now `catalog.slice()` so JSON order is play order.
- Room change after first pointerdown starts that room from index 0 (no pinned preferredId).
- Serial room audio fade (1.1s out / 1.3s in), one player PLAYING at a time. Overlap of two playing YT iframes is a ToS + iOS problem; do not bring it back.
- Square covers from iTunes/Deezer in `assets/covers/`. Player prefers those. One residual YouTube thumb: El Chaval — Hasta El Palo (`aXeA2OaW8GI`, a mix, no catalog art).
- First 15 of each room were reordered as bangers (see below). Rest of catalog kept.
- Playback watchdog + Shift+D debug. Fake `paused`/`ended` resume instead of skip. Errors retry the **same** id three times, 1.5s apart, before skip. Watchdog nudges only; it must not advance the queue.

---

## Founder taste (do not relitigate)

**Art.** DSA-3.0 Tropical Chorus + the Codex dsa3 plates. Rejected: airport, glitter, photoreal, magazine type, cartoon grins, cinematic AI film-look, kids-book gouache, copying saloon.wtf’s red shop. Film stills in `~/Downloads/IMG_1911.HEIC`… are mood only. **Stop generating images** unless he asks. Use the three plates.

**Type.** He thought italic sentence case looked weird and asked about all-caps. Caps shipped. Later design read: **we should have dropped italic and kept mixed case** — kicker + nav are already caps; the wordmark should be the only speaking line. He has not approved putting mixed case back. Ask before changing.

**Name.** Keep Bajo el secador. Not En la secadora.

**Music.** Official channels only (VEVO / Topic / artist / Fania / Warner / Karen / JN). No lyrics rips, karaoke, mixes, AI. Prefer ~1M+ views. Never consecutive same artist in the authored list (min gap ~7–8).

**Player.** Must stay a **spinning circle**, not a 16:9 card. Album art must be square. YouTube `hqdefault` is 4:3 letterboxed; `maxresdefault` often 404s or is 16:9. Do not go back to maxres as the vinyl src.

---

## Secador opener (what Play must start)

JSON order, first 15:

1. Juan Gabriel — Amor Eterno (`RgKqxLAhRKE`)
2. Luis Miguel — Suave (`ksoI-1X9sr4`)
3. Ana Gabriel — Simplemente Amigos (`kkF5eGMxwEQ`)
4. Olga Tañón — Como Olvidar (`OkOJGgqcwro`)
5. Selena — Como La Flor (`N3tdl7-puY4`)
6. José José — El Triste
7. Rocío Dúrcal — La Gata Bajo La Lluvia
8. Amanda Miguel — El Me Mintió
9. Thalía — Amor a La Mexicana
10. Luis Miguel — La Incondicional
11. Milly Quezada — Volvió Juanita
12. Ana Gabriel — Evidencias
13. Chayanne — Dejaría Todo
14. Selena — Amor Prohibido
15. Marco Antonio Solís — Si No Te Hubieras Ido

Silla opens: Obsesión → Propuesta Indecente → Darte un Beso…  
Esquina opens: A Pedir Su Mano → El Cantante → Suavemente…

---

## YouTube playlists (Javy, unlisted)

Site pills point here. **These lists are stale** vs the cleaned JSON (old collector rips + chart-pass extras still on YT).

| Room | Playlist |
|---|---|
| Secador | https://www.youtube.com/playlist?list=PLHGerkzq-_SQ |
| Silla | https://www.youtube.com/playlist?list=PLUXmVaLcUP14 |
| Esquina | https://www.youtube.com/playlist?list=PLHayRTekRcmM |

Unused leftover: `PLO_FA7afLkTI` (old 42-video list). Do not delete unless he says so.

Updating YT lists needs a signed-in session + innertube `SAPISIDHASH`. Cookie import alone → 401. Everyday Chrome often has **Allow JavaScript from Apple Events** off. gstack browse was wedged (“No active page”) for much of the last session. Playwright headed Chromium *does* work for QA (`python3` + `playwright`).

Innertube WEB player without `poToken` reports almost everything `UNPLAYABLE`. That is not a real embed signal. Use oembed + view counts + channel.

---

## P0 — finish this first (audio)

Founder last state: **press Play on Secador, silence.** Also: Play used to jump the queue (Amor Eterno → Suave → Simplemente Amigos → El Me Mintió in ~1s).

**Root causes already found**

1. Vinyl used 16:9 / missing `maxresdefault` → looked broken. Fixed with local squares.
2. Dual YT player cloned the **same** video (`warmIdle`) → error 150/153 × double events → skip storm. `warmIdle` removed.
3. Fake `ENDED`/`PAUSED` treated as skip. Now resume if `wanted === "play"` and it is not a real end (`dur >= 8` and `cur` near end).
4. Player was **1×1 + `clip-path: inset(50%)` + `opacity: 0`**. Chrome will not start audio. Last change: `#yt-host` is `480×270` parked at `left: -9999px`, no clip. `hideIframe()` must **not** shrink it back to 1px.
5. `probeVolume()` called `setVolume(0)` on first Ready — could mute the first note. Removed from onReady.

**Verify on a real click in Javy’s Chrome** (automation often cannot autoplay):

1. Hard-refresh `#salon`.
2. Press Play **once**.
3. Must hear **Amor Eterno** and stay there. Vinyl spins. `body.is-playing`.
4. Next/prev follow JSON order. Room chip Silla/Esquina starts that room at index 0 after first gesture.
5. Shift+D: you should see `yt:playing`, not a skip storm.

If still silent: check Shift+D for `yt:unstarted` / `error` / `nudge`. If Amor Eterno (`RgKqxLAhRKE`) is embed-blocked, swap **that id only** for another official Juan Gabriel *Amor Eterno* with art, do not reshuffle the list.

Do not “fix” silence by hunting a random song.

---

## P1 — after audio is honest

1. **Type.** Ask Javy: restore mixed-case two-line lockup (upright Fraunces, no italic, no `uppercase`) vs keep current caps. Design rec is mixed case.
2. **Rewrite the three YouTube playlists** to match `public/*.json` ids (same order). Headed signed-in Chromium + innertube edit, or he does it once by hand from the id lists.
3. **Title/id audit.** Several mid-list **labels do not match the playing video** (resolver recovered the wrong song, art was then matched to the video). Examples from the cover pass: listed “Ku-Ku-Ku” plays Dominicana; “Horoscopo” plays Me Sabe A Poco; “Hasta El Palo” is a mix. Fix: oembed each id, rename or replace id, keep official 1M+ rule.
4. **Init git.** No history exists.
5. **PWA / OG / apple-touch-icon.** Saloon has `site.webmanifest` + `opengraph.png`. We 404 favicon. Optional.
6. **Do not build Spotify.** Do not build global “everyone hears the same song” unless he asks (needs a backend). Online count is local `BroadcastChannel` only (`bes-presence`) — say so if he notices it is not worldwide.

---

## Do not

- Generate new salon/colmado/barbería images unless he asks.
- Feed `saloon.wtf/bg.avif` into ImageGen.
- Copy Deluxe Saloon Devanagari SVG or the red shop.
- Change the vinyl to a 16:9 card.
- Two YouTube players `PLAYING` at once (RMF + iOS).
- Add lyrics/karaoke/mix/AI clips.
- Sign Javy up for Spotify.
- Rename to En la secadora.
- Claim YouTube lists are clean. They are not.
- Trust innertube `UNPLAYABLE` without poToken.
- Use gstack `browse` as the only QA — it was wedged. Use Playwright headed or his real Chrome.

---

## Player map (`js/player.js`)

- `ROOMS` — names, lockup lines, kickers, themes, JSON paths, YT playlist URLs.
- `loadRoom(id, autoplay)` — fetch JSON, `buildQueue()` = catalog order, paint, then `mixInto` if already playing, else `ensurePlayer`.
- `failForward` — retry same id (3 hits, 1.5s apart) then skip once.
- `nudgePlay` / `startWatchdog` — resume only.
- `setCover` — local `assets/covers/{id}.jpg` first, then mqdefault.
- Presence: `BroadcastChannel("bes-presence")`.

---

## Clean-room / legal

Official embeds only. Do not download audio. Do not rehost videos. Covers are catalog stills from iTunes/Deezer, not ripped frames. Backgrounds are original Codex plates.

---

## Success

Javy hard-refreshes Secador, presses Play **once**, hears Amor Eterno, vinyl spins, order holds, rooms fade the picture and start the new mix from song 1. Then you can touch type, YT playlist sync, and the wrong-title audit.
