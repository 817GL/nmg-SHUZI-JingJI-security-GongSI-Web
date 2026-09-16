# Sanitized Mock API Data

This directory contains synthetic example payloads for public development, documentation, tests, and security review.

The data is intentionally fictional. It does not contain production API tokens, credentials, internal hostnames, real customer records, or production business data.

## Files

- `bootstrap.json` — example response for `/api/bootstrap`
- `results.json` — example response for `/api/results`
- `systems.json` — example response for `/api/systems`
- `result.json` — example detail payload used by matching and validation views

These files document the front-end data shapes and can be used as fixtures when building a future local mock server or automated tests.

Do not replace these fixtures with captures from a production environment. Add new examples using synthetic names such as `Example Pool A`, `Example System A`, and `Example Organization`.
