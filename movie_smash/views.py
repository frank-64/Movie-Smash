from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', context=None)

def practice(request):
    return render(request, 'practice.html', context=None)