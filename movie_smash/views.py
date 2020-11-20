import csv
import math
import sqlite3

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Movies
import random

db_file = 'C:/Users/Frankie/PycharmProjects/Django-Website/db.sqlite3'

def top100(request):
    query_results = Movies.objects.all().order_by('-elo')
    return render(request, 'top100.html', {'qr':query_results})

def calculate_elo(r1, r2):
    # Implement elo algorithm for movies 1 and 2
    # r1, r2 = elo for 1 and 2 respectively
    # n1, n2 = New elo for 1 and 2 respectively
    # p1, p2 = Probability of winning
    # Constant k=30
    k = 100.0
    p1 = 1.0 / (1.0 + math.pow(10, (r2 - r1) / 400.0))
    p2 = 1.0 / (1.0 + math.pow(10, (r1 - r2) / 400.0))
    n1 = r1 + k * (1 - p1)
    n2 = r2 + k * (0 - p2)
    return (round(n1,1),round(n2,1))



@csrf_exempt
def edit_rankings(request):
    if request.method == "POST":
        req_body = request.body.decode('UTF-8')
        ids = req_body.split(",")
        try:
            movie1 = Movies.objects.get(pk=ids[0])
            movie2 = Movies.objects.get(pk=ids[1])
            elos = calculate_elo(movie1.elo, movie2.elo)
            movie1.elo = elos[0]
            movie2.elo = elos[1]
            movie1.save()
            movie2.save()
        except Movies.DoesNotExist:
            print("MovieID not found")
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
    r1 = random.randint(1, 100)
    r2 = random.randint(1, 100)
    while (r1 == r2):
        r1 = random.randint(1, 100)
        r2 = random.randint(1, 100)
    m1 = query_results[r1-1]
    m2 = query_results[r2-1]
    return render(request, 'index.html', {'m1': m1, 'm2': m2})
