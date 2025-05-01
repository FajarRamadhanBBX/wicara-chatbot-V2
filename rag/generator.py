from openai import OpenAI
from dotenv import load_dotenv
import os
from fastapi.encoders import jsonable_encoder

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def answer_prompt(prompt: str) -> str:
    response = client.responses.create(
        model="o4-mini",
        input=prompt
    )
    print(response)

    response = jsonable_encoder(response)
    
    return response['output'][1]['content'][0]['text']