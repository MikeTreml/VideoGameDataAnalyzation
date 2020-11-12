import requests
import json

def run_request():
    response = requests.get('https://api.dccresource.com/api/games')
    game = response.json()
    print(game)
