# Two-projector flavor lift (WP325)

## Minimal noncommuting extension

WP325 adds a second nonorthogonal rank-one relational projector (Q) to the
WP323 projector (P). The exact witness uses

\[
P=\operatorname{diag}(1,0,0),
\qquad
Q=\frac12
\begin{pmatrix}
1&1&0\\
1&1&0\\
0&0&0
\end{pmatrix}.
\]

The projectors do not commute. Fixed affine combinations in their span can
have three distinct eigenvalues, and two sector combinations can have a
nonzero Hermitian commutator. Thus a second projector genuinely escapes the
spectral-degeneracy obstruction of WP324.

## Residual obstruction

Both projectors annihilate ((0,0,1)^T). Every element of
\(\operatorname{span}\{I,P,Q\}\) therefore preserves that common line. Mixing
is confined to the complementary two-dimensional block. In the exact witness,

\[
\operatorname{Tr}\left([H_u,H_d]^3\right)=0
\]

despite nondegenerate spectra and a nonzero commutator.

The lift can produce two-family mixing but not generic three-family CP
violation. It reaches a proper stratum rather than the generic `physical16`
domain.

## Successor gate

A further independently derived covariant must break the common invariant
line. Its source, coefficients, stable matching, and CP-sensitive instrument
must be established before it can carry selector authority.

Run `uv run --with sympy python
research/flavor/checkers/wp325_two_projector_flavor_lift.py` to regenerate the
exact capability and no-go audit.
