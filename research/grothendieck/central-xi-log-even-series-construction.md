# The reflection-even Xi series removes derivative noise at the boundary

Expand the completed logarithmic derivative at `q=s-1/2=0`. Reflection makes
it odd:

\[
 \frac{\Xi'}{\Xi}(1/2+q)=\sum_{n\ge0}c_{2n+1}q^{2n+1}.
\]

Since `t=q^2` and `Xi'/Xi=2q ell'(t)`, the cancellation-free coefficients are

\[
 \ell'(t)=\frac12\sum_{n\ge0}c_{2n+1}t^n.
\]

A 100-digit order-13 `q` jet with Euler depth 300 constructs `ell'` through
degree five. Its even-parity residual is about `1.46e-36`, at the gamma
asymptotic truncation scale. Forming `F=(4t-1)ell'` and
`H=(F')^(-1/2)` gives

\[
 H''(0)\approx-3.6043843454\times10^{-5},\qquad
 H'''(0)\approx4.4659254461\times10^{-7}.
\]

Evaluating this `t` series at `10^-8`, `2*10^-8`, and `3*10^-8` lands inside
the independently directed point intervals for `H`. This back-substitution
selects the even series over earlier high-order point differentiation.

The prior finite-difference and unreduced point-jet values `H'''~3.8` were
derivative/cancellation artifacts and are retracted. Near the boundary the
series value is about seven orders smaller. The first-cell oscillation is of
order `9e-15`, not `8e-8`, before rigorous series-remainder propagation.

This is still a scalar high-precision series rather than a directed Taylor
model. The next step is to interval-enclose its coefficients and remainder.
It does not prove continuum concavity or RH.

That coefficient enclosure is now complete: the directed centered jet passes
reflection parity and certifies both `H''(0)<0` and `H'''(0)>0`. See
`central-xi-log-boundary-jet-interval-certificate.md`.

## Durable verification

- Checker: `checkers/central_xi_log_even_series.py`
- Result: `results/central-xi-log-even-series.json`
