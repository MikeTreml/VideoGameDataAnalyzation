import requests
import json


def run_request():
    response = requests.get('https://api.dccresource.com/api/games')
    games = response.json()
    return games

run_request()