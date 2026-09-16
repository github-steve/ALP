# Project loops

## Batch image reprocess

Re-optimize all existing ALP paintings for web gallery and detail pages. Processes zips of 15-20 images per batch until all 100+ are done.

**Trigger:** zip file of paintings received  
**Authority:** extract, resize, edit HTML/CSS, commit — never merge  
**Approval gate:** unknown filename (not in gallery) → pause and ask (may be new painting)  
**Stop:** no more zips to process

**Steps per image:**
1. Extract zip to workspace temp dir
2. Rename to canonical slug (e.g., `2024-waterloo-fall.jpg`)
3. Resize: 400px q82 progressive → `images/NAME.jpg` / 1400px q90 → `images/NAME_detail.jpg`
4. Gallery: sold badge (`circle-container`), `loading="lazy"`, `alt` text
5. Detail page: `<img>` with `_detail.jpg`, "Acrylic on wood", dimensions blank if unknown, prev/next links
6. SEO: verify title, meta description, Open Graph tags, Twitter card, canonical URL, JSON-LD structured data match existing page patterns
7. Sort gallery by year then alphabetically; update prev/next links accordingly
8. Verify Buy Me a Coffee link in footer
9. Append filename to batch manifest (`/Users/hermesagent/workspace/alp-reprocess-manifest.md`)
10. Commit each batch: `chore: web-optimize batch N (M images) [vX.Y.Z]`

**Verify (per batch):** all manifest images exist at correct sizes, prev/next links consistent, gallery sort correct, coffee link present, SEO tags present and correct, version bumped in commit
