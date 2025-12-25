from fastapi import FastAPI, Depends, HTTPException, Request
from slowapi.middleware import SlowAPIMiddleware

from utils.scoring import calculate_match_score
from utils.extract_json import extract_json
from schemas import ResumeAnalyzerRequest, ResumeAnalyzerResponse
from auth import authenticate
from rate_limit import limiter
from prompt import build_prompt
from llm.factory import get_llm
from utils import extract_json

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
    # -------- Tier check --------
    if user_tier == "free" and len(payload.resume) > 10000:
        raise HTTPException(
            status_code=403,
            detail="Free tier resume too large"
        )

    # -------- Build prompt --------
    prompt = build_prompt(
        payload.resume,
        payload.job_description
    )

    # -------- Get LLM --------
    llm = get_llm(
        provider=payload.provider,
        api_key=payload.llm_api_key
    )

    # -------- Call LLM --------
    raw = llm.chat(prompt, payload.model)

    # -------- Parse JSON --------
    try:
        analysis = extract_json(raw)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to parse LLM JSON: {str(e)}"
        )

    # -------- Deterministic ATS scoring --------
    try:
        analysis["match_score"] = calculate_match_score(analysis)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to calculate match score: {str(e)}"
        )

    return analysis
