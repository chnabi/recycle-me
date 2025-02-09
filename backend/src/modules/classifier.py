#builtin 
import base64 

#external 
from fastapi import APIRouter, Request
from openai import AsyncOpenAI
#internal 

class ClassifierModule: 
    def __init__(self, openai_client: AsyncOpenAI):
        self.openai_client = openai_client
    
    async def query_vision(self, openai_client, base64_image: str):
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"role": "system", "content": "You are an expert in identifying recyclables."},
                        {
                            "type": "text",
                            "text": "What is this material is the object in this picture made of?",
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                        },
                    ],
                }
            ],
        )
        return

