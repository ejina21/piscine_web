from django.db import models


class Planets(models.Model):
    name = models.CharField(unique=True, max_length=64)
    climate = models.CharField(max_length=255, null=True)
    diameter = models.IntegerField(null=True)
    orbital_period = models.IntegerField(null=True)
    population = models.BigIntegerField(null=True)
    rotation_period = models.IntegerField(null=True)
    surface_water = models.FloatField(null=True)
    terrain = models.CharField(max_length=128, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(unique=True, max_length=64)
    birth_year = models.CharField(max_length=32, null=True)
    gender = models.CharField(max_length=32, null=True)
    eye_color = models.CharField(max_length=32, null=True)
    hair_color = models.CharField(max_length=32, null=True)
    height = models.IntegerField(null=True)
    mass = models.FloatField(null=True)
    homeworld = models.ForeignKey(Planets, max_length=68, on_delete=models.DO_NOTHING, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Movies(models.Model):
    title = models.CharField(max_length=64, unique=True)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32)
    producer = models.CharField(max_length=128)
    release_date = models.DateField()
    characters = models.ManyToManyField(People, related_name='movies_people')

    def __str__(self):
        return self.title
