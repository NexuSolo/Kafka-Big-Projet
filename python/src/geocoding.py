import requests
from weather import get_weather

def fetch_lat_long(address: str):
    params = {
        "q": address,
        "autocomplete": 1,
        "limit": 1,
        "type": "municipality"
    }

    url = "https://api-adresse.data.gouv.fr/search"
    response = requests.get(url, params=params)
    data = response.json()

    if data == {}:
        return False
    
    latitude = data["features"][0]["geometry"]["coordinates"][1]
    longitude = data["features"][0]["geometry"]["coordinates"][0]

    return get_weather(latitude, longitude)
