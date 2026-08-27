# Correlation-forbidding symmetry tradeoff: WP706

## Candidate symmetry

The quartic ((n\mathbin\cdot m)^2) is invariant under the admitted diagonal
(SO(3)), triplet exchange, and independent sign flips. None of those source
symmetries forces its coefficient (lambda_c) to vanish.

An enlarged independent rotation group

\[
SO(3)_n\mathbin\times SO(3)_m
\]

does forbid the contraction: rotating (m=e_1) to (m=e_2) while holding
(n=e_1) fixed changes ((n\mathbin\cdot m)^2) from one to zero, while all
norm-only quartics remain unchanged.

## Cost to the faithful frame

The enlargement also removes the only angular potential in the WP649/WP661
frame constructor. For the exact norm potential

\[
V_0=(|n|^2-1)^2+(|m|^2-1)^2,
\]

the orthogonal point (n=e_1,m=e_2) has Hessian spectrum

\[
0,0,0,0,8,8.
\]

Only three zero modes belong to the admitted diagonal (SO(3)) orbit. The
fourth is a physical relative-angle modulus. Restoring
((n\mathbin\cdot m)^2) lifts it and gives the WP649 spectrum

\[
0,0,0,4,8,8.
\]

Thus the simple symmetry that protects the WP704 slice simultaneously removes
the presentation rigidifier that made the ordered two-triplet frame useful.

## Common-source obstruction

The faithful flavor words (J_n) and (J_m) act on the same quark flavor
space. A common quark or messenger contraction identifies the two rotation
frames and preserves only the diagonal subgroup. Once that interface is
admitted, ((n\mathbin\cdot m)^2) is symmetry-allowed and its vanishing is not
radiatively protected without an additional selection rule.

## Disposition

The currently obvious symmetry repair cannot make WP704 a genuine selector
while retaining WP649's faithful-frame rigidification. It trades the
infrared-repulsive coupling for a physical angular modulus, and the common
flavor interface breaks the protecting product symmetry.

This is not a theorem that every possible UV symmetry fails. A reopening must
exhibit a different symmetry or grading that forbids the correlation quartic,
allows both triplets to couple to one physical flavor space, lifts the relative
angle through a source-derived alternative, and remains closed under the full
RG and threshold grammar.

The smallest exact falsifier is the fourth Hessian zero mode of (V_0) modulo
the three-dimensional diagonal orbit.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp706_c_forbidding_symmetry_tradeoff.py

Generated result: results/wp706_c_forbidding_symmetry_tradeoff.json.
