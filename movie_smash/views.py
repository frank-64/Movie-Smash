import csv
from django.shortcuts import render
from .models import Movies


def index(request):
    # with open('movie_smash/movies.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for row in reader:
    #         m = Movies(movieID=row[1], title=row[2], release_date=row[0], popularity=0)
    #         m.save()
    query_results = Movies.objects.all()
    return render(request, 'index.html', {'query_results':query_results})