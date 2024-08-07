import streamlit as st
from kafka import KafkaProducer
import json
import threading
from time import sleep
from environment import KAFKA_BROKER, KAFKA_TOPIC
from geocoding import fetch_lat_long
from dashboards import producer_dashboard

def producer(location):
    producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])
    data = fetch_lat_long(location)
    if data:
        res = json.dumps(data).encode("utf-8")
        producer.send(KAFKA_TOPIC, res)
        return res
    return None

def producer_loop():
    producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])
    while True:
        location = "Paris"
        data = fetch_lat_long(location)
        if data:    
            res = json.dumps(data).encode("utf-8")
            producer.send(KAFKA_TOPIC, res)
            sleep(900)

if __name__ == "__main__":
    producer_dashboard()
    thread = threading.Thread(target=producer_loop)
    thread.start()

    location = st.text_input('Location')
    action = st.button('Produce weather data to Kafka')
    if action:
        message = producer(location)
        if message:
            print(message)
            st.success("Weather data produced to Kafka.")
        else:
            st.error("Error producing data to Kafka.")
    