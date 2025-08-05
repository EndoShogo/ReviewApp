#!/bin/bash

# Exit on error
set -e

echo "Installing Python dependencies for Vercel..."
pip install -r requirements-vercel.txt

echo "Setting Django settings module..."
export DJANGO_SETTINGS_MODULE=reviewproject.settings_vercel

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying database migrations..."
python manage.py migrate

echo "Vercel build completed successfully!" 