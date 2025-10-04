"""
Vercel用のAPIエンドポイント
"""
from django.core.wsgi import get_wsgi_application
import os

# Django設定の読み込み
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reviewproject.settings_vercel')

application = get_wsgi_application()

def handler(request):
    """
    Vercel Function用のハンドラー
    """
    return application(request)
