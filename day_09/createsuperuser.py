#!/usr/bin/env python
import os

import django


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'day_09.settings')
    django.setup()

    from django.contrib.auth import get_user_model
    from chat.models import Chat
    user_cls = get_user_model()

    if user_cls.objects.filter(username='admin').exists():
        print('Пользователь "admin" уже существует')
    else:
        user_cls.objects.create_superuser(
            username='admin',
            email='admin@admin.com',
            password='admin',
            first_name='admin',
            last_name='adminov',
        )
        print('Пользователь "admin" создан')

    if user_cls.objects.filter(username='test').exists():
        print('Пользователь "test" уже существует')
    else:
        user_cls.objects.create_superuser(
            username='test',
            email='test@test.com',
            password='test',
            first_name='test',
            last_name='test',
        )
        print('Пользователь "test" создан')

    for i in range(3):
        Chat.objects.get_or_create(
            name=f'chatroom_{i}',
        )


if __name__ == '__main__':
    main()
