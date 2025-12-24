from abc import ABC, abstractmethod

class LLMProvider(ABC):

    @abstractmethod
    def chat(self, prompt: str, model: str) -> str:
        pass
