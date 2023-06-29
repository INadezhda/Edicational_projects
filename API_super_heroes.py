import json
import requests
from pprint import pprint


def get_link(link_url):

    params = {}
    # max_heroes=[]
    response = requests.get(link_url)
    dict = response.json()

    for i in dict:
        if i['name'] == 'Hulk' or i['name'] == 'Captain America' or i['name'] == 'Thanos':
            name_heroes = i['name']
            params[name_heroes] = i['powerstats']['intelligence']
    # print(params)
    # max_heroes.append(max(sorted(params.items(), key=lambda x:x[1])))
    max_heroes = max(sorted(params.items(), key=lambda x: x[1]))
    print(f'Самый умный супергерой: {max_heroes} \n')
    return max_heroes


link_url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
get_link(link_url)
