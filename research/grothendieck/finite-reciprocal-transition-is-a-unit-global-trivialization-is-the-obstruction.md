# Finite reciprocal transition is a unit; global trivialization is the obstruction

## Question

How does archimedean completion act on the finite graded determinant packet,
and where does reciprocal sewing first cease to be an ordinary scalar
identity?

## Finite completed Euler object

Write

\[
s=\frac12+z
\]

and use the standard completed prefactor

\[
B(s)
=
\frac12s(s-1)\pi^{-s/2}\Gamma(s/2).
\]

For a finite prime set (X), define

\[
E_X(s)
=
\prod_{p\in X}(1-p^{-s})^{-1},
\qquad
C_X(s)=B(s)E_X(s).
\]

Archimedean completion acts by tensoring the finite arithmetic determinant
line with the one-dimensional factor (B(s)).  It does not mix the first and
second arithmetic cumulants.

## Exact reciprocal transition

The direct and reciprocal presentations are related by

\[
u_X(z)
=
\frac{C_X(1/2+z)}{C_X(1/2-z)}.
\]

Using

\[
\gamma_p(z)
=
\frac{1-p^{-1/2}e^{-z\log p}}
{1-p^{-1/2}e^{z\log p}},
\]

one obtains

\[
u_X(z)
=
\frac{B(1/2+z)}{B(1/2-z)}
\prod_{p\in X}\gamma_p(z)^{-1}.
\]

This is an exact finite-cutoff identity.  In the open critical strip,

\[
0<\Re s<1,
\]

every factor is holomorphic and nonzero.  Therefore (u_X) is a transition
unit and cannot change the finite determinant divisor.

On the seam (z=it), real structure gives

\[
|u_X(it)|=1.
\]

Finite reciprocal sewing is therefore unitary on the seam without any appeal
to zero locations.

## The odd packet is the logarithmic transition

In a convergence chamber, logarithmic expansion gives

\[
\log u_X(z)
=
\log\frac{B(1/2+z)}{B(1/2-z)}
-
\sum_{p\in X}\log\gamma_p(z).
\]

The second term is the odd prime-power tower

\[
-2
\sum_{p\in X}
\sum_{k\ge1}
\frac{p^{-k/2}}k
\sinh(kz\log p).
\]

Separating (k=1), (k=2), and (k\ge3) recovers exactly the graded
determinant packet.  The archimedean anomaly and the arithmetic odd currents
are thus components of one finite determinant-line connection.

## Where the finite diagram stops

For each finite (X), completion and determinant reconstruction commute
projectively through the explicit unit (u_X).  But the scalar sequence

\[
u_X(z)
\]

does not acquire a direct Euler-product limit in the critical strip.  Its
primitive logarithmic component is already distributional, and the square
component lies below absolute summability.

Consequently the completed functional equation cannot be obtained by taking
an ordinary scalar limit of the finite transition units.  The theta modular
identity supplies a global trivialization only after the entire graded packet
is retained.

The exact completion problem is to lift the family \(\{u_X\}_X\) to a
transition in the completed determinant line, not to obtain termwise
convergence to an ordinary nonzero scalar function.

## Consequence for zero confinement

Every finite cutoff has divisor-preserving reciprocal transport.  Therefore
no finite Euler packet can distinguish the actual completed divisor from a
hostile divisor-bearing scalar multiplier that is inserted only after
completion.

The missing theorem must prove that theta modular trivialization is the unique
completion-stable extension of the source transition packet, up to a
nowhere-vanishing unit.  That is a canonical-section rigidity problem at the
infinite boundary, not a finite positivity problem.

## Falsifiers

The proposed determinant-line completion fails if:

- the primitive or square logarithmic current is discarded;
- two inequivalent completed transitions extend every finite (u_X) while
  carrying different divisors;
- the extension depends on the exhaustion of the primes;
- or modular trivialization holds only after inserting the completed scalar
  function itself.

## Result

Archimedean completion and finite determinant reconstruction are compatible
through an explicit reciprocal transition unit.  The entire obstruction lies
in lifting the cutoff family of units to a canonical completed
determinant-line transition.  This is where modular theta sewing must do work
that no finite Euler calculation can perform.
