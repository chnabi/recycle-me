# builtin
import base64

# external
from fastapi import APIRouter, Request
from openai import AsyncOpenAI
import pandas as pd

# internal
from src.models import ImageRequest


class ClassifierModule:
    def __init__(self, openai_client: AsyncOpenAI):
        self.openai_client = openai_client

    async def query_vision(self, image: ImageRequest):
        img_str = base64.b64encode(image.image).decode("utf-8")
        print("arrived")
        response = await self.openai_client.chat.completions.create(
            model="gpt-4-turbo",  # Adjust the model if necessary
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert in recycling, identify the recycling category of the object in the picture If unsure, provide your best estimate. Use context of the brand and type of object as well",
                },
                {
                    "role": "user",
                    "content": "What is the primary material of the object in this image? Please provide a short phrase answer (e.g plastic bin, aluminum, etc).",
                },
                {"role": "user", "content": f"data:image/png;base64,{img_str}"},
            ],
        )

        # Extract the material from the response
        material = response.choices[0].message.content  # Adjust if needed
        return material

    async def find_guidelines(self, material: str):
        return
