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
                    "content": "You are an expert in material identification for recycling purposes. These are the choices:'Aluminum', 'Aluminum foil', 'Batteries', 'Cardboard', 'Cartons', 'Ceramic items', 'Clean pizza boxes', 'Clothing', 'Corrugated cardboard', 'Diapers', 'Disposable cups', 'Electronics', 'Food boxes', 'Glass bottles', 'Glass jars', 'Glassware', 'Greasy pizza boxes', 'Magazines', 'Metal cans', 'Mixed paper', 'Newspapers', 'Paper', 'Paper bags', 'Plastic bags', 'Plastic bottles', 'Plastic cups', 'Plastic jugs', 'Plastic lids', 'Plastic straws', 'Plastic tubs', 'Scrap metal', 'Shredded paper', 'Single-use cups', 'Styrofoam', 'Textiles', 'Tires', 'Toys', 'Wires'. If unsure, provide your best estimate.",
                },
                {
                    "role": "user",
                    "content": "What is the object in this image? Please include a description of the material. Give a short phrase or one word answer in plain text",
                },
                {"role": "user", "content": f"data:image/png;base64,{img_str}"},
            ],
        )

        material = response.choices[0].message.content
        print(material)
        return material

    async def find_guidelines(self, material, city, long, lat, county):
        response = check_item_in_city(county, city, material, lat, long)
        return response
