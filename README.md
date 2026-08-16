# Bajo el secador

Three rooms, one page. Codex plates in the back. Hidden official YouTube audio. Same bones as [saloon.wtf](https://saloon.wtf) — not its art, logo, or music.

```bash
cd /Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador
python3 -m http.server 8876 --bind 127.0.0.1
```

Use **localhost**, not `127.0.0.1`. YouTube blocks embeds from the numeric address (error 150).

Open http://localhost:8876/

| Hash | Room | Mix | First song |
|---|---|---|---|
| `#salon` | Bajo el secador | 110 · baladas y merengue | Juan Gabriel — Amor Eterno |
| `#barberia` | En la silla | 68 · bachata | Aventura — Obsesión |
| `#colmado` | En la esquina | 86 · salsa y merengue | Juan Luis Guerra — A Pedir Su Mano |

Clock top-left. Presence top-center (this origin, live tabs only). YouTube Music pill top-right. Wordmark in the quiet band of each painting. Glass player at the bottom: spinning circular art, authored order, no shuffle.

Sala de espera. Radio de salón. El video de YouTube no se ve: solo se oye.

Hard-refresh after JS/CSS/JSON edits (`Cmd+Shift+R`). Debug overlay: **Shift+D**.

## Qué hay

- `index.html` — página única
- `css/styles.css` — Fraunces + Figtree, glass dock, full-bleed plates
- `js/player.js` — IFrame API oficial, dos hosts 480×270 fuera de pantalla, fade entre salas
- `public/salon.json` / `barberia.json` / `colmado.json` — orden de la radio
- `assets/{salon,barberia,colmado}.jpg` — placas Codex DSA-3.0
- `assets/covers/` — carátulas cuadradas de catálogo (iTunes/Deezer)

El pill abre las mismas listas en YouTube Music (`PLHGerkzq-_SQ`, `PLUXmVaLcUP14`, `PLHayRTekRcmM`). El reproductor de la página sigue usando embeds oficiales de YouTube. Las primeras 15 de cada sala son los bangers de entrada.

Añadir a la pantalla de inicio: Safari usa `apple-touch-icon.png` (el secador de casco) y el `theme-color` de cada sala.

Hace falta un servidor local. Abrir `index.html` como archivo no carga las listas. El primer toque en reproducir arranca el audio (regla de autoplay del navegador).
