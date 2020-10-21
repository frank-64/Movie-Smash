from django.shortcuts import render
from .models import Movies
import random

def index(request):

    query_results = Movies.objects.all()
    m1 = query_results[random.randint(0, 500)]
    m2 = query_results[random.randint(0, 500)]
    return render(request, 'index.html', {'m1': m1, 'm2': m2})
