from fastapi import APIRouter, Request

from src.modules.classifier import ClassifierModule

from src.models import ImageRequest

router: APIRouter = APIRouter()


@router.post("/inform")
async def inform_recycle(image: ImageRequest, request: Request):
    classifier_module: ClassifierModule = request.app.state.classifier_module
    material = await classifier_module.query_vision(image)
    return {"material": material}
