from __future__ import annotations

from pathlib import Path


LIT_SUFFIX = ".lit.md"
TEX_SUFFIX = ".tex"


def lit_to_tex_path(lit_path: Path) -> Path:
    if not lit_path.name.endswith(LIT_SUFFIX):
        raise ValueError(f"not a {LIT_SUFFIX} file: {lit_path}")

    tex_name = lit_path.name[: -len(LIT_SUFFIX)] + TEX_SUFFIX
    return lit_path.with_name(tex_name)


def find_lit_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []

    for path in paths:
        if path.is_dir():
            files.extend(path.rglob(f"*{LIT_SUFFIX}"))
            continue

        if path.is_file():
            if not path.name.endswith(LIT_SUFFIX):
                raise ValueError(f"not a {LIT_SUFFIX} file: {path}")
            files.append(path)
            continue

        raise ValueError(f"path does not exist: {path}")

    return files
