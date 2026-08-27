# Asymmetric cubic lifting: WP697

## Hostile completion test

Perturb the WP696 symmetric source by

\[
\lambda_h=\lambda+\delta,
\qquad
\lambda_x=\lambda-\delta,
\]

while retaining equal vacuum norms and retuning the quadratic masses by
stationarity. The opposite-portal Hessians remain exactly isospectral for all
\(\delta\).

Nondegenerate eigenvector perturbation gives

\[
g_{HLL}^{(+)}
=\sqrt2v(3\lambda-p)+O(\delta^2),
\]

and

\[
g_{HLL}^{(-)}
=-\frac{\sqrt2v(3\lambda-p)}{2p}\delta
+O(\delta^2).
\]

Thus any generic nonzero quartic asymmetry lifts the negative-branch zero at
first order. The exact absence claim from WP695–WP696 is not completion-safe.

## What survives

The positive branch has no linear asymmetry correction, while the negative
branch is asymmetry-suppressed. The robust prediction near the symmetric slice
is therefore a rate hierarchy, not an exact forbidden decay.

This remains an identifier rather than a selector. The next gate is a
nonasymptotic finite-asymmetry margin, followed by the remaining flavor
orientation invariants, loops, widths, and calibrated detector response.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp697_asymmetric_cubic_lifting.py

Generated result: results/wp697_asymmetric_cubic_lifting.json.
