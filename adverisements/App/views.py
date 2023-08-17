# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    n = ['Oleg', 'Olga', 'Ivan', 'Ron']
    return render(request, 'new.html', context={'names': n})


def new(request):
    return render(request, 'new.html', context=None)


def base(request):
    return render(request, 'base.html', context=None)
