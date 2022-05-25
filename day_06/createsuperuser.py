#!/usr/bin/env python
import os
import logging

import django


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'day_06.settings')
    django.setup()

    from django.contrib.auth import get_user_model

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


if __name__ == '__main__':
    main()
