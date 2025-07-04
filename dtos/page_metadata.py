from pydantic import BaseModel
from typing import List
from constants.types.metadata import MetadataType

class PageMetadataDto(BaseModel):
    type: str = MetadataType.PAGE
    url: str
    title: str
    path: str
    tags: List[str]
    more_information: str