.PHONY: install test lint type-check build clean act-test act-debug

# Development setup
install:
	pip install -e .[dev]

# Testing
test:
	pytest tests/ -v

test-cov:
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term

# Code quality
lint:
	ruff check src/ tests/

lint-fix:
	ruff check src/ tests/ --fix

type-check:
	mypy src/

# Build
build:
	python -m build

# Cleanup
clean:
	rm -rf build/ dist/ *.egg-info/
	rm -rf .pytest_cache/ .mypy_cache/ .ruff_cache/
	rm -rf htmlcov/ .coverage coverage.xml
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

# Local workflow testing with act
act-test:
	@echo "Running CI workflow locally with act..."
	@echo "Note: First run may download runner image (~500MB)"
	act push -j lint

act-debug:
	@echo "Running debug workflow locally..."
	act workflow_dispatch -j debug --input debug_level=verbose --input dump_contexts=true

act-list:
	@echo "Available workflows and jobs:"
	act -l

# Help
help:
	@echo "Available targets:"
	@echo "  install     - Install package with dev dependencies"
	@echo "  test        - Run tests"
	@echo "  test-cov    - Run tests with coverage"
	@echo "  lint        - Run linter"
	@echo "  lint-fix    - Run linter with auto-fix"
	@echo "  type-check  - Run type checker"
	@echo "  build       - Build package"
	@echo "  clean       - Remove build artifacts"
	@echo "  act-test    - Test lint job locally with act"
	@echo "  act-debug   - Run debug workflow locally"
	@echo "  act-list    - List all workflows and jobs"
