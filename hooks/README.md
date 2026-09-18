# Git Hooks

The `hooks/` directory contains git hooks for the ALP site.

## Purpose

Automatically run minifiers on CSS and JS files before each commit, and update all HTML references to point to the minified versions.

## Hooks

- **pre-commit** — Runs `minify.sh`, then stages the minified files (`css/style.min.css`, `js/site-effects.min.js`) and all updated HTML references.

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
