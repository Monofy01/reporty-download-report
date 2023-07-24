import base64
import json

from src.s3.client_s3 import S3Client


def handler(event: dict, context):
    print(f'REQUEST :: {event}')
    request_data = json.loads(event['body'])
    filename = request_data['file_name']
    binary_data = S3Client.download_file(filename)
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/octet-stream',
            'Content-Disposition': f'attachment; filename="{filename.split("/")[0]}"'
        },
        'body': binary_data,
        'isBase64Encoded': False  # Indicar que los datos no están codificados en base64
    }