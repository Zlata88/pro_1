from django.urls import path
from .views import index, base, new

urlpatterns = [
    path('', index),
    path('base', base),
    path('new', new)
]
