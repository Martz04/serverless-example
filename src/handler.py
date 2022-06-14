import os, sys
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, "thumbnail"))

import json

from thumbnail import config
from thumbnail.actions import upload_img_action
from thumbnail.domain import commands


size = int(os.environ["THUMBNAIL_SIZE"])
config.bootstrap_dependencies()

def s3_thumbnail_generator(event, context):
    # parse event
    print("EVENT:::", event)
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]
    img_size = event["Records"][0]["s3"]["object"]["size"]

    if not key.endswith("_thumbnail.png"):

        cmd = commands.UploadImageCommand(
            bucket=bucket,
            key=key,
            size=size
        )

        file_repository = config.adapters["file_repository"]
        db_repository = config.adapters["db_repository"]
        url = upload_img_action.execute(cmd, file_repository, db_repository)

        body = {
            "message": "Image converted successfully",
            "input": event,
            "url": url
        }
        return {"statusCode": 200, "body": json.dumps(body)}

    return {"statusCode": 201}
