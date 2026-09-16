# Architecture Overview

This document describes the public source scope of the API Usage Statistics Dashboard.

## Current public-source architecture

```text
Browser
  |
  | static HTML / CSS / JavaScript
  v
web/index.html + web/styles.css + web/app.js
  |
  | relative HTTP requests to /api/*
  v
Backend service boundary
  |
  +-- connectivity / collection jobs
  +-- system inventory and validation
  +-- local database operations
  +-- report and file operations
```

The front end intentionally uses relative `/api/...` paths so deployment-specific hosts and credentials do not need to be hard-coded into browser source.

## Repository scope

The public repository currently includes the Web front-end source, launch scripts, documentation, sanitized fixtures, and historical packaging information.

Historical packaging notes reference a Windows `server/web_server.exe`. The complete source for that packaged backend is not currently part of the public source tree, so this repository must not be described as a complete backend implementation.

## Front-end responsibilities

`web/app.js` currently handles:

- navigation and dashboard rendering;
- API connectivity and collection requests;
- task progress polling;
- system inventory search and database import/export actions;
- result matching and validation views;
- report-generation requests;
- log/file views;
- server-setting updates.

The browser does not need to contain production credentials. When a token is required by a deployment, it should be supplied at runtime and handled by the server according to the deployment's security policy.

## Public mock data

`examples/mock/` contains synthetic payloads that approximate the response shapes consumed by the front end. They are intended for documentation, tests, future local mock-server development, and public security review.

No production captures should be committed as fixtures.

## Security boundaries

Public source must not contain:

- production tokens or passwords;
- private keys or certificates;
- VPN credentials;
- production-only endpoints that are not intended for disclosure;
- real logs or business records;
- sensitive database contents.

See `SECURITY.md` for reporting and handling guidance.

## Development direction

Near-term engineering priorities are:

1. expand automated tests around public source and fixtures;
2. improve input validation and error handling;
3. separate environment-specific configuration from source code;
4. provide a local mock API for end-to-end front-end development;
5. continue backend-source migration where redistribution is appropriate;
6. strengthen CI and security review.
