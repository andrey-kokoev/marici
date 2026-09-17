# Correction: Legendre Green recursion is geometric, not finitely terminating

The Legendre operator preserves polynomial degree; it does not lower it.
Therefore repeated application to a degree-999 polynomial does not generally
vanish. The earlier claim of literal finite termination was false.

The useful fact is instead spectral separation. On polynomials of degree at
most `d`, the Legendre operator has eigenvalues at most `d(d+1)`. For a target
Legendre mode `n>d`, every Green iteration contributes the ratio

\[
\rho_{d,n}=\frac{d(d+1)}{n(n+1)}<1.
\]

At `d=999`, `n>=5000`,

\[
\rho_{999,5000}<0.04.
\]

Thus the iterated bulk remainder is geometric. After `r` integrations its
norm is bounded by `rho^r` times the initial polynomial norm, while the
extracted boundary terms involve the first `r` Legendre-operator jets. A
finite certificate chooses `r` so that the geometric remainder fits the
residual budget and encloses only those finitely many jets.

This correction preserves the boundary-jet strategy but changes its logical
basis from finite termination to a quantitative geometric remainder.
