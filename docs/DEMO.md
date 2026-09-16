# Local Sanitized Demo

The repository includes a small local demo server that uses synthetic fixtures only. It is intended for public review, UI development, testing, and learning without requiring access to any production API or private environment.

## Requirements

- Python 3.10 or later
- a modern Web browser

No `pip install` step is required.

## Start the demo

From the repository root:

```bash
python examples/mock/run_demo.py
```

Then open:

```text
http://127.0.0.1:8088
```

Use another port if needed:

```bash
python examples/mock/run_demo.py --port 8765
```

## What the demo provides

The demo serves the existing `web/` front end and synthetic responses for the main read paths, including:

- `/api/bootstrap`
- `/api/results`
- `/api/systems`
- `/api/result`
- `/api/logs`
- `/api/files`
- mock task-status responses

Common task buttons return a synthetic completed job so contributors can exercise the front-end flow without contacting external services.

Upload/import operations are intentionally disabled in the public demo.

## Data safety

Everything under `examples/mock/` must remain synthetic. Never copy production payloads, tokens, logs, database records, internal-only endpoints, or other sensitive material into the demo fixtures.

The CI workflow validates the fixture JSON and runs a smoke test against this demo server.
