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
            model="gpt-4o",  # Adjust the model if necessary
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert in material identification for recycling purposes. Analyze the image and determine the primary material of the object shown (e.g ). If unsure, provide your best estimate and explain your reasoning.",
                },
                {
                    "role": "user",
                    "content": "What is the object in this image? Please include a description of the material. Give a short phrase or one word answer",
                },
                {"role": "user", "content": f"data:image/png;base64,{img_str}"},
            ],
        )

        # Extract the material from the response
        material = response.choices[0].message.content  # Adjust if needed
        return material

    async def find_guidelines(self, material: str):
        return
