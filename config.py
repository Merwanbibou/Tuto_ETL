# config.py

# Configuration de l'API
API_URL = "https://api.open-meteo.com/v1/forecast"
API_PARAMS = {
    "latitude": 48.8566,  # Latitude de Paris
    "longitude": 2.3522,  # Longitude de Paris
    "hourly": "temperature_2m"
}

# Configuration AWS S3
AWS_ACCESS_KEY = "YOUR_AWS_ACCESS_KEY"
AWS_SECRET_KEY = "YOUR_AWS_SECRET_KEY"
S3_BUCKET_NAME = "your-s3-bucket-name"
S3_FILE_NAME = "weather_data.csv"
