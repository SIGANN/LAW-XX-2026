# LAW XX Website (Pelican)

This repository hosts the sources for the 20th Linguistic Annotation Workshop website.

## Project layout

- `content/` – AsciiDoc pages for Home, CFP, Committee, Invited Speakers, Program, and Accepted Papers. Everything is stubbed with clear TODOs so editors know what to fill in.
- `plugins/` – Local copies of the AsciiDoc reader and bibliography helper used by `lgessler/`.
- `themes/academic/` – Theme used for rendering.
- `pelicanconf.py` – Pelican configuration customized for LAW XX.
- `requirements.txt` – Python dependencies (Pelican, ghp-import, AsciiDoc tooling, etc.).

The legacy LAW XIX static site still lives under `LAW-XIX-2025/` for reference.

## Local development

1. Create a virtualenv and install dependencies: `pip install -r requirements.txt`.
2. Build the site: `pelican content -s pelicanconf.py -o output`.
3. Preview locally with a simple server, e.g., `python -m http.server --directory output 8000`.

## Deployment

```bash
ghp-import output -b gh-pages
```

Then push the `gh-pages` branch to GitHub.
