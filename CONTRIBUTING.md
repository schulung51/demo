# Contributing Guide

## Commit Message Convention

This project follows [Conventional Commits](https://www.conventionalcommits.org/).

### Format

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

### Types

| Type | Description | Version Bump |
|------|-------------|--------------|
| `feat` | New feature | Minor (0.X.0) |
| `fix` | Bug fix | Patch (0.0.X) |
| `docs` | Documentation | None |
| `style` | Code style (formatting) | None |
| `refactor` | Code refactoring | None |
| `perf` | Performance improvement | Patch (0.0.X) |
| `test` | Tests | None |
| `build` | Build system | None |
| `ci` | CI configuration | None |
| `chore` | Maintenance | None |

### Breaking Changes

Add `!` after the type or include `BREAKING CHANGE:` in the footer:

```
feat!: redesign CLI interface

BREAKING CHANGE: --output flag renamed to --out
```

Breaking changes trigger a **Major** version bump (X.0.0).

### Examples

```bash
# Feature
git commit -m "feat: add badge color customization"

# Bug fix with scope
git commit -m "fix(cli): handle empty repository name"

# Documentation
git commit -m "docs: add API reference"

# Breaking change
git commit -m "feat!: change default output format to SVG"
```

### Setup Commit Template

```bash
git config commit.template .gitmessage
```

## Development Workflow

1. Create a feature branch: `git checkout -b feat/my-feature`
2. Make changes and commit using conventional commits
3. Push and create a Pull Request
4. After merge to main, release is created automatically

## Automatic Releases

When commits are pushed to `main`:
1. Tests run automatically
2. Version is calculated from commit messages
3. CHANGELOG.md is updated
4. Git tag is created
5. GitHub Release is published

Only `feat:`, `fix:`, `perf:`, and breaking changes trigger releases.
