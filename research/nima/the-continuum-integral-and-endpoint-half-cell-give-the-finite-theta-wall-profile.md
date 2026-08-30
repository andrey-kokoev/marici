# The continuum integral and endpoint half-cell give the canonical finite theta-wall profile

## One-grade cutoff

For \(r>-1\), define

\[
S_{r,N}(u)
=
e^{ru}
\sum_{n=1}^{N}
n^re^{-\pi n^2e^{2u}}.
\]

Its continuum label integral is

\[
I_{r,N}(u)
=
e^{ru}
\int_0^N
x^re^{-\pi x^2e^{2u}}\,dx.
\]

With \(t=xe^u\),

\[
I_{r,N}(u)
=
e^{-u}
\int_0^{Ne^u}
t^re^{-\pi t^2}\,dt.
\]

This is exactly the moving \(O(N)\) wall profile found by scaling. It is not a
fitted counterterm.

## Endpoint half-cell

Euler--Maclaurin also supplies the upper endpoint contribution

\[
E_{r,N}(u)
=
\frac12
N^re^{ru}e^{-\pi N^2e^{2u}}.
\]

In the moving coordinate \(u=v-\log N\),

\[
I_{r,N}(v-\log N)
=
N e^{-v}
\int_0^{e^v}
t^re^{-\pi t^2}\,dt,
\]

while

\[
E_{r,N}(v-\log N)
=
\frac12
e^{rv}e^{-\pi e^{2v}}.
\]

Thus:

- \(I_{r,N}\) cancels the order-\(N\) moving wall;
- \(E_{r,N}\) cancels the order-one trapezoidal edge left at the sharp label
  boundary.

The next Euler--Maclaurin term contains a label derivative at \(N\), which is
\(O(N^{-1})\) in the moving chart.

## Four-grade wall packet

For the prime packet, define

\[
W_{p,N}^{\mathrm{wall}}(u)
=
\sum_{j=0}^{3}
c_{j,p}
\left(
I_{r_j,N}(u)+E_{r_j,N}(u)
\right),
\qquad
r_j=j+\frac12.
\]

Then the canonical renormalized cutoff is

\[
\Psi_{p,N}^{\mathrm{ren}}
=
\Psi_{p,N}-W_{p,N}^{\mathrm{wall}}.
\]

This counterterm is determined entirely by the same label density and the
sharp-cutoff endpoint convention.

## Limiting coefficient wall

For fixed \(u\),

\[
I_{r,N}(u)
\longrightarrow
C_re^{-u},
\]

where

\[
C_r
=
\frac12
\pi^{-(r+1)/2}
\Gamma\!\left(\frac{r+1}{2}\right),
\]

and

\[
E_{r,N}(u)\longrightarrow0.
\]

Therefore

\[
W_{p,N}^{\mathrm{wall}}(u)
\longrightarrow
\rho_pe^{-u}.
\]

The finite moving wall and the infinite coefficient wall are two scales of
one continuum-label constructor.

## Local moving-chart remainder

Euler--Maclaurin gives, on each compact \(v\)-interval,

\[
\Psi_{p,N}^{\mathrm{ren}}(v-\log N)
=
O(N^{-1}),
\]

after the integral and endpoint half-cell are removed, with analogous bounds
for each fixed number of \(v\)-derivatives.

Hence the moving layer that previously had amplitude \(N\) is reduced past
order one. This is the first viable finite-cutoff candidate for Green
convergence.

## Remaining analytic theorem

The moving-chart estimate does not alone prove convergence over the entire
line. The next theorem must combine three regions:

1. fixed compact \(u\)-sets, using ordinary theta convergence;
2. the moving window \(u+\log N=O(1)\), using the estimate above;
3. the far negative tail, using uniform Euler--Maclaurin remainder bounds.

The desired conclusion is

\[
\Psi_{p,N}^{\mathrm{ren}}
\longrightarrow
\Psi_p-\rho_pe^{-u}
\]

in the graph norm of

\[
\mathcal C=D_u^2-\frac14.
\]

## Compatibility burden

Because \(E_{r,N}\) is attached to the sharp label endpoint, changing the
cutoff convention changes the finite comparison cell. Abel or smooth
cutoffs have their own source-derived boundary profile.

The wall profile must also be transported through the labelwise covariant
derivative before summation. This is a typed Euler--Maclaurin naturality
square, not merely a scalar asymptotic.

## Hostile

Subtract only the continuum integral. The order-\(N\) divergence disappears,
but an order-one profile still travels to \(-\infty\). Every compact test
passes while strong Green convergence can still fail through escaping norm.
