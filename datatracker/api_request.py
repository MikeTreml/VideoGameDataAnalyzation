from typing import Dict, Any, Union

import requests
import json
from types import SimpleNamespace

# api request for whole json get. list wist dot notation.

consoledict = {"2600": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "3DO": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "3DS": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "DC": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "DS": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "GB": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "GBA": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "GC": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "GEN": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "GG": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "N64": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "NES": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "NG": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "PC": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "PCFX": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "PS": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "PS2": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "PS3": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "PS4": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "PSP": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "PSV": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "SAT": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "SCD": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "SNES": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "TG16": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "Wii": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "WiiU": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "WS": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "X360": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "XB": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
               "XOne": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0}}

# def giving a range from 2013 to 2017
def request_default():
    response = requests.get('https://api.dccresource.com/api/games')
    jsonobject = response.text
    result = {}
    fulldata = json.loads(jsonobject, object_hook=lambda d: SimpleNamespace(**d))
    resultyear = list(filter(lambda x: str(x.year) == '2013' or
                                   str(x.year) == '2014' or
                                   str(x.year) == '2015' or
                                   str(x.year) == '2016' or
                                   str(x.year) == '2017', fulldata))
    for item in resultyear:
        consoledict[item.platform]["naSales"] += item.naSales
        consoledict[item.platform]["euSales"] += item.euSales
        consoledict[item.platform]["jpSales"] += item.jpSales
        consoledict[item.platform]["otherSales"] += item.otherSales
        consoledict[item.platform]["globalSales"] += item.globalSales
    for console, sales in consoledict.items():
        for key in sales:
            if sales["globalSales"] > 0:
                result[console] = sales

    return result

# select year from drop down
def request_games_year(year):
    response = requests.get('https://api.dccresource.com/api/games')
    jsonobject = response.text
    fulldata = json.loads(jsonobject, object_hook=lambda d: SimpleNamespace(**d))
    result = list(filter(lambda x: str(x.year) == year, fulldata))
    return result

# search function by string
def request_search_string(searchstring):
    response = requests.get('https://api.dccresource.com/api/games')
    jsonobject = response.text
    fulldata = json.loads(jsonobject, object_hook=lambda d: SimpleNamespace(**d))
    result = list(filter(lambda x: searchstring.lower() in x.name.lower(), fulldata))
    return result

# select year to lst the consoles that sold the number of games that year
def request_console_year(year):
    response = requests.get('https://api.dccresource.com/api/games')
    jsonobject = response.text
    fulldata = json.loads(jsonobject, object_hook=lambda d: SimpleNamespace(**d))
    resultyear = list(filter(lambda x: str(x.year) == year, fulldata))
    result = {}

    for item in resultyear:
        consoledict[item.platform]["naSales"] += item.naSales
        consoledict[item.platform]["euSales"] += item.euSales
        consoledict[item.platform]["jpSales"] += item.jpSales
        consoledict[item.platform]["otherSales"] += item.otherSales
        consoledict[item.platform]["globalSales"] += item.globalSales

    for console, sales in consoledict.items():
        for key in sales:
            if sales["globalSales"] > 0:
                result[console] = sales
    return result


def request_console_game(name):
    response = requests.get('https://api.dccresource.com/api/games')
    jsonobject = response.text
    fulldata = json.loads(jsonobject, object_hook=lambda d: SimpleNamespace(**d))
    resultyear = list(filter(lambda x: str(x.name) == name, fulldata))
    result = {}

    for item in resultyear:
        consoledict[item.platform]["naSales"] += item.naSales
        consoledict[item.platform]["euSales"] += item.euSales
        consoledict[item.platform]["jpSales"] += item.jpSales
        consoledict[item.platform]["otherSales"] += item.otherSales
        consoledict[item.platform]["globalSales"] += item.globalSales

    for console, sales in consoledict.items():
        for key in sales:
            if sales["globalSales"] > 0:
                result[console] = sales
    return result
