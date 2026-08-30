# The Moving Theta Frontier Is an Exact Boundary Current

## Exact primitive

The moving-front profile

\[
F(\rho)
=
\rho^2(2\pi\rho^2-3)e^{-\pi\rho^2}
\]

is an exact derivative:

\[
F(\rho)
=
-\frac{d}{d\rho}
\left(
\rho^3e^{-\pi\rho^2}
\right).
\]

Indeed,

\[
\frac{d}{d\rho}
\left(
\rho^3e^{-\pi\rho^2}
\right)
=
\left(
3\rho^2-2\pi\rho^4
\right)
e^{-\pi\rho^2}.
\]

## Continuum current closure

Define

\[
J(\rho)=\rho^3e^{-\pi\rho^2}.
\]

Then

\[
\int_0^\infty F(\rho)\,d\rho
=
-J(\infty)+J(0)=0.
\]

The zero continuum mass is therefore not a numerical coincidence between two
Gaussian moments. It is boundary-current exactness.

## Discrete anomaly

For mesh

\[
h=e^{-u},
\]

the reflected source is

\[
\Phi(-u)
=
2\pi h^{1/2}
\sum_{n\geq1}F(nh).
\]

The continuum current closes at both endpoints, but the sampled derivative
does not telescope:

\[
h\sum_{n\geq1}F(nh)
\neq
\int_0^\infty F(\rho)\,d\rho.
\]

Thus the completed theta value is a discrete-current anomaly: the discrepancy
between sampling an exact derivative and integrating it.

This is source-local. The current \(J\) is derived before examining zeros,
oscillatory transforms, or the desired sign.

## Connection to modular sewing

Poisson summation does not create the boundary current. It transports the
discrete anomaly of that current into the reciprocal lattice chart. The
completed theta relation is therefore naturally typed as exact continuum
current, then lattice sampling anomaly, then reciprocal sewing.

This is the missing distinction between ordinary symmetrization and theta
completion. Ordinary averaging sees only the signed profile. Theta completion
retains the sampling incidence that turns its exact continuum cancellation
into a nonzero reciprocal residue.

## Next gate

The RH-bearing question becomes sharper:

Does the Mellin-transported discrete-current anomaly admit a doubled Green
identity whose only bulk term is the native Gram energy and whose boundary
term is the reciprocal image of \(J\)?

The first hostile test is to deform the sampling lattice while keeping the
same exact current. If the desired orientation survives arbitrary sampling,
the arithmetic explanation is not specific enough.

## Falsifier

The current identity fails if

\[
F+J'\ne0.
\]

It is decided by direct differentiation.
