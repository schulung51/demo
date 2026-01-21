"""Tests for the badge-gen CLI."""

import subprocess
import sys

from badge_gen.cli import main


def test_cli_importable():
    """CLI main function should be callable."""
    assert callable(main)


def test_cli_help():
    """CLI should show help text."""
    result = subprocess.run(
        [sys.executable, "-m", "badge_gen.cli", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "repository" in result.stdout.lower()


def test_cli_requires_repo():
    """CLI should fail without --repo argument."""
    result = subprocess.run(
        [sys.executable, "-m", "badge_gen.cli"],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
