from fastapi import APIRouter, Form, File, UploadFile, Request
from fastapi.responses import JSONResponse
from io import BytesIO
from src.modules.classifier import ClassifierModule

from src.models import InfoRequest

router: APIRouter = APIRouter()


@router.post("/inform")
async def inform_recycle(
    request: Request,
    file: UploadFile = File(...),
    city: str = Form(...),
    long: float = Form(...),
    lat: float = Form(...),
    county: str = Form(...),
):  # Use File for image

    # Read the uploaded image file
    image_data = await file.read()

    # Get the classifier module from the app state
    classifier_module = request.app.state.classifier_module

    # Classify the image using the classifier module
    material = await classifier_module.query_vision(image_data)

    # Find recycling guidelines based on the material
    recycleable: str = await classifier_module.find_guidelines(
        material, city, long, lat, county
    )
    return JSONResponse(content={"material": material, "recycling_info": recycleable})
