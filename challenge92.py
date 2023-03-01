#!/usr/bin/python3

import requests
import time
import reverse_geocoder as rg


iss = "http://api.open-notify.org/iss-now.json"

def main():
    position = requests.get(iss).json()

    epoch = position["timestamp"]
    currtime = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(epoch))
    
    lat = position['iss_position']['latitude']
    lon = position['iss_position']['longitude']

    coords_tuple = (lat, lon)
    result = rg.search(coords_tuple, verbose=False)

    print("Current location of the ISS:")
    print(f"Timestamp: {currtime}")
    print(f"Lon: {position['iss_position']['longitude']}")
    print(f"Lat: {position['iss_position']['latitude']}")
    print(f"City/Country: {result[0]['name']}, {result[0]['cc']}")

if __name__ == "__main__":
    main()

