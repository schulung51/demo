# badge-gen

Minimaler Beispiel-CLI für eine GitHub-Actions-Schulung.

## Zweck

Dieses Repository demonstriert GitHub Actions Konzepte:
- Kapitel 1: Event-Modell, Runner, Workflow-Syntax
- Kapitel 2: Jobs, Matrix-Strategien, Failure-Handling
- Kapitel 3: Secrets, Variables, Permissions, Environments
- Kapitel 4: Caching, Debugging, Performance-Optimierung
- Kapitel 5: Repository-Automatisierung, Releases, Conventional Commits

## Lokale Entwicklung

```bash
# Installation mit Dev-Dependencies
make install

# Code formatieren
make format

# Tests ausführen
make test

# Code-Qualität prüfen
make lint
make type-check

# Package bauen
make build
```

## Conventional Commits

Dieses Projekt verwendet [Conventional Commits](https://www.conventionalcommits.org/) für automatische Versionierung und Changelog-Generierung.

### Commit-Template einrichten

```bash
make setup-git
```

### Commit-Typen

| Type | Beschreibung | Version-Bump |
|------|--------------|--------------|
| `feat` | Neues Feature | Minor |
| `fix` | Bug-Fix | Patch |
| `docs` | Dokumentation | - |
| `style` | Formatierung | - |
| `refactor` | Refactoring | - |
| `perf` | Performance | Patch |
| `test` | Tests | - |
| `ci` | CI/CD | - |
| `chore` | Wartung | - |

### Beispiele

```bash
git commit -m "feat: add badge color customization"
git commit -m "fix(cli): handle empty input"
git commit -m "feat!: redesign API"  # Breaking Change
```

## CI/CD Workflows

| Workflow | Trigger | Zweck |
|----------|---------|-------|
| `ci.yml` | Push, PR | Lint, Tests |
| `auto-format.yml` | Push, PR | Code automatisch formatieren |
| `release.yml` | Push to main | Version bump, Changelog, GitHub Release |
| `debug.yml` | Manual | Debugging |
| `pages.yml` | Push to main | GitHub Pages |
| `deploy.yml` | Tags | PyPI Deployment |

## Releases

Releases werden automatisch erstellt wenn:
1. Commits mit `feat:`, `fix:`, `perf:` oder Breaking Changes auf `main` gepusht werden
2. Tests erfolgreich durchlaufen
3. `conventional-changelog-action` eine neue Version berechnet

Der Release-Prozess:
1. Version in `pyproject.toml` aktualisieren
2. `CHANGELOG.md` generieren
3. Git-Tag erstellen
4. GitHub Release mit Artefakten erstellen

## Changelog

Siehe [CHANGELOG.md](CHANGELOG.md) für alle Änderungen.
