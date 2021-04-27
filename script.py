import requests
# import pathlib
import datetime
import boto3


QUERY = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=-1"
S3_BUCKET = 'karaduck-data-raw'
S3_KEY_PREFIX = 'vlille-api'
FILE_PREFIX = 'vlille_api_'

def lambda_handler(event, context):
    response = requests.get(QUERY)
    filename = f"{FILE_PREFIX}{datetime.datetime.utcnow().isoformat()}.json"
    # pathlib.Path(filename).write_bytes(response.content)
    client = boto3.client('s3')
    # with open(filename, 'rb') as file:
    client.put_object(Body=response.content, Bucket=S3_BUCKET, Key=f"{S3_KEY_PREFIX}/{filename}")
