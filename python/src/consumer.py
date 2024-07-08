import json
import streamlit as st
from kafka import KafkaConsumer
from dashboards import consumer_dashboard
from environment import KAFKA_TOPIC, KAFKA_BROKER

def process_data(message):
    data = message.value

    if 'initialized' not in st.session_state:
        st.session_state['col1'], st.session_state['col2'] = st.columns(2)
        st.session_state['location'] = st.session_state['col1'].empty()
        st.session_state['region'] = st.session_state['col2'].empty()
        st.session_state['temperature'] = st.session_state['col2'].empty()
        st.session_state['condition'] = st.session_state['col1'].empty()
        st.session_state['last_updated'] = st.empty()
        st.session_state['initialized'] = True

    # Mettre à jour les placeholders avec de nouvelles données
    st.session_state['location'].metric("Location", data["location"])
    st.session_state['region'].metric("Region", data["region"], data["country"])
    st.session_state['temperature'].metric("Temperature (°C)", data["temp_c"])
    st.session_state['condition'].metric("Condition", data["condition"])
    last_updated = data["last_updated"]
    st.session_state['last_updated'].success(f"Last updated: {last_updated}")

def consume_message():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    )

    for message in consumer:
        process_data(message)

if __name__ == '__main__':
    consumer_dashboard()
    consume_message()