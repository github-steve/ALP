#!/usr/bin/env python3
"""
Generate the paintings gallery page with FAA-style flexbox layout.
Reads existing paintings and outputs clean, paginated HTML.
"""
import os
import re
import json

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXISTING_PAGE = os.path.join(REPO_ROOT, "mandy-budan-paintings.html")
OUTPUT_DIR = os.path.join(REPO_ROOT, "html", "generated")
PAGINATION = 16  # images per page

def parse_existing_paintings():
    """Extract painting data from the existing gallery page."""
    with open(EXISTING_PAGE, 'r') as f:
        content = f.read()
    
    paintings = []
    
    # Find all artwork divs
    pattern = r'<div class="artwork" id="([^"]+)" itemscope[^>]*>.*?<div class="artwork-image"><a href="([^"]+)"><img[^>]*src="([^"]+)" alt="([^"]+)"[^>]*>.*?<div class="artwork-title"[^>]*>([^<]+)</div>.*?<span itemprop="dateCreated">([^<]+)</span>.*?<span itemprop="size">([^<]+)</span>.*?<span itemprop="artMedium">([^<]+)</span>(.*?)</div>\s*</div>'
    
    matches = re.findall(pattern, content, re.DOTALL)
    
    for match in matches:
        slug, link, img_src, alt, title, year, size, medium, extra = match
        
        # Check for sold badge
        sold = 'circle-container' in extra
        
        # Fix image path: images/slug.jpg -> /ALP/images/paintings/year/slug.jpg
        # Extract year from slug (first 4 chars)
        year_prefix = slug[:4]
        img_filename = os.path.basename(img_src)
        fixed_img_src = f"/ALP/images/paintings/{year_prefix}/{img_filename}"
        
        # Fix detail link: html/slug.html -> /ALP/html/paintings/year/slug.html
        fixed_link = f"/ALP/html/paintings/{year_prefix}/{slug}.html"
        
        paintings.append({
            'slug': slug,
            'link': fixed_link,
            'img_src': fixed_img_src,
            'alt': alt,
            'title': title.strip(),
            'year': year.strip(),
            'size': size.strip(),
            'medium': medium.strip(),
            'sold': sold
        })
    
    return paintings

def parse_year_breaks():
    """Extract year-break markers from existing page."""
    with open(EXISTING_PAGE, 'r') as f:
        content = f.read()
    
    years = []
    pattern = r'<div class="year-break[^"]*"><h2>(\d{4})'
    matches = re.findall(pattern, content)
    
    for year in matches:
        latest = 'latest-year' in content.split(f'year-break')[1].split('</div>')[0] if 'latest-year' in content else False
        years.append({'year': year, 'latest': latest})
    
    return years

def generate_page(paintings, page_num, total_pages, output_path):
    """Generate a single gallery page."""
    
    # Group paintings by year for year-break display
    years_order = sorted(set(p['year'] for p in paintings), reverse=True)
    paintings_by_year = {y: [] for y in years_order}
    for p in paintings:
        paintings_by_year[p['year']].append(p)
    
    # Build gallery HTML
    gallery_html = ""
    
    for year in years_order:
        year_paintings = paintings_by_year[year]
        if not year_paintings:
            continue
        
        is_latest = year == max(years_order)
        latest_class = " latest-year" if is_latest else ""
        latest_badge = ' <span class="latest-badge">Latest</span>' if is_latest else ""
        year_note = '<p class="year-note">My most recent work. More coming soon…</p>' if is_latest else ""
        
        gallery_html += f'    <div class="year-break{latest_class}"><h2>{year}{latest_badge}</h2>{year_note}</div>\n'
        
        for p in year_paintings:
            sold_badge = ""
            if p['sold']:
                sold_badge = '<div class="circle-container"><div class="circle-inner"></div><span class="tooltip">Sold</span></div>'
            
            gallery_html += f'''    <div class="artwork" id="{p['slug']}" itemscope itemtype="https://schema.org/VisualArtwork">
      <span itemprop="artist" itemscope itemtype="https://schema.org/Person"><meta itemprop="name" content="Mandy Budan"></span>
      <div class="artwork-image"><a href="{p['link']}"><img loading="lazy" itemprop="image" src="{p['img_src']}" alt="{p['alt']}"></a>{sold_badge}</div>
      <div class="artwork-info">
        <div class="artwork-title" itemprop="name">{p['title']}</div>
        <div class="artwork-meta">
          <span itemprop="dateCreated">{p['year']}</span>
          <span itemprop="size">{p['size']}</span>
          <span itemprop="artMedium">{p['medium']}</span>
        </div>
      </div>
    </div>
'''
    
    # Pagination HTML
    pagination_html = ""
    if total_pages > 1:
        pagination_html += '    <nav aria-label="Gallery pagination" class="mt-4"><ul class="pagination justify-content-center">\n'
        for i in range(1, total_pages + 1):
            active = " active" if i == page_num else ""
            page_file = f"mandy-budan-paintings-page{i}.html" if i > 1 else "mandy-budan-paintings.html"
            pagination_html += f'      <li class="page-item{active}"><a class="page-link" href="/ALP/{page_file}">{i}</a></li>\n'
        pagination_html += '    </ul></nav>\n'
    
    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="index, follow">
  <meta name="description" content="Browse original abstract landscape paintings by Mandy Budan. Acrylic on wood, created in Toronto.">
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

