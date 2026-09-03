# Quarter leading minors have finite Schur-positive expansions

## Question

Can Newton positivity be approached through an all-size Schur-positive representation rather than further minor-size sampling?

## Claim boundary

Cauchy–Binet gives the representation at every size, but nonnegativity of all coefficient minors has been exhaustively verified only through size seven.

## Disposition

Writing

\[
p_j(x)=\prod_{s\in\{1,5/4,3/2,7/4\}}(x+s)_j,
\]

Cauchy–Binet expands \(\det(p_j(x_i))/V(x)\) in Schur polynomials. Its coefficients are maximal minors of the monomial-coefficient matrix of the \(p_j\). Exact enumeration through size seven found no negative coefficient minor among 152,173 cases: 62,040 are positive and 90,133 vanish by degree support. A reversed degree order gives a negative control. This supplies a finite Schur-positive representation and identifies the all-size missing theorem as total nonnegativity of the nested coefficient matrix. The next executable leaf is `quarter-coefficient-matrix-planar-network`, testing whether the recursions \(p_{j+1}=p_j\prod_s(x+s+j)\) admit a positive planar-network factorization.
