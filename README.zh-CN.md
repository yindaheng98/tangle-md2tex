# tangle-md2tex

从 literate Markdown 文件中抽取 LaTeX fenced code block，生成同名 `.tex` 文件。

English documentation: [README.md](README.md).

## 这个工具做什么

`tangle-md2tex` 读取后缀为 `.lit.md` 的 Markdown 文件，找到 info string 精确为 `latex` 的 fenced code block，并把这些 LaTeX 内容写入同目录下的 `.tex` 文件。

例如：

````markdown
```latex
第一段。

第二段。
```

这里写解释：为什么这样写、这一段承接哪里、下一步要修改什么。
````

会生成：

```tex
第一段。

第二段。
```

## Literate Programming 的思想

Literate programming 的核心思想是：程序或文稿不只是给机器处理的文本，也应该是给人阅读、检查和修改的文本。

在传统写法里，`.tex` 文件通常混在一起承载两件事：

- 真正要输出到论文里的 LaTeX 正文。
- 写作者自己的思考、解释、计划、修改理由和上下文。

时间一长，正文会变得难检查，解释又容易污染最终输出。`tangle-md2tex` 用一个很小的约定把这两件事分开：

- `.lit.md` 是人读的源文件，可以穿插解释、笔记、审稿意见、TODO 和上下文。
- ```latex fenced block 里放机器要抽取的 LaTeX 正文。
- 运行 `tanglemd2tex` 后生成 `.tex`，只包含 LaTeX 正文。

这样写论文时，你可以把“为什么这样写”放在 Markdown 解释里，把“最终进入论文的内容”放在 `latex` block 里。生成出来的 `.tex` 保持干净，源文件则保留完整思路。

## 文件命名

源文件使用 `.lit.md` 后缀：

```text
paper.lit.md -> paper.tex
sections/intro.lit.md -> sections/intro.tex
```

目录输入会递归扫描其中所有 `.lit.md` 文件。

## 写法示例

````markdown
# Introduction

这一节先建立背景，再指出当前方法的问题。

```latex
\section{Introduction}

Recent writing agents can generate fluent academic prose from high-level user instructions.
```

这一句建立背景，说明系统已经具备从抽象指令生成学术文本的能力。

```latex
However, fluent prose alone does not make a generated manuscript easy to inspect, revise, or trust.
```

这一句把论述从“能写”转向“能否被检查和信任”。
````

生成的 `.tex` 是：

```tex
\section{Introduction}

Recent writing agents can generate fluent academic prose from high-level user instructions.
However, fluent prose alone does not make a generated manuscript easy to inspect, revise, or trust.
```

## 换行和空行

工具会原样保留 `latex` fenced block 内部的内容，包括：

- 开头空行。
- 段落之间的空行。
- 结尾空行。

这很重要，因为 LaTeX 依赖空行来区分段落。工具不会对 LaTeX 内容做 `strip()`，也不会额外格式化或校验 LaTeX。

多个 `latex` block 会按出现顺序直接拼接。是否在 block 之间留空行，由你在各个 fenced block 内部控制。

## 安装

```bash
pip install tangle-md2tex
```

本地开发安装：

```bash
python -m pip install -e .
```

## 命令行用法

处理单个文件：

```bash
tanglemd2tex paper.lit.md
```

处理目录下所有 `.lit.md` 文件：

```bash
tanglemd2tex sections/
```

不传参数时，默认递归扫描当前目录：

```bash
tanglemd2tex
```

也可以用模块方式运行：

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

## 规则

- 源文件必须以 `.lit.md` 结尾。
- 输出文件和源文件同目录，后缀改为 `.tex`。
- 只抽取 info string 为 `latex` 的 fenced code block。
- Markdown 解释文本不会进入 `.tex` 输出。
- 工具不解析、不检查、不格式化 LaTeX。

## 许可证

MIT
