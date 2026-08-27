# The Polar Port Is the Green Boundary Completion of the Bulk-Odd Port

## Setup

Put \(z=s-\tfrac12\), and let the centered positive half-line source be
\(g(u)\). Define

\[
I_g(z)=\int_0^\infty g(u)\sinh(zu)\,du
\]

and the centered source operator

\[
L=\partial_u^2-\frac14.
\]

Assume the source and its first derivative decay strongly enough that the
boundary terms at infinity vanish. Write \(c=g(0)\).

## Exact Green identity

Twice integrating by parts gives

\[
\int_0^\infty (Lg)(u)\sinh(zu)\,du
=cz+\left(z^2-\frac14\right)I_g(z).
\]

Consequently,

\[
2I_g(z)+\frac{2cz}{z^2-\tfrac14}
=
\frac{2}{z^2-\tfrac14}
\int_0^\infty(Lg)(u)\sinh(zu)\,du.
\]

The two terms on the left are precisely the bulk-odd port and the polar-odd
port. Their sum is therefore not an arbitrary augmentation. It is the unique
Dirichlet boundary completion created when the bulk odd transform is pushed
through \(L\).

## Interpretation

This supplies the source-derived mate missing from entry 3248:

\[
g\xrightarrow{L}Lg
\xrightarrow{\mathcal O}
R_2+R_3.
\]

The scale atom falsifier failed because an atom is not stable under this
second-order source operation: its Green image includes derivative
distributions. The polar channel remembers exactly the boundary datum erased
by treating the odd transform as a bare scalar.

The appearance of \(1/4\) is forced twice and consistently. It is the square
of the reciprocal center \(1/2\), and it is the potential term in the centered
Green operator. Thus the critical offset is now present at the source-dynamics
level, not inserted from the zero diagram.

## What this does not prove

The identity supplies the missing transport and boundary typing, but it does
not orient the transform of \(Lg\). Even when \(Lg\) has one sign, its odd
transform is oscillatory away from the nonoscillatory axis. The next gate is
therefore exact and source-specific:

> Determine the sign-band or factorization structure of \(L\Phi\) for the
> completed theta source, including its modular reflection and endpoint
> incidence.

A generic positive source is no longer the relevant hostile class. The proper
falsifier must preserve the centered Green relation and the theta source's
modular sewing.
