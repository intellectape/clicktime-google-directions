from googleplaces import GooglePlaces
import googlemaps
import re
import requests
from datetime import datetime

google_places = GooglePlaces('AIzaSyC_TAtDzzsRxRUsncrO3oQbML3ShmFeVLM')
google_maps = googlemaps.Client(key = 'AIzaSyA520AtS3sWlvFe67glVoFnJFtxIaU06Cg')

geocode_clicktime = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=282+2nd+Street+4th+floor,+San+Francisco,+CA+94105').json()['results'][0]['geometry']['location']


print(geocode_clicktime)

def directions_function(myLoc, transport, food):
    global google_places
    global google_maps
    global geocode_clicktime

    find_donuts = google_places.nearby_search(lat_lng = geocode_clicktime,
                    name = 'donut',
                    types = 'food',
                    rankby = 'distance' if food == 'distance' else 'prominance').places[0]
    
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