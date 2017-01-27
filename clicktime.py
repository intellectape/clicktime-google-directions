from googleplaces import GooglePlaces
import googlemaps
import re
import json
import requests
import sys
from datetime import datetime

if len(sys.argv) != 3:
    print("python clicktime.py <driving | bicycling | walking | transit> <distance | prominence>")
    print("No route to show!")
    exit(1)

google_places = GooglePlaces('AIzaSyC_TAtDzzsRxRUsncrO3oQbML3ShmFeVLM')
google_maps = googlemaps.Client(key = 'AIzaSyA520AtS3sWlvFe67glVoFnJFtxIaU06Cg')

geocode_clicktime = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=282+2nd+Street+4th+floor,+San+Francisco,+CA+94105').json()['results'][0]['geometry']['location']

def main():
    print(geocode_clicktime)
    directionsArray = directions_function(getLocAuto(), sys.argv[1], sys.argv[2])
    
    for index in directionsArray:
        print(index)

def getLocAuto():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longitude']
    return {'lat': lat, 'lng': lon}

def directions_function(myLoc = getLocAuto(), transport='walking', food='distance'):
    global google_places
    global google_maps
    global geocode_clicktime

    find_donuts = google_places.nearby_search(lat_lng = geocode_clicktime,
                    name = 'donut',
                    types = 'food',
                    rankby = food).places[0]
    
    directions_to_donuts = google_maps.directions(myLoc,
                                     find_donuts.geo_location,
                                     mode=transport,
                                     departure_time = datetime.now())
    directions_to_office = google_maps.directions(find_donuts.geo_location,
                                    geocode_clicktime,
                                     mode=transport)
    directions = []
    rex = re.compile('<.*?>')
    for route in directions_to_donuts[0]['legs'][0]['steps']:
        cleantext = re.sub(rex, ' ', route['html_instructions'])
        directions.append(cleantext)

    directions.append('Starting from Donuts Shop to Office.....')
    for route in directions_to_office[0]['legs'][0]['steps']:
        cleantext = re.sub(rex, ' ', route['html_instructions'])
        directions.append(cleantext)
    
    directions.append('Reached ClickTime Office!!!')

    return directions

# from decimal import *
# myLoc = {'lat': Decimal('35.7750447'), 'lng': Decimal('-78.6837875')}

if __name__=="__main__":
    main()