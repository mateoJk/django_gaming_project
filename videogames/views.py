from django.shortcuts import render
from .models import Videogame


def videogame_list(request):
    videogames = Videogame.objects.all()
    return render(request, 'videogames/list.html', {'videogames': videogames})
