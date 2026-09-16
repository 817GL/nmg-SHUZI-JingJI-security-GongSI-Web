# API Usage Statistics Dashboard

A lightweight Web dashboard for collecting, validating, reviewing, and reporting API usage statistics across multiple service pools.

This project grew out of a real operational need: repetitive API connectivity checks, usage-data collection, validation, system inventory review, and report preparation were taking significant manual effort. I currently maintain the project independently and continue improving its reliability, documentation, maintainability, and security.

> 中文说明：这是一个用于多资源池接口调用统计、数据校验、系统名录管理与报表输出的 Web 工具。仓库公开内容不应包含生产环境凭据、真实 Token、VPN 凭据、内部敏感地址或生产业务数据。

## Features

- API connectivity testing
- API usage data collection and basic counting/validation
- System inventory and baseline management
- Name matching and exception review
- SQLite-based local data management
- Excel-oriented reporting workflow
- Task status, logs, and file management
- Configurable service-pool settings

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

Work in progress includes:

- broader SQLite compatibility
- additional collection workflows
- Excel template-preserving output
- system database scan / validation / change-event handling
- automated tests
- stronger security review and configuration handling

## Repository Scope

This repository currently contains the Web front-end source, launch scripts, documentation, and historical packaging information.

Important: the packaged `server/web_server.exe` referenced by historical release notes does **not** mean that the complete backend source code is present in this repository. The current public source scope should therefore not be described as a complete backend implementation.

Key source files include:

- `web/index.html`
- `web/styles.css`
- `web/app.js`
- `START_WEB.cmd`
- `STOP_WEB.cmd`
- `OPEN_WEB.cmd`

## Running the Packaged Web Version

For the packaged Windows x64 build, start the application with:

```text
START_WEB.cmd
```

Default local address:

```text
http://127.0.0.1:8088
```

The packaged build and source snapshot may not have identical capabilities while migration work is ongoing.

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

The repository `.gitignore` excludes common credential, key, temporary-data, and runtime-data patterns. Security issues should be reported according to `SECURITY.md`.

## Roadmap

- [ ] Complete backend-source migration where redistribution is permitted
- [ ] Add automated tests
- [ ] Add a sanitized/mock API environment
- [ ] Improve configuration separation for local and production use
- [ ] Add CI checks
- [ ] Expand validation and error handling
- [ ] Improve security scanning and dependency review
- [ ] Improve contributor and developer documentation

## Contributing

See `CONTRIBUTING.md` for contribution guidance. Please never include production credentials, private endpoints, or real business data in issues or pull requests.

## Maintenance

The project is currently maintained independently. The focus is practical maintainability: reducing repetitive operational work, improving correctness, and making the codebase easier and safer to review and evolve.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
