# The Moving Theta Frontier Has Exactly Zero Continuum Mass

## Frontier rescaling

The reflected completed source is

\[
\Phi(-u)
=
\sum_{n\geq1}n^{-1/2}\phi_1(\log n-u).
\]

Introduce the moving coordinate

\[
\rho=ne^{-u}.
\]

Using the explicit primitive profile gives

\[
n^{-1/2}\phi_1(\log n-u)
=
2\pi e^{-u/2}
F(\rho),
\]

where

\[
F(\rho)
=
\rho^2(2\pi\rho^2-3)e^{-\pi\rho^2}.
\]

Therefore

\[
\Phi(-u)
=
2\pi e^{-u/2}
\sum_{n\geq1}F(ne^{-u}).
\]

## Exact continuum cancellation

The signed frontier profile has zero total mass:

\[
\int_0^\infty F(\rho)\,d\rho=0.
\]

Indeed,

\[
\int_0^\infty \rho^2e^{-\pi\rho^2}\,d\rho
=
\frac1{4\pi},
\]

and

\[
\int_0^\infty \rho^4e^{-\pi\rho^2}\,d\rho
=
\frac3{8\pi^2}.
\]

Hence

\[
2\pi\frac3{8\pi^2}
-
3\frac1{4\pi}
=
0.
\]

## Meaning of the cancellation

The large-\(u\) reflected source is a fine Riemann sum with mesh \(e^{-u}\).
Its naive continuum contribution would have size \(e^{u/2}\), but that entire
bulk term cancels because \(F\) has zero mass.

What survives is not continuum bulk. It is the arithmetic discrepancy between
the lattice sum and its zero integral:

\[
\sum_{n\geq1}F(ne^{-u})
-
e^u\int_0^\infty F(\rho)\,d\rho
=
\sum_{n\geq1}F(ne^{-u}).
\]

This is the natural entry point for Poisson sewing. The completed positive tail
is a lattice-discrepancy phenomenon after exact signed continuum cancellation.

## Why finite cutoffs fail

A fixed cutoff samples only the negative small-\(\rho\) lobe once \(u\) is
large. The positive lobe near the moving scale \(n\asymp e^u\) is omitted.
The infinite label tower is required not merely for convergence but to realize
the zero-mass cancellation across both lobes of \(F\).

## Explanatory compression

Three earlier observations are now one mechanism:

- every finite invariant cutoff becomes negative;
- compensating labels move with \(\log n\approx u\);
- the full source remains tiny, positive, and even.

They occur because the moving frontier has a signed zero-mass continuum limit,
and modular arithmetic controls the residual lattice discrepancy.

## Scope boundary

Zero continuum mass does not determine the sign of the lattice discrepancy.
The RH-bearing theorem must still explain the orientation of the Poisson-dual
residual under oscillatory Mellin transport.

## Falsifier

The reduction fails if either the rescaled profile is incorrect or its integral
is nonzero. Both are decided by the displayed elementary calculation.
