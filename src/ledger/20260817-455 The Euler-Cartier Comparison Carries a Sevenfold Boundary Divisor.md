---
id: 455
date: 2026-08-17
title: The Euler-Cartier Comparison Carries a Sevenfold Boundary Divisor
---

# The Euler--Cartier Comparison Carries a Sevenfold Boundary Divisor

Entry 454 produced a geometric rank-two lattice with basis (1,a).  The
Euler-resonance quotient of Benincasa Entry 449 has divided representatives

\[
1,qquad a^7(b+1).
\]

Their equal rank does not by itself identify the lattices.  On the (u)-chart
of the weighted Rees space, (a^2=ut), so

\[
a^7(b+1)=a\,u^3t^3(b+1).
\]

After compensating the Rees degree (u^3), restriction to the Cartier section

\[
t=\frac{b^2-1}{2}
\]

sends the second Euler generator to the geometric generator (a) multiplied
by

\[
t^3(b+1)
=\frac18(b-1)^3(b+1)^4.
\]

This coefficient is generically invertible but is not a unit on the full
(b)-axis.  Its divisor is

\[
3[b=1]+4[b=-1].
\]

The total multiplicity seven is exactly the relative (a)-degree separating
the two Euler generators.  The weighted Rees grading decomposes that degree as
three powers of (u) plus the residual odd generator (a); the remaining
boundary coefficient remembers how that odd layer approaches the two special
directions.

Therefore the plain global identification

\[
\mathbb Q\langle[1],[a^7(b+1)]\rangle
\stackrel?\simeq
\mathbb Q[b]\langle1,a\rangle
\]

is refuted.  An identification exists only away from (b=\pm1).  Globally it
would require a boundary lattice modification carrying divisor
(3[1]+4[-1]), or an independently derived sector twist with precisely that
transition.  Introducing such a twist merely to force agreement would be
post hoc.

This also explains why the two-dimensional numerical agreement was real but
insufficient: it detects the generic rank while forgetting the integral
lattice at the resonant boundary.

The next gate is to derive the boundary lattice from the transformed exact
complex and its sector line bundles, or refute its existence.  Only a derived
transition equal to the sevenfold divisor can identify the Euler plane with
the Cartier pushforward.

The executable audit is
research/voevodsky/check_soft_axis_euler_cartier_grading.py.
