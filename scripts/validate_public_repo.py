#!/usr/bin/env python3
"""Lightweight CI validation for the public repository.

This intentionally uses only the Python standard library so it can run in a
clean GitHub Actions environment without installing project dependencies.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "web/index.html",
    "web/styles.css",
    "web/app.js",
    "examples/mock/bootstrap.json",
    "examples/mock/results.json",
    "examples/mock/systems.json",
    "examples/mock/result.json",
]

MOCK_JSON_FILES = [
    "examples/mock/bootstrap.json",
    "examples/mock/results.json",
    "examples/mock/systems.json",
    "examples/mock/result.json",
]

# High-confidence patterns only. This is a guardrail, not a replacement for a
# dedicated secret scanner or manual review.
SECRET_PATTERNS = {
    "private key block": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub classic token": re.compile(r"\bghp_[A-Za-z0-9]{30,}\b"),
    "GitHub fine-grained token": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{30,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "OpenAI-style secret key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "Bearer credential": re.compile(r"\bBearer\s+[A-Za-z0-9._~+/-]{24,}={0,2}\b", re.IGNORECASE),
}

TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".json",
    ".js",
    ".css",
    ".html",
    ".yml",
    ".yaml",
    ".py",
    ".cmd",
}

SKIP_PARTS = {".git"}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        fail("missing required public-repository files: " + ", ".join(missing))


def validate_mock_json() -> None:
    for relative in MOCK_JSON_FILES:
        path = ROOT / relative
        try:
            with path.open("r", encoding="utf-8") as handle:
                payload = json.load(handle)
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            fail(f"invalid JSON fixture {relative}: {exc}")
        if not isinstance(payload, dict):
            fail(f"mock fixture must contain a JSON object: {relative}")


def iter_text_files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {"LICENSE", ".gitignore"}:
            continue
        yield path


def scan_high_confidence_secrets() -> None:
    findings: list[str] = []
    for path in iter_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                findings.append(f"{path.relative_to(ROOT)}: {label}")

    if findings:
        fail("possible secret material detected:\n  " + "\n  ".join(findings))


def validate_public_docs() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for heading in ("Security and Data Handling", "Contributing", "License"):
        if heading not in readme:
            fail(f"README is missing expected section: {heading}")


def main() -> int:
    validate_required_files()
    validate_mock_json()
    scan_high_confidence_secrets()
    validate_public_docs()
    print("Public repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
