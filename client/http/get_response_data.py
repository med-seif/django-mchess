import requests

def get_monthly_available_archives(username, year, month):
    result = requests.get('https://api.chess.com/pub/player/seiftn/games/2021/06')
    return result.json()

def get_monthly_archive(username, year, month):
    result = requests.get('https://api.chess.com/pub/player/seiftn/games/2021/06')
    return result.json()

def get_monthly_archive_by_url(url):
    result = requests.get(url)
    return result.json()
