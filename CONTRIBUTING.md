# Contributing

Thanks for your interest in improving this project.

The project is currently maintained independently and is being improved for broader public review and reuse. Small, focused contributions are preferred.

## Good contribution areas

Useful contributions include:

- bug fixes
- input-validation improvements
- safer error handling
- automated tests
- documentation improvements
- accessibility and UI fixes
- configuration cleanup
- mock/sample data and local development helpers
- security hardening that does not expose sensitive environment details

## Public-data rule

All public examples must use synthetic or sanitized values.

Do not include:

- production API tokens or passwords
- VPN credentials
- private keys or certificates
- internal-only hostnames, IP addresses, or endpoints that are not intended for disclosure
- production logs containing sensitive information
- real business records or sensitive database contents

The fixtures in `examples/mock/` show the preferred style for public examples.

## Local development and demo

A sanitized local demo can be started with:

```bash
python examples/mock/run_demo.py
```

Then open `http://127.0.0.1:8088`.

The demo does not contact production services and should remain based on synthetic fixtures only. See `docs/DEMO.md` and `docs/ARCHITECTURE.md` for more context.

## Before submitting

Please make sure your change:

1. does not contain secrets or production-sensitive data;
2. uses mock or sanitized values in examples;
3. keeps the change focused and documents behavior changes;
4. avoids committing generated runtime data or temporary files;
5. considers input validation, error handling, and data exposure when relevant.

Run the lightweight repository validation:

```bash
python scripts/validate_public_repo.py
```

If JavaScript changed, also run:

```bash
node --check web/app.js
```

GitHub Actions performs these checks and also starts the sanitized demo server for a basic smoke test.

## Pull requests

A useful pull request should explain:

- what problem it solves;
- what changed;
- how the change was tested;
- whether it affects configuration, stored data, API behavior, reporting, or security.

The repository includes a pull-request checklist to help prevent accidental sensitive-data publication.

For security-sensitive findings, please follow `SECURITY.md` rather than publishing sensitive exploit details in a public issue.

## Development direction

Current priorities include broader automated testing, configuration separation, stronger validation, continued security review, and continued backend-source migration where appropriate.
