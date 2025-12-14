# badge-gen

Minimaler Beispiel-CLI für eine GitHub-Actions-Schulung.

Zweck dieses Repositories:
- Demonstration von GitHub Actions Workflows
- Event-Modell, Runner, Permissions, Releases
- Kein produktiver Anspruch

## Nutzung (lokal)

```bash
pip install -e .
badge-gen --repo octocat/Hello-World
```

## CI

Dieses Repository enthält eine einfache CI-Pipeline:
- Ruff (Linting)
- mypy (Type Checking)

Details siehe `.github/workflows/ci.yml`
