#!/bin/bash
# Quick setup script for students using the defensive programming course

echo "🚀 Setting up Defensive Programming Course Environment..."

# Check if Python 3.8+ is available
python_version=$(python3 --version 2>&1 | cut -d' ' -f2 | cut -d'.' -f1,2)
required_version="3.8"

if ! python3 -c "import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)"; then
    echo "❌ Error: Python 3.8+ is required. Found: $(python3 --version)"
    echo "Please install Python 3.8 or newer and try again."
    exit 1
fi

echo "✅ Python version check passed: $(python3 --version)"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
else
    echo "📦 Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
python -m pip install --upgrade pip

# Install requirements
echo "📚 Installing course dependencies..."
pip install -r requirements.txt

# Install the package in editable mode for easier imports
echo "🔗 Installing package in editable mode..."
pip install -e .

# Set PYTHONPATH for current session
export PYTHONPATH="$(pwd):$PYTHONPATH"

echo ""
echo "🎉 Setup complete! To get started:"
echo ""
echo "1. Activate the virtual environment:"
echo "   source .venv/bin/activate"
echo ""
echo "2. Set PYTHONPATH (for current session):"
echo "   export PYTHONPATH=\$(pwd):\$PYTHONPATH"
echo ""
echo "3. Run a quick test:"
echo "   python -m pytest defensive_programming_v2/topics/00-intro/test_template_for_students_00_intro.py -v"
echo ""
echo "4. Start with Topic 00:"
echo "   cd defensive_programming_v2/topics/00-intro"
echo "   python starter.py"
echo ""
echo "💡 Tip: Add 'export PYTHONPATH=\$(pwd):\$PYTHONPATH' to your shell profile"
echo "   to avoid setting it every time you open a new terminal."
echo ""
echo "📖 Read the README.md for detailed instructions and workflow."