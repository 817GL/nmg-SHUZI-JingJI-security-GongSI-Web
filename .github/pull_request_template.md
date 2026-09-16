## Summary

Describe the problem and the change.

## Testing

Explain how the change was tested. Include commands or sanitized mock data where useful.

## Security / data-handling checklist

- [ ] I did not include production API tokens, passwords, VPN credentials, private keys, or certificates.
- [ ] I did not include private endpoints, sensitive logs, production database contents, or real business records.
- [ ] Public examples use synthetic or sanitized values.
- [ ] I considered input validation, error handling, and data exposure where relevant.
- [ ] I ran `python scripts/validate_public_repo.py`.
- [ ] I ran `node --check web/app.js` when JavaScript changed.

## Impact

Note whether this changes API behavior, configuration, stored data, reporting, or security behavior.
