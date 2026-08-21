# The fifth quadrature weight blindly predicts multiplicity one

For the quarter-point moment measure, a zero of multiplicity `m` at compact
coordinate `u=(1/4+gamma^2)^(-1)` contributes atom mass `m u`. Therefore the
Gaussian quadrature mass `w_max` at the largest Jacobi node gives the blind
finite-rank estimator

\[
 \widehat m_1=\frac{w_{\max}}{u_{\max}}.
\]

At size five the source-derived compression gives

\[
 u_{\max}\approx0.00499898469251,\qquad
 w_{\max}\approx0.00499903813347,
\]

and hence

\[
 \boxed{\widehat m_1\approx1.00001069036}.
\]

No zero location or multiplicity enters construction. Thus the same five-node
quadrature that predicts the first spectral edge within a few millionths also
predicts a simple top atom within about `1.1e-5`.

This refines the earlier scalar multiplicity warning. A completed infinite
scalar measure can encode multiplicity through atom mass, but finite moments
do not create or certify an eigenspace dimension. The ratio above is a residue
estimate, not a proof that the first zero is simple.

## Scope

The quadrature-weight calculation is ordinary floating point and is not yet
interval-certified. It predicts spectral mass, not geometric eigenspace
multiplicity, and it does not prove simplicity or RH.

## Durable verification

- Checker: `checkers/quarter_point_blind_multiplicity.py`
- Result: `results/quarter-point-blind-multiplicity.json`

Christoffel interval evaluation subsequently certifies
`m_hat in [1.0000106856271,1.0000106950984]`. See
`quarter-point-multiplicity-interval-certificate.md`.
