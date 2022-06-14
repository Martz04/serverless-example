from dataclasses import dataclass

class Event:
    pass


@dataclass
class ThumbnailCreated(Event):
    location: str
    img_size: int
