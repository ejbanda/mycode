#!/usr/bin/env python3
import requests
import datetime
import reverse_geocoder as rg

API = 'http://api.open-notify.org/iss-now.json'

def location(api):
    lon = api["iss_position"]["longitude"]
    lat = api["iss_position"]["latitude"]
    coord = (lat, lon)
    loc = rg.search(coord)
    city = loc[0]['name']
    country = loc[0]['cc']
    print('CURRENT LOCATION OF THE ISS: ')
    print(f'Timestamp: {datetime.datetime.fromtimestamp(api["timestamp"])}')
    print(f'Lon: {lon}\nLat: {lat}')
    print(f'City/Country: {city}, {country}')

def main():
    req = requests.get(API)
    issNow = req.json()
    location(issNow)
    

if __name__ == "__main__":
    main()
