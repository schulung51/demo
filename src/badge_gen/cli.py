"""Command-line interface for badge-gen."""

import argparse
import sys
from pathlib import Path


def create_badge(name: str, value: str, color: str) -> str:
    """Generate a simple SVG badge."""
    # Einfache Badge-Generierung (vereinfacht)
    name_width = len(name) * 7 + 10
    value_width = len(value) * 7 + 10
    total_width = name_width + value_width

    colors = {
        "green": "#4c1",
        "yellow": "#dfb317",
        "red": "#e05d44",
        "blue": "#007ec6",
        "gray": "#555",
        "orange": "#fe7d37",
    }
    color_hex = colors.get(color, colors["blue"])

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}" height="20">
  <linearGradient id="b" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <mask id="a">
    <rect width="{total_width}" height="20" rx="3" fill="#fff"/>
  </mask>
  <g mask="url(#a)">
    <rect width="{name_width}" height="20" fill="#555"/>
    <rect x="{name_width}" width="{value_width}" height="20" fill="{color_hex}"/>
    <rect width="{total_width}" height="20" fill="url(#b)"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="Verdana,sans-serif" font-size="11">
    <text x="{name_width/2}" y="15" fill="#010101" fill-opacity=".3">{name}</text>
    <text x="{name_width/2}" y="14">{name}</text>
    <text x="{name_width + value_width/2}" y="15" fill="#010101" fill-opacity=".3">{value}</text>
    <text x="{name_width + value_width/2}" y="14">{value}</text>
  </g>
</svg>"""
    return svg


def main() -> None:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(description="Generate simple repository badges")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Create badge command
    create_parser = subparsers.add_parser("create", help="Create a badge")
    create_parser.add_argument(
        "--name",
        "-n",
        required=True,
        help="Badge label (left side)",
    )
    create_parser.add_argument(
        "--value",
        "-v",
        required=True,
        help="Badge value (right side)",
    )
    create_parser.add_argument(
        "--color",
        "-c",
        default="blue",
        choices=["green", "yellow", "red", "blue", "gray", "orange"],
        help="Badge color (default: blue)",
    )
    create_parser.add_argument(
        "--output",
        "-o",
        help="Output file path (default: stdout)",
    )

    # Legacy: simple repo argument for backwards compatibility
    parser.add_argument(
        "--repo",
        help="GitHub repository in the form owner/name",
    )

    args = parser.parse_args()

    if args.command == "create":
        svg = create_badge(args.name, args.value, args.color)
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(svg)
            print(f"Badge saved to {args.output}")
        else:
            print(svg)
    elif args.repo:
        # Legacy behavior
        print(f"Badge generation placeholder for repository: {args.repo}")
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
