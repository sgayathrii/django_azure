# food/views.py
from django.shortcuts import render, redirect

# Create your views here.



def index(request):
    return render(request, 'food/index.html', context=None)