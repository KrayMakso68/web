from os import name

from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_index, name='news_home'),
    path('create', views.create, name='create'),
]