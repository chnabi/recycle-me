from fastapi import APIRouter, File, UploadFile, Request
from fastapi.responses import JSONResponse
from io import BytesIO
from src.modules.classifier import ClassifierModule

from src.models import InfoRequest

router: APIRouter = APIRouter()


@router.post("/inform")
async def inform_recycle(request: Request, data: InfoRequest):
    image_data = await data.img.read()
    classifier_module: ClassifierModule = request.app.state.classifier_module
    material = await classifier_module.query_vision(image_data)
    recycleable: str = await classifier_module.find_guidelines(material, data)
    return {"material": material}
