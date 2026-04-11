# MishMash Cookbook & Annual Report

Official cookbook and annual report series for the
**MishMash Centre for AI and Creativity**, built with
[Jupyter Book 2](https://next.jupyterbook.org/) (powered by [MyST-MD](https://mystmd.org/)).

Chapters cover the years **2024–2030**.

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Build the site content

```bash
jupyter-book build --site .
```

This generates the site content in `_build/`.

### 3. Live preview

Start a local development server with live-reload:

```bash
jupyter-book start .
```

Visit [http://localhost:3000](http://localhost:3000) to browse the book.

## Repository Structure

```
myst.yml            ← Jupyter Book 2 project & site configuration
requirements.txt    ← Python dependencies (jupyter-book>=2)
intro.md            ← Introduction / landing page
2024/index.md       ← 2024 Annual Report chapter
2025/index.md       ← 2025 Annual Report chapter
2026/index.md       ← 2026 Annual Report chapter
2027/index.md       ← 2027 Annual Report chapter
2028/index.md       ← 2028 Annual Report chapter
2029/index.md       ← 2029 Annual Report chapter
2030/index.md       ← 2030 Annual Report chapter
```

## Licence

Content is released under
[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) unless stated
otherwise.
