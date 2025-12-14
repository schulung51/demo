# Changelog

All notable changes to this project will be documented in this file.

## [0.6.0] - 2025-01-15

### Added
- Composite Actions for reusable CI components
  - `setup-python-env`: Python setup with caching
  - `quality-checks`: Linting, type checking, formatting
  - `run-tests`: Tests with coverage reporting
- Reusable workflow `ci-reusable.yml`
- SHA-pinning for all third-party actions
- Dependabot configuration for automatic updates
- Security policy documentation
- Actions documentation in docs/ACTIONS.md

### Changed
- CI workflow now uses local Composite Actions
- All action references use commit SHAs

### Security
- Implemented SHA-pinning for supply chain security
- Added Dependabot for automated security updates

## [0.5.0] - 2025-01-01

### Added
- Repository automation with auto-format workflow
- Conventional commits support
- Automated changelog generation
- Release workflow with GitHub Releases

## [0.4.0] - 2024-12-15

### Added
- Caching for pip dependencies
- Debug workflow for troubleshooting
- Local testing support with act
- Makefile for development commands

## [0.3.0] - 2024-12-01

### Added
- GitHub Pages deployment workflow
- Environment-based deployments
- Secrets and variables demonstration

## [0.2.0] - 2024-11-15

### Added
- Multi-platform CI
- Matrix testing
- Security scanning workflows

## [0.1.0] - 2024-11-01

### Added
- Initial project setup
- Basic CLI structure
- CI workflow with linting
