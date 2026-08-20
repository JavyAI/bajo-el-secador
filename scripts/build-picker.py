#!/usr/bin/env python3
"""Build plate-picker catalog + JPEG thumbs from Codex conversation outputs."""

from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path

from PIL import Image

CODEX = Path("/Users/javyai/Documents/CODEX/2026-08-16")
SITE = Path("/Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador")
PICKER = SITE / "picker"
THUMBS = PICKER / "thumbs"
SRC = PICKER / "src"

ROOMS = [
    {
        "id": "colmado",
        "name": "En el colmado",
        "kicker": "La bocina",
        "conversation": "en-la-esquina-four-state",
        "wired": "EN-LA-ESQUINA-FINAL-SITE-MASTER.png",
        "theme": "#65556b",
    },
    {
        "id": "secador",
        "name": "En el secador",
        "kicker": "El chisme",
        "conversation": "el-secador-dominican-salon",
        "wired": "el-secador-winning-populated-yamasa-v1.png",
        "theme": "#98abb8",
    },
    {
        "id": "barberia",
        "name": "En la barbería",
        "kicker": "El corte",
        "conversation": "en-la-silla-dominican-barberia",
        "wired": "en-la-silla-founder-selected-tigueres-viral-final.png",
        "theme": "#1a5d5a",
    },
    {
        "id": "limpieza",
        "name": "En la limpieza",
        "kicker": "El domingo",
        "conversation": "domingo-de-limpieza",
        "wired": "todo-en-su-sitio-site-wide-v2.png",
        "theme": "#0c9bea",
    },
    {
        "id": "galeria",
        "name": "En la galería",
        "kicker": "La radio",
        "conversation": "radio-en-la-galeria",
        "wired": "RADIO-EN-LA-GALERIA-R4H-SALOON-WIDE-1994-DAY-CANDIDATE-01.png",
        "theme": "#73b8d9",
    },
    {
        "id": "malecon",
        "name": "En el malecón",
        "kicker": "Los novios",
        "conversation": "enamorados-del-malecon",
        "wired": "FINAL-VIRAL-HERO-WIDE-1536x1024.png",
        "theme": "#7687d5",
    },
]

SKIP = (
    "small",
    "selection-board",
    "preview",
    "overlay",
    "diagnostics",
    "thumb",
    "zone",
    "mask",
    "difference",
    "geometry-overlay",
)


def skip_name(name: str) -> bool:
    n = name.lower()
    if not n.endswith(".png"):
        return True
    return any(token in n for token in SKIP)


def label_of(name: str) -> str:
    stem = Path(name).stem
    stem = stem.replace("-", " ").replace("_", " ")
    return stem


def main() -> None:
    THUMBS.mkdir(parents=True, exist_ok=True)
    SRC.mkdir(parents=True, exist_ok=True)

    catalog = {"rooms": []}
    total = 0

    for room in ROOMS:
        out_dir = CODEX / room["conversation"] / "outputs"
        src_link = SRC / room["id"]
        if src_link.is_symlink() or src_link.exists():
            src_link.unlink()
        os.symlink(out_dir, src_link, target_is_directory=True)

        room_thumbs = THUMBS / room["id"]
        room_thumbs.mkdir(parents=True, exist_ok=True)

        images = []
        for path in sorted(out_dir.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True):
            if not path.is_file() or skip_name(path.name):
                continue
            try:
                with Image.open(path) as im:
                    im = im.convert("RGB")
                    w, h = im.size
                    thumb_w = 720
                    if w > thumb_w:
                        thumb_h = int(h * (thumb_w / w))
                        im = im.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
                    thumb_name = path.stem + ".jpg"
                    dest = room_thumbs / thumb_name
                    im.save(dest, "JPEG", quality=78, optimize=True)
            except Exception as exc:
                print(f"skip {path.name}: {exc}")
                continue

            st = path.stat()
            images.append(
                {
                    "id": path.stem,
                    "file": path.name,
                    "abs": str(path),
                    "src": f"src/{room['id']}/{path.name}",
                    "thumb": f"thumbs/{room['id']}/{thumb_name}",
                    "w": w,
                    "h": h,
                    "kb": round(st.st_size / 1024),
                    "mtime": datetime.fromtimestamp(st.st_mtime).strftime("%H:%M"),
                    "label": label_of(path.name),
                    "wired": path.name == room["wired"],
                }
            )
            total += 1

        catalog["rooms"].append(
            {
                "id": room["id"],
                "name": room["name"],
                "kicker": room["kicker"],
                "conversation": room["conversation"],
                "theme": room["theme"],
                "wired": room["wired"],
                "images": images,
            }
        )
        print(f"{room['id']}: {len(images)} plates")

    (PICKER / "catalog.json").write_text(json.dumps(catalog, indent=2), encoding="utf-8")
    print(f"catalog {total} images -> {PICKER / 'catalog.json'}")


if __name__ == "__main__":
    main()
