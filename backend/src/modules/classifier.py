# builtin
import base64

# external
from fastapi import APIRouter, Request
from openai import AsyncOpenAI
import pandas as pd

# internal
from modules.data_processing import check_item_in_city, find_county_by_city
from src.models import InfoRequest


class ClassifierModule:
    def __init__(self, openai_client: AsyncOpenAI):
        self.openai_client = openai_client

    async def query_vision(self, image: bytes):
        img_str = base64.b64encode(image).decode("utf-8")
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

        material = response.choices[0].message.content
        return material

    async def find_guidelines(self, material, geo_info: InfoRequest):
        county = find_county_by_city(geo_info.city)
        response = check_item_in_city(
            county, geo_info.city, material, geo_info.lat, geo_info.long
        )
        return response
