from typing import Dict, Any, Union
import requests
import json
from types import SimpleNamespace

# one api request on page load
from fuzzywuzzy.fuzz import partial_token_sort_ratio

api_request = requests.get('https://api.dccresource.com/api/games')


# def giving a range from 2013 to 2017
def request_default():
    response = api_request
    jsonobject = response.text
    fulldata = json.loads(jsonobject, object_hook=lambda d: SimpleNamespace(**d))
    resultyear = list(filter(lambda x: str(x.year) == '2013' or
                                   str(x.year) == '2014' or
                                   str(x.year) == '2015' or
                                   str(x.year) == '2016' or
                                   str(x.year) == '2017', fulldata))

    return process_filter(resultyear)

# select year from drop down
def request_games_year(year):
    response = api_request
    jsonobject = response.text
    fulldata = json.loads(jsonobject, object_hook=lambda d: SimpleNamespace(**d))
    result = list(filter(lambda x: str(x.year) == str(year), fulldata))

    return result

# search function by string
def request_search_string(searchstring):
    response = api_request
    jsonobject = response.text
    top = 0
    result = []
    fulldata = json.loads(jsonobject, object_hook=lambda d: SimpleNamespace(**d))
    #result = list(filter(lambda x: searchstring.lower() in x.name.lower(), fulldata))  #****old search ******
    for x in fulldata:
        save = partial_token_sort_ratio(searchstring.lower(), x.name.lower() + " " + x.platform.lower() + " " +
                                        str(x.year) + " " + str(x.rank) + " " + x.genre.lower() + " " +
                                        x.publisher.lower(), force_ascii=True, full_process=True)
        if save >= 70:
            if save >= top:
                result.insert(1, x)
                top = save
            else:
                result.append(x)
    return result

# select year to lst the consoles that sold the number of games that year
def request_console_year(year):
    response = api_request
    jsonobject = response.text
    fulldata = json.loads(jsonobject, object_hook=lambda d: SimpleNamespace(**d))
    resultyear = list(filter(lambda x: str(x.year) == year, fulldata))

    return process_filter(resultyear)

# for one title shows the number of copies sold per console
def request_console_game(name):
    response = api_request
    jsonobject = response.text
    fulldata = json.loads(jsonobject, object_hook=lambda d: SimpleNamespace(**d))
    resultyear = list(filter(lambda x: str(x.name) == name, fulldata))

    return process_filter(resultyear)

# displays each years top selling console
def top_console():
    year = 1980
    response = api_request
    jsonobject = response.text
    fulldata = json.loads(jsonobject, object_hook=lambda d: SimpleNamespace(**d))
    results = []
    c = 0
    while c < 37:
        resultyear = list(filter(lambda x: x.year == (year + c), fulldata))
        save = 0
        resulttemp = []
        filtered = process_filter(resultyear)
        for i in filtered:
            if i[5] > save:
                resulttemp = i
                resulttemp[0] = i[0] + " (" + str(year + c) +")"
                save = i[5]
                print(save)
        results.append(resulttemp)
        c += 1
    return(results)

def process_filter(dict):
    results = []
    console_dict = {"2600": {"naSales": 0, "euSales": 0, "jpSales": 0, "otherSales": 0, "globalSales": 0},
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
    for item in dict:
        console_dict[item.platform]["naSales"] += round(item.naSales, 2)
        console_dict[item.platform]["euSales"] += round(item.euSales, 2)
        console_dict[item.platform]["jpSales"] += round(item.jpSales, 2)
        console_dict[item.platform]["otherSales"] += round(item.otherSales, 2)
        console_dict[item.platform]["globalSales"] += round(item.globalSales, 2)

    for console, sales in console_dict.items():
            if sales["globalSales"] > 0:
                result = [console, round(sales["naSales"], 2), round(sales["euSales"], 2), round(sales["jpSales"], 2), round(sales["otherSales"], 2), round(sales["globalSales"], 2)]
                results.append(result)

    return(results)