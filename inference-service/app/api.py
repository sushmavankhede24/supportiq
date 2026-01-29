from .llm.factory import get_llm_client
from .prompt import PROMPT_V1
from .schemas import InferenceRequest, InferenceResponse


def format_conversation(messages):
    return "\n".join(f"{m.role}: {m.content}" for m in messages)


def run_inference(req: InferenceRequest) -> InferenceResponse:
    conversation = format_conversation(req.messages)

    prompt = PROMPT_V1.format(intent=req.intent, conversation=conversation)

    llm = get_llm_client()
    result = llm.generate(prompt)

    return InferenceResponse(
        reply=result["reply"],
        confidence=result["confidence"],
        model_version=result["model_version"],
    )
