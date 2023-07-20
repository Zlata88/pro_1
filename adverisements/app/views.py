from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1 style="text-align: center;background-color:green">Домашка по 4 занятию</h1>')


