# badge-gen

Minimaler Beispiel-CLI für eine GitHub-Actions-Schulung.

## Zweck

Dieses Repository demonstriert GitHub Actions Konzepte:
- Kapitel 1: Event-Modell, Runner, Workflow-Syntax
- Kapitel 2: Jobs, Matrix-Strategien, Failure-Handling
- Kapitel 3: Secrets, Variables, Permissions, Environments

## Lokale Entwicklung

```bash
# Installation mit Dev-Dependencies
pip install -e .[dev]

# CLI ausführen
badge-gen --repo octocat/Hello-World

# Tests ausführen
pytest

# Package bauen
python -m build
```

## CI/CD Workflows

| Workflow | Zweck |
|----------|-------|
| `ci.yml` | Linting und Unit Tests (explizite Permissions) |
| `multi-platform.yml` | Matrix-Testing (Linux, Windows, macOS) |
| `security.yml` | Parallele Security-Scans |
| `pages.yml` | GitHub Pages Deployment |
| `deploy.yml` | PyPI Deployment mit Environments |
| `config-demo.yml` | Variables und Secrets Demo |

## Environment-Setup

Für die Deployment-Workflows müssen folgende Environments konfiguriert werden:

### Staging Environment
- **Name:** `staging`
- **Deployment Branches:** `develop`
- **Secrets:** `STAGING_PYPI_TOKEN` (optional)

### Production Environment
- **Name:** `production`
- **Deployment Branches:** `main`, `v*` tags
- **Protection Rules:**
  - Required Reviewers: 1-2 Maintainer
  - Wait Timer: 10 Minuten (optional)
- **Secrets:** `PROD_PYPI_TOKEN` (optional)

### GitHub Pages Environment
- **Name:** `github-pages`
- Wird automatisch von GitHub erstellt

## Variables und Secrets

### Repository Variables (nicht sensitiv)
```
API_URL=https://api.example.com
LOG_LEVEL=info
```

### Repository Secrets (sensitiv)
```
API_KEY=<your-api-key>
STAGING_PYPI_TOKEN=<test-pypi-token>
PROD_PYPI_TOKEN=<pypi-token>
```
