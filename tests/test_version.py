"""Tests for package version."""
import badge_gen


def test_version_exists():
    """Package should have a version string."""
    assert hasattr(badge_gen, "__version__")
    assert isinstance(badge_gen.__version__, str)


def test_version_format():
    """Version should follow semver pattern."""
    version = badge_gen.__version__
    parts = version.split(".")
    assert len(parts) >= 2, "Version should have at least major.minor"
