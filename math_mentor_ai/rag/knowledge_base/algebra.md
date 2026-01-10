# algebra.md

## Linear Equations
- Single variable: \( ax + b = 0 \), solution \( x = -\frac{b}{a} \) (\( a \neq 0 \))
- Systems (2 eq): Substitution or elimination method
- Matrix form: \( A\vec{x} = \vec{b} \), unique sol if det(A) ≠ 0
- Cases: Unique solution, infinite solutions (dependent), no solution (inconsistent)
- Domain constraints: Coefficient matrix invertible
- Common errors: Sign errors in elimination; division by zero
- Template: \( 2x + 3y = 5 \), \( 4x - y = 3 \)

## Quadratic Equations
- Standard form: \( ax^2 + bx + c = 0 \) (\( a \neq 0 \))
- Discriminant: \( D = b^2 - 4ac \)
  | D Value | Roots |
  |---------|-------|
  | > 0     | 2 distinct real |
  | = 0     | 1 real (repeated) |
  | < 0     | 0 real, 2 complex |
- Quadratic formula: \( x = \frac{-b \pm \sqrt{D}}{2a} \)
- Sum of roots: \( -b/a \), product: \( c/a \)
- Vertex: \( x = -\frac{b}{2a} \)
- Common errors: Forgetting factor 2a; sign errors in ±√D

## Polynomials
- Factor Theorem: If f(r) = 0 then (x-r) is a factor
- Remainder Theorem: f(a) = remainder when divided by (x-a)
- Rational Root Theorem: Possible roots ±(factors numerator)/(factors denominator)
- Synthetic division for root testing
- Quadratic factors using discriminant method
- Domain: All real coefficients
- Common errors: Sign errors in synthetic division

## Identities
| Identity | Formula |
|----------|---------|
| Square | \( (a \pm b)^2 = a^2 \pm 2ab + b^2 \) |
| Difference squares | \( a^2 - b^2 = (a+b)(a-b) \) |
| Cubes | \( a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2) \) |
| Sum cubes | \( (a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3 \) |
| Triple square | \( (a+b+c)^2 = a^2+b^2+c^2 + 2ab+2bc+2ca \) |

- Verification: Expand both sides
- Domain: All real numbers

## Inequalities
- Linear: \( ax + b > 0 \), solution \( x > -\frac{b}{a} \) (flip sign if a < 0)
- Quadratic: Find roots, test sign in intervals
  - a > 0: Outside roots (>0), between roots (<0)
  - a < 0: Opposite direction
- Rational inequalities: Critical points (zeros + asymptotes), sign chart
- AM-GM: \( \frac{x_1 + \dots + x_n}{n} \geq \sqrt[n]{x_1 \dots x_n} \)
- Domain constraints: Consider denominator zeros
- Common errors: Forgetting to flip inequality; incorrect test intervals

## Sequences & Series
### Arithmetic Progression (AP)
- nth 
