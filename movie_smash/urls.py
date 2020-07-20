from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index URL'),
    #path('practice.html', views.practice, name='practice URL')
]