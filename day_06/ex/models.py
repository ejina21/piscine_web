from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

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


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reputation = models.IntegerField(default=0)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ProfileUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profileuser.save()