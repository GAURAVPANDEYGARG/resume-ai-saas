def build_prompt(resume: str, jd: str) -> str:
    return f"""
You are an ATS resume analyzer.

RULES:
- Output ONLY valid JSON
- No explanation
- No markdown
- No extra text

Return this exact schema:
{{
  "match_score": 0-100,
  "strengths": [],
  "weaknesses": [],
  "improvement_suggestions": [],
  "resume_improvements": {{
    "missing_keywords": [],
    "summary_improvements": "",
    "quantifiable_metrics": [],
    "ats_optimization": []
  }}
}}

Resume:
{resume}

Job Description:
{jd}

Output ONLY JSON now.
"""
