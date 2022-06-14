# import sys
import os
from thumbnail.domain import model

current_dir = os.path.dirname(os.path.abspath(__file__))
IMAGE_SIZE = 128


def test_library():
    with open(os.path.join(current_dir, "assets/voters_short.png"), "rb") as content:
        img = model.get_image(content.read())
        thumbnail = model.image_to_thumbnail(img, IMAGE_SIZE)
        assert img is not None
        assert thumbnail is not None
