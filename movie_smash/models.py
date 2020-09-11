from django.db import models

# Create your models here.
class Movies(models.Model):
    movieID = models.CharField(primary_key=True, unique=False, max_length=100)
    title = models.CharField(max_length=200)
    release_date = models.IntegerField()
    popularity = models.FloatField()

    def __str__(self):
        return self.title


