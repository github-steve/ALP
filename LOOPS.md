# Project loops

## Batch image reprocess

Re-optimize all existing ALP paintings for web gallery and detail pages. Processes zips of 15-20 images per batch until all 100+ are done.

**Trigger:** zip file of paintings received  
**Authority:** extract, resize, edit HTML/CSS, commit — never merge  
**Approval gate:** unknown filename (not in gallery) → pause and ask (may be new painting)
**Skip rule:** if a painting's source file isn't in the zip, skip it entirely — do not generate from the 400px gallery image  
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

## Batch studies reprocess

Re-optimize all existing ALP studies for web gallery and detail pages. Processes zips of studies per batch until all are done. Studies use numeric IDs (e.g., 2025-223), images in `images/studies2/`, with `_sm` suffix for gallery thumbnails.

**Trigger:** zip file of studies received
**Authority:** extract, resize, edit HTML/CSS, commit — never merge
**Approval gate:** unknown filename (not in gallery) → pause and ask (may be new study)
**Skip rule:** if a study's source file isn't in the zip, skip it entirely — do not generate from the gallery thumbnail
**Stop:** no more zips to process

**Study metadata (all studies):**
- All sold — every entry gets a `circle-container` sold badge
- All acrylic on wood
- Dimensions: 5 x 7 (landscape) or 7 x 5 (portrait) — determine from image orientation at resize time

**Steps per study:**
1. Extract zip to workspace temp dir
2. Rename to match gallery ID (e.g., `2025-223.jpg`)
3. Resize: 400px q82 → `images/studies2/NAME_sm.jpg` / 1400px q90 → `images/studies2/NAME.jpg`
4. Detect orientation — if width > height: dimensions are `5 x 7`; if height > width: `7 x 5`
5. Gallery: sold badge (`circle-container`), `loading="lazy"`, `alt` text, link to `html/studies2/NAME.html`, correct dimensions in meta
6. Detail page: `<img>` with full-resolution image (not `_sm`), prev/next links, Buy Me a Coffee footer, correct dimensions
7. Sort gallery by year (desc), then study number (desc)
8. Verify Buy Me a Coffee link in footer
9. Append study ID to studies manifest (`/Users/hermesagent/workspace/alp_warm/alp-studies-reprocess-manifest.md`)
10. Commit each batch: `chore: web-optimize studies batch N (M images) [vX.Y.Z]`

**Verify (per batch):** all manifest images exist at correct sizes, prev/next links consistent, gallery sort correct, coffee link present, sold badges on all entries, correct dimensions per orientation, version bumped in commit
