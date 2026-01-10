
def intent_router(parsed_output: dict):
    """
    Decides which agent flow to trigger based on the structured parser output.
    Returns: "solve_math", "explain_only", or "chitchat" (future).
    """
    text = parsed_output["problem_text"] or ""
    text_lower = text.lower()
    
    # If the parser failed or input is empty
    if not text or parsed_output.get("is_ambiguous"):
        return "chitchat"

    # Detect if user just wants an explanation without solving
    # e.g. "Explain Pythagorean theorem" vs "Solve x^2+y^2=z^2"
    if "explain" in text_lower and "=" not in text_lower and not parsed_output["variables"]:
        return "explain_only"
        
    # Default to solving
    return "solve_math"
