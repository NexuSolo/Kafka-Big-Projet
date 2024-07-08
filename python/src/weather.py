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
        
        print(f"Météo à {location}, {region}, {country} :")
        print(f"Température: {temp_c}°C")
        print(f"Condition: {condition}")
    else:
        print(f"Erreur {response.status_code} : Impossible de récupérer les données météo")