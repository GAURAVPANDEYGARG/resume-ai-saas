from llm.openai_provider import OpenAIProvider
from llm.groq_provider import GroqProvider

def get_llm(provider: str, api_key: str):
    provider = provider.lower()

    if provider == "openai":
        return OpenAIProvider(api_key)

    if provider == "groq":
        return GroqProvider(api_key)

    raise ValueError("Unsupported LLM provider")
