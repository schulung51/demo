# badge-gen

A simple badge generator for GitHub repositories - used as a GitHub Actions training project.

## Features

- Generate SVG badges with customizable labels, values, and colors
- GitHub Pages deployment with automatic badge gallery
- PyPI publishing with Trusted Publishing (OIDC)
- Comprehensive CI/CD pipeline

## Installation

```bash
pip install badge-gen
```

## Usage

### Create a badge

```bash
# Output to stdout
badge-gen create --name "build" --value "passing" --color green

# Save to file
badge-gen create -n "coverage" -v "87%" -c yellow -o badge.svg
```

### Available colors

- `green` - Success, passing
- `yellow` - Warning, partial
- `red` - Error, failing
- `blue` - Info, default
- `gray` - Inactive, unknown
- `orange` - Important, attention

## GitHub Actions Training

This repository demonstrates:

| Chapter | Topic |
|---------|-------|
| 1 | Event-Modell, Runner, Workflow-Syntax |
| 2 | Jobs, Matrix-Strategien, Failure-Handling |
| 3 | Secrets, Variables, Permissions, Environments |
| 4 | Caching, Debugging, Performance-Optimierung |
| 5 | Repository-Automatisierung, Conventional Commits |
| 6 | Actions-Ökosystem, Composite Actions, Reusable Workflows |
| 7 | Deployment-Strategien, GitHub Pages, PyPI Publishing |

## Workflows

| Workflow | Trigger | Description |
|----------|---------|-------------|
| `ci.yml` | Push, PR | Lint, test with matrix |
| `release.yml` | Push to main | Automatic versioning and release |
| `deploy-pages.yml` | Push to main | Deploy badge gallery to GitHub Pages |
| `publish-pypi.yml` | Release published | Publish to PyPI via OIDC |

## Environments

| Environment | Purpose | Protection |
|-------------|---------|------------|
| `github-pages` | GitHub Pages | Auto |
| `github-releases` | GitHub Releases | Optional |
| `testpypi` | TestPyPI Publishing | Branch: main |
| `pypi` | PyPI Publishing | Branch: main, Reviewer |

## Development

```bash
# Install with dev dependencies
make install

# Run tests
make test

# Format code
make format

# Build package
make build
```

## License

MIT
