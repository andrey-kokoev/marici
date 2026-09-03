# Gaussian heat Riesz family is bounded and total

## Question

Do the actual completed-heat Gaussian probes on logarithmic labels extend continuously to the order completion, and are they jointly faithful there?

## Claim boundary

Yes in the Hilbert norm. For every positive heat parameter, the Gaussian label evaluation is bounded, and the family over all positive parameters is total. This does not identify its source kernel with the completed Weil form or prove graph-norm density.

## Gaussian functional

For \(\tau>0\), define

\[
G_\tau(c)
=
\sum_i c_i
\exp\left(-\frac{\lambda_i^2}{4\tau}\right).
\]

For

\[
F_\tau(\lambda)
=
\exp\left(-\frac{\lambda^2}{4\tau}\right),
\]

the adjacent-gap dual norm is

\[
\lVert G_\tau\rVert_*^2
=
\sum_i
\frac{|F_\tau(\lambda_i)-F_\tau(\lambda_{i+1})|^2}
{2(\lambda_{i+1}-\lambda_i)}.
\]

Interval Cauchy--Schwarz gives

\[
\lVert G_\tau\rVert_*^2
\leq
\frac12
\int_{\lambda_0}^{\infty}
|F_\tau'(u)|^2du.
\]

For \(\lambda_0=0\), this becomes

\[
\lVert G_\tau\rVert_*^2
\leq
\frac{\sqrt{2\pi}}
{16\sqrt\tau}.
\]

Thus every completed-heat Gaussian evaluation has a Riesz vector \(g_\tau\in\mathcal H_{\rm ord}\).

## Totality

Under the cumulative-sum realization, summation by parts gives

\[
G_\tau(c)
=
-\frac1{\sqrt2}
\int_0^\infty
(Jc)(u)F_\tau'(u)du.
\]

If \(g\in\mathcal H_{\rm ord}\) is orthogonal to all Gaussian Riesz vectors, then

\[
\int_0^\infty
u g(u)e^{-a u^2}du
=0
\]

for every \(a>0\). With \(x=u^2\), this is the Laplace transform of \(g(\sqrt x)\), up to a constant factor. Laplace uniqueness gives \(g=0\) almost everywhere. Therefore

\[
\overline{
\operatorname{span}
\{g_\tau:\tau>0\}
}^{\lVert\cdot\rVert_{\rm ord}}
=
\mathcal H_{\rm ord}.
\]

## Correction of probe type

The earlier family

\[
\sum_i c_i e^{-t\lambda_i}
\]

is also bounded and total, but it is a Mellin-semigroup family. It must not be identified with the completed-heat Gaussian family above. Their parameters and source maps are different.

## Remaining comparison

The Gaussian observer family is now known to be jointly faithful in the source-positive order topology. What remains absent is the source-derived equality

\[
K(\tau,\sigma)
=
q_{\Gamma+P}(g_\tau,g_\sigma)
\]

with a jointly regularized polarized completed form. Similar dependence on \(\tau\) does not construct this equality.

## Disposition

`gaussian_heat_observer_hilbert_density` passes. `gaussian_jet_form_core` remains open at graph-norm density and completed-form action. The prior Mellin-versus-heat modality defect has been repaired and reported.

## Verification

- `research/voevodsky/checkers/check_gaussian_heat_riesz_family.py`
- `research/voevodsky/results/gaussian_heat_riesz_family.json`
