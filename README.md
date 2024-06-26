
# Tuto_ETL

## Description
Ce projet implémente un processus ETL (Extraction, Transformation, Chargement) complet en Python. Il extrait des données météorologiques d'une API publique, les transforme en un format structuré, et les charge dans un bucket S3.

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/Merwanbibou/Tuto_ETL.git
    cd Tuto_ETL
    ```

2. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

3. Configurez les paramètres dans `config.py`.

## Utilisation

Pour exécuter le script ETL, lancez la commande suivante :
```bash
python etl.py
```

## Configuration

Assurez-vous de configurer correctement les paramètres API et AWS S3 dans config.py (N'oubliez pas de sécuriser vos clés AWS en utilisant des variables d'environnement).







