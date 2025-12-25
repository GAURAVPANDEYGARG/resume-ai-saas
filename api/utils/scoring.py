def calculate_match_score(data: dict) -> int:
    score = 0

    # -------- Skills (40%) --------
    total_skills = len(data["matched_skills"]) + len(data["missing_skills"])
    if total_skills > 0:
        score += int((len(data["matched_skills"]) / total_skills) * 40)

    # -------- Tools (25%) --------
    total_tools = len(data["matched_tools"]) + len(data["missing_tools"])
    if total_tools > 0:
        score += int((len(data["matched_tools"]) / total_tools) * 25)

    # -------- Experience (20%) --------
    experience_map = {
        "high": 20,
        "medium": 12,
        "low": 5
    }
    score += experience_map.get(data["experience_match"], 0)

    # -------- Keyword penalty (15%) --------
    missing_keywords = len(data["resume_improvements"]["missing_keywords"])
    score += max(0, 15 - (missing_keywords * 2))

    # -------- Hard penalties --------
    if data["experience_match"] == "low":
        score -= 10

    if len(data["missing_skills"]) > len(data["matched_skills"]):
        score -= 15

    return max(0, min(score, 100))
