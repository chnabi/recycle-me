from pydantic import BaseModel


class ImageRequest(BaseModel):
    image: str


class MaterialOutput(BaseModel):
    material: str
