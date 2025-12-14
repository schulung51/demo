from badge_gen.cli import main


def test_cli_importable():
    assert callable(main)
