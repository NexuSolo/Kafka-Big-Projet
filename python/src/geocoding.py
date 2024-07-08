import requests

def fetch_lat_long(address: str):
    params = {
        "q": address,
        "autocomplete": 1,
        "limit": 1,
    }

    url = "https://api-adresse.data.gouv.fr/search"
    response = requests.get(url, params=params)
    data = response.json()

    if data == {}:
        return False
    
    result = {
        "lat": data["features"][0]["geometry"]["coordinates"][1],
        "long": data["features"][0]["geometry"]["coordinates"][0],
    }
    return result
