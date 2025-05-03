from openai import OpenAI
from .llm_client import BaseLLMClient
import os

class GeminiClient(BaseLLMClient):
    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY")
        )
        self.model = "google/learnlm-1.5-pro-experimental:free"

    def generate(self, prompt, history):
        
        messages = history
        # Append current prompt
        messages.append({"role": "user", "content": prompt})

        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
            )
            print(completion)
            full_response = completion.choices[0].message.content.strip()
        except Exception as e:
            full_response = f"Error from Gemini via OpenRouter: {str(e)}"

        return full_response
