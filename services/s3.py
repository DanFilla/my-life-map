import os
import datetime
import boto3
import logging

logger = logging.getLogger(__name__)

class S3Service:
    def __init__(self):
        self.bucket_name = os.environ.get('BUCKET_NAME')
        self.region = os.environ.get('REGION')
        self.base_url = f'https://{self.bucket_name}.s3.{self.region}.amazonaws.com'
        self.s3 = boto3.client('s3', aws_access_key_id=os.environ.get('ACCESS_KEY'), aws_secret_access_key=os.environ.get('SECRET_KEY'))

    def _get_auth_headers(self):
        headers = {
            'x-amz-content-sha256': 'UNSIGNED-PAYLOAD',
            'x-amz-date': datetime.datetime.now().strftime("%Y%m%dT%H%M%S") + "Z",
        }
        return headers

    def upload(self, file_data, file_key, *args, **kwargs):
        try:
            logger.debug("bucket: " + self.bucket_name)
            logger.debug("region: " + self.region)
            logger.debug("base_url: " + self.base_url)

            #self.s3.upload_fileobj(file_data, self.bucket_name, file_key)
            self.s3.put_object(
                Body=file_data,
                Bucket=self.bucket_name,
                Key=file_key,
                ContentType="application/json",
                ContentDisposition='inline',
            )

            s3_url = f'https://{self.bucket_name}.s3.{self.region}.amazonaws.com/{file_key}'
            logger.debug("s3_url: ", s3_url)

            logger.debug(f'Successfully uploaded to {s3_url}')

            return s3_url
        except Exception as e:
            logger.error(f'Failed upload: {e}')
            return None

    def delete(self, s3_file_path):
        try:
            self.s3.delete_object(Bucket=self.bucket_name, Key=s3_file_path)
            print(f'Successfully deleted object: {s3_file_path}')
        except Exception as e:
            print(f'Failed to delete object: {s3_file_path}. Error: {e}')

#    def download(self, s3_file_path, local_file_path):
#        url = f'{self.base_url}/{s3_file_path.lstrip("/")}'
#        headers = self._get_auth_headers()
#        response = requests.get(url, headers=headers)
#
#        if response.status_code == 200:
#            with open(local_file_path, 'wb') as file:
#                file.write(response.content)
#            print(f'Successfully downloaded {s3_file_path} to {local_file_path}')
#        else:
#            print(f'Failed to download {s3_file_path} to {local_file_path}. Status Code: {response.status_code}')
#            print(response.text)