from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
import requests
import json


# Create your views here.
def index(request: HttpRequest):
    response = HttpResponse()
    result = requests.get('https://api.chess.com/pub/player/seiftn/games/2021/06')
    result_json = result.json()

    return HttpResponse(result.json())
