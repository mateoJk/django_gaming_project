from django.urls import path
from . import views

urlpatterns = [
    path('', views.videogame_list, name='videogame_list'),
]
