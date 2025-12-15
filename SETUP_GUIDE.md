# Environment Setup Guide

Diese Anleitung beschreibt die manuelle Konfiguration der GitHub Environments.

## 1. Environments erstellen

Navigiere zu: **Settings → Environments → New environment**

### Staging Environment

1. Name: `staging`
2. Deployment branches: **Selected branches** → `develop`
3. Environment secrets:
   - `STAGING_PYPI_TOKEN` (optional, für Test PyPI)

### Production Environment

1. Name: `production`
2. Deployment branches: **Selected branches** → `main`
3. Protection rules:
   - ☑️ Required reviewers → Maintainer auswählen
   - ☑️ Prevent self-review (empfohlen)
   - Wait timer: `10` Minuten (optional)
4. Environment secrets:
   - `PROD_PYPI_TOKEN` (optional, für PyPI)

## 2. Repository Variables anlegen

Navigiere zu: **Settings → Secrets and variables → Actions → Variables**

| Name | Wert | Beschreibung |
|------|------|--------------|
| `API_URL` | `https://api.example.com` | API Basis-URL |
| `LOG_LEVEL` | `info` | Logging-Level |

## 3. Repository Secrets anlegen

Navigiere zu: **Settings → Secrets and variables → Actions → Secrets**

| Name | Beschreibung |
|------|--------------|
| `API_KEY` | Beispiel-API-Key für Demo |

## 4. GitHub Pages aktivieren

Navigiere zu: **Settings → Pages**

1. Source: **GitHub Actions**
2. Das `github-pages` Environment wird automatisch erstellt

## 5. Workflow-Berechtigungen prüfen

Navigiere zu: **Settings → Actions → General → Workflow permissions**

Empfohlen: **Read repository contents and packages permissions**
(Workflows setzen explizite Permissions)
