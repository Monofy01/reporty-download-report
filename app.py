import base64
import json

from src.s3.client_s3 import S3Client


def handler(event: dict, context):
    print(f'REQUEST :: {event}')
    request_data = json.loads(event['body'])
    filename = request_data['file_name']
    binary_data = S3Client.download_file(filename)# Encode the binary data to base64
    base64_data = base64.b64encode(binary_data).decode('utf-8')

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/octet-stream',
            'Content-Disposition': f'attachment; filename="{filename.split("/")[1]}"'
        },
        'body': base64_data,
        'isBase64Encoded': True
    }