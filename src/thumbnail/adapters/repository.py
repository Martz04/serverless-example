import abc
import json
from thumbnail.domain import model


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, item: model.ThumbnailItem):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, thumbnail_id: str):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, thumbnail_id: str):
        raise NotImplementedError


class DynamoDBRepository(AbstractRepository):

    def __init__(self, table):
        self.table = table

    def add(self, item: model.ThumbnailItem):
        return self.table.put_item(Item={**item.__dict__})

    def delete(self, id: str):
        return self.table.delete_item(Key={"id": id})

    def get(self, id: str):
        return self.table.get_item(Key={"id": id})

    def list(self, exclusiveStartKey=None):
        if exclusiveStartKey:
            return self.table.scan(ExclusiveStartKey=exclusiveStartKey)
        return self.table.scan()


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

    def delete(self, thumbnail_id: str):
        raise NotImplementedError
