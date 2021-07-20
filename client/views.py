from django.http import HttpRequest, HttpResponse
from .models import Game
from django.shortcuts import render
from django.core.paginator import Paginator
from chessdotcom import *


# Create your views here.
def index(request: HttpRequest):
    def get_paged_games(n: int):
        games = Game.objects.all().order_by('game_date','game_time')
        return Paginator(games, 20).page(n)

    page = 1
    if request.GET.get('page'):
        page = request.GET.get('page')

    context = {
        'games': get_paged_games(page),
    }
    return render(request, 'client/games/index.html', context)

def stats(request: HttpRequest):
    return render(request, 'client/games/stats.html')
