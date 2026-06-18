# tangle-md2tex

Extract LaTeX fenced code blocks from literate Markdown files.

中文文档见 [README.zh-CN.md](README.zh-CN.md).

## What It Does

`tangle-md2tex` reads Markdown files ending in `.lit.md`, extracts fenced code blocks whose info string is exactly `latex`, and writes the extracted LaTeX to a sibling `.tex` file.

For example:

````markdown
```latex
First paragraph.

Second paragraph.
```

This prose explains why the LaTeX above is written this way.
````

becomes:

```tex
First paragraph.

Second paragraph.
```

## Literate Markdown Format

Use `.lit.md` as the source file extension:

```text
paper.lit.md -> paper.tex
sections/intro.lit.md -> sections/intro.tex
```

Only `latex` fenced code blocks are extracted:

````markdown
```latex
\section{Introduction}

This is the manuscript text.
```

Explanation, notes, outlines, TODOs, or review comments can live here. They are
not copied into the generated `.tex` file.
````

Fence contents are copied as-is from `markdown-it-py`'s token content. Leading
blank lines, paragraph-separating blank lines, and trailing blank lines inside a
`latex` fence are preserved because LaTeX uses blank lines to separate
paragraphs.

## Install

```bash
pip install tangle-md2tex
```

For local development:

```bash
python -m pip install -e .
```

## Usage

Process one file:

```bash
tanglemd2tex paper.lit.md
```

Process every `.lit.md` file under a directory:

```bash
tanglemd2tex sections/
```

If no path is given, the current directory is scanned recursively:

```bash
tanglemd2tex
```

You can also run it as a module:

```bash
python -m tanglemd2tex paper.lit.md
```

## Python API

```python
from pathlib import Path

from tanglemd2tex import tangle_file, tangle_text

tex_text = tangle_text(markdown_text)
tex_path = tangle_file(Path("paper.lit.md"))
```

## Rules

- Source files must end with `.lit.md`.
- Output files are written next to the source file with the `.tex` extension.
- Only fenced code blocks with info string `latex` are extracted.
- Non-LaTeX Markdown prose is treated as explanation and ignored by the output.
- The tool does not parse or validate LaTeX.

## License

MIT
