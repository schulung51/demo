# Environment Setup Guide

Diese Anleitung beschreibt die Konfiguration der GitHub Environments für Deployments.

## Environments Übersicht

| Environment | Zweck | Protection Rules |
|-------------|-------|------------------|
| `github-pages` | GitHub Pages | Automatisch erstellt |
| `github-releases` | GitHub Releases | Optional: Reviewer |
| `testpypi` | Test PyPI Publishing | Branch: main |
| `pypi` | PyPI Publishing | Branch: main, Reviewer |
| `staging` | Staging Deployment | Keine |
| `production` | Production Deployment | Reviewer, Wait Timer |

## 1. GitHub Pages Environment

Navigiere zu: **Settings → Pages**

1. Source: **GitHub Actions**
2. Das `github-pages` Environment wird automatisch erstellt

## 2. PyPI Environments (für Package Publishing)

### TestPyPI

1. **TestPyPI Trusted Publisher konfigurieren:**
   - https://test.pypi.org/manage/account/publishing/
   - Owner: `<github-username>`
   - Repository: `badge-gen`
   - Workflow: `publish-pypi.yml`
   - Environment: `testpypi`

2. **GitHub Environment erstellen:**
   - Settings → Environments → New environment → `testpypi`
   - Deployment branches: `main`

### PyPI (Production)

1. **PyPI Trusted Publisher konfigurieren:**
   - https://pypi.org/manage/account/publishing/
   - Owner: `<github-username>`
   - Repository: `badge-gen`
   - Workflow: `publish-pypi.yml`
   - Environment: `pypi`

2. **GitHub Environment erstellen:**
   - Settings → Environments → New environment → `pypi`
   - Deployment branches: `main`
   - Required reviewers: Maintainer hinzufügen

## 3. Release Environment

Navigiere zu: **Settings → Environments → New environment**

1. Name: `github-releases`
2. Optional: Required reviewers für wichtige Releases

## 4. Staging/Production (für Web-Deployments)

### Staging

1. Settings → Environments → New environment → `staging`
2. Deployment branches: `main`, `develop`
3. Environment secrets: `STAGING_API_KEY` etc.

### Production

1. Settings → Environments → New environment → `production`
2. Deployment branches: `main`
3. Protection rules:
   - ☑️ Required reviewers → Maintainer auswählen
   - ☑️ Prevent self-review
   - Wait timer: `10` Minuten (optional)
4. Environment secrets: `PRODUCTION_API_KEY` etc.

## Trusted Publishing (OIDC)

Trusted Publishing ermöglicht Deployments ohne langlebige API-Tokens.

### Vorteile
- Keine Secrets im Repository
- Automatische Token-Rotation
- Besseres Audit-Log
- Kurzlebige Credentials

### Funktionsweise
1. Workflow fordert OIDC-Token an (`id-token: write`)
2. GitHub signiert Token mit Repository-Infos
3. PyPI validiert Token gegen Trusted Publisher Config
4. Upload wird autorisiert

### Permissions erforderlich
```yaml
permissions:
  id-token: write  # Für OIDC Token
```
