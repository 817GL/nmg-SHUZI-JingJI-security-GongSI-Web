#!/usr/bin/env python3
"""Run a local, read-only-friendly demo using synthetic API data.

The demo uses only Python's standard library and never connects to production
services. It serves the existing Web UI plus sanitized mock API responses.
"""

from __future__ import annotations

import argparse
import json
import mimetypes
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
WEB = ROOT / "web"
MOCK = ROOT / "examples" / "mock"


def load_json(name: str):
    return json.loads((MOCK / name).read_text(encoding="utf-8"))


class DemoHandler(BaseHTTPRequestHandler):
    server_version = "ApiUsageDemo/1.0"

    def log_message(self, fmt: str, *args) -> None:
        print(f"[demo] {self.address_string()} - {fmt % args}")

    def send_json(self, payload, status: int = 200) -> None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def send_text(self, text: str, status: int = 200) -> None:
        data = text.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def serve_static(self, relative: str) -> None:
        allowed = {
            "index.html": WEB / "index.html",
            "styles.css": WEB / "styles.css",
            "app.js": WEB / "app.js",
            "app_icon.png": WEB / "app_icon.png",
        }
        target = allowed.get(relative)
        if target is None or not target.is_file():
            self.send_error(404)
            return
        data = target.read_bytes()
        content_type = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        if path == "/":
            self.serve_static("index.html")
            return
        if path in {"/styles.css", "/app.js", "/app_icon.png"}:
            self.serve_static(path.lstrip("/"))
            return
        if path == "/api/bootstrap":
            self.send_json(load_json("bootstrap.json"))
            return
        if path == "/api/results":
            self.send_json(load_json("results.json"))
            return
        if path == "/api/systems":
            self.send_json(load_json("systems.json"))
            return
        if path == "/api/result":
            self.send_json(load_json("result.json"))
            return
        if path == "/api/logs":
            self.send_json({"lines": ["Mock demo mode: no production logs are loaded."]})
            return
        if path == "/api/files":
            self.send_json({"items": []})
            return
        if path.startswith("/api/jobs/"):
            self.send_json(
                {
                    "kind": "Mock task",
                    "status": "success",
                    "started_at": "2026-09-16 12:00:00",
                    "progress": ["Synthetic demo task completed."],
                    "result": {},
                }
            )
            return
        self.send_error(404)

    def do_POST(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        content_length = int(self.headers.get("Content-Length", "0") or 0)
        body = self.rfile.read(content_length) if content_length else b""

        if path == "/api/settings":
            try:
                request = json.loads(body.decode("utf-8")) if body else {}
            except (UnicodeDecodeError, json.JSONDecodeError):
                self.send_json({"error": "Invalid JSON"}, 400)
                return
            self.send_json({"settings": request})
            return

        if path == "/api/events/ack":
            self.send_json({"ok": True})
            return

        if path in {
            "/api/test",
            "/api/collect",
            "/api/scan",
            "/api/audit",
            "/api/excel",
        }:
            self.send_json({"job_id": "mock-job-1"})
            return

        # Upload/import actions are intentionally disabled in the public demo.
        if path.startswith("/api/database/") or path.startswith("/api/government/"):
            self.send_json({"error": "This action is disabled in the sanitized public demo."}, 501)
            return

        self.send_error(404)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the sanitized local demo server")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8088, type=int)
    args = parser.parse_args()

    server = ThreadingHTTPServer((args.host, args.port), DemoHandler)
    print(f"Sanitized demo server: http://{args.host}:{args.port}")
    print("This demo uses synthetic fixtures only and does not contact production services.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
