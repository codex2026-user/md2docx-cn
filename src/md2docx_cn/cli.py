"""Command-line interface for md2docx-cn."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path

from .converter import convert_markdown


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="md2docx-cn",
        description="Convert Chinese Markdown articles into Word documents.",
    )
    parser.add_argument("source", type=Path, help="UTF-8 Markdown input file")
    parser.add_argument("-o", "--output", required=True, type=Path)
    parser.add_argument("--author", default="", help="Word document author")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    output = convert_markdown(args.source, args.output, author=args.author)
    print(f"Created: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
