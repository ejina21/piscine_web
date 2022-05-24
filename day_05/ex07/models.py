from django.utils import timezone

from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=64, unique=True)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32)
    producer = models.CharField(max_length=128)
    release_date = models.DateField()
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField()

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.created:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Movies, self).save(force_insert, force_update, using, update_fields)