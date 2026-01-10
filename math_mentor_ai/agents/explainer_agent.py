def explainer_agent(problem_text, steps, solution):
    """
    Generates a natural language explanation of the solution steps.
    """
    if not steps:
        return "I couldn't find a solution effectively."

    explanation = [f"**Problem:** {problem_text}\n"]
    explanation.append("Here is the step-by-step logic:\n")

    for i, step in enumerate(steps):
        # Clean up step text if it's raw from tools
        clean_step = step.replace("Equation:", "").replace("Expression:", "").strip()
        explanation.append(f"{i+1}. {clean_step}")

    explanation.append(f"\n**Final Result:** The answer is {solution}.")
    
    return "\n".join(explanation)
