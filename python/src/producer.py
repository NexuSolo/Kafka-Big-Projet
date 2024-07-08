import json
from kafka import KafkaProducer
from environment import KAFKA_BROKER, KAFKA_TOPIC
from geocoding import fetch_lat_long

def producer(localisation):
    producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])
    data = fetch_lat_long(localisation)

    if data:
        res = json.dumps(data).encode("utf-8")
        producer.send(KAFKA_TOPIC, res)
        producer.flush()
        print(f"Data sent to topic {KAFKA_TOPIC}")

    return None

if __name__ == "__main__":
    pass