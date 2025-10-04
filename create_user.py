#!/usr/bin/env python
"""
Vercel環境でユーザーを作成するスクリプト
"""
import os
import sys
import django

# Django設定を読み込み
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reviewproject.settings_vercel')
django.setup()

from django.contrib.auth.models import User

def create_user():
    # ユーザーを作成
    username = 'testuser'
    password = 'testpass123'
    email = 'test@example.com'
    
    # 既存のユーザーをチェック
    if User.objects.filter(username=username).exists():
        print(f'ユーザー {username} は既に存在します')
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        print(f'パスワードを更新しました')
    else:
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        print(f'ユーザー {username} を作成しました')
    
    print(f'ユーザー名: {username}')
    print(f'パスワード: {password}')

if __name__ == '__main__':
    create_user()
