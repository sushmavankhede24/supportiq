import os

import requests

from .base import LLMClient

HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct"


class HuggingFaceLLMClient(LLMClient):

    def __init__(self):
        self.api_key = os.getenv("HF_API_TOKEN")

    def generate(self, prompt: str) -> dict:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {"inputs": prompt}

        response = requests.post(HF_API_URL, headers=headers, json=payload)
        response.raise_for_status()

        output = response.json()[0]["generated_text"]

        return {
            "reply": output.strip(),
            "confidence": 0.75,
            "model_version": "mistral-7b",
        }
