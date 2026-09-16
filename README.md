# API Usage Statistics Dashboard

[![CI](https://github.com/817GL/nmg-SHUZI-JingJI-security-GongSI-Web/actions/workflows/ci.yml/badge.svg)](https://github.com/817GL/nmg-SHUZI-JingJI-security-GongSI-Web/actions/workflows/ci.yml)

A lightweight Web dashboard for collecting, validating, reviewing, and reporting API usage statistics across multiple service pools.

This project grew out of a real operational need: repetitive API connectivity checks, usage-data collection, validation, system inventory review, and report preparation were taking significant manual effort. I currently maintain the project independently and continue improving its reliability, documentation, maintainability, and security.

> 中文说明：这是一个用于多资源池接口调用统计、数据校验、系统名录管理与报表输出的 Web 工具。公开仓库使用脱敏/模拟数据，不应包含生产环境凭据、真实 Token、VPN 凭据、内部敏感地址或生产业务数据。

## Features

- API connectivity testing
- API usage data collection and basic counting/validation
- System inventory and baseline management
- Name matching and exception review
- SQLite-oriented local data management
- Excel-oriented reporting workflow
- Task status, logs, and file management
- Configurable service-pool settings
- Sanitized local demo fixtures for public development and review
- GitHub Actions checks for syntax, fixture validity, basic secret guardrails, and demo smoke testing

## Current Status

The project is under active maintenance.

Current Web version: **v2.0.2**

Completed or partially completed work includes:

- Web interface and navigation
- Basic service endpoints
- Connectivity testing for multiple service pools
- Usage-detail collection for supported pools
- Basic counting and validation
- System inventory workflows
- Task progress and log views
- sanitized public mock data and local demo server
- basic CI validation and smoke testing

Work in progress includes:

- broader SQLite compatibility
- additional collection workflows
- Excel template-preserving output
- system database scan / validation / change-event handling
- broader automated tests
- stronger security review and configuration handling

## Repository Scope

This repository currently contains the Web front-end source, launch scripts, documentation, sanitized fixtures, public-development tooling, and historical packaging information.

Important: the packaged `server/web_server.exe` referenced by historical release notes does **not** mean that the complete backend source code is present in this repository. The current public source scope should therefore not be described as a complete backend implementation.

Key source and development files include:

- `web/index.html`
- `web/styles.css`
- `web/app.js`
- `examples/mock/` — synthetic API fixtures and local demo server
- `scripts/validate_public_repo.py` — lightweight public-repository validation
- `docs/ARCHITECTURE.md` — current public architecture and security boundaries
- `docs/DEMO.md` — local sanitized demo instructions

## Sanitized Local Demo

A local demo is available without production APIs, credentials, or private infrastructure. It uses only synthetic fixtures.

From the repository root:

```bash
python examples/mock/run_demo.py
```

Then open:

```text
http://127.0.0.1:8088
```

The mock payloads live under `examples/mock/`. See `docs/DEMO.md` for details.

## Packaged Windows Version

Historical packaging information describes a Windows x64 standalone build. Where the complete package is available locally, it is started with:

```text
START_WEB.cmd
```

Default local address:

```text
http://127.0.0.1:8088
```

The packaged build and the current public source snapshot may not have identical capabilities while migration work is ongoing.

## Quality Checks

The repository includes a small CI workflow intended to keep the public source reviewable without adding a heavy toolchain. It currently performs:

- JavaScript syntax checking with Node.js
- Python syntax checking
- JSON validation for sanitized fixtures
- required-file checks
- high-confidence secret-pattern guardrails
- a local mock-server smoke test

Run the main repository validation locally with:

```bash
python scripts/validate_public_repo.py
```

For JavaScript changes, also run:

```bash
node --check web/app.js
```

These checks are guardrails and do not replace dedicated security scanning or manual review.

## Security and Data Handling

Do **not** commit or publish:

- production API tokens
- passwords or credentials
- VPN credentials
- private keys or certificates
- internal-only endpoints that should not be public
- production logs
- temporary business data
- sensitive database contents

The repository `.gitignore` excludes common credential, key, temporary-data, and runtime-data patterns. Public examples must use synthetic or sanitized values. Security issues should be reported according to `SECURITY.md`.

## Roadmap

- [ ] Complete backend-source migration where redistribution is appropriate
- [ ] Expand automated tests
- [x] Add sanitized/mock API fixtures and a local demo environment
- [ ] Improve configuration separation for local and production use
- [x] Add CI checks and demo smoke testing
- [ ] Expand validation and error handling
- [ ] Improve security scanning and dependency review
- [x] Add contributor, architecture, demo, and security documentation

## Contributing

See `CONTRIBUTING.md` for contribution guidance. GitHub issue and pull-request templates are included to encourage reproducible reports and sanitized examples.

Please never include production credentials, private endpoints, real business data, or sensitive logs in issues or pull requests.

## Maintenance

The project is currently maintained independently. The focus is practical maintainability: reducing repetitive operational work, improving correctness, and making the codebase easier and safer to review and evolve.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
