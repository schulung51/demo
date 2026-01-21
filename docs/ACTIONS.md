# Custom Actions Guide

This repository contains reusable Composite Actions for CI/CD workflows.

## Available Actions

### setup-python-env

Sets up Python with caching and installs project dependencies.

**Usage:**
```yaml
- uses: ./.github/actions/setup-python-env
  with:
    python-version: '3.12'  # optional, default: '3.12'
    install-dev: 'true'     # optional, default: 'true'
```

**Outputs:**
- `cache-hit`: Whether pip cache was hit
- `python-path`: Path to Python executable

### quality-checks

Runs linting, type checking, and formatting checks.

**Usage:**
```yaml
- uses: ./.github/actions/quality-checks
  with:
    run-lint: 'true'         # optional, default: 'true'
    run-typecheck: 'true'    # optional, default: 'true'
    run-format-check: 'true' # optional, default: 'true'
    source-dir: 'src/'       # optional, default: 'src/'
    test-dir: 'tests/'       # optional, default: 'tests/'
```

**Outputs:**
- `lint-result`: Lint check result
- `typecheck-result`: Type check result

### run-tests

Runs pytest with coverage reporting.

**Usage:**
```yaml
- uses: ./.github/actions/run-tests
  with:
    coverage-threshold: '80'  # optional, default: '0' (no threshold)
    test-dir: 'tests/'        # optional, default: 'tests/'
    coverage-report: 'xml'    # optional: xml/html/term
```

**Outputs:**
- `coverage`: Coverage percentage
- `test-result`: Test result (passed/failed)

## Reusable Workflows

### ci-reusable.yml

Complete CI workflow that can be called from other repositories.

**Usage:**
```yaml
jobs:
  ci:
    uses: owner/repo/.github/workflows/ci-reusable.yml@v1
    with:
      python-version: '3.12'
      run-lint: true
      run-security: true
      coverage-threshold: 80
    secrets:
      codecov-token: ${{ secrets.CODECOV_TOKEN }}
```

**Inputs:**
| Input | Type | Default | Description |
|-------|------|---------|-------------|
| python-version | string | '3.12' | Python version |
| os | string | 'ubuntu-latest' | Runner OS |
| run-lint | boolean | true | Run linting |
| run-security | boolean | false | Run security checks |
| coverage-threshold | number | 0 | Minimum coverage % |

**Secrets:**
- `codecov-token`: Optional Codecov upload token

**Outputs:**
- `coverage`: Test coverage percentage

## SHA-Pinning

All actions should be pinned to specific commit SHAs for security:

```yaml
# Find SHA for a tag
git ls-remote --tags https://github.com/actions/checkout.git | grep v4.1.1

# Use SHA with version comment
uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11  # v4.1.1
```

Dependabot will automatically create PRs to update pinned SHAs.
