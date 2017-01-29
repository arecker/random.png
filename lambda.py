import random

import boto3


def handler(*args, **kwargs):
    s3 = boto3.client('s3')
    keys = [o['Key'] for o in s3.list_objects(Bucket='random.png')['Contents']]
    image = s3.get_object(Bucket='random.png', Key=random.choice(keys))['Body']
    return image
