#!/bin/bash
# ALP minify script — minifies CSS + JS and updates all HTML references
# Run from the repo root

echo "=== ALP Minify ==="

# Install tools if missing
if ! command -v csso &> /dev/null || ! command -v minify &> /dev/null; then
  echo "Installing minifiers..."
  npm install -g csso-cli minify
fi

# Minify CSS
echo "Minifying CSS..."
csso css/style.css --output css/style.min.css

# Minify JS
echo "Minifying JS..."
minify js/site-effects.js > js/site-effects.min.js

# Update all HTML references
echo "Updating HTML references..."
find . -name "*.html" -exec perl -pi -e 's/href="css\/style\.css"/href="css\/style.min.css"/g' {} +
find . -name "*.html" -exec perl -pi -e 's/href="..\/css\/style\.css"/href="..\/css\/style.min.css"/g' {} +
find . -name "*.html" -exec perl -pi -e 's/href="..\/..\/css\/style\.css"/href="..\/..\/css\/style.min.css"/g' {} +
find . -name "*.html" -exec perl -pi -e 's/src="js\/site-effects\.js"/src="js\/site-effects.min.js"/g' {} +
find . -name "*.html" -exec perl -pi -e 's/src="..\/js\/site-effects\.js"/src="..\/js\/site-effects.min.js"/g' {} +
find . -name "*.html" -exec perl -pi -e 's/src="..\/..\/js\/site-effects\.js"/src="..\/..\/js\/site-effects.min.js"/g' {} +

# Report
echo ""
echo "Done!"
echo "CSS: $(wc -c < css/style.min.css) bytes"
echo "JS:  $(wc -c < js/site-effects.min.js) bytes"
echo "HTML files updated: $(find . -name '*.html' | wc -l)"
