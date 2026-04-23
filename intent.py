def classify_intent(text: str):
    text = text.lower()

    if any(g in text for g in ["hi", "hello", "hey"]):
        return "greeting"

    if any(k in text for k in ["price", "pricing", "plan", "cost"]):
        return "product"

    if any(k in text for k in ["buy", "start", "sign up", "pro plan", "subscribe", "want"]):
        return "high_intent"

    return "product"