<!-- Scroll progress bar (position:fixed top gradient) -->
<div class="scroll-progress"></div>

<!-- Skip link for keyboard users -->
<a href="#main" class="skip-link">Skip to main content</a>

<!-- Bootstrap 5 Navbar -->
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

<!-- Spacer for fixed navbar -->
<div style="height: 4.5rem;"></div>

<main id="main">
  <div class="container py-4">

    <!-- Artist Statement -->
    <section class="artist-statement text-center mb-4">
      <h1>The Paintings</h1>
    </section>

    <!-- Pull Quote -->
    <div class="pull-quote mb-4">
      <p>"Normality is a paved road - it's comfortable to walk, but no flowers grow on it."<br>- Vincent Van Gogh</p>
    </div>

    <!-- Gallery -->
    <div class="gallery">
{gallery_html}    </div>

{pagination_html}  </div>
</main>

<!-- Footer -->
<footer class="text-center py-3 mt-4">
  All artwork and images copyright &copy; Mandy Budan 2025
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
<script data-goatcounter="https://budanart.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
<script src="/ALP/js/site-effects.min.js"></script>

<script>
(function(){{
  var loc=window.location;
  var path=loc.pathname.replace(/\\/[^\\/]*$/,"/");
  var base=loc.origin+path;
  var ogUrl=document.querySelector('meta[property="og:url"]');
  var ogImg=document.querySelector('meta[property="og:image"]');
  var canonical=document.querySelector('link[rel="canonical"]');
  if(ogUrl) ogUrl.setAttribute("content", loc.href);
  if(ogImg){{
    var p = ogImg.getAttribute("data-img") || "";
    if(p && p.indexOf("/")!==0) p = "/ALP/" + p;
    ogImg.setAttribute("content", loc.origin + p);
  }}
  if(canonical) canonical.setAttribute("href", loc.href);
}})();
</script>

</body>
</html>'''
    
    with open(output_path, 'w') as f:
        f.write(full_html)
    
    return len(full_html)

if __name__ == "__main__":
    print("Parsing existing paintings page...")
    paintings = parse_existing_paintings()
    print(f"Found {len(paintings)} paintings")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    total_pages = (len(paintings) + PAGINATION - 1) // PAGINATION
    
    for page_num in range(1, total_pages + 1):
        start = (page_num - 1) * PAGINATION
        end = start + PAGINATION
        page_paintings = paintings[start:end]
        
        if page_num == 1:
            filename = "mandy-budan-paintings.html"
        else:
            filename = f"mandy-budan-paintings-page{page_num}.html"
        
        output_path = os.path.join(REPO_ROOT, filename)
        size = generate_page(page_paintings, page_num, total_pages, output_path)
        print(f"Generated {filename} ({size} bytes) with {len(page_paintings)} paintings")
    
    print(f"\nTotal: {len(paintings)} paintings across {total_pages} pages")
