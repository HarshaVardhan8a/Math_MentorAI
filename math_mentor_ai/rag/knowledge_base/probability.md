# probability.md

## Classical Probability
- Finite sample space with equally likely outcomes
- \( P(A) = \frac{\# \text{favorable outcomes}}{\# \text{total outcomes}} \)
- Domain: Discrete uniform probability space
- Assumptions: Each outcome equally likely
- Common errors: 
  - Non-uniform outcomes
  - Continuous distributions
- Example template: Single die → 6 outcomes

## Conditional Probability
- \( P(A|B) = \frac{P(A \cap B)}{P(B)} \), requires \( P(B) > 0 \)
- Independence: \( P(A \cap B) = P(A)P(B) \)
- Multiplication rule: \( P(A \cap B) = P(A)P(B|A) \)
- Domain constraints: Events A, B with P(B)≠0
- Common pitfalls:
  - Assuming independence
  - Division by zero when P(B)=0

## Bayes' Theorem
- \( P(A|B) = \frac{P(B|A)P(A)}{P(B)} \)
- Total probability: \( P(B) = \sum P(B|A_i)P(A_i) \) for partition \{A_i\}
- Domain: P(B)>0; prior probabilities sum to 1
- Key insight: Updates beliefs with evidence
- Common errors:
  - Ignoring low priors (false positives)
  - Forgetting partition in denominator

## Permutations & Combinations
| Concept | Formula | Order Matters? |
|---------|---------|----------------|
| Permutations \( P(n,r) \) | \( \frac{n!}{(n-r)!} \) | Yes |
| Combinations \( C(n,r) \) | \( \frac{n!}{r!(n-r)!} \) | No |
| Factorial | \( n! = n(n-1)\cdots1 \) | - |

- Domain: \( n \geq r \geq 0 \), integers
- With repetition: \( n^r \) (perm), \( C(n+r-1,r) \) (comb)
- Common mistakes:
  - \( r > n \) gives 0
  - Forgetting divide by r! for combinations

## Binomial Probability
- n independent trials, success probability p
- \( P(X = k) = \binom{n}{k} p^k (1-p)^{n-k} \)
- Mean: \( \mu = np \)
- Variance: \( \sigma^2 = np(1-p) \)
- Domain: \( 0 \leq p \leq 1 \), n positive integer
- Validity requires independence between trials
- Common errors:
  - Using for dependent events
  - Normal approximation for small n
