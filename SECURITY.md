# Security Policy

Security is especially important for this project because it interacts with API-oriented operational workflows and may be deployed in environments containing sensitive configuration.

## Do not publish sensitive information

Please do not include any of the following in issues, pull requests, screenshots, logs, examples, or commits:

- production API tokens
- usernames or passwords
- VPN credentials
- private keys, certificates, or secret files
- internal-only hostnames, IP addresses, or endpoints that are not intended for public disclosure
- production logs containing sensitive data
- real business records or database contents

Use sanitized or mock values in all public examples.

## Reporting a security issue

If you discover a security issue, please avoid publishing exploit details or sensitive environment information in a public issue. Contact the maintainer privately through an appropriate GitHub contact channel when available.

When reporting a problem, include only the minimum information needed to reproduce the issue and replace any sensitive values with placeholders.

## Scope

Security review currently focuses on:

- unsafe handling of credentials and tokens
- input validation
- API request handling
- file upload/download behavior
- local configuration handling
- data exposure through logs or generated files
- dependency and packaging risks

This policy will be expanded as the project and its public source scope evolve.
