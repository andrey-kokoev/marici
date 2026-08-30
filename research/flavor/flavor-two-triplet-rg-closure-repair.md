# Two-triplet RG-closure repair: WP661

## Defect

WP649's tree-level frame potential contains \((n\mathbin\cdot m)^2\) but omits
the separately allowed quartic \(|n|^2|m|^2\). The exact one-loop support
contraction is

\[
\operatorname{Tr}
\left[\operatorname{Hess}(n\mathbin\cdot m)^2\right]^2
=4|n|^4+4|m|^4+8|n|^2|m|^2+40(n\mathbin\cdot m)^2.
\]

The mixed norm term has nonzero coefficient and cannot consistently remain
absent. WP649 was a valid tree-level construction, not an RG-closed source
action.

## Minimal repair

The field-flip-even quartic support basis is

\[
|n|^4,\quad |m|^4,\quad |n|^2|m|^2,\quad (n\mathbin\cdot m)^2.
\]

At the exact repaired benchmark

\[
V=(|n|^2-1)^2+(|m|^2-1)^2+(n\mathbin\cdot m)^2+|n|^2|m|^2,
\]

the stationary vacuum remains orthogonal but shifts to

\[
|n|^2=|m|^2=\frac23.
\]

Its Hessian has exactly three orbit zeros and positive physical eigenvalues
\(8,8/3,8/3\). The ordered pair still has trivial \(SO(3)\) stabilizer.

## Corrected disposition

The faithful-frame conclusion survives minimal one-loop support closure.
WP649's unit normalization and physical Hessian values do not. Full source
authority still requires complete beta functions, an RG-preserved positive
stability chamber, and messenger-induced symmetry-breaking terms.

The selector verdict is unchanged: closure repairs the rigidifier and selects
no scalar sector coefficient.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp661_two_triplet_rg_closure_repair.py

Generated result: results/wp661_two_triplet_rg_closure_repair.json.
