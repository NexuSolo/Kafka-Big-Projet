# Kafka-Big-Projet

## Description

Ce projet est une application de streaming de données météorologiques utilisant Apache Kafka. Il comprend un producteur qui envoie des données météorologiques pour un emplacement spécifique à un topic Kafka, et un consommateur qui lit ces données et les affiche sur un tableau de bord.

## Architecture

Le projet est structuré comme suit :

- `docker-compose.yml` : Contient la configuration pour démarrer les services Kafka et Zookeeper.
- `python/` : Contient le code source de l'application en Python.
  - `src/` : Dossier contenant les scripts Python.
    - `consumer.py` : Script du consommateur qui lit les données du topic Kafka.
    - `dashboards.py` : Contient les tableaux de bord pour les producteurs et consommateurs.
    - `environment.py` : Charge les variables d'environnement nécessaires.
    - `geocoding.py` : Utilitaire pour convertir les emplacements en coordonnées géographiques.
    - `producer.py` : Script du producteur qui envoie les données météorologiques au topic Kafka.
    - `weather.py` : Utilitaire pour récupérer les données météorologiques.
  - `.env` : Fichier pour les variables d'environnement (exclu par `.gitignore`).
- `requierement.txt` : Fichier contenant les dépendances Python nécessaires.

## Prérequis

- Docker et Docker Compose
- Python 3.8 ou supérieur
- Se créer un compte sur WeatherApi (https://www.weatherapi.com) pour générer une clé

## Installation

1. Clonez le dépôt et s'y déplacer :
```sh
git clone https://exemple.com/Kafka-Big-Projet.git
cd Kafka-Big-Projet
```

2. Lancez les services Kafka et Zookeeper avec Docker Compose :
```sh
docker-compose up -d
```

3. Installez les dépendances Python :
```sh
pip install -r requierement.txt
```

4. Remplir le .env notamment avec la clé de WeatherAPI :
```sh
KAFKA_BROKER = "localhost:9092"
KAFKA_TOPIC = "weather_data"
KAFKA_GROUP_ID = "weather_consumer_group"
WEATHER_API_API_Key = votre clé
```


## Utilisation

### Démarrer le producteur

Exécutez le script du producteur pour commencer à envoyer des données météorologiques :
```sh
python python/src/producer.py
```
Consultable sur : http://localhost:8502

### Démarrer le consommateur

Exécutez le script du consommateur pour lire les données du topic Kafka et afficher le tableau de bord :
```sh
python python/src/consumer.py
```
Consultable sur : http://localhost:8501
