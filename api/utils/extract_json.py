import json
import re

def extract_json(text: str) -> dict:
    """
    Extracts valid JSON from LLM response.
    """

    match = re.search(r"\{.*\}", text, re.S)
    if not match:
        raise ValueError("No JSON found in LLM response")

    return json.loads(match.group())
