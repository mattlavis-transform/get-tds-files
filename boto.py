import boto3
import os
from dotenv import load_dotenv

load_dotenv('.env')

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_REGION = os.getenv('AWS_REGION')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = os.getenv('BUCKET_NAME')

file_name = "readme.txt"
file_name2 = "xi/changes/readme.txt"
file_name2 = "xi/icl_vme/readme.txt"
file_name2 = "xi/csv/readme.txt"

s3 = boto3.resource(
    's3',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)


s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

# content="String content to write to a new S3 file"
# s3.Object(BUCKET_NAME, 'newfile2.txt').put(Body=content)
response = s3_client.upload_file(file_name, BUCKET_NAME, file_name2)