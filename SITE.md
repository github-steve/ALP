# Abstract Landscape Paintings (ALP)

**Owner:** Steve Budan  
**Artist:** Mandy Budan  
**Live URL:** https://www.abstractlandscapepainting.com/  
**GitHub:** https://github.com/github-steve/ALP

## What It Is

A static website showcasing the abstract landscape paintings and studies of Mandy Budan, a Canadian artist. Built as a portfolio/gallery with individual detail pages for each work.

## Site Structure

```
├── index.html              # Landing / hero / "What's on my easel"
├── paintings.html          # Gallery of all paintings (105 paintings)
├── mandy-budan-small-original-paintings.html  # Studies gallery (222 studies)
├── mandy-budan-about.html  # Artist bio, awards, exhibitions
├── mandy-budan-store.html  # Links to Etsy shop
├── html/                   # Individual detail pages
│   ├── 2006-*.html … 2026-*.html   # Painting detail pages
│   └── studies2/
│       └── 2012-*.html … 2025-*.html  # Study detail pages
├── css/
│   ├── style.css           # Source stylesheet
│   └── style.min.css       # Minified (auto-generated)
├── js/
│   ├── site-effects.js     # Source JS (scroll progress, animations)
│   └── site-effects.min.js # Minified (auto-generated)
├── fonts/
│   └── inter/              # Inter WOFF2 (Regular, Medium, Bold)
└── images/
    ├── studies2/           # Study images (gallery + detail)
    └── [painting images]   # Painting images
```

## Key Facts

| | |
|---|---|
| **Paintings** | 105 |
| **Studies** | 222 |
| **Detail pages** | 327 |
| **Fonts** | Inter WOFF2, self-hosted (no CDN) |
| **Analytics** | GoatCounter (`budanart.goatcounter.com`) |
| **No Bootstrap** | Bare CSS, no framework |

## Build & Deploy

### Dependencies
- Node.js (for minifiers)
- `npm install -g csso-cli minify`

### Minification
```bash
bash minify.sh
```
Runs `csso` (CSS) + `minifier` (JS), updates all HTML references to minified versions, and appends a version query string for cache busting.

### Git Hook (automatic)
Pre-commit hook runs `minify.sh` automatically on every commit. Install once with:
```bash
bash hooks/install.sh
```

### Cache Busting
`minify.sh` reads the version from `index.html` and appends `?v=X.XX.X` to all CSS/JS references. Bump the version in `index.html` to force browsers to fetch fresh files.

## Deployment

| Environment | Platform | URL |
|-------------|----------|-----|
| Development | GitHub Pages | `github-steve.github.io/ALP/` |
| Production | inMotion shared hosting | `www.abstractlandscapepainting.com/` |

### Deploy to inMotion
1. Zip the repo (exclude `.git/`, `node_modules/`, `.vscode/`, `batch_watermark_visible.py`)
2. Upload to `public_html/` via cPanel or FTP
3. Files are static — no server-side processing needed

## Batch Image Processing

See [LOOPS.md](LOOPS.md) for the detailed workflow for processing new painting/study batches.

Summary:
- **Paintings:** Extract zip → resize (400px gallery / 1400px detail) → watermark → commit
- **Studies:** Extract zip → resize (400px `_sm` / 694px detail) → watermark → commit
- Watermark script: `batch_watermark_visible.py` (© Mandy Budan, 40% opacity)

## Maintenance

- **Bump version** in `index.html` (e.g., `<!-- ALP Design v2.7.121 -->`) when making visual changes
- **Watermark new images** with `batch_watermark_visible.py` before adding
- **New paintings/studies**: follow the existing naming convention (`YYYY-slug.html`)
- **GoatCounter**: included on every page via `<script data-goatcounter="...">`



## Planned / TODO

- [ ] Convert to Bootstrap (user noted as planned)
- [ ] Migrate fully to inMotion hosting under new domain

## Notes

- No server-side code — pure static HTML/CSS/JS
- All artwork images © Mandy Budan 2005–2026
- No Google Analytics — privacy-conscious (GoatCounter only)
