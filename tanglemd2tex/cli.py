from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .core import tangle_file
from .lit_file import find_lit_files


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="tanglemd2tex",
        description="Extract ```latex``` fenced blocks from .lit.md files into .tex files.",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help=(
            ".lit.md files or directories to scan recursively. "
            "Defaults to the current directory."
        ),
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    paths = args.paths or [Path(".")]

    try:
        lit_files = find_lit_files(paths)
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    if not lit_files:
        print("ERROR: no .lit.md files found", file=sys.stderr)
        return 1

    status = 0
    for lit_path in lit_files:
        try:
            tex_path = tangle_file(lit_path)
        except Exception as error:
            print(f"ERROR: {error}", file=sys.stderr)
            status = 1
            continue

        print(f"WROTE: {tex_path}")

    return status
