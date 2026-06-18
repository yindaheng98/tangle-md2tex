from __future__ import annotations

from pathlib import Path
from markdown_it import MarkdownIt

from .lit_file import lit_to_tex_path


def tangle_text(text: str) -> str:
    return "".join(
        token.content
        for token in MarkdownIt("commonmark").parse(text)
        if token.type == "fence" and token.info.strip() == "latex"
    )


def tangle_file(lit_path: Path) -> Path:
    tex_path = lit_to_tex_path(lit_path)
    text = lit_path.read_text(encoding="utf-8")
    tex_text = tangle_text(text)
    tex_path.write_text(tex_text, encoding="utf-8")
    return tex_path
