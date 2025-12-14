# badge-gen

Minimaler Beispiel-CLI für eine GitHub-Actions-Schulung.

## Zweck

Dieses Repository demonstriert GitHub Actions Konzepte:
- Kapitel 1: Event-Modell, Runner, Workflow-Syntax
- Kapitel 2: Jobs, Matrix-Strategien, Failure-Handling
- Kapitel 3: Secrets, Variables, Permissions, Environments
- Kapitel 4: Caching, Debugging, Performance-Optimierung

## Lokale Entwicklung

```bash
# Installation mit Dev-Dependencies
make install
# oder: pip install -e .[dev]

# Tests ausführen
make test
make test-cov  # mit Coverage

# Code-Qualität
make lint
make type-check

# Package bauen
make build
```

## Lokales Workflow-Testing mit act

[act](https://github.com/nektos/act) ermöglicht lokales Testen von GitHub Actions Workflows.

### Installation

```bash
# macOS
brew install act

# Linux
curl -sSf https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# Windows
choco install act-cli
```

### Verwendung

```bash
# Lint-Job lokal testen
make act-test

# Debug-Workflow ausführen
make act-debug

# Alle Workflows/Jobs auflisten
make act-list

# Mit Secrets (Datei aus .secrets.example kopieren)
cp .secrets.example .secrets
# Werte eintragen, dann:
act push --secret-file .secrets
```

## CI/CD Workflows

| Workflow | Zweck | Caching |
|----------|-------|---------|
| `ci.yml` | Lint, Test, Build | ✅ pip cache |
| `debug.yml` | Context-Dump, System-Info | - |
| `cache-demo.yml` | Caching-Mechanismen Demo | ✅ |
| `multi-platform.yml` | Matrix-Testing | ✅ pip cache |
| `security.yml` | Security-Scans | - |
| `pages.yml` | GitHub Pages | - |
| `deploy.yml` | PyPI Deployment | - |

## Performance-Optimierungen

Der CI-Workflow nutzt folgende Optimierungen:

1. **Caching**: `setup-python` mit `cache: 'pip'`
2. **Concurrency**: Alte Runs werden bei neuem Push abgebrochen
3. **Parallele Jobs**: `lint` und `test` laufen gleichzeitig
4. **Optimierte Matrix**: Windows/macOS nur mit neuester Python-Version
5. **Selektive Steps**: Coverage nur für Ubuntu+Python 3.12
