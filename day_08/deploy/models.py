from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=50)
    file = models.ImageField(upload_to='pictures')

    def __str__(self):
        return self.title