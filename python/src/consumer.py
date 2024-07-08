import json
import streamlit as st
from kafka import KafkaConsumer
from dashboards import consumer_dashboard
from environment import KAFKA_TOPIC, KAFKA_BROKER

def process_data(message):
    data = message.value

    col1, col2 = st.columns(2)

    col1.metric("Location", data["location"])
    col2.metric("Region", data["region"])
    col1.metric("Country", data["country"])

    col2.metric("Temperature (°C)", data["temp_c"])
    col1.metric("Condition", data["condition"])
    last_updated = data["last_updated"]
    st.success(f"Last updated: {last_updated}")

def consume_message():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    )

    for message in consumer:
        print(message)
        process_data(message)

if __name__ == '__main__':
    consumer_dashboard()
    consume_message()