#!/bin/bash
# Install git hooks for ALP
# Run this once after cloning: bash hooks/install.sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
HOOKS_DIR="$SCRIPT_DIR/../.git/hooks"

echo "Installing git hooks..."
mkdir -p "$HOOKS_DIR"
cp "$SCRIPT_DIR/pre-commit" "$HOOKS_DIR/pre-commit"
chmod +x "$HOOKS_DIR/pre-commit"
echo "Done! pre-commit hook installed."
