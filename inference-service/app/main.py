from fastapi import FastAPI

from .api import run_inference
from .schemas import InferenceRequest, InferenceResponse

app = FastAPI(title="SupportIQ Inference Service")


@app.post("/infer", response_model=InferenceResponse)
def infer(request: InferenceRequest):
    return run_inference(request)


@app.get("/health")
def health():
    return {"status": "ok"}
