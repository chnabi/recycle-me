from pydantic import BaseModel
from io import BytesIO
from fastapi import UploadFile
from enum import Enum


class RecycleEnum(Enum):
    YES = "yes"
    NO = "no"
    UNSURE = "unsure"


class InfoRequest(BaseModel):
    img: UploadFile
    city: str
    long: int
    lat: int


class InfoOutput(BaseModel):
    recycleable: RecycleEnum
    info: str
    waste_center: str | None


class MaterialOutput(BaseModel):
    material: str
