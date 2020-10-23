import csv
from django.shortcuts import render
from .models import Movies
import random

def index(request):
    # Parsing movies from CSV
    # with open('./movies.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for row in reader:
    #         m = Movies(movieID=row[1], title=row[2], release_date=row[0], popularity=0)
    #         m.save()
    # return render(request, 'index.html')

    # Display movies on the index page
    query_results = Movies.objects.all()
    m1 = query_results[random.randint(0, 100)]
    m2 = query_results[random.randint(0, 100)]
    return render(request, 'index.html', {'m1': m1, 'm2': m2})
