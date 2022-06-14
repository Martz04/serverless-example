import uuid
from datetime import datetime
from thumbnail.domain import commands, model
from thumbnail.adapters import repository
from thumbnail.domain import events

def execute(
        cmd: commands.UploadImageCommand,
        file_repository:repository.AbstractRepository,
        db_repository: repository.AbstractRepository
):
    image = _get_s3_image(cmd, file_repository)
    print("IMAGE RETURNED FROM BUCKET")
    thumbnail = image.create_thumbnail(cmd.key, cmd.size)

    event = _upload_thumbnail(
        bucket=cmd.bucket,
        key=image.new_filename(cmd.key),
        size=cmd.size,
        thumbnail=thumbnail,
        repository=file_repository
    )

    _save_thumbnail(event, db_repository)

    return event.location


def _get_s3_image(cmd, repository):
    response = repository.get(cmd.bucket, cmd.key)
    content = response["Body"].read()

    return model.MyImage(content)


def _upload_thumbnail(bucket, key, size, thumbnail, repository):
    print(f"UPLOADING IMAGE:: {key} to bucket {bucket}")
    response = repository.add(bucket, key, thumbnail)
    print(response)

    return events.ThumbnailCreated(
        f"{repository.endpoint_url}/{bucket}/{key}",
        size
    )


def _save_thumbnail(event: events.ThumbnailCreated, repository):
    to_int = float(event.img_size * 0.53) / 1000
    thumbnail_item = model.ThumbnailItem(
        id=str(uuid.uuid4()),
        url=str(event.location),
        reduced_size=str(to_int) + str(" KB"),
        created_at=str(datetime.now()),
        updated_at=str(datetime.now())
    )
    response = repository.add(thumbnail_item)
    print(response)
