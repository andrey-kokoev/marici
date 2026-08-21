# Endpoint reduction leaves one coupled gamma--prime Pick inequality

Loewner positivity of `F` is equivalent to the Pick condition

\[
 \operatorname{Im}F(t)\ge0\qquad(\operatorname{Im}t>0).
\]

Choose the principal square root and put `s=1/2+sqrt(t)`. Since

\[
 S(t)=\frac{1}{2s-1}\frac{\Xi'}{\Xi}(s),\qquad
 F(t)=(4t-1)S(t),
\]

the completed logarithmic derivative gives

\[
 F(t)=\frac{4s(s-1)}{2s-1}
 \left[\frac1s+\frac1{s-1}-\frac12\log\pi
 +\frac12\psi(s/2)+\frac{\zeta'}{\zeta}(s)\right].
\]

The endpoint pair cancels exactly:

\[
 \frac{4s(s-1)}{2s-1}\left(\frac1s+\frac1{s-1}\right)=4.
\]

Therefore the universal RH-equivalent source target is the single coupled
inequality

\[
 \boxed{\operatorname{Im}\left\{
 \frac{4s(s-1)}{2s-1}
 \left[-\frac12\log\pi+rac12\psi(s/2)
 +\frac{\zeta'}{\zeta}(s)\right]\right\}\ge0}
\]

for the image of the upper `t` half-plane.

Neither gamma nor the Euler term has a fixed Pick sign separately. In the
absolute Euler half-plane the imaginary part of `zeta'/zeta` is an oscillatory
prime sine sum. Positivity, if true, is a completed coupling theorem after the
canonical endpoint reduction—not a sectorwise inequality.

Under nonnegative squared spectral coordinates,

\[
 F(t)=4\sum m_\lambda-sum_\lambda
 \frac{m_\lambda(1+4\lambda)}{t+\lambda}
\]

maps the upper half-plane to itself manifestly. Conversely, the Pick property
and known meromorphic pole structure force a positive real resolvent measure,
recovering the Loewner kernel and self-adjoint Jacobi operator.

## Attack options

1. Prove the boxed inequality directly using an integral representation that
   couples `psi` and `zeta'/zeta` before taking imaginary parts.
2. Construct it as the boundary value of the positive heat/reflection kernel
   already derived in the Gaussian lane.
3. Find one upper-half-plane point with negative imaginary part; this would
   falsify the proposed universal Pick theorem and hence the current RH route.

## Scope

The reduction is exact and the conditional spectral Pick representation is
proved. The boxed source inequality is not proved; RH remains open.

## Durable verification

- Checker: `checkers/reduced_source_pick_identity.py`
- Result: `results/reduced-source-pick-identity.json`

A first zero-free hostile grid scan finds no negative value, with minimum
sampled imaginary part about `7.34e-4`. This is numerical reconnaissance, not
a proof. See `reduced-source-pick-first-hostile-scan.md`.
