def get_text_input(user_text: str):
    """
    Handles plain text math input
    """
    if not user_text or user_text.strip() == "":
        return {
            "text": None,
            "confidence": 0.0
        }

    return {
        "text": user_text.strip(),
        "confidence": 1.0
    }
