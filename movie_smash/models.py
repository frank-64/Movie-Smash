from django.db import models
from django import forms
# Create your models here.
class Movies(models.Model):
    movieID = models.CharField(primary_key=True, unique=False, max_length=9)
    title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    elo = models.FloatField(default=1000)
    image_url = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.title

class MovieSmashed(models.Model):
    print()