from thumbnail.domain import commands, model
from thumbnail.adapters import repository

def execute(
        cmd: commands.GetImageCommand,
        db_repository: repository.AbstractRepository
):
    response = db_repository.get(cmd.id)
    print(response)

    return response["Item"]