import os

from .huggingface import HuggingFaceLLMClient
from .mock import MockLLMClient


def get_llm_client():
    provider = os.getenv("LLM_PROVIDER", "mock")

    if provider == "huggingface":
        return HuggingFaceLLMClient()

    return MockLLMClient()
