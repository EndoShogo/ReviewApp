#!/bin/bash

set -e

# Install system dependencies
apt-get update && apt-get install -y libsqlite3-dev

# Install Python dependencies
python3 -m pip install -r requirements.txt

# Set Django settings module
export DJANGO_SETTINGS_MODULE=reviewproject.settings_production

# Run Django management commands
python3 manage.py collectstatic --noinput
# python manage.py migrate