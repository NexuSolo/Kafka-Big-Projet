# Projet Kafka

- Nicolas THEAU
- Sebastien ZHOU
- Yanis ROZIER

## Description

Ce projet est une application de streaming de données météorologiques utilisant Apache Kafka. Il comprend un producteur qui envoie des données météorologiques pour un emplacement spécifique à un topic Kafka, et un consommateur qui lit ces données et les affiche sur un tableau de bord.
Cette application affiche la météo de Paris toutes les 15 minutes, elle peut également afficher la météo d'une autre ville française au choix en écrivant dans la zone de texte du `Producteur`.

## Architecture

Le projet est structuré comme suit :

- `docker-compose.yml` : Contient la configuration pour démarrer les services Kafka, Zookeeper et Python
- `python/` : Contient le code source de l'application en Python.
  - `src/` : Dossier contenant les scripts Python.
    - `consumer.py` : Script du consommateur qui lit les données du topic Kafka.
    - `dashboards.py` : Contient les tableaux de bord pour les producteurs et consommateurs.
    - `environment.py` : Charge les variables d'environnement nécessaires.
    - `geocoding.py` : Utilitaire pour convertir les emplacements en coordonnées géographiques.
    - `producer.py` : Script du producteur qui envoie les données météorologiques au topic Kafka.
    - `weather.py` : Utilitaire pour récupérer les données météorologiques.
    - `Dockerfile` : Contient les instructions pour construire l'image Docker de l'application, incluant l'environnement d'exécution et les dépendances nécessaires.
    - `.env` : Fichier pour les variables d'environnement (exclu par `.gitignore`).
    - `requierement.txt` : Fichier contenant les dépendances Python nécessaires.



## Prérequis

- Docker et Docker Compose
- Se créer un compte sur WeatherApi (https://www.weatherapi.com) pour générer une clé

## Installation

1. Clonez le dépôt et s'y déplacer :
```sh
git clone https://github.com/NexuSolo/Kafka-Big-Projet.git
cd Kafka-Big-Projet
```
2. Remplir le .env notamment avec la clé de WeatherAPI :
```sh
KAFKA_BROKER = "kafka:29092"
KAFKA_TOPIC = "weather_data"
KAFKA_GROUP_ID = "weather_consumer_group"
WEATHER_API_API_Key = <votre clé>
```

3. Lancez les services Kafka, Zookeeper et Python avec Docker Compose :
```sh
docker-compose up -d
```

## Utilisation

### Le producer

Consultable sur : http://localhost:8502

### Le consumer

Consultable sur : http://localhost:8501


## Affichage

L'affichage des données dans ce projet est géré par **Streamlit**, un framework open-source qui permet de créer rapidement des applications web pour la visualisation de données.