# Contributing

Thanks for your interest in improving this project.

The project is currently maintained independently and is still being cleaned up and documented for broader public review. Small, focused contributions are preferred.

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

## Before submitting

Please make sure your change:

1. does not contain production API tokens, passwords, VPN credentials, private keys, certificates, or other secrets;
2. does not expose internal-only hostnames, IP addresses, endpoints, logs, or business data;
3. uses mock or sanitized values in examples;
4. keeps the change focused and documents any behavior change;
5. avoids committing generated runtime data or temporary files.

## Pull requests

A useful pull request should explain:

- what problem it solves;
- what changed;
- how the change was tested;
- whether it affects configuration, stored data, API behavior, or security.

For security-sensitive findings, please follow `SECURITY.md` rather than publishing sensitive exploit details in a public issue.

## Development direction

Current priorities include automated testing, mock API support, configuration separation, stronger validation, CI checks, and continued security review.
