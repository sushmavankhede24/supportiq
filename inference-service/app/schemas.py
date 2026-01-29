from typing import List, Literal

from pydantic import BaseModel


class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str


class InferenceRequest(BaseModel):
    session_id: str
    intent: str
    messages: List[Message]


class InferenceResponse(BaseModel):
    reply: str
    confidence: float
    model_version: str
