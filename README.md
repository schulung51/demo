# badge-gen

Minimaler Beispiel-CLI für eine GitHub-Actions-Schulung.

## Zweck

Dieses Repository demonstriert GitHub Actions Konzepte:
- Kapitel 1: Event-Modell, Runner, Workflow-Syntax
- Kapitel 2: Jobs, Matrix-Strategien, Failure-Handling

## Lokale Entwicklung

```bash
# Installation mit Dev-Dependencies
pip install -e .[dev]

# CLI ausführen
badge-gen --repo octocat/Hello-World

# Tests ausführen
pytest

# Linting
ruff check src/ tests/
mypy src/
```

## CI/CD Workflows

| Workflow | Zweck |
|----------|-------|
| `ci.yml` | Linting und Unit Tests |
| `multi-platform.yml` | Matrix-Testing (Linux, Windows, macOS × Python 3.11/3.12) |
| `security.yml` | Parallele Security-Scans (Bandit, pip-audit) |
