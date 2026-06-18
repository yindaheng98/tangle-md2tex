from __future__ import annotations

from markdown_it import MarkdownIt


def extract_latex_text(text: str) -> str:
    latex_blocks = [
        token.content.strip()
        for token in MarkdownIt("commonmark").parse(text)
        if token.type == "fence" and token.info.strip() == "latex"
    ]

    if not latex_blocks:
        return ""

    return "\n\n".join(latex_blocks).rstrip() + "\n"
