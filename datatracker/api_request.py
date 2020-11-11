import requests
from . import videogame

def run_request():
    response = requests.get('https://api.dccresource.com/api/games')
    game = videogame.video_game_decoder(response)
    print(game.name)
