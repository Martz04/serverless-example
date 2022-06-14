from dataclasses import dataclass

class Command:
    pass


@dataclass
class UploadImageCommand(Command):
    bucket: str
    key: str
    size: str