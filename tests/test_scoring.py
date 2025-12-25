from api.utils.scoring import calculate_match_score
from tests.ats_test_cases import TEST_CASES

def test_ats_scoring():
    for case in TEST_CASES:
        data = {
            "matched_skills": case["matched_skills"],
            "missing_skills": case["missing_skills"],
            "matched_tools": case["matched_tools"],
            "missing_tools": case["missing_tools"],
            "experience_match": case["experience_match"],
            "resume_improvements": {
                "missing_keywords": case["missing_keywords"]
            }
        }

        score = calculate_match_score(data)
        low, high = case["expected_range"]

        assert low <= score <= high, (
            f"{case['name']} failed: got {score}, expected {low}-{high}"
        )

        print(f"✅ {case['name']} → {score}")
