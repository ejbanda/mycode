#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def fetch(url):
    resp = requests.get(url)
    data = resp.json()
    print("\t",data['name'])

def loopMe(database, term):
    for item in database[term]:
        fetch(item)

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        name = got_dj['name']

        print(f'Character: {name}')
        print('Book appearances: ')
        loopMe(got_dj, 'books')

        print('Allegiances: ')
        loopMe(got_dj, 'allegiances')

        print('POV Books: ')
        loopMe(got_dj, 'povBooks')

if __name__ == "__main__":
        main()

