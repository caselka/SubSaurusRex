#!/bin/bash

echo "🔧 Setting up Sub Saurus Rex..."

echo "🐍 Creating a virtual environment..."
python3 -m venv venv

echo "📂 Activating the virtual environment..."
source venv/bin/activate

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "✅ Setup complete! Run the scanner using:"
echo "   source venv/bin/activate && python3 scanner.py example.com 20 1000 --web"
