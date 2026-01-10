# linear_algebra.md

## Vectors
- Vector in ℝ²: \( \vec{v} = (v_1, v_2) \)
- Addition: \( \vec{u} + \vec{v} = (u_1 + v_1, u_2 + v_2) \)
- Scalar multiplication: \( c\vec{v} = (cv_1, cv_2) \)
- Zero vector: \( \vec{0} = (0,0) \)
- Linear combination: \( c_1\vec{v_1} + c_2\vec{v_2} \)
- Domain: Real components
- Common errors: Direction vs magnitude confusion

## Dot Product
- \( \vec{u} \cdot \vec{v} = u_1v_1 + u_2v_2 \)
- Magnitude: \( |\vec{v}| = \sqrt{\vec{v} \cdot \vec{v}} = \sqrt{v_1^2 + v_2^2} \)
- Properties: Commutative, distributive
- Orthogonal: \( \vec{u} \cdot \vec{v} = 0 \)
- Projection: \( \text{proj}_{\vec{u}}\vec{v} = \frac{\vec{u} \cdot \vec{v}}{|\vec{u}|^2} \vec{u} \)
- Angle: \( \cos\theta = \frac{\vec{u} \cdot \vec{v}}{|\vec{u}| |\vec{v}|} \)
- Common errors: Mixing dot vs cross product notation

## Matrices
- 2×2 matrix: \( A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \)
- Addition: Element-wise, same dimensions
- Scalar multiplication: Each element × scalar
- Matrix multiplication: \( (AB)_{ij} = \sum_k a_{ik}b_{kj} \)
- Dimensions: Columns A = rows B for multiplication
- Properties: Associative, distributive, NOT commutative (AB ≠ BA)
- Identity: \( I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \)
- Common errors: Row-column order in multiplication

## Determinant (2×2)
- \( \det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc \)
- Singular: det A = 0 (no inverse, dependent rows/columns)
- Properties: 
  - det(kA) = k² det A
  - det(AB) = det A · det B
  - Row swap: det → -det
- Domain: Square matrices only
- Common errors: Sign errors (bc vs cb)

## Inverse (2×2)
- Exists if det A ≠ 0
- Formula: \( A^{-1} = \frac{1}{\det A} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} \)
- Verification: \( A A^{-1} = I \)
- Properties: \( (A^{-1})^{-1} = A \), \( (AB)^{-1} = B^{-1}A^{-1} \)
- Domain constraints: det A ≠ 0
- Common errors: Wrong sign pattern; divide by zero

## Systems of Equations
- 2×2 system: \( A\vec{x} = \vec{b} \), solution \( \vec{x} = A^{-1}\vec{b} \)
- Three cases:
  | det A | Solution |
  |-------|----------|
  | ≠ 0   | Unique   |
  | = 0   | None or infinite |
- Cramer's Rule: \( x = \frac{\det\begin{pmatrix} b_1 & a_{12} \\ b_2 & a_{22} \end{pmatrix}}{\det A} \)
- Gaussian elimination: Row operations to RREF
- Common errors: Inconsistent signs; dependent equations missed
