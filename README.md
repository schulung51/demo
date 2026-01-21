# badge-gen

Minimaler Beispiel-CLI für eine GitHub-Actions-Schulung.

## Zweck

Dieses Repository demonstriert GitHub Actions Konzepte:
- Kapitel 1: Event-Modell, Runner, Workflow-Syntax
- Kapitel 2: Jobs, Matrix-Strategien, Failure-Handling
- Kapitel 3: Secrets, Variables, Permissions, Environments
- Kapitel 4: Caching, Debugging, Performance-Optimierung
- Kapitel 5: Repository-Automatisierung, Releases, Conventional Commits
- Kapitel 6: Actions-Ökosystem, Composite Actions, Reusable Workflows

## Lokale Entwicklung

```bash
make install    # Dependencies installieren
make test       # Tests ausführen
make lint       # Linting
make format     # Code formatieren
make build      # Package bauen
```

## Custom Actions

Dieses Repository enthält wiederverwendbare Composite Actions:

| Action | Beschreibung |
|--------|--------------|
| `setup-python-env` | Python Setup mit Caching |
| `quality-checks` | Linting, Type-Checking, Formatting |
| `run-tests` | Tests mit Coverage |

**Verwendung:**
```yaml
steps:
  - uses: ./.github/actions/setup-python-env
    with:
      python-version: '3.12'
```

Siehe [docs/ACTIONS.md](docs/ACTIONS.md) für Details.

## Reusable Workflows

Der `ci-reusable.yml` Workflow kann von anderen Repositories aufgerufen werden:

```yaml
jobs:
  ci:
    uses: owner/repo/.github/workflows/ci-reusable.yml@v1
    with:
      python-version: '3.12'
      run-lint: true
```

## Security

### SHA-Pinning

Alle Third-Party Actions sind auf Commit-SHAs gepinnt:

```yaml
uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11  # v4.1.1
```

### Dependabot

Automatische Updates für:
- GitHub Actions (wöchentlich)
- Python Dependencies (wöchentlich)

Siehe [SECURITY.md](SECURITY.md) für Details.

## Workflows

| Workflow | Trigger | Beschreibung |
|----------|---------|--------------|
| `ci.yml` | Push, PR | CI mit Composite Actions |
| `ci-reusable.yml` | workflow_call | Reusable CI Workflow |
| `release.yml` | Push to main | Automatische Releases |
| `auto-format.yml` | Push, PR | Code-Formatierung |
