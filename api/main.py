from fastapi import FastAPI, Depends, HTTPException, Request
from slowapi.middleware import SlowAPIMiddleware
from schemas import ResumeAnalyzerRequest, ResumeAnalyzerResponse
from auth import authenticate
from rate_limit import limiter
from prompt import build_prompt
from llm.factory import get_llm
from utils import extract_json
import json

app = FastAPI(title="Resume Analyzer SaaS")

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.post("/analyze", response_model=ResumeAnalyzerResponse)
@limiter.limit("5/minute")
def analyze(
        request: Request,
        payload: ResumeAnalyzerRequest,
        user_tier: str = Depends(authenticate)
):
    if user_tier == "free" and len(payload.resume) > 10000:
        raise HTTPException(403, "Free tier resume too large")

    prompt = build_prompt(payload.resume, payload.job_description)

    llm = get_llm(
        provider=payload.provider,
        api_key=payload.llm_api_key
    )

    raw = llm.chat(prompt, payload.model)

    try:
        data = extract_json(raw)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to parse LLM JSON: {str(e)}"
        )

    return data
