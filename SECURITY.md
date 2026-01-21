# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.6.x   | :white_check_mark: |
| < 0.6   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it by:

1. **DO NOT** open a public issue
2. Email the maintainers directly
3. Include detailed information about the vulnerability

## Security Practices

### GitHub Actions Security

This project follows security best practices for GitHub Actions:

#### SHA-Pinning

All third-party actions are pinned to specific commit SHAs:

```yaml
# ✅ Secure - SHA-pinned with version comment
uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11  # v4.1.1

# ❌ Insecure - Tag can be moved
uses: actions/checkout@v4
```

#### Minimal Permissions

Workflows use minimal permissions:

```yaml
permissions:
  contents: read  # Only what's needed
```

#### Dependabot

Automatic security updates via Dependabot for:
- GitHub Actions
- Python dependencies

### Third-Party Action Verification

Before using a third-party action:

1. Check for verified creator badge
2. Review the action's source code
3. Pin to a specific commit SHA
4. Keep updated via Dependabot
