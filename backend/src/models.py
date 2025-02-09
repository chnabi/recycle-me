from pydantic import BaseModel
from io import BytesIO


class ImageRequest(BaseModel):
    image: bytes


class MaterialOutput(BaseModel):
    material: str
