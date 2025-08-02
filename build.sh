#!/bin/bash

# Exit on error
set -e

# Install system dependencies
apt-get update && apt-get install -y libsqlite3-dev

# Install Python dependencies
python3 -m pip install -r requirements.txt

# Set Django settings module
export DJANGO_SETTINGS_MODULE=reviewproject.settings_production

# Collect static files
python3 manage.py collectstatic --noinput

# Apply database migrations
python3 manage.py migrate