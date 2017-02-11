import random
import base64

from chalice import Chalice
import boto3

app = Chalice(app_name='randompng')
S3 = boto3.client('s3')
BUCKET = 'random.png'


@app.route('/', cors=True)
def handler():
    keys = [o['Key'] for o in S3.list_objects(Bucket=BUCKET)['Contents']]
    image = S3.get_object(Bucket=BUCKET, Key=random.choice(keys))['Body']
    return base64.b64encode(image.read())
