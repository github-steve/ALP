# Git Hooks

The `hooks/` directory contains git hooks for the ALP site.

## Purpose

Automatically run minifiers on CSS and JS files before each commit, update all HTML references to point to the minified versions, and append a version query string to bust browser cache.

## Hooks

- **pre-commit** — Runs `minify.sh`, then stages the minified files (`css/style.min.css`, `js/site-effects.min.js`) and all updated HTML references.

## Cache Busting

The minifier reads the version from `index.html` (e.g., `v2.7.112`) and appends it as a query string to all CSS/JS references:

```html
<link rel="stylesheet" href="css/style.min.css?v=2.7.112">
<script src="js/site-effects.min.js?v=2.7.112"></script>
```

When you bump the version in `index.html`, the query string changes, forcing browsers to fetch the new file instead of using a cached copy.

## Installation

Run once after cloning the repo:

```bash
bash hooks/install.sh
```

This copies the hooks into `.git/hooks/` and makes them executable.

## Manual Minification

To minify without committing:

```bash
bash minify.sh
```

## Requirements

- `csso-cli` (CSS minifier)
- `minify` (JS minifier)

Install with: `npm install -g csso-cli minify`
The minifier script installs them automatically if missing.
