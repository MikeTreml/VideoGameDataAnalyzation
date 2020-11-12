import requests
import json
from types import SimpleNamespace
here = 'outside'
# api request for whole json get. list wist dot notation.
def run_request():
    response = requests.get('https://api.dccresource.com/api/games')
    jsonobject = response.text
    global here
    here = json.loads(jsonobject, object_hook=lambda d: SimpleNamespace(**d))
    return here[1]
   # return json.loads(jsonobject, object_hook=lambda d: SimpleNamespace(**d))