import requests
import math

URL_PATH = "https://nominatim.openstreetmap.org/search"

def get_lat_lon(location):
    PARAMS = {'q' : location, 'format': 'jsonv2'}
    headers = {
        'User-Agent': 'DistanceCalc/1.0'
    }

    r = requests.get(URL_PATH, params = PARAMS, headers = headers)
    data = r.json()

    latitude = float(data[0]['lat'])
    longitude = float(data[0]['lon'])

    return [latitude, longitude]
#end function

def calculate_distance(orig, dest): 
    #longgitude = 2nd part of returned coord array
    dlon = dest[1] - orig[1]  #dlon = lon2 - lon1
    # lat = 1st part at index 0 
    dlat = dest[0] - orig[0] #dlat = lat2 - lat1
    #a = (sin(dlat/2))^2 + cos(lat1) * cos(lat2) * (sin(dlon/2))^2
    a = (math.sin(math.radians(dlat/2)))**2 + \
         math.cos(math.radians(orig[0])) * \
         math.cos(math.radians(dest[0])) * \
         (math.sin(math.radians(dlon/2)))**2
    #c = 2 * atan2( sqrt(a), sqrt(1-a) )
    c = 2 * math.atan2(math.sqrt(a) , math.sqrt(1-a))
    R = 3961
    d = R * c
    
    return d
#end function