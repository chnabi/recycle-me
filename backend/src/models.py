from pydantic import BaseModel
from io import BytesIO
from fastapi import UploadFile


class InfoRequest(BaseModel):
    img: UploadFile
    city: str
    long: int
    lat: int


class MaterialOutput(BaseModel):
    material: str
