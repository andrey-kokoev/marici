# Robust dual-Jacobian margins (WP307)

## Source-side exactness

WP306's source gate requires zero response after admitted source redundancies
are removed. A nominally zero Jacobian is insufficient if uncertainty support
contains any nonzero completion. The exact hostile completion

\[
\Delta J_{\mathrm{src}}=
\begin{pmatrix}1/100&0\\0&0\end{pmatrix}
\]

has small norm but rank one. It destroys exact parameter-independent
prediction. Small response can support an approximate sensitivity statement,
not an exact numerical selector claim.

## Detector-side margin

For detector response, a positive singular-value gap is robust. If

\[
\sigma_{\min}(J_{\mathrm{det}})>\epsilon,
\]

then every additive perturbation of spectral norm at most $\epsilon$ remains
full rank. The checker uses nominal singular values $1,2$. At uncertainty
radius $1/2$, the guaranteed lower margin is $1/2$. At the boundary radius
1, an explicit perturbation makes the detector singular.

## Classification

The two gates have different robust forms:

- exact prediction requires a structural source-response zero throughout the
  admitted support;
- detector identification requires a positive smallest-singular-value margin
  exceeding calibrated uncertainty.

The next constructor must therefore prove the source zero rather than estimate
it, while the detector route must measure a quantitative margin and its support.

Run `uv run --with sympy python
research/flavor/checkers/wp307_robust_dual_jacobian_margins.py` to regenerate
the exact robustness audit.
