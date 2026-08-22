# Analytic source differentiation removes the finite-difference gate

The central source slope `F'(t)` can be evaluated without a difference
stencil. Carry `eta(s)`, `eta'(s)`, and `eta''(s)` through the Euler transform,
and carry `digamma` with `trigamma`. Differentiating the exact reduced source
formula then gives `F'` directly, including the cancellation at
`s=1/2+sqrt(t)`.

At 80 and 90 decimal digits with Euler depths 120 and 132, the analytic method
reproduces all 21 positive boundary chord gaps. The minimum is
`3.64972e-20` on `[10^-8,10^-7]`; the maximum run discrepancy is
`1.84e-26`. This agrees with the corrected finite-difference evaluation far
beyond the digits relevant to the sign while eliminating its truncation error.

Twice differentiating the positive Laplace formula for each Euler difference
introduces `(log(t)-psi(s))^2-psi'(s)`. On `1/2<=s<=3/5`, a split at unit
Laplace time gives

\[
 |d_k''(s)|\le\frac{26}{k}+\frac4{k^2}+\frac2{k^3}.
\]

Thus the depth-120 eta-double-prime tail is below

\[
 2^{-120}\left(\frac{26}{120}+\frac4{120^2}+\frac2{120^3}\right),
\]

about `1.63e-37`. After the same factor-ten nonlinear allowance and hostile
boundary amplification, its budget is about `2.45e-21`, below the conservative
`3.4e-20` chord margin.

The analytic transform tails and differentiation are now budgeted. The sole
remaining implementation-level step for these 21 finite chords is outward-
rounded propagation of the complete nonlinear calculation. This is not yet a
global concavity theorem, an interval certificate, or an RH proof.

Directed nonlinear propagation is now complete and gives the positive
interval in `central-reciprocal-slope-interval-certificate.md`.

## Durable verification

- Analytic checker: `checkers/reduced_source_central_analytic_slope.py`
- Tail checker: `checkers/eta_second_derivative_euler_tail_bound.py`
- Results: `results/reduced-source-central-analytic-slope.json` and
  `results/eta-second-derivative-euler-tail-bound.json`
