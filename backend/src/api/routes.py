from fastapi import APIRouter, File, UploadFile, Request
from fastapi.responses import JSONResponse
from io import BytesIO
from src.modules.classifier import ClassifierModule

from src.models import ImageRequest

router: APIRouter = APIRouter()


@router.post("/inform")
async def inform_recycle(request: Request, image: UploadFile = File(...)):
    image_data = await image.read()
    image_request: ImageRequest = ImageRequest(image=image_data)
    classifier_module: ClassifierModule = request.app.state.classifier_module
    material = await classifier_module.query_vision(image_request)
    return {"material": material}
