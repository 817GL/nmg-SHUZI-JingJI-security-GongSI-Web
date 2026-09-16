# Changelog

This changelog tracks notable changes in the public repository. Historical packaged-build notes are kept separate from the ongoing public-source cleanup and development work.

## Unreleased

### Added

- MIT open-source license
- public `SECURITY.md` and `CONTRIBUTING.md`
- sanitized synthetic API fixtures under `examples/mock/`
- local standard-library mock demo server
- architecture and demo documentation
- GitHub Actions syntax, fixture, validation, and demo smoke checks
- lightweight high-confidence secret-pattern guardrails
- GitHub issue and pull-request templates
- Dependabot configuration for GitHub Actions
- CODEOWNERS entry for the current maintainer

### Changed

- README reorganized around public development, security, maintenance, and repository scope
- `.gitignore` expanded for local test/build artifacts

## Web v2.0.2

### Changed

- removed the packaged runtime's dependency on locally installed Python, Node.js, pip, and npm
- packaged the Windows x64 Web service as a standalone server executable
- improved support for offline startup, non-system drive letters, and paths containing Chinese characters

### Migrated in the packaged build

- Web static interface
- basic bootstrap, log, file, settings, and task-status endpoints
- service-pool connectivity testing
- supported usage-detail collection and JSON result storage
- basic count/signature consistency validation

### Still under migration

- complete SQLite compatibility layer
- remaining collection workflows
- Excel template-preserving output
- system database scan, validation, rename, add, and recovery-event workflows

> The historical packaged backend executable is referenced by release notes, but its complete source is not currently part of the public source tree.
