from django.db import models


class Planets(models.Model):
    name = models.CharField(unique=True, max_length=64)
    climate = models.CharField(max_length=255, null=True)
    diameter = models.PositiveIntegerField(null=True)
    orbital_period = models.PositiveIntegerField(null=True)
    population = models.BigIntegerField(null=True)
    rotation_period = models.PositiveIntegerField(null=True)
    surface_water = models.FloatField(null=True)
    terrain = models.CharField(max_length=128, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
