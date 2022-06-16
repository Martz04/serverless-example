from thumbnail.domain import commands, model
from thumbnail.adapters import repository

def execute(
        cmd: commands.ListImagesCommand,
        db_repository: repository.DynamoDBRepository
):
    response = db_repository.list()
    data = response["Items"]

    while "LastEvaluatedKey" in response:
        response = db_repository.list(
            exclusiveStartKey= response["LastEvaluatedKey"]
        )
        data.extend(resonse["Items"])

    print(data)
    return data