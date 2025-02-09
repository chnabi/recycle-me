from fastapi import APIRouter, File, UploadFile, Request
from fastapi.responses import JSONResponse
from io import BytesIO
from src.modules.classifier import ClassifierModule

from src.models import ImageRequest

router: APIRouter = APIRouter()


@router.post("/inform")
async def inform_recycle(
    request: Request, file: UploadFile = File(...)
):  # Use "file" instead of "image"
    image_data = await file.read()
    image_request = ImageRequest(image=image_data)
    classifier_module: ClassifierModule = request.app.state.classifier_module
    material = await classifier_module.query_vision(image_request)
    return {"material": material}
