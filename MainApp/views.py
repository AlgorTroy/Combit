from django.shortcuts import render
from .models import Tile
# Create your views here.


def show_tile(request):
    tile = Tile.objects.all()
    return render(request, 'MainAppTemplates/index.html', {'tile': tile})
