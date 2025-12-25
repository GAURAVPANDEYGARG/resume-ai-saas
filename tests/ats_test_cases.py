TEST_CASES = [
    {
        "name": "Perfect Match",
        "matched_skills": ["Java", "Spring Boot", "REST", "Microservices"],
        "missing_skills": [],
        "matched_tools": ["Docker", "Jenkins"],
        "missing_tools": [],
        "experience_match": "high",
        "missing_keywords": [],
        "expected_range": (85, 95)
    },
    {
        "name": "Partial Match",
        "matched_skills": ["Java"],
        "missing_skills": ["Spring Boot", "Microservices"],
        "matched_tools": ["Git"],
        "missing_tools": ["Docker", "Jenkins"],
        "experience_match": "medium",
        "missing_keywords": ["REST", "CI/CD"],
        "expected_range": (55, 70)
    },
    {
        "name": "Weak Match",
        "matched_skills": ["HTML"],
        "missing_skills": ["Java", "Spring Boot"],
        "matched_tools": [],
        "missing_tools": ["Docker"],
        "experience_match": "low",
        "missing_keywords": ["API", "Backend"],
        "expected_range": (30, 45)
    }
]
