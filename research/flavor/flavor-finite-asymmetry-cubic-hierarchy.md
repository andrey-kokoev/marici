# Finite-asymmetry cubic hierarchy: WP698

## Exact mass-basis coordinate

Let \(t>0\) be the ratio of the two components of the normalized heavy radial
eigenvector. The quartic asymmetry and spectral splitting obey

\[
\frac{\delta}{p}=\frac{1-t^2}{2t},
\qquad
R=\sqrt{p^2+\delta^2}
=\frac{p(t^2+1)}{2t}.
\]

The exact branch cubics factor as

\[
g_{HLL}^{(+)}
=\frac{v(t+1)[6\lambda t-p(t^2+1)]}
{(t^2+1)^{3/2}},
\]

and

\[
g_{HLL}^{(-)}
=\frac{v(t-1)[6\lambda t-p(t^2+1)]}
{(t^2+1)^{3/2}}.
\]

Therefore

\[
\frac{g_{HLL}^{(-)}}{g_{HLL}^{(+)}}
=\frac{t-1}{t+1},
\qquad
\frac{\Gamma_-}{\Gamma_+}
=\left(\frac{t-1}{t+1}\right)^2.
\]

## Stable open-decay domain

The common spectrum is

\[
m_L^2=2v^2(\lambda-R),
\qquad
m_H^2=2v^2(\lambda+R).
\]

Strict stability and open heavy-to-two-light phase space require

\[
\frac{3\lambda}{5}<R<\lambda.
\]

Inside this domain the common cubic factor is strictly positive. For every
finite \(t>0\), the negative-branch rate is strictly below the positive-branch
rate. At \(t=1\), the symmetry-protected negative rate is zero. The hierarchy
approaches equality only in the singular orientation limits \(t\to0\) or
\(t\to\infty\).

## Classification

WP698 upgrades the perturbative WP697 result to a nonasymptotic
source-derived rate hierarchy over the full finite-asymmetry radial domain.
It identifies but does not select. Physical authority still requires a
covariant full-flavor embedding and a detector-level lower bound after widths,
loops, efficiencies, backgrounds, and uncertainty.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp698_finite_asymmetry_cubic_hierarchy.py

Generated result: results/wp698_finite_asymmetry_cubic_hierarchy.json.
