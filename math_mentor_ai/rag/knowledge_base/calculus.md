# calculus.md

## Limits
- Definition: \( \lim_{x \to a} f(x) = L \) if ∀ε>0 ∃δ>0 s.t. 0<|x-a|<δ ⇒ |f(x)-L|<ε
- Basic rules:
  | Rule | Formula |
  |------|---------|
  | Constant | \( \lim c = c \) |
  | Sum | \( \lim(f+g) = \lim f + \lim g \) |
  | Product | \( \lim(fg) = (\lim f)(\lim g) \) |
  | Quotient | \( \lim\frac{f}{g} = \frac{\lim f}{\lim g} \) (lim g ≠ 0) |
  | Power | \( \lim x^n = a^n \) |
- One-sided: \( x \to a^- \) (left), \( x \to a^+ \) (right)
- Indeterminate \( \frac{0}{0} \): Factor, rationalize, L'Hôpital (deriv num/den)
- Domain: Where f defined except possibly at a
- Common errors: Cancel before limit exists; ignore one-sided limits
- Standard: \( \lim_{x\to0} \frac{\sin x}{x} = 1 \)

## Derivatives
- Definition: \( f'(a) = \lim_{h\to0} \frac{f(a+h)-f(a)}{h} \)
- Basic rules:
  | Function | Derivative |
  |----------|------------|
  | Constant c | 0 |
  | \( x^n \) | \( n x^{n-1} \) |
  | \( e^x \) | \( e^x \) |
  | \( \sin x \) | \( \cos x \) |
  | \( \cos x \) | \( -\sin x \) |
  | \( \ln x \) | \( 1/x \) (x>0) |
- Advanced:
  | Rule | Formula |
  |------|---------|
  | Product | \( (fg)' = f'g + fg' \) |
  | Quotient | \( (f/g)' = \frac{f'g - fg'}{g^2} \) |
  | Chain | \( [f(g(x))]' = f'(g(x)) \cdot g'(x) \) |
- Implicit: Differentiate both sides w.r.t. x
- Domain: Where f differentiable (continuous + no sharp corners)
- Common errors: Forgetting chain rule; quotient denominator

## Optimization
- Critical points: Solve \( f'(x) = 0 \) or undefined
- First derivative test: Sign change left/right of critical point
- Second derivative test: \( f''(x) > 0 \) local min, \( f''(x) < 0 \) local max
- Global extrema: Evaluate f at critical points + endpoints (closed interval)
- Template:
  1. Domain [a,b]
  2. f'(x)=0 → critical points
  3. f'' test or endpoint comparison
- Common errors: Missing endpoints; wrong domain
- Word problems: Translate to f(x), apply above

## Integrals
### Indefinite (Antiderivatives)
- \( \int f(x) \, dx = F(x) + C \) where \( F'(x) = f(x) \)
- Basic forms:
  | Integral | Antiderivative |
  |----------|----------------|
  | \( \int x^n \, dx \) | \( \frac{x^{n+1}}{n+1} + C \) (n ≠ -1) |
  | \( \int e^x \, dx \) | \( e^x + C \) |
  | \( \int \frac{1}{x} \, dx \) | \( \ln|x| + C \) |
  | \( \int \sin x \, dx \) | \( -\cos x + C \) |
  | \( \int \cos x \, dx \) | \( \sin x + C \) |

### Definite
- Fundamental Theorem: \( \int_a^b f(x) \, dx = F(b) - F(a) \)
- Properties: \( \int_a^a = 0 \), \( \int_a^b = -\int_b^a \)
- Area: \( \int_a^b |f(x)| \, dx \) for total area
- Common errors: Forgetting +C (indefinite only); limit swap sign change

## Continuity
- Continuous at a: \( \lim_{x\to a} f(x) = f(a) \)
- Three parts must hold: lim exists, equals f(a), f(a) defined
- Types of discontinuity:
  | Type | Characteristics |
  |------|-----------------|
  | Removable | lim exists ≠ f(a) or f(a) undefined |
  | Jump | left limit ≠ right limit |
  | Infinite | vertical asymptote |
- Continuous functions: Polynomials, rationals (den≠0), exp, trig, compositions
- Intermediate Value Theorem: Continuous [a,b] takes every value between f(a),f(b)
- Domain constraints: Check piecewise definitions
- Common errors: Piecewise one-sided limits; removable vs jump confusion
