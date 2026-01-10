import sympy
from sympy import symbols, solve, sympify, Eq, simplify
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
import re

transformations = (standard_transformations + (implicit_multiplication_application,))

def normalize_math_text(text: str) -> str:
    # Redundant normalization to be safe
    text = text.lower()
    replacements = {
        " plus ": "+", " minus ": "-", " times ": "*", " multiplied by ": "*",
        " divided by ": "/", " over ": "/", " equals to ": "=", " equals ": "=",
        " equal to ": "=", " is equal to ": "=", "=": "="
    }
    for word, symbol in replacements.items():
        text = text.replace(word, symbol)
    return text.strip()

def solve_linear_steps(lhs, rhs, variable):
    """
    Generates steps for simple linear equations like ax + b = c
    """
    steps = []
    # reformulate as ax + b = c -> ax = c - b -> x = (c-b)/a
    # This is a heuristic for display; real solving is done by sympy.
    try:
        # Move all to LHS: expression = 0
        expr = lhs - rhs
        # Poly form
        poly = expr.as_poly(variable)
        if poly and poly.degree() == 1:
            coeffs = poly.all_coeffs() # [a, const] -> ax + const = 0
            a = coeffs[0]
            b = coeffs[1]
            
            # Original: ax + b = 0  => ax = -b
            target = -b
            steps.append(f"Subtract {b} from both sides: {a}{variable} = {target}")
            
            # Divide
            res = target / a
            steps.append(f"Divide both sides by {a}: {variable} = {res}")
            return steps
    except:
        pass
    return []

def solver_agent(problem_text, retrieved_chunks):
    """
    Solve the math problem using SymPy.
    """
    steps = []
    
    # 1. Cleaning & Normalization
    cleaned_text = re.sub(r"\b(solve|find|calculate|determine|value|of|for|simplify)\b", "", problem_text, flags=re.IGNORECASE)
    cleaned_text = normalize_math_text(cleaned_text)
    cleaned_text = cleaned_text.replace("?", "")
    
    # 2. Variable Detection (Regex as requested + SymPy backup)
    # The parser likely handled this, but we double check for the context of this specific internal solve
    detected_vars = re.findall(r"[a-zA-Z]", cleaned_text)

    try:
        solution = None
        
        if "=" in cleaned_text:
            # FIX 3: Split Equation Before Simplifying
            lhs_str, rhs_str = cleaned_text.split("=", 1)
            
            # Parse with implicit multiplication
            lhs = parse_expr(lhs_str, transformations=transformations)
            rhs = parse_expr(rhs_str, transformations=transformations)
            
            steps.append(f"Equation: {sympy.latex(lhs)} = {sympy.latex(rhs)}")
            
            # Identify variable to solve for
            atoms = lhs.free_symbols.union(rhs.free_symbols)
            
            if not atoms:
                # Arithmetic check
                if simplify(lhs - rhs) == 0:
                    return {"solution": "True", "steps": ["LHS equals RHS."], "confidence": 1.0, "error": None}
                else:
                    return {"solution": "False", "steps": ["LHS does not equal RHS."], "confidence": 1.0, "error": None}

            target_var = list(atoms)[0] # Default to first found
            
            # Generate heuristic steps for linear case
            linear_steps = solve_linear_steps(lhs, rhs, target_var)
            if linear_steps:
                steps.extend(linear_steps)
            else:
                steps.append(f"Solving for {target_var}...")

            # Solve: lhs - rhs = 0
            solutions = solve(lhs - rhs, target_var, dict=True)
            
            if not solutions:
                solution = "No solution found"
            else:
                # Format output
                sol_list = []
                for s in solutions:
                    # s is a dict {x: 3}
                    val = list(s.values())[0]
                    sol_list.append(str(val))
                
                solution = ", ".join(sol_list)
                steps.append(f"Final Answer: {target_var} = {solution}")

        else:
            # Expression evaluation
            expr = parse_expr(cleaned_text, transformations=transformations)
            steps.append(f"Expression: {sympy.latex(expr)}")
            
            if not expr.free_symbols:
                solution = str(expr.evalf())
                steps.append(f"Use arithmetic to evaluate.")
            else:
                solution = str(sympy.simplify(expr))
                steps.append(f"Simplify terms.")
            
        return {
            "solution": solution,
            "steps": steps,
            "confidence": 1.0,
            "error": None
        }

    except Exception as e:
        return {
            "solution": None,
            "steps": [],
            "confidence": 0.0,
            "error": f"Math error: {str(e)}"
        }
