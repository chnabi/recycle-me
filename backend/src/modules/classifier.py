# builtin
import base64

# external
from fastapi import APIRouter, Request
from openai import AsyncOpenAI

# internal
from src.models import ImageRequest


class ClassifierModule:
    def __init__(self, openai_client: AsyncOpenAI):
        self.openai_client = openai_client

    async def query_vision(self, image: ImageRequest):
        response = await self.openai_client.chat.completions.create(
            model="gpt-4",  # Adjust the model if necessary
            messages=[
                {
                    "role": "user",
                    "content": "What material is the object in this image made of? Please provide the material type only (e.g., plastic, glass, metal).",
                },
                {"role": "user", "content": f"{image.image}"},
            ],
        )

        # Extract the material from the response
        material = response.choices[0].message.content  # Adjust if needed
        return material
