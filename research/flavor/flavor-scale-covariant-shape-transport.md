# Scale-covariant shape transport (WP256)

## Frozen test

Keep the WP251 object-coherent instrument unchanged and replace WP253's fixed
GeV bins only by the preregistered source-relative coordinate

\[
x=\frac{m_{\mathrm{vis}}}{M_{\mathrm{source}}},
\qquad
(0,1/3,1/2,2/3,5/6,1,\infty).
\]

The exact source-local parameter-set hash resolves in every file, all three
frozen trigger names are present, and no menu or name mismatch occurs. The
selected counts reproduce WP254 exactly. The dimensionless templates are

\[
S_{130}=(12,241,418,185,39,0),\quad
S_{140}=(4,123,163,87,12,0),\quad
S_{160}=(22,226,256,154,20,0).
\]

## Leave-one-out result

Predict the normalized 140 GeV shape by the same mass-linear weights used in
WP255:

\[
\widehat S_{140}=\frac23 S_{130}+\frac13 S_{160}.
\]

Exact closure still fails. The total-variation residual is

\[
\frac{12641608}{354073635}\simeq 0.03570.
\]

This is smaller than WP255's fixed-bin value
\(23108773/354073635\simeq0.06527\), with exact ratio
\(12641608/23108773\). Source-relative scaling therefore captures a real
finite-pilot trend, but it is not an exact transport law.

## Claim boundary

WP256 is a negative exact-closure result with a positive diagnostic: scaling
by the declared source mass improves interpolation, yet leaves nonzero bin
residuals. It neither supplies source authority for interpolation nor permits
transport to the 133.774 and 151.287 GeV physical poles. Direct samples at
those masses, or a source-derived uncertain response kernel validated under
weighted completion and correlated detector uncertainties, remain necessary.

Run `uv run --with sympy python
research/flavor/checkers/wp256_scale_covariant_shape_transport.py` for the
exact residual, comparison with WP255, and deliberate zero-residual failure.
