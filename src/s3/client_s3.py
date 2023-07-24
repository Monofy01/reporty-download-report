import boto3

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