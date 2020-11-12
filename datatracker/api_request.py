import requests
import json
from types import SimpleNamespace
here = 'outside'
# api request for whole json get. list wist dot notation.
def run_request():
    response = requests.get('https://api.dccresource.com/api/games')
    jsonobject = response.text
    fulldata = json.loads(jsonobject, object_hook=lambda d: SimpleNamespace(**d))
    result = list(filter(lambda x: x.year == 1996, fulldata))
    return result
   # return json.loads(jsonobject, object_hook=lambda d: SimpleNamespace(**d))

def search_request(searchstring):
    response = requests.get('https://api.dccresource.com/api/games')
    jsonobject = response.text
    fulldata = json.loads(jsonobject, object_hook=lambda d: SimpleNamespace(**d))
    result = list(filter(lambda x: searchstring.lower() in x.name.lower(), fulldata))
    return result
    #for n in result:
        #print(n.name)
