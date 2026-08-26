# Zero-bias chart completion (WP333)

## Boundary chart

WP332's logarithmic chart excludes (epsilon=0), but the underlying WP331
instrument does not lose sensitivity there. Use the nonlogarithmic coordinates

\[
x=-\log A=\beta\Delta,
\qquad
C=\kappa c_0,
\qquad
L=2\beta\epsilon c_0.
\]

At zero bias the response Jacobian has determinant

\[
-2\beta c_0\Delta\kappa,
\]

which is nonzero on the admitted positive support. Its squared singular values
are

\[
\Delta^2,
\qquad
\kappa^2,
\qquad
4\beta^2c_0^2.
\]

The signed bias is reconstructed continuously through zero:

\[
\epsilon=\frac{L\Delta\kappa}{2xC}.
\]

## Robustness and units

At the boundary, an additive Jacobian perturbation smaller than the least of
(\Delta), (kappa), and (2\beta c_0) preserves full rank. These quantities
cannot be compared until a calibrated detector metric and common units are
declared. The formula is therefore a typed margin contract, not a free
dimensionful norm comparison.

Finite-sample inference near (L=0) also requires an uncertainty model for the
branch frequency. Exact local identifiability does not imply arbitrarily sharp
statistical resolution.

Run `uv run --with sympy python
research/flavor/checkers/wp333_zero_bias_chart_completion.py` to regenerate the
exact boundary audit.
