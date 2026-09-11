# Warm-Inviting Style Revert — Implementation Plan (Updated)

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Revert the site to the warm-inviting style while keeping the fullscreen image hero from the modern design, and switching all fonts to Playfair Display.

**Branch:** `warm-inviting-hero` (from `warm-inviting`)

---

## Decisions (confirmed)

1. **Hero:** White text over fullscreen image with scrim. Text is "Abstract Landscapes" and will change occasionally — keep the same structure.
2. **Gallery:** Keep year-section groupings, but use the card-based grid (shadow, hover lift) from warm-inviting.
3. **Pages to update:** 5 main pages only (Landing, Paintings, Studies, About, Store). Skip detail pages for now.
4. **Fonts:** Playfair Display only (remove Source Sans 3, Space Grotesk, Inter).
5. **Colors:** Warm-inviting palette (cream bg, terracotta accents, light nav). Will change later.

---

## Task 1: Create branch from warm-inviting

```bash
git checkout warm-inviting
git checkout -b warm-inviting-hero
```

## Task 2: Replace hero in index.html

**Files:** Modify `index.html`

Replace the warm-inviting text hero with the fullscreen image hero from `main`:

```html
<section class="hero">
  <div class="hero-bg">
    <img src="images/2026-rhythm-and-hues-hero.jpg" alt="">
  </div>
  <div class="hero-content">
    <h1>Abstract Landscapes</h1>
    <p>Original paintings capturing the feeling of Canadian scenery - the light, the color, the quiet moments that stay with you.</p>
  </div>
</section>
```

CSS:
```css
.hero { min-height: 100vh; display: flex; align-items: flex-end; padding: 0 3rem 4rem; position: relative; }
.hero-bg { position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.9; }
.hero-bg img { width: 100%; height: 100%; object-fit: cover; }
.hero-content { position: relative; z-index: 2; max-width: 800px; background: rgba(0,0,0,0.5); padding: 2rem 2rem 0; border-radius: 8px; }
.hero h1 { font-family: 'Playfair Display', serif; font-size: 5rem; font-weight: 400; color: #fff; line-height: 1; margin-bottom: 1.5rem; letter-spacing: -0.02em; }
.hero p { color: rgba(255,255,255,0.9); font-size: 1.1rem; max-width: 500px; line-height: 1.8; }
```

## Task 3: Switch all fonts to Playfair Display

**Files:** Modify all 5 main pages + css/styles.css + css/studies.css

**Google Fonts** — replace with:
```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

**Font-family replacements:**
- `Source Sans 3`, `-apple-system, sans-serif` → `Playfair Display', serif`
- `Space Grotesk', sans-serif` → `Playfair Display', serif`
- `Inter', sans-serif` → `Playfair Display', serif`

**Body font-weight:** Adjust to 400 (Playfair Display is heavier than Source Sans 3 at 300).

## Task 4: Apply warm color palette

**Files:** Modify all 5 main pages

**body:**
- background: `#fdf8f3` (cream)
- color: `#2c2c2c`

**nav:**
- background: `#fff`
- box-shadow: `0 1px 0 rgba(0,0,0,0.05)`

**brand:**
- color: `#4a3f35`

**nav-links a:**
- color: `#4a3f35`

**nav-links a:hover / .active:**
- color: `#c88d3d` (terracotta)

**headings:**
- color: `#4a3f35`

**body text:**
- color: `#5a5048`

**muted/meta text:**
- color: `#7a6e62` or `#a09080`

**accent/links:**
- color: `#c88d3d`

**sold badge:**
- background: `#c67a2a`
- color: `#fff`

## Task 5: Card-based gallery grid with year sections

**Files:** Modify `paintings.html`, `mandy-budan-small-original-paintings.html`

**CSS:**
```css
.featured-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1.5rem;
}
.featured-item {
  background: #fff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0,0,0,0.06);
  transition: transform 0.2s, box-shadow 0.2s;
}
.featured-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.1);
}
.featured-item img { width: 100%; height: auto; display: block; }
.featured-info { padding: 0.75rem; }
.featured-title { font-family: 'Playfair Display', serif; font-size: 0.95rem; font-weight: 500; color: #4a3f35; }
.featured-meta { font-size: 0.72rem; color: #a09080; margin-top: 0.15rem; }
```

**HTML structure (per year section):**
```html
<div class="year-section">
  <div class="year-header">
    <h2>2026</h2>
  </div>
  <div class="featured-grid">
    <div class="featured-item">
      <a href="..."><img src="..." alt="..."></a>
      <div class="featured-info">
        <div class="featured-title">Rhythm and Hues</div>
        <div class="featured-meta">2026 - 18 x 24</div>
      </div>
    </div>
    ...
  </div>
</div>
```

## Task 6: WCAG fixes

**Files:** Modify all 5 main pages

- Add `<a href="#main" class="skip-link">Skip to main content</a>` after `<body>`
- Wrap content in `<main id="main">`
- Add `aria-current="page"` to active nav link
- Add focus-visible style:
  ```css
  a:focus-visible, button:focus-visible, [tabindex]:focus-visible {
    outline: 2px solid #c88d3d;
    outline-offset: 2px;
  }
  ```

## Task 7: Bump version and push

**Version:** v2.4.1 → v2.7.0 (new theme merge)

```bash
git add -A
git commit -m "Merge warm-inviting style with modern hero; Playfair Display fonts; card grid; v2.7.0"
git push origin warm-inviting-hero
git checkout main
git merge warm-inviting-hero
git push origin main
```

---

## Files to Change

- `index.html` — hero + fonts + colors + WCAG
- `paintings.html` — grid + fonts + colors + WCAG
- `mandy-budan-small-original-paintings.html` — grid + fonts + colors + WCAG
- `mandy-budan-about.html` — fonts + colors + WCAG
- `mandy-budan-store.html` — fonts + colors + WCAG
- `css/styles.css` — fonts + colors
- `css/studies.css` — fonts + colors

## Verification

1. Hero shows fullscreen image with white text + scrim
2. Nav is light/cream
3. All text is Playfair Display
4. Gallery has year sections with card grid
5. Background is cream (#fdf8f3)
6. Accents are terracotta (#c88d3d)
7. Skip link + aria-current + focus rings present
