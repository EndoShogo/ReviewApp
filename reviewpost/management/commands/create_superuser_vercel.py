from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Create superuser for Vercel environment'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, default='admin', help='Username for superuser')
        parser.add_argument('--password', type=str, default='admin123', help='Password for superuser')
        parser.add_argument('--email', type=str, default='admin@example.com', help='Email for superuser')

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        email = options['email']

        # 既存のユーザーをチェック
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            user.is_staff = True
            user.is_superuser = True
            user.set_password(password)
            user.save()
            self.stdout.write(
                self.style.SUCCESS(f'ユーザー "{username}" をスーパーユーザーに更新しました')
            )
        else:
            # 新しいスーパーユーザーを作成
            user = User.objects.create_superuser(
                username=username,
                password=password,
                email=email
            )
            self.stdout.write(
                self.style.SUCCESS(f'スーパーユーザー "{username}" を作成しました')
            )

        self.stdout.write(f'ユーザー名: {username}')
        self.stdout.write(f'パスワード: {password}')
        self.stdout.write(f'メール: {email}')
