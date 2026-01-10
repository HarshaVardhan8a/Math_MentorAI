import re

SUPPORTED_TOPICS = {
    "algebra": ["solve", "equation", "value of", "roots", "find x", "calculate"],
    "probability": ["probability", "chance", "likelihood", "odds"],
    "calculus": ["derivative", "limit", "integral", "rate of change"],
    "linear_algebra": ["matrix", "determinant", "vector"],
    "arithmetic": ["add", "subtract", "multiply", "divide", "compute"]
}


def normalize_math_text(text: str) -> str:
    """
    Converts natural language math to symbolic math.
    e.g. "2x plus 5 equals 11" -> "2x + 5 = 11"
    """
    text = text.lower()
    
    replacements = {
        " plus ": "+",
        " minus ": "-",
        " times ": "*",
        " multiplied by ": "*",
        " divided by ": "/",
        " over ": "/",
        " equals to ": "=",
        " equals ": "=",
        " equal to ": "=",
        " is equal to ": "=",
        "=": "=" 
    }
    
    for word, symbol in replacements.items():
        text = text.replace(word, symbol)
        
    return text.strip()

def detect_topic(problem_text: str):
    text = problem_text.lower()
    
    # Explicit keyword search
    for topic, keywords in SUPPORTED_TOPICS.items():
        for kw in keywords:
            if kw in text:
                return topic

    # Implicit detection
    if "=" in text:
        return "linear_equation"  # More specific than algebra
    
    vars = extract_variables(text)
    if vars:
        return "algebra"
    
    if len(re.findall(r"[0-9]+", text)) > 0:
        return "arithmetic"

    return "general_math"


def extract_variables(text: str):
    """
    Extract math variables like x, y, z from expressions.
    """
    # Remove common instruction words first
    cleaned_text = re.sub(
        r"\b(solve|find|calculate|determine|value|of|the|for)\b",
        "",
        text,
        flags=re.IGNORECASE
    )

    # Match single letters that look like variables
    # Exclude i, e if you want, but for now allow them as they are common vars
    matches = re.findall(r"[a-zA-Z]", cleaned_text)
    
    # Filter out matches that are part of remaining words if any (though regex above is strict on chars)
    # Better: re.findall(r"\b[a-zA-Z]\b", cleaned_text) might be too strict if "2x" -> "x" is not space separated?
    # "2x" -> x is NOT \b[a-zA-Z]\b. 
    # Current regex [a-zA-Z] matches every letter. "plus" -> p,l,u,s. 
    # WE MUST RUN THIS ON NORMALIZED TEXT (where words are gone) OR be smarter.
    
    # User suggestion: re.findall(r"[a-zA-Z]", equation)
    # This implies we should run it ON THE EQUATION (content), not instructions.
    
    unique_vars = sorted(list(set(matches)))
    return unique_vars


def parser_agent(raw_text: str):
    """
    Converts cleaned input text into structured problem format
    """
    if not raw_text or len(raw_text.strip()) < 2:
        return {
            "problem_text": None,
            "topic": None,
            "variables": [],
            "constraints": [],
            "is_ambiguous": True,
            "needs_clarification": True,
            "clarification_question": "The input is too short. Please provide a math problem."
        }

    # 1. Normalize first
    clean_text = normalize_math_text(raw_text)
    
    # 2. Extract variables from the normalized text (where "plus" is "+")
    # This prevents "plus" -> p,l,u,s
    variables = extract_variables(clean_text)
    
    # 3. Detect topic
    topic = detect_topic(clean_text)

    is_ambiguous = False
    clarification_question = None

    if topic == "general_math" and not variables and not re.search(r"\d", clean_text):
        is_ambiguous = True
        clarification_question = "I couldn't detect a math problem. Could you rephrase?"

    return {
        "problem_text": clean_text, # Return normalized text!
        "topic": topic,
        "variables": variables,
        "constraints": [],
        "is_ambiguous": is_ambiguous,
        "needs_clarification": is_ambiguous,
        "clarification_question": clarification_question
    }
