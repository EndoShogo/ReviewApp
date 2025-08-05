import os
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reviewproject.settings_vercel')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse

# Create WSGI application
application = get_wsgi_application()

def handler(request, context):
    """Vercel serverless function handler"""
    return application(request, context)

# For local development
if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv) 