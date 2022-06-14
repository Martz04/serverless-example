from io import BytesIO
from PIL import Image, ImageOps
from dataclasses import dataclass
from typing import Any


class MyImage:
    def __init__(self, content):
        self._content = content
        self._file = BytesIO(content)
        self._img = Image.open(self._file)

    def to_thumbnail(self, size):
        return ImageOps.fit(self._img, (size, size), Image.ANTIALIAS)

    def new_filename(self, key):
        key_split = key.rsplit(".", 1)
        return key_split[0] + "_thumbnail.png"


    def create_thumbnail(self, name, size):
        out_thumbnail = BytesIO()
        self._img.save(out_thumbnail, 'PNG')
        out_thumbnail.seek(0)
        return out_thumbnail


@dataclass
class ThumbnailItem:
    id: str
    url: str
    reduced_size: str
    created_at: str
    updated_at: str