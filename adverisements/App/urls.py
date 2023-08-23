# from django.urls import path
# from .views import index, base, new
#
# urlpatterns = [
#     path('', index),
#     path('base', base),
#     path('new', new)
# ]
from django.urls import path
from .views import index, top_sellers

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
]
