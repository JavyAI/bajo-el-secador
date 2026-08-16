# Bajo el secador

Three rooms, one page. Codex plates in the back. Hidden YouTube audio. Same bones as [saloon.wtf](https://saloon.wtf).

```
cd /Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador
python3 -m http.server 8876 --bind 127.0.0.1
```

Open http://127.0.0.1:8876/

| Hash | Room | Plate | Playlist |
|---|---|---|---|
| `#salon` | Bajo el secador | `assets/salon.jpg` (DSA-3.0 v3) | [PLHGerkzq-_SQ](https://www.youtube.com/playlist?list=PLHGerkzq-_SQ) |
| `#barberia` | En la silla | `assets/barberia.jpg` (DSA-3.0 v4) | [PLUXmVaLcUP14](https://www.youtube.com/playlist?list=PLUXmVaLcUP14) |
| `#colmado` | En la esquina | `assets/colmado.jpg` (DSA-3.0 v4) | [PLHayRTekRcmM](https://www.youtube.com/playlist?list=PLHayRTekRcmM) |

Clock top-left. Presence top-center (this origin, live tabs). YouTube top-right. Wordmark in the quiet band of each painting. Glass player at the bottom.

Sala de espera. Radio de salón. El video de YouTube no se ve: solo se oye.

## Cómo abrir

Desde esta carpeta:

```bash
python3 -m http.server 8765
```

Luego abre [http://127.0.0.1:8765](http://127.0.0.1:8765).

También sirve:

```bash
npx serve .
```

Hace falta un servidor local. Abrir `index.html` como archivo no carga `public/tracks.json`.

El primer toque en reproducir, anterior o siguiente arranca el audio (regla de autoplay del navegador).

## Qué hay

- `index.html` — página única
- `css/styles.css` — paleta del cuadro: teal, mango, crema, índigo
- `js/player.js` — iframe oficial de YouTube, 1×1, sin pointer-events; controles propios
- `public/tracks.json` — 42 videos oficiales (sin repetir id)
- `assets/salon.jpg` — fondo de sala, placa wow 16:9 edit2

## Estaciones

- **Todas**
- **Secador** — baladas bajo el casco
- **Sábado** — Olga Tañón

Aleatorio y repetir vienen encendidos. Si se puede, no suenan dos temas de la misma artista seguidos.
