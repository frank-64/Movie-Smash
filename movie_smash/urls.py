from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index URL'),
    path('', views.top100, name='top 100 table')
]