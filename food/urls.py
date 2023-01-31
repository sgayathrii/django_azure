from django.urls import re_path as url
from django.urls import path
from food import views


urlpatterns = [
    path('', views.index, name='index'),
]