from django.db import models
from django.contrib.auth.models import User


class Upvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')
    tip = models.ForeignKey('Tip', on_delete=models.CASCADE, verbose_name='Статья')

    class Meta:
        unique_together = ('user', 'tip',)


class Downvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')
    tip = models.ForeignKey('Tip', on_delete=models.CASCADE, verbose_name='Статья')

    class Meta:
        unique_together = ('user', 'tip',)


class Tip(models.Model):
    content = models.TextField(verbose_name='Контент')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')
    date = models.DateField(auto_now_add=True)
    positive = models.IntegerField(default=0, verbose_name='Лайк')
    negative = models.IntegerField(default=0, verbose_name='Дизлайк')