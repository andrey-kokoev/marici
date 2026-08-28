# Mellin--Poisson Boundary Curvature Is the Polar Packet

## Exact split

Let

\[
\psi(t)=\sum_{n\ge1}e^{-\pi n^2t}.
\]

In the initial convergence sector,

\[
\Lambda(s)
=
\pi^{-s/2}\Gamma(s/2)\zeta(s)
=
\int_0^\infty\psi(t)t^{s/2}\,\frac{dt}{t}.
\]

Using theta reflection on the interval \(0<t<1\) gives

\[
\Lambda(s)
=
\int_1^\infty
\psi(t)
\left(t^{s/2}+t^{(1-s)/2}\right)
\frac{dt}{t}
+
\frac1{s-1}-\frac1s.
\]

The last two terms are exactly the boundary anomaly of completing the
Mellin--Poisson comparison square.

## Polar packet

Multiplying by the completion factor gives

\[
\xi(s)=\frac12s(s-1)\Lambda(s).
\]

The two boundary currents become

\[
\frac{s}{2},
\qquad
\frac{1-s}{2}.
\]

Their symmetric and antisymmetric coordinates are

\[
\frac{s}{2}+\frac{1-s}{2}
=
\frac12,
\]

\[
\frac{s}{2}-\frac{1-s}{2}
=
s-\frac12.
\]

Thus the boundary curvature sought after the flat
Gaussian--prime connection is precisely the already derived polar packet:

- the symmetric channel is the neutral half carrier;
- the antisymmetric channel is the centered critical coordinate.

There is no additional boundary degree hidden in this square.

## Zero-state audit

At a nontrivial zero of \(\xi\), neither polar component is forced to vanish.
Instead, the completed tail contribution cancels the symmetric boundary
carrier:

\[
\frac12s(s-1)
\int_1^\infty
\psi(t)
\left(t^{s/2}+t^{(1-s)/2}\right)
\frac{dt}{t}
=
-\frac12.
\]

Therefore scalar zero-state nullity is not vanishing polar boundary flux. A
Green identity whose endpoint term contains only the polar packet cannot
close by imposing \(\xi(s)=0\).

The antisymmetric channel explains why the seam is
\(\operatorname{Re}s=1/2\), but it does not couple automatically to the
tail cancellation producing a zero.

## Consequence

The hoped-for boundary-curvature repair is now closed at rank two. The missing
zero-to-flux bridge must retain a mixed tail--boundary state whose endpoint
condition is equivalent to cancellation between the tail contribution and
\(1/2\), not merely a condition on either polar current separately.

This returns the programme to the exact boundary-control problem: construct a
source-derived state space in which the tail and neutral carrier are
components of one boundary vector, and derive a reciprocal current whose
vanishing follows from that vector condition.

## Falsifier

Any proposed boundary proof fails if it:

- sets the polar packet to zero at a nontrivial \(\xi\)-zero;
- discards the neutral half carrier;
- uses only the antisymmetric coordinate \(s-1/2\);
- or converts tail--carrier cancellation into boundary-flux vanishing without
  an explicit source-derived incidence map.
