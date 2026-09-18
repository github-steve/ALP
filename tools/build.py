#!/usr/bin/env python3
"""
ALP Site Build Script
Reads shared templates and injects them into HTML pages.
Usage: python tools/build.py
"""
import os
import re
import glob

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(REPO_ROOT, "templates")

def load_template(name):
    path = os.path.join(TEMPLATES_DIR, name)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def replace_nav(html, nav_template):
    """Replace existing <nav>...</nav> with shared template."""
    pattern = r"<nav>.*?</nav>"
    replacement = nav_template.strip()
    result = re.sub(pattern, replacement, html, count=1, flags=re.DOTALL)
    return result

def add_bootstrap_assets(html):
    """Add Bootstrap CSS/JS to <head> if missing."""
    if "bootstrap" in html.lower():
        return html
    # Add before </head>
    bootstrap_css = '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">'
    bootstrap_js = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>'
    html = html.replace("</head>", f"    {bootstrap_css}\n</head>")
    html = html.replace("</body>", f"    {bootstrap_js}\n</body>")
    return html

def build():
    nav_template = load_template("nav-bootstrap.html")
    
    # Find all HTML files (excluding templates/ and tools/)
    patterns = [
        os.path.join(REPO_ROOT, "*.html"),
        os.path.join(REPO_ROOT, "html", "**", "*.html"),
    ]
    
    for pattern in patterns:
        for filepath in glob.glob(pattern, recursive=True):
            if "templates/" in filepath or "tools/" in filepath:
                continue
            
            with open(filepath, "r", encoding="utf-8") as f:
                original = f.read()
            
            modified = replace_nav(original, nav_template)
            modified = add_bootstrap_assets(modified)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(modified)
            
            relpath = os.path.relpath(filepath, REPO_ROOT)
            print(f"Updated {relpath}")

if __name__ == "__main__":
    build()
