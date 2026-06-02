# SNUCSE CTA Lab Website

This repository contains the Jekyll source for the Computer Theory and Applications Lab website at Seoul National University.

## Structure

- `_pages/`: top-level site pages and publication fragments
- `_news/`: news entries
- `_areas/`: research area pages
- `_kpark/`: professor profile page
- `_layouts/`, `_includes/`, `_sass/`, `_js/`: Jekyll theme templates and source assets
- `assets/`: generated or static CSS, JavaScript, images, and icons served by the site
- `script/`: helper scripts for local build, preview, and publication conversion

Generated build output is written to `_site/` and is intentionally not tracked.

## Local Preview

Install Ruby gems once:

```sh
bundle install
```

Build the site:

```sh
bundle exec jekyll build
```

Serve the site locally before pushing:

```sh
script/server
```

Then open `http://127.0.0.1:4000/` or `http://localhost:4000/`.

The repository also has the original Gulp workflow:

```sh
npm install
npm start
```

For ordinary content updates, `script/server` or `bundle exec jekyll serve` is the simpler path.
