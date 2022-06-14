import abc
import json
from thumbnail.domain import model


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, item: model.ThumbnailItem):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, thumbnail_id: str) -> model.ThumbnailItem:
        raise NotImplementedError


class DynamoDBRepository(AbstractRepository):

    def __init__(self, aws_client):
        self.aws_client = aws_client

    def add(self, item: model.ThumbnailItem):
        return self.aws_client.put_item(Item={**item.__dict__})

    def get(self, reference) -> model.ThumbnailItem:
        raise NotImplementedError


class FileRepository(AbstractRepository):
    def __init__(self, aws_client):
        self.aws_client = aws_client
        self.endpoint_url = aws_client.meta.endpoint_url

    def add(self, bucket, key, object):
        return self.aws_client.put_object(
            ACL="public-read",
            Body=object,
            Bucket=bucket,
            ContentType="image/png",
            Key=key
        )

    def get(self, bucket, key):
        return self.aws_client.get_object(Bucket=bucket, Key=key)
