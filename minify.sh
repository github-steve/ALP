#!/bin/bash
# ALP minify script — minifies CSS + JS, updates HTML references, appends version
# Run from the repo root

echo "=== ALP Minify ==="

# Install tools if missing
if ! command -v csso &> /dev/null || ! command -v minify &> /dev/null; then
  echo "Installing minifiers..."
  npm install -g csso-cli minify
fi

# Extract version from index.html
VERSION=$(grep -o 'ALP Design v[0-9.]*' index.html | head -1 | sed 's/ALP Design v//')
if [ -z "$VERSION" ]; then
  VERSION="dev"
fi
echo "Version: $VERSION"

# Minify CSS
echo "Minifying CSS..."
csso css/style.css --output css/style.min.css

# Minify JS
echo "Minifying JS..."
minify js/site-effects.js > js/site-effects.min.js

# Update all HTML references (add version + minified names)
echo "Updating HTML references..."
V="v=$VERSION"

# CSS references
find . -name "*.html" -exec perl -pi -e "s/href=\"css\\/style(\\.min)?\\.css\"/href=\"css\\/style.min.css?$V\"/g" {} +
find . -name "*.html" -exec perl -pi -e "s/href=\"\\.\\.\\/css\\/style(\\.min)?\\.css\"/href=\"..\\/css\\/style.min.css?$V\"/g" {} +
find . -name "*.html" -exec perl -pi -e "s/href=\"\\.\\.\\/\\.\\.\\/css\\/style(\\.min)?\\.css\"/href=\"..\\/..\\/css\\/style.min.css?$V\"/g" {} +

# JS references
find . -name "*.html" -exec perl -pi -e "s/src=\"js\\/site-effects(\\.min)?\\.js\"/src=\"js\\/site-effects.min.js?$V\"/g" {} +
find . -name "*.html" -exec perl -pi -e "s/src=\"\\.\\.\\/js\\/site-effects(\\.min)?\\.js\"/src=\"..\\/js\\/site-effects.min.js?$V\"/g" {} +
find . -name "*.html" -exec perl -pi -e "s/src=\"\\.\\.\\/\\.\\.\\/js\\/site-effects(\\.min)?\\.js\"/src=\"..\\/..\\/js\\/site-effects.min.js?$V\"/g" {} +

# Report
echo ""
echo "Done!"
echo "CSS: $(wc -c < css/style.min.css) bytes"
echo "JS:  $(wc -c < js/site-effects.min.js) bytes"
echo "HTML files updated: $(find . -name '*.html' | wc -l)"
