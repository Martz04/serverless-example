from dataclasses import dataclass

class Command:
    pass


@dataclass
class UploadImageCommand(Command):
    bucket: str
    key: str
    size: str


@dataclass
class DeleteImageCommand(Command):
    id: str


@dataclass
class GetImageCommand(Command):
    id: str


@dataclass
class ListImagesCommand(Command):
    pass