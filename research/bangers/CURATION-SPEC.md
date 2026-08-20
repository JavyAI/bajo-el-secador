# Curation spec — 8 rooms × AYER + HOY

**16 lists.** Not 14. Silla is on the board. 100 AYER + 100 HOY per room.

## Eras
- **AYER** = ~1980–2010 (80s / 90s / 2000s)
- **HOY** = ~2011–now
- Views rank *inside* the cultural pool. Views do **not** pick #1.
- Forgotten / overtaken #1 sits **in** the first 15, never as opener.

## First 15
- Wow in 15 seconds for **this room**.
- Official YouTube only (VEVO / artist / label Topic / Fania / Warner / Karen / JN / Planet).
- 11-char id. No lyrics, karaoke, DJ mixes, AI, sped-up.
- No consecutive same artist.
- Authored #1s stay: Secador *Amor Eterno* · Silla *Obsesión* · Colmado *A Pedir Su Mano* · Marquesina *Dueña del Swing* · Malecón *Burbujas*.
- Cover must work on the vinyl: prefer existing `assets/covers/{id}.jpg` or a real `i.ytimg.com/vi/{id}/mqdefault.jpg` (not a 404, not a letterboxed-only ghost).

## 100
- Exhaustive for the room × era. Neighbors with 15 minutes of fame stay in the 100, not the throne.
- Every id doubly checked: official channel + playable embed + artwork + enough views to prove it is real (first 15 prefer 1M+ except protected Dominican monuments).

## Output
Write `research/bangers/curation/{room}-ayer.json` and `{room}-hoy.json`:

```json
{
  "room": "colmado",
  "era": "ayer",
  "count": 100,
  "introCount": 15,
  "tracks": [
    {
      "id": "xxxxxxxxxxx",
      "artist": "",
      "title": "",
      "year": 1990,
      "channel": "",
      "views": 0,
      "official": true,
      "artworkOk": true,
      "intro": true
    }
  ]
}
```

First 15 have `"intro": true` in authored order. Rest fill 16–100. No duplicate ids inside a list.
