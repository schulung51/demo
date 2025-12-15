.PHONY: install test lint type-check format build clean act-test act-debug release-dry-run

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

# Formatting
format:
	black src/ tests/
	ruff check --fix src/ tests/

format-check:
	black --check src/ tests/
	ruff check src/ tests/

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
	act push -j lint

act-format:
	@echo "Running auto-format workflow locally..."
	act push -W .github/workflows/auto-format.yml

act-debug:
	@echo "Running debug workflow locally..."
	act workflow_dispatch -j debug --input debug_level=verbose --input dump_contexts=true

act-list:
	@echo "Available workflows and jobs:"
	act -l

# Release
release-dry-run:
	@echo "Simulating release (no actual changes)..."
	@echo "Would analyze commits since last tag and calculate next version."
	@echo ""
	@echo "Recent commits:"
	@git log --oneline -10

# Git setup
setup-git:
	@echo "Setting up git commit template..."
	git config commit.template .gitmessage
	@echo "Done. Your commits will now show the conventional commit template."

# Help
help:
	@echo "Available targets:"
	@echo "  install        - Install package with dev dependencies"
	@echo "  test           - Run tests"
	@echo "  test-cov       - Run tests with coverage"
	@echo "  lint           - Run linter"
	@echo "  lint-fix       - Run linter with auto-fix"
	@echo "  type-check     - Run type checker"
	@echo "  format         - Format code with black and ruff"
	@echo "  format-check   - Check code formatting"
	@echo "  build          - Build package"
	@echo "  clean          - Remove build artifacts"
	@echo "  act-test       - Test lint job locally with act"
	@echo "  act-format     - Test auto-format workflow locally"
	@echo "  act-debug      - Run debug workflow locally"
	@echo "  act-list       - List all workflows and jobs"
	@echo "  release-dry-run- Show what release would do"
	@echo "  setup-git      - Configure git commit template"
