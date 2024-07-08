import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(latitude, longitude):
    api_key = os.getenv('WEATHER_API_API_Key')
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={latitude},{longitude}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        
        location = weather_data['location']['name']
        region = weather_data['location']['region']
        country = weather_data['location']['country']
        temp_c = weather_data['current']['temp_c']
        condition = weather_data['current']['condition']['text']
        last_updated = weather_data['current']['last_updated']
        
        return {
            "location": location,
            "region": region,
            "country": country,
            "temp_c": temp_c,
            "condition": condition,
            "last_updated": last_updated
        }
    else:
        print(f"Erreur {response.status_code} : Impossible de récupérer les données météo")