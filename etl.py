# etl.py

import requests
import pandas as pd
import boto3
from config import API_URL, API_PARAMS, AWS_ACCESS_KEY, AWS_SECRET_KEY, S3_BUCKET_NAME, S3_FILE_NAME

def extract_data(url, params):
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()

def transform_data(data):
    hourly_data = data['hourly']['temperature_2m']
    df = pd.DataFrame(hourly_data, columns=['time', 'temperature_2m'])
    df['time'] = pd.to_datetime(df['time'])
    return df

def load_data_to_s3(df, bucket_name, file_name, aws_access_key, aws_secret_key):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )
    csv_buffer = df.to_csv(index=False)
    s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=csv_buffer)

def main():
    # Extraction
    data = extract_data(API_URL, API_PARAMS)

    # Transformation
    df = transform_data(data)

    # Chargement
    load_data_to_s3(df, S3_BUCKET_NAME, S3_FILE_NAME, AWS_ACCESS_KEY, AWS_SECRET_KEY)
    print("ETL process completed successfully.")

if __name__ == "__main__":
    main()
