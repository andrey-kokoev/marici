# Independent efficiency-control calibration: WP657

## Exact confounding

With separate channel efficiencies, the two normalized log yields have the
form

\[
r_L=2u+\eta_L,
\qquad
r_R=2v+\eta_R.
\]

If the two log-efficiencies are profiled without independent calibration, both
source-magnitude directions are erased. The profiled source information has
rank zero.

## Independent detector controls

Let two control samples measure \(\eta_L\) and \(\eta_R\) independently with
Fisher precisions \(\kappa_L\) and \(\kappa_R\). The profiled source
information becomes

\[
F_{\mathrm{src}}=
\operatorname{diag}
\left(
\frac{4\kappa_L}{1+\kappa_L},
\frac{4\kappa_R}{1+\kappa_R}
\right),
\]

with determinant

\[
\frac{16\kappa_L\kappa_R}
{(1+\kappa_L)(1+\kappa_R)}.
\]

Both strictly positive controls are necessary and sufficient for rank two.
If either precision vanishes, at least one magnitude remains unidentifiable.

## Authority boundary

The controls are detector-derived only when their support, transfer factors,
covariance, and uncertainties are bound independently of the target signal.
Fitting efficiencies from the desired signal answer would preserve the exact
confounding rather than repair it.

This calibrates identification and does not select source values.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp657_efficiency_control_calibration.py

Generated result: results/wp657_efficiency_control_calibration.json.
