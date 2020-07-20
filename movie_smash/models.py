from django.db import models

# Create your models here.
class Movies(models.Model):
    movieID = models.IntegerField(primary_key=True, unique=False)
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    popularity = models.FloatField()

    def __str__(self):
        return self.title


