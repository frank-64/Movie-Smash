import csv
from django.shortcuts import render
from .models import Movies
import random

def index(request):
    # parse the movies.csv file into the database
    # with open('./movies.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for row in reader:
    #         m = Movies(movieID=row[1], title=row[2], release_year=row[0])
    #         m.save()
    #

    query_results = Movies.objects.all()
    m1 = query_results[random.randint(0, 500)]
    m2 = query_results[random.randint(0, 500)]
    return render(request, 'index.html', {'m1': m1, 'm2': m2})
