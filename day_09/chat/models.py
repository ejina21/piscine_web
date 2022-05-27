from django.db import models


class Chat(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название комнаты')

    def __str__(self):
        return self.name