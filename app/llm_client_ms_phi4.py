import os
from openai import OpenAI
from .llm_client import BaseLLMClient

class MS_PHI4Client(BaseLLMClient):
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )


    def generate(self, prompt, history):
        
        messages = history
        messages.append({"role": "user", "content": prompt})

        completion = self.client.chat.completions.create(
            model="microsoft/phi-4-reasoning-plus:free",
            messages=messages
        )

        response = completion.choices[0].message.content
        return response