# Relational generation spurion (WP322)

## Reference construction

Introduce a nondegenerate Hermitian source object (X) and transform the pair
((X,B)) simultaneously under the generation basis group. On the diagonal
binary domain, the mixed moments

\[
\operatorname{Tr}B,
\qquad
\operatorname{Tr}(XB),
\qquad
\operatorname{Tr}(X^2B)
\]

form a Vandermonde system. For (X=\operatorname{diag}(1,2,3)), its determinant
is 2, so the three occupancies are reconstructed exactly.

## Typing

With (X) proportional to the identity, the moment tower sees only Hamming
weight and has four classes. A nondegenerate (X) separates all eight labelled
words. This repairs readout faithfulness by adding relational structure.

It does not reveal absolute labels of the original experiment. The physical
object is now the pair ((X,B)), and choosing the diagonal representative of
(X) leaves only its stabilizer groupoid. The reference eigenvalues supply the
ordering data.

## Selector disposition

The reference is a relational rigidifier and, on the declared binary domain, a
faithful readout. It does not select an occupancy, a flux magnitude, or a
`physical16` point. Even a physical realization of (X) leaves the separate
cardinality-to-charge and charge-selection arrows missing.

Run `uv run --with sympy python
research/flavor/checkers/wp322_relational_generation_spurion.py` to regenerate
the exact audit.
