"""Tests for the badge-gen CLI."""
import subprocess
import sys
import tempfile
from pathlib import Path

from badge_gen.cli import create_badge, main


def test_cli_importable():
    """CLI main function should be callable."""
    assert callable(main)


def test_create_badge_returns_svg():
    """create_badge should return valid SVG."""
    result = create_badge("test", "value", "green")
    assert result.startswith("<svg")
    assert "test" in result
    assert "value" in result


def test_create_badge_colors():
    """create_badge should support different colors."""
    for color in ["green", "yellow", "red", "blue", "gray", "orange"]:
        result = create_badge("label", "value", color)
        assert "<svg" in result


def test_cli_create_command():
    """CLI create command should work."""
    result = subprocess.run(
        [sys.executable, "-m", "badge_gen.cli", "create", "-n", "test", "-v", "ok"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "<svg" in result.stdout


def test_cli_create_with_output():
    """CLI create command should write to file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output = Path(tmpdir) / "badge.svg"
        result = subprocess.run(
            [
                sys.executable, "-m", "badge_gen.cli",
                "create", "-n", "test", "-v", "ok", "-o", str(output)
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert output.exists()
        content = output.read_text()
        assert "<svg" in content


def test_cli_help():
    """CLI should show help text."""
    result = subprocess.run(
        [sys.executable, "-m", "badge_gen.cli", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "badge" in result.stdout.lower()
