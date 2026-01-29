import random

from .base import LLMClient


class MockLLMClient(LLMClient):

    def generate(self, prompt: str) -> dict:
        responses = [
            "I understand your issue and I’m here to help.",
            "This looks like a common problem. Let me explain.",
            "Thanks for reaching out. Here’s what you can do next.",
        ]

        return {
            "reply": random.choice(responses),
            "confidence": round(random.uniform(0.7, 0.9), 2),
            "model_version": "mock-v1",
        }
