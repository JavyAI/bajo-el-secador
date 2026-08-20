# Sopita — En el colmado

Six rooms, one page. Deluxe plates in the back. Hidden official YouTube audio. Lists live on YouTube Music; the on-page player loads those playlists.

```bash
cd /Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador
python3 -m http.server 8876 --bind 0.0.0.0
```

Use **localhost**, not `127.0.0.1`. YouTube blocks embeds from the numeric address (error 150).

Open http://localhost:8876/

| Hash | Station | List |
|---|---|---|
| `#colmado` | Sopita Colmado | De día / De noche |
| `#secador` | Sopita Salón | De día / De noche |
| `#barberia` | Sopita Barbería | De día / De noche |
| `#limpieza` | Sopita Limpieza | De día / De noche |
| `#galeria` | Sopita Galería | De día / De noche |
| `#malecon` | Sopita Malecón | De día / De noche |

Clock top-left. Presence top-center (same browser origin only, not a global count). YT Music pill top-right. Glass player at the bottom.

Edit a list on YouTube, then switch room or reload. The player fetches the playlist from YouTube on each room load.

Hard-refresh after JS/CSS edits (`Cmd+Shift+R`). Debug overlay: **Shift+D**.

## Qué hay

- `index.html` — página única
- `css/styles.css` — Fraunces + Figtree, glass dock, full-bleed plates
- `js/player.js` — IFrame API oficial, playlists de YouTube, fade entre salas
- `public/playlists.json` — IDs de las 12 listas
- `assets/{colmado,salon,barberia,limpieza,galeria,malecon}{,-hoy}.jpg` — placas

## Hosting (miles de oyentes)

`python3 -m http.server` is only for LAN. For ~5000 people at once, put the static site on a CDN (Cloudflare Pages, Netlify, or S3 + CloudFront) from this repo. `_headers` sets long cache on `/assets`, `/css`, `/js`.

Audio is YouTube’s problem: each visitor’s browser talks to YouTube, not our origin. Our origin serves HTML, CSS, JS, and one plate (~1 MB). That is what a CDN is for.

Do not expect the “aquí” number to show 5000. It only counts tabs on the same origin in the same browser. A real presence count needs a tiny backend.
