#!/bin/bash

set -xe

# Install node modules
cd frontend
npm install
cd ..

# Create venv
python -m venv venv

# Enter venv
source venv/bin/activate

# Update pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Create requirements.txt
pip freeze > requirements.txt

# Start tmux session
tmux new-session -d -s dev 'npx tailwindcss -i ./static/styles.css -o ./static/tailwind.css --watch'
tmux split-window -h 'uvicorn main:app --reload'
tmux attach-session -t dev