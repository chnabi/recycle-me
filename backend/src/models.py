from pydantic import BaseModel
from io import BytesIO
from fastapi import UploadFile, File
from enum import Enum


class RecycleEnum(Enum):
    YES = "yes"
    NO = "no"
    UNSURE = "unsure"


class InfoRequest(BaseModel):
    img: str
    city: str
    long: float
    lat: float
    county: str


class InfoOutput(BaseModel):
    recycleable: RecycleEnum
    info: str
    material: str


class MaterialOutput(BaseModel):
    material: str
