import os
from pathlib import Path
from .settings import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
# 一時的にデバッグを有効にしてエラーを調査
DEBUG = False  # 本番環境ではFalseに設定

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'i*6jbl9g%ccgn#ufkec^@iy_kunipc8p$*6oq=hbys5se2#k(o')

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.vercel.app',
    '.now.sh',
    '.onrender.com',
    '*'
]

import dj_database_url

# Database for Vercel Postgres
# Vercelの環境変数 `POSTGRES_URL` を優先的に読み込む
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('POSTGRES_URL', 'sqlite:///db.sqlite3'), 
        conn_max_age=600, 
        ssl_require=False,
        conn_health_checks=True,
    )
}

# Vercel Postgresの設定
if 'POSTGRES_URL' in os.environ:
    DATABASES['default']['DISABLE_SERVER_SIDE_CURSORS'] = True
    DATABASES['default']['OPTIONS'] = {
        'sslmode': 'require',
        'connect_timeout': 30,
    }
else:
    # SQLiteの場合は設定を調整
    DATABASES['default']['OPTIONS'] = {
        'timeout': 30,
    }

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media_image/'

# Security settings for Vercel
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False  # Vercel handles SSL

# Session settings for Vercel
SESSION_COOKIE_SECURE = False  # Vercel環境ではFalseに設定
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 86400  # 24時間
SESSION_SAVE_EVERY_REQUEST = True

# CSRF settings
CSRF_COOKIE_SECURE = False  # Vercel環境ではFalseに設定
CSRF_COOKIE_HTTPONLY = True

# Static files handling
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Django 4.2 compatibility
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ログ設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'reviewpost': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
    },
}

# Vercel Redis for Caching
if 'REDIS_URL' in os.environ:
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": os.environ.get('REDIS_URL'),
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        }
    } 