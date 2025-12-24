from fastapi import Header, HTTPException

# Demo keys — replace later with Stripe-generated keys
API_KEYS = {
    "free-key-123": "free",
    "pro-key-456": "pro"
}

def authenticate(x_api_key: str = Header(...)):
    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API key")

    return API_KEYS[x_api_key]
