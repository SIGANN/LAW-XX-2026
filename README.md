# LAW XX Website

This repository hosts the sources for the LAW-XX (20th Linguistic Annotation Workshop) website.

## Layout

- `content/` – `.adoc` sources for pages on the site
- `plugins/` – internal, used for parsing `.adoc` files
- `themes/` – styles and base HTML templates. References in `pelicanconf.py`. `themes/lawxx` is used for this year.
- `pelicanconf.py` – Pelican configuration.

## Local development

1. Create a virtualenv and install dependencies: `pip install -r requirements.txt`.
2. Build the site: `pelican content -s pelicanconf.py -o output` (or just `pelican`).
3. Preview locally with a simple server, e.g., `python -m http.server --directory output 8000`.

## Deployment

Any change to `main` will trigger an automatic update to the website.
(See `.github/`.)

This should not be necessary, but to manually update the `gh-pages` branch:

```bash
ghp-import output -b gh-pages
```

Then push the `gh-pages` branch to GitHub.
