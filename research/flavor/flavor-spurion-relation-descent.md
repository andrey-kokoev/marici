# The illustrative flavor-spurion relation is component data (WP65, move 6/12)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

The source sketches

\[
Y_{12}=(\chi_1+\chi_2)Y_{22}
\]

with scalar equal-magnitude (mathbb Z_8) vevs. An exact Yukawa matrix is
constructed satisfying this relation. A rational common-left weak-basis
rotation preserves its Gram spectrum and all audited polynomial invariants but
makes the same scalar component relation fail.

Therefore the equation partitions component presentations in a chosen
generation frame; it does not descend to `physical16`. It is a presentation
rigidifier, not a physical selector.

Descent could be repaired only by declaring the spurions' full flavor
representations and a covariant tensor contraction producing the Yukawa pair,
then quotienting the joint flavon-Yukawa vacuum orbit. The source explicitly
defers that theory and declares no instrument.

Smallest exact falsifier: one (3/5,4/5) common-left rotation, with zero
physical-invariant residual and nonzero component-relation residual.

Verification:
`uv run --with sympy python research/flavor/checkers/wp65_spurion_relation_descent.py`.
