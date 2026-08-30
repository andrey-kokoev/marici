# 1752 — The Local Nodal Germ Cannot Determine the Two-Bit Cusp Extension

## Local-versus-global test

The local nodal anticanonical model determines:

- one vanishing cycle;
- the width-two monodromy of Entry 1147;
- a local Lefschetz thimble bounding that cycle.

It does not determine a global integral lift of that thimble through the
primitive infinity-Gysin sequence.

Write

\[
\mathcal A_{--}
=\mathbb Z\langle e_6,v_{\rm alg}\rangle.
\]

The four globally possible nearby lattices have presentations

\[
\boxed{
2m=a e_6+bv_{\rm alg},
\qquad (a,b)\in(\mathbb Z/2)^2.
}
\]

A different global lift

\[
m\longmapsto m+k_1e_6+k_2v_{\rm alg}
\]

changes the integral coefficients by

\[
(a,b)\longmapsto(a+2k_1,b+2k_2)
\]

and therefore preserves the parity vector. All four vectors have the same
local nodal boundary and width-two elliptic monodromy.

The presentation has Smith torsion \(\mathbb Z/2\) for \((a,b)=(0,0)\).
For each nonzero parity vector the relation is primitive and the total
coinvariant group is free. The local germ distinguishes none of these cases.

## Narrow result

\[
\boxed{
\text{Local Picard--Lefschetz data fixes the width two but not the
global }(\mathbb Z/2)^2\text{ extension.}
}
\]

Thus the finite calculation requested after Entry 1751 cannot be completed
from a formal/analytic nodal normal form alone. It requires a globally
marked integral thimble in the actual degree-two del Pezzo family, together
with its coordinates in the primitive Gysin lattice.

This is a global coefficient-marking requirement, not a new carrier
incidence.

## Durable artifacts

- research/benincasa/checkers/local_pl_parity_ambiguity.rs
- research/benincasa/results/local-pl-parity-ambiguity.json
- research/benincasa/local-pl-parity-ambiguity.md

## Next falsifier

Construct the global anticanonical pencil map of the frozen compactified
surface. Transport one source-labelled vanishing path from a smooth fiber to
the total-energy nodal fiber and intersect its thimble with two integral
algebraic cycles generating \(\mathcal A_{--}\). Their parities determine
\((a,b)\) without choosing a rational master-basis splitting.
