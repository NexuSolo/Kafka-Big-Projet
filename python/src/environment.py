from dotenv import load_dotenv
import os

load_dotenv()

WEATHER_API_API_KEY = os.getenv("WEATHER_API_API_Key")
KAFKA_BROKER = os.getenv("KAFKA_BROKER")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")
KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID")