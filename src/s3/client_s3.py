from datetime import datetime, timedelta

import boto3
from botocore.exceptions import ClientError

from src.config.enviroments import ENVS


class S3Client:
    def __init__(self):
        self.data = ""
    @staticmethod
    def download_file(filename):
        s3 = boto3.client('s3')
        try:
            response = s3.get_object(Bucket=ENVS.S3_BUCKET_NAME, Key=filename)
            file_content = response["Body"].read()

            return file_content
        except Exception as e:
            return f"Error al descargar el archivo: {str(e)}"

    @staticmethod
    def generate_signed_url(filename):  # Set expiration to 3 minutes (180 seconds)
        s3 = boto3.client('s3')
        try:
            expiration_time = datetime.utcnow() + timedelta(seconds=180)
            response = s3.generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': ENVS.S3_BUCKET_NAME,
                    'Key': filename
                },
                ExpiresIn=180,
                HttpMethod='GET'
            )
            return response
        except ClientError as e:
            return f"Error al generar la URL firmada: {str(e)}"