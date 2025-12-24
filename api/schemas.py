from pydantic import BaseModel
from typing import List

class ResumeAnalyzerRequest(BaseModel):
    resume: str
    job_description: str
    model: str
    provider: str
    llm_api_key: str

class ResumeImprovements(BaseModel):
    missing_keywords: List[str]
    summary_improvements: str
    quantifiable_metrics: List[str]
    ats_optimization: List[str]

class ResumeAnalyzerResponse(BaseModel):
    match_score: int
    strengths: List[str]
    weaknesses: List[str]
    improvement_suggestions: List[str]
    resume_improvements: ResumeImprovements
