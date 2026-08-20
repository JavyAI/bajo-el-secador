#!/usr/bin/env python3
"""Tiny POST /select server so the plate picker can lock picks to disk."""

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

OUT = Path("/Users/javyai/Documents/CODEX/2026-08-15/bajo-el-secador/picker/selection.json")
PORT = 8878


class Handler(BaseHTTPRequestHandler):
    def _cors(self) -> None:
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self) -> None:
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_POST(self) -> None:
        if self.path.rstrip("/") != "/select":
            self.send_response(404)
            self._cors()
            self.end_headers()
            return
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length)
        data = json.loads(raw.decode("utf-8"))
        OUT.write_text(json.dumps(data, indent=2), encoding="utf-8")
        body = json.dumps({"ok": True, "path": str(OUT)}).encode("utf-8")
        self.send_response(200)
        self._cors()
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
        print(f"locked {len(data.get('rooms', {}))} rooms -> {OUT}", flush=True)

    def log_message(self, fmt: str, *args) -> None:
        print("%s - %s" % (self.address_string(), fmt % args), flush=True)


if __name__ == "__main__":
    httpd = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"picker-save on http://127.0.0.1:{PORT}/select", flush=True)
    httpd.serve_forever()
