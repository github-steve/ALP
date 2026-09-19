#!/usr/bin/env python3
"""
Build studies gallery using Bootstrap classes.
Usage: python tools/build_studies.py
"""
import os
import re
import subprocess

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT = os.path.join(REPO_ROOT, "mandy-budan-small-original-paintings.html")

def get_original_content():
    result = subprocess.run(
        ["git", "show", "HEAD~1:mandy-budan-small-original-paintings.html"],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        exit(1)
    return result.stdout

def parse_original(content):
    studies = []
    blocks = content.split('<div class="artwork"')[1:]

    for block in blocks:
        slug_match = re.search(r'id="([^"]+)"', block)
        if not slug_match:
            continue
        slug = slug_match.group(1)

        sold = 'circle-container' in block

        alt_match = re.search(r'alt="([^"]+)"', block)
        alt = alt_match.group(1) if alt_match else slug

        title_match = re.search(r'artwork-title[^"]*"[^>]*>([^<]+)</div>', block)
        title = title_match.group(1).strip() if title_match else slug

        year_match = re.search(r'dateCreated">([^<]+)</span>', block)
        size_match = re.search(r'"size">([^<]+)</span>', block)
        medium_match = re.search(r'artMedium">([^<]+)</span>', block)

        year = year_match.group(1).strip() if year_match else slug[:4]
        size = size_match.group(1).strip() if size_match else ""
        medium = medium_match.group(1).strip() if medium_match else ""

        year_dir = slug[:4]

        # Build image path - try _sm first, then fall back to regular
        img_base = f"images/studies/{year_dir}/{slug}"
        if os.path.exists(os.path.join(REPO_ROOT, f"{img_base}_sm.jpg")):
            img_src = f"/ALP/{img_base}_sm.jpg"
        else:
            img_src = f"/ALP/{img_base}.jpg"

        studies.append({
            'slug': slug,
            'alt': alt,
            'title': title,
            'year': year,
            'size': size,
            'medium': medium,
            'sold': sold,
            'img_src': img_src,
            'link': f"/ALP/html/studies/{year_dir}/{slug}.html"
        })

    return studies

def generate(studies):
    years = sorted(set(p['year'] for p in studies), reverse=True)
    by_year = {y: [] for y in years}
    for p in studies:
        by_year[p['year']].append(p)

    cards_html = ""

    for year in years:
        year_studies = by_year[year]
        if not year_studies:
            continue

        is_latest = year == max(years)
        latest_badge = ' <span class="badge text-bg-warning ms-2">Latest</span>' if is_latest else ""

        cards_html += f'''    <!-- {year} -->
    <div class="year-section mb-4">
      <h2>{year}{latest_badge}</h2>
      <div class="d-flex flex-wrap gap-3 pt-3">
'''

        for p in year_studies:
            sold_badge = ""
            if p['sold']:
                sold_badge = '<span class="sold-indicator"></span>'

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
  <meta name="description" content="Small original studies by Mandy Budan. Affordable acrylic works on wood.">
  <meta property="og:title" content="Studies - Mandy Budan">
  <meta property="og:description" content="Small original studies by Mandy Budan.">
  <meta property="og:image" content="/ALP/images/studies/2025/2025-223_sm.jpg">
  <meta property="og:type" content="website">
  <meta property="og:url" content="">
  <link rel="canonical" href="">
  <title>Studies - Mandy Budan</title>
  <link rel="icon" type="image/x-icon" href="/ALP/favicon.ico">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
  <link rel="stylesheet" href="/ALP/css/style.css">
</head>
<body>

<div class="scroll-progress"></div>
<a href="#main" class="skip-link">Skip to main content</a>

<nav class="navbar navbar-expand-md fixed-top alp-nav" data-bs-theme="dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="/ALP/index.html"><strong>MANDY BUDAN</strong> <span class="fw-normal d-none d-md-inline">Abstract Landscapes</span></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item"><a class="nav-link" href="/ALP/index.html">Home</a></li>
        <li class="nav-item"><a class="nav-link" href="/ALP/mandy-budan-paintings.html">Paintings</a></li>
        <li class="nav-item"><a class="nav-link active" aria-current="page" href="/ALP/mandy-budan-small-original-paintings.html">Studies</a></li>
        <li class="nav-item"><a class="nav-link" href="/ALP/mandy-budan-about.html">About</a></li>
        <li class="nav-item"><a class="nav-link" href="/ALP/mandy-budan-store.html">SHOP</a></li>
      </ul>
    </div>
  </div>
</nav>

<div style="height: 0.5rem;"></div>

<main id="main">
  <div class="container py-4">

    <section class="artist-statement text-center mb-4">
      <h1>The Studies</h1>
    </section>

    <div class="pull-quote mb-4">
      <p>"Feet, what do I need you for when I have wings to fly?"<br>- Frida Kahlo</p>
    </div>

{cards_html}  </div>
</main>

<footer class="text-center py-3 mt-4">
  All artwork and images copyright &copy; Mandy Budan 2025
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
<script data-goatcounter="https://budanart.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
<script src="/ALP/js/site-effects.min.js"></script>
<script src="/ALP/js/dark-mode.js"></script>

<button id="bgToggle" class="bg-toggle" aria-label="Toggle background color">☾</button>
<button id="scrollTopBtn" class="scroll-btn" aria-label="Scroll to top">↑</button>
<button id="scrollBottomBtn" class="scroll-btn" aria-label="Scroll to bottom">↓</button>

<script src="/ALP/js/scroll-buttons.js"></script>
<script src="/ALP/js/nav-scroll.js"></script>

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

    return len(studies)

if __name__ == "__main__":
    content = get_original_content()
    studies = parse_original(content)
    print(f"Parsed {len(studies)} studies")

    count = generate(studies)
    print(f"Generated mandy-budan-small-original-paintings.html with {count} studies")
