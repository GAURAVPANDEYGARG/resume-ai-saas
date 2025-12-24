from groq import Groq
from llm.base import LLMProvider

class GroqProvider(LLMProvider):

    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)

    def chat(self, prompt: str, model: str) -> str:
        response = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content
