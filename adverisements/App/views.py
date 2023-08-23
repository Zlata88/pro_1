# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render
from .models import Adverisements


def index(request):
    advertisements = Adverisements.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')
