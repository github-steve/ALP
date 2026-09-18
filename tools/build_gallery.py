#!/usr/bin/env python3
"""
Build paintings gallery using Bootstrap classes.
Parses original gallery page and generates clean Bootstrap markup.
Usage: python tools/build_gallery.py
"""
import os
import re
import subprocess

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT = os.path.join(REPO_ROOT, "mandy-budan-paintings.html")

def get_original_content():
    """Get the original 1365-line gallery page from git history."""
    result = subprocess.run(
        ["git", "show", "HEAD~3:mandy-budan-paintings.html"],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        exit(1)
    return result.stdout

def parse_original(content):
    """Extract painting data from the original gallery page."""
    paintings = []
    
    # Split by artwork divs
    blocks = content.split('<div class="artwork"')[1:]  # Skip first empty/header split
    
    for block in blocks:
        # Extract slug
        slug_match = re.search(r'id="([^"]+)"', block)
        if not slug_match:
            continue
        slug = slug_match.group(1)
        
        # Check if sold (circle-container present)
        sold = 'circle-container' in block
        
        # Extract alt
        alt_match = re.search(r'alt="([^"]+)"', block)
        alt = alt_match.group(1) if alt_match else slug
        
        # Extract title
        title_match = re.search(r'artwork-title[^"]*"[^>]*>([^<]+)</div>', block)
        title = title_match.group(1).strip() if title_match else slug
        
        # Extract year, size, medium
        year_match = re.search(r'dateCreated">([^<]+)</span>', block)
        size_match = re.search(r'"size">([^<]+)</span>', block)
        medium_match = re.search(r'artMedium">([^<]+)</span>', block)
        
        year = year_match.group(1).strip() if year_match else slug[:4]
        size = size_match.group(1).strip() if size_match else ""
        medium = medium_match.group(1).strip() if medium_match else ""
        
        year_dir = slug[:4]
        
        paintings.append({
            'slug': slug,
            'alt': alt,
            'title': title,
            'year': year,
            'size': size,
            'medium': medium,
            'sold': sold,
            'img_src': f"/ALP/images/paintings/{year_dir}/{slug}.jpg",
            'link': f"/ALP/html/paintings/{year_dir}/{slug}.html"
        })
    
    return paintings

def generate_gallery(paintings):
    """Generate Bootstrap gallery HTML."""
    
    # Group by year (newest first)
    years = sorted(set(p['year'] for p in paintings), reverse=True)
    by_year = {y: [] for y in years}
    for p in paintings:
        by_year[p['year']].append(p)
    
    # Build gallery cards HTML
    cards_html = ""
    
    for year in years:
        year_paintings = by_year[year]
        if not year_paintings:
            continue
        
        is_latest = year == max(years)
        latest_badge = ' <span class="badge text-bg-warning ms-2">Latest</span>' if is_latest else ""
        
        cards_html += f'''    <!-- {year} -->
    <div class="year-section mb-4">
      <h2 class="border-bottom pb-2 mb-3">{year}{latest_badge}</h2>
      <div class="d-flex flex-wrap gap-3">
'''
        
        for p in year_paintings:
            sold_badge = ""
            if p['sold']:
                sold_badge = '<span class="position-absolute top-0 end-0 badge text-bg-danger m-2">SOLD</span>'
            
            cards_html += f'''        <div class="card artwork-card">
          <div class="position-relative">
            <a href="{p['link']}">
              <img src="{p['img_src']}" class="card-img-top" alt="{p['alt']}" loading="lazy">
            </a>
            {sold_badge}
          </div>
          <div class="card-body">
            <h3 class="card-title h6 mb-1">{p['title']}</h3>
            <p class="card-text text-body-secondary small">
              {p['year']} &middot; {p['size']} &middot; {p['medium']}
            </p>
          </div>
        </div>
'''
        
        cards_html += "      </div>\n    </div>\n\n"
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="index, follow">
  <meta name="description" content="Browse 100+ original abstract landscape paintings by Mandy Budan. Each work is acrylic on wood, created in Toronto.">
  <meta property="og:title" content="Paintings - Mandy Budan Art">
  <meta property="og:description" content="Browse original abstract landscape paintings by Mandy Budan.">
  <meta property="og:image" content="/ALP/images/paintings/2026/2026-rhythm-and-hues.jpg">
  <meta property="og:type" content="website">
  <meta property="og:url" content="">
  <link rel="canonical" href="">
  <title>Paintings - Mandy Budan Art</title>
  <link rel="icon" type="image/x-icon" href="/ALP/favicon.ico">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
  <link rel="stylesheet" href="/ALP/css/style.css">
</head>
<body>

<div class="scroll-progress"></div>
<a href="#main" class="skip-link">Skip to main content</a>

<nav class="navbar navbar-expand-lg fixed-top alp-nav" data-bs-theme="dark">
  <div class="container-fluid px-3">
    <a class="navbar-brand" href="/ALP/index.html"><strong>MANDY BUDAN</strong> <span class="fw-normal">Abstract Landscapes</span></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item"><a class="nav-link" href="/ALP/index.html">Home</a></li>
        <li class="nav-item"><a class="nav-link active" aria-current="page" href="/ALP/mandy-budan-paintings.html">Paintings</a></li>
        <li class="nav-item"><a class="nav-link" href="/ALP/mandy-budan-small-original-paintings.html">Studies</a></li>
        <li class="nav-item"><a class="nav-link" href="/ALP/mandy-budan-about.html">About</a></li>
        <li class="nav-item"><a class="nav-link" href="/ALP/mandy-budan-store.html">SHOP</a></li>
      </ul>
    </div>
  </div>
</nav>

<div style="height: 4.5rem;"></div>

<main id="main">
  <div class="container py-4">

    <section class="artist-statement text-center mb-4">
      <h1>The Paintings</h1>
    </section>

    <div class="pull-quote mb-4">
      <p>"Normality is a paved road - it's comfortable to walk, but no flowers grow on it."<br>- Vincent Van Gogh</p>
    </div>

{cards_html}  </div>
</main>

<footer class="text-center py-3 mt-4">
  All artwork and images copyright &copy; Mandy Budan 2025
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
<script data-goatcounter="https://budanart.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
<script src="/ALP/js/site-effects.min.js"></script>

<script>
(function(){{
  var loc=window.location;
  var ogUrl=document.querySelector('meta[property="og:url"]');
  var canonical=document.querySelector('link[rel="canonical"]');
  if(ogUrl) ogUrl.setAttribute("content", loc.href);
  if(canonical) canonical.setAttribute("href", loc.href);
}})();
</script>

</body>
</html>'''
    
    with open(OUTPUT, 'w') as f:
        f.write(html)
    
    return len(paintings)

if __name__ == "__main__":
    content = get_original_content()
    paintings = parse_original(content)
    print(f"Parsed {len(paintings)} paintings")
    
    count = generate_gallery(paintings)
    print(f"Generated mandy-budan-paintings.html with {count} paintings")
