# MishMash Cookbook and Annual Reports

The running record of the MishMash Centre for AI and Creativity: what the centre is, how it came about, how it works, and one annual report per year from 2024 to 2030. Each year's chapter is the basis of the centre's annual report to the Research Council. Built with [Jupyter Book 2](https://next.jupyterbook.org/) on the [MyST](https://mystmd.org/) document engine and published at https://mishmash-norway.github.io/MishMash-Cookbook/.

## Build

```bash
pip install -r requirements.txt
jupyter-book build --html      # static site in _build/html
jupyter-book start             # live preview at http://localhost:3000
```

The facts and figures for each year are generated from the website's data: run `python3 tools/facts.py` (with `../mishmash-web` next to this repository, or `MISHMASH_WEB` set) before building, and it writes `reports/_facts/YYYY.md`. The colours and the banner are in `assets/style.css`, matching mishmash.no.

Node.js 18 or newer is needed; the MyST engine installs itself on first run. Pushing to `main` rebuilds and deploys the site through `.github/workflows/deploy.yml`.

## Layout

```
myst.yml            project and table of contents
intro.md            landing page
centre/             description, organisation, partners, how we work, history, glossary
reports/            one chapter per year, 2024.md to 2030.md
colophon.md         how the book is made, sources, AI disclosure
```

The partner list and the glossary are generated from the data files of the [centre website](https://github.com/MishMash-Norway/mishmash-web); edit them there.

## Licence

Text is released under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) unless stated otherwise.
