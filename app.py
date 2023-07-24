import base64
import json

from src.s3.client_s3 import S3Client


def handler(event: dict, context):
    print(f'REQUEST :: {event}')
    request_data = json.loads(event['body'])
    filename = request_data['file_name']
    signed_url = S3Client.generate_signed_url(filename)
    response = {
        'url_firmada': signed_url
    }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps(response),
    }