# How this book is made

The book is written in Markdown and built with Jupyter Book 2, which runs on the MyST document engine. Every push to the main branch of the repository rebuilds the site with GitHub Actions and publishes it to GitHub Pages. To build it on your own machine:

```bash
pip install -r requirements.txt
jupyter-book build --html
```

The output lands in `_build/html`. For a live preview with reload, run `jupyter-book start`.

## Where the facts come from

The partner list and the glossary are generated from the data files of the centre website, so that each fact is written once. The history and the annual reports draw on the Research Council's announcements, the government's press release of 7 September 2023, the centre's application and grant letter, the website's news and event pages, and the conference programmes. Sources for the dates in the history chapter:

- Government press release on the AI billion, 7 September 2023.
- Research Council news: the centre call (8 February 2024), 122 sketches (21 June 2024), 19 applications to the final round (4 April 2025), six centres funded (11 June 2025).
- The MishMash application of 15 January 2025 and the grant letter of 20 June 2025.
- mishmash.no news and events, 2025 to 2026.

## AI disclosure

The first version of this book was drafted with an AI coding agent, Claude, working from the sources above and from the centre's own files, and edited by the centre director. The agent drafted and checked; a person decided. The centre uses AI openly in its own communication and says so, here as on the website's [AI colophon](https://mishmash.no/about/ai-colophon/). Responsibility for what is written here rests with the centre, not with the model.

## Licence

Text is released under the [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) licence unless stated otherwise. The build tooling is under the licence in the repository.
