#!/usr/bin/env python
import os

import django


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'day_07.settings')
    django.setup()

    from django.contrib.auth import get_user_model
    from blog.models import Article, UserFavouriteArticle
    user_cls = get_user_model()
    import random

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

    for i in range(5):
        Article.objects.get_or_create(
            title=f'title_{i}',
            author=random.choice(user_cls.objects.all()),
            synopsis=f'synopsis_{i}',
            content='lorem ipsum',
        )

    UserFavouriteArticle.objects.get_or_create(user=user_cls.objects.get(username='admin'), article=random.choice(Article.objects.all()))
    UserFavouriteArticle.objects.get_or_create(user=user_cls.objects.get(username='admin'), article=random.choice(Article.objects.all()))


if __name__ == '__main__':
    main()
