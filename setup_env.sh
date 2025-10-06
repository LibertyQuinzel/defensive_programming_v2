#!/usr/bin/env bash
# Simple environment setup for beginners.

set -euo pipefail

if [ -d ".venv" ]; then
    echo "Virtualenv '.venv' already exists. Activate with: source .venv/bin/activate"
    exit 0
fi

python3 -m venv .venv
echo "Created virtualenv .venv"
echo "Activating and installing requirements..."
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
echo "Setup complete. Activate with: source .venv/bin/activate"
