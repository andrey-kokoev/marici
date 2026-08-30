# The alternate-chart interior core is oscillatory

Companion to `checkers/magnetic_core_oscillation_checks.py` (6/6, exit 0) and
`results/magnetic_core_oscillation.json`.

Let (A_g) be the interior core obtained from the even row-(3) alternate
chart after removing the two reflected endpoint columns and target rows
(0,3).  Its dimension is

\[
\dim A_g=g+8.
\]

In the inherited Hall ordering, let

\[
\Delta_j(g)=\det A_g[1{:}j,1{:}j]
\]

be the (j)-th leading principal minor.  Exact fraction-free elimination for
every even (2\le g\le60) gives

\[
\boxed{\operatorname{sgn}\Delta_j(g)=(-1)^j}
\]

for all 1,170 tested leading minors.  No pivot exchange is required.
Equivalently, the ordinary Gaussian pivots

\[
p_j(g)=\frac{\Delta_j(g)}{\Delta_{j-1}(g)}
\]

are strictly negative.  Since (g+8) is even,

\[
\det A_g>0.
\]

This reveals the structural content hidden by the enormous raw determinant
ratios.  The core is behaving as an oscillatory/sign-regular matrix in its
source-derived Hall order.  Its invertibility should therefore follow from a
cone-preserving elimination theorem rather than from a closed product for the
unnormalized determinant.

The ordering is essential.  Swapping the first two observation rows creates
a zero first pivot and destroys strict oscillation.  Thus the sign law belongs
to the coherently transported orientation system, not to an arbitrary
coordinate ordering.

Combining this result with the endpoint Schur reduction gives

\[
\det M_{\mathrm{alt}}
=\pm\underbrace{\det A_g}_{\text{oscillatory core}}
\underbrace{(2g+7)(4)^{\overline g}}_{\text{fixed endpoint}}
\underbrace{\tau_g}_{\text{transverse response}}.
\]

Both nontrivial factors now have finite local transport descriptions:
oscillatory pivots for the core and a hypergeometric character for
(	au_g).

## Scope

The sign law is exact through even grade (60), not yet an all-grade proof.
The remaining symbolic task is to derive the negative-pivot property from the
banded path coefficients, ideally by showing that each fraction-free update
preserves the oriented cone.
