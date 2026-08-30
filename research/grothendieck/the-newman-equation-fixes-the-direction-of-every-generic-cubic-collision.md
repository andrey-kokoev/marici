# The Newman Equation Fixes the Direction of Every Generic Cubic Collision

## Local theorem

Suppose \(H_\lambda(z)\) obeys

\[
\partial_\lambda H=-\partial_z^2H
\]

and has a generic double real zero at \((\lambda_0,z_0)\):

\[
H=0,
\qquad
H_z=0,
\qquad
H_{zz}\neq0.
\]

Taylor expansion and the heat equation give

\[
H_\lambda(z)
=
\frac{H_{zz}(\lambda_0,z_0)}2
\left((z-z_0)^2-2(\lambda-\lambda_0)\right)
+\text{higher terms}.
\]

The source-dependent coefficient factors out. The local zero equation is

\[
(z-z_0)^2=2(\lambda-\lambda_0).
\]

Therefore every generic Newman collision has the same orientation:

- for \(\lambda>\lambda_0\), two zeros lie on the seam;
- at \(\lambda=\lambda_0\), they form one double zero;
- for \(\lambda<\lambda_0\), they form an off-seam conjugate pair.

Increasing Newman time absorbs off-seam charge into the seam. Backward heat
from the real-zero phase emits off-seam charge whenever it crosses a collision.

## Consequence

The collision channel no longer needs a sign theorem. Its sign is universal
and unfavorable to backward continuation. The theta-specific question is
reachability:

> Can the completed theta heat orbit reach the double-zero locus at a
> nonnegative heat time?

If it does, the local equation automatically produces off-seam zeros on the
earlier-time side. If it does not, finite-height collision emission is absent.

This separates two tasks that had been conflated:

1. collision orientation is fixed by the heat operator;
2. collision avoidance must come from the particular theta orbit.

## Relation to the Newman constant

Starting at a de Bruijn time where all zeros are real and transporting toward
zero, the first finite-height loss of real-rootedness must occur at a double
zero with this normal form. If the threshold is not witnessed at finite
height, the only remaining mechanism is the all-scale infinity incidence from
the preceding packets.

Thus the two RH failure channels sharpen to:

1. reachability of the real double-zero discriminant at \(\lambda>0\);
2. off-seam incidence through infinity without a finite collision.

## Hard-to-vary source target

At a candidate collision on the real spectral axis, theta supplies the two
simultaneous equations

\[
\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(xu)\,du=0,
\]

and

\[
\int_0^\infty u e^{\lambda u^2}\Phi(u)\sin(xu)\,du=0.
\]

The next theorem must exclude their simultaneous vanishing for
\(\lambda>0\) by a source property absent from generic positive even seeds.
Plain positivity of \(\Phi\) is insufficient; positive cosine transforms can
have multiple real zeros.

The most useful candidate is a labelled modular Wronskian or total-positivity
law that makes the two quadratures transverse. It must be proved before scalar
aggregation and tested against the hostile self-Fourier carriers already
known to have off-critical Mellin zeros.

## Scope

The local collision orientation is universal and exact. Collision avoidance
and infinity control remain unresolved and together carry the full RH burden.

