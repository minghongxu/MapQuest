# Minghong Xu 81491461

import urllib.parse
import urllib.request
import json

Consumer_Key = 'mllR3ja1ZWWKPkgXZdCAsuOG1LbpRYSy'
#Consumer Secret	STgPkq9497yyzWw8

MAPQUEST_ROUTE_URL = 'http://open.mapquestapi.com/directions/v2'
MAPQUEST_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1'

def build_route_url(location: list) -> str:
    '''
    Get the beginning address and destination, then build a URLthat can be used
    to ask MapQuest API for the information about routes
    '''
    parameters = [('key', Consumer_Key), ('from', location[0])]
    for i in location[1:]:
        parameters.append(('to', i))
    return MAPQUEST_ROUTE_URL + '/route?' + urllib.parse.urlencode(parameters)


def build_elevation_url(latlong: str) -> str:
    '''
    Get the latitude and longitude , then build a URLthat can be used
    to ask MapQuest API for the information about its elevation
    '''
    parameters = [('key', Consumer_Key), ('latLngCollection', latlong)]
    return MAPQUEST_ELEVATION_URL + '/profile?' + urllib.parse.urlencode(parameters)


def url_dict(url: str) -> dict:
    '''
    Become a URL to JSON response, and become it to a dictionary
    '''
    response = None

    try:
        response = urllib.request.urlopen(url)
        text = response.read().decode(encoding = 'utf-8')
        return json.loads(text)
    finally:
        if response != None:
            response.close()



