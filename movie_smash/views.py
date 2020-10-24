import csv

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Movies
import random


def top100(request):
    return render(request, 'top100.html')

@csrf_exempt
def edit_rankings(request):
    if request.method == "POST":
        req_body = request.body.decode('UTF-8')
        ids = req_body.split(",")


    return HttpResponse(None)


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
    m1 = query_results[random.randint(1, 100)]
    m2 = query_results[random.randint(1, 100)]
    return render(request, 'index.html', {'m1': m1, 'm2': m2})
