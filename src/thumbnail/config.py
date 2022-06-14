import os
import boto3
from thumbnail.adapters import repository

adapters = {
    "db_repository": None,
    "file_repository": None
}

def bootstrap_dependencies():

    dynamodb, s3 = get_client()

    db_table = str(os.environ["DYNAMODB_TABLE"])
    adapters["db_repository"] = repository.DynamoDBRepository(dynamodb.Table(db_table))
    adapters["file_repository"] = repository.FileRepository(s3)


def get_client():
    if 'LOCALSTACK_HOSTNAME' in os.environ:
        endpoint_url = 'http://%s:4566' % os.environ['LOCALSTACK_HOSTNAME']
        print("LOCAL ENVIRONMENT:::", endpoint_url)
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url=endpoint_url,
            region_name=str(os.environ["REGION_NAME"])
        )
        s3 = boto3.client("s3", endpoint_url=endpoint_url)

        return dynamodb, s3
    else:
        dynamodb = boto3.resource('dynamodb', region_name=str(os.environ["REGION_NAME"]))
        s3 = boto3.client("s3")

        return dynamodb, s3
