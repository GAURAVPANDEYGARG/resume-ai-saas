def build_prompt(resume: str, jd: str) -> str:
    return f"""
You are an ATS (Applicant Tracking System) analyzer.

OBJECTIVE:
Extract ATS-relevant matching signals between the resume and job description.

OUTPUT RULES (CRITICAL):
- Output ONLY valid JSON
- No explanations
- No markdown
- No extra text

RETURN THIS SCHEMA EXACTLY:
{{
  "matched_skills": [],
  "missing_skills": [],
  "matched_tools": [],
  "missing_tools": [],
  "experience_match": "high | medium | low",
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

RULES:
- Use ONLY resume + job description
- Prefer exact keyword matches
- Do NOT infer or assume experience
- Be strict and realistic

RESUME:
{resume}

JOB DESCRIPTION:
{jd}

Return ONLY JSON.
"""
