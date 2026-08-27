# Scalar Zero Exclusion Forces the Constructible Terminal Image to Have Rank at Most One

The first zero-state lift has been computed as a categorical pullback. If
`T_s:P_s -> W_s` is the source constructor and `q_s:W_s -> C` is the scalar
Evans readout, then the admissible zero object is

\[
Z_s=\ker(q_sT_s).
\]

Writing `S_s=im T_s`, scalar zero exclusion is equivalent to
`S_s intersect ker q_s` being zero. If `S_s` is a complex linear subspace,
this forces the scalar restriction `q_s|S_s` to be injective and hence

\[
\dim_{\mathbb C}S_s\leq1.
\]

Thus every pre-Evans source solution module of complex rank at least two
necessarily contains a nonzero scalar-null state. Adding a faithful terminal
observer cannot change this intersection; even the identity observer merely
detects the hostile vector `(1,-1)` killed by `q(x,y)=x+y`.

This closes the terminal-observability route and retypes the remaining RH gate.
The primitive, square, seam, and archimedean channels can contribute to
exclusion only by entering the source equations or boundary domain and reducing
the pre-Evans solution module to a distinguished ray or nonlinear transverse
locus. Their joint faithfulness as ports is insufficient.

The next finite calculation is therefore the complex rank of the doubled
theta-tail solution module after the complete source boundary conditions at
infinity but before the Evans endpoint condition.

Research packet:
`research/grothendieck/scalar-zero-exclusion-forces-the-constructible-terminal-image-to-have-rank-at-most-one.md`

Exact checker:
`research/grothendieck/checkers/check_constructible_terminal_rank_obstruction.py`

The checker passes 6/6 exact tests.
