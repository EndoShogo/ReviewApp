#!/bin/bash

# Exit on error
set -e

echo "Installing Python dependencies..."
python3 -m pip install -r requirements.txt

echo "Setting Django settings module..."
export DJANGO_SETTINGS_MODULE=reviewproject.settings_production

echo "Collecting static files..."
python3 manage.py collectstatic --noinput

echo "Applying database migrations..."
python3 manage.py migrate

echo "Build completed successfully!"
