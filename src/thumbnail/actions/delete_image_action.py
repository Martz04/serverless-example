from thumbnail.domain import commands, model
from thumbnail.adapters import repository

def execute(
        cmd: commands.DeleteImageCommand,
        file_repository:repository.AbstractRepository,
        db_repository: repository.AbstractRepository
):
    # Set the default error response
    bad_response = {
        "statusCode": 500,
        "body": f"An error occured while deleting post {cmd.id}"
    }

    all_good_response = {
        "deleted": True,
        "itemDeletedId": cmd.id
    }

    response = db_repository.delete(cmd.id)
    print(response)

    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json",
                    "Access-control-Allow-Origin": "*"},
            "body": json.dumps(all_good_response),
        }

    return bad_response