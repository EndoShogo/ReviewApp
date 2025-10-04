"""
WSGI config for reviewproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Vercel環境用の設定を強制的に設定
# カスタム環境変数がある場合はそれを使用、なければデフォルト設定を使用
custom_settings = os.environ.get('DJANGO_SETTINGS', 'reviewproject.settings_vercel')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', custom_settings)

application = get_wsgi_application()

# Vercel用のエイリアス
app = application
