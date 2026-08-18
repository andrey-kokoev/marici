---
id: 461
date: 2026-08-17
title: The Full Weighted Strict Transform Is a Trivial Double Section
---

# The Full Weighted Strict Transform Is a Trivial Double Section

Entry 460 isolates the remaining nearby-cycle question.  Before transporting
the exact complex, the full Cayley--Menger carrier itself admits an exact
factorization on the weighted (u)-chart.

Use (a^2=ut), divide the full relation by its exceptional factor (u^2), and
put

\[
\psi=t+\frac12(1-b^2).
\]

Direct coefficient comparison gives

\[
\frac{K}{u^2}
=\left(\psi-\frac54u+\frac12u^2\right)^2.
\]

Thus the polynomial translation

\[
z=\psi-\frac54u+\frac12u^2
\]

identifies the complete strict-transform family with

\[
z^2=0
\]

over the (u)-base.  The doubled section does not split, collide, or acquire
nontrivial carrier monodromy: it is algebraically constant after translation.
In particular, the reduced section has identity monodromy.

This sharply locates the remaining difficulty.  Ordinary topological nearby
cycles are insensitive to nilpotent thickening, so the carrier hypersurface
alone cannot distinguish the two Euler classes or generate their transport.
Any nontrivial specialization datum must reside in the transformed exact-form
complex--its sector lattices, differential, or support framing--not in the
Cayley--Menger equation.

The result also explains why the Newton initial form was a perfect square: it
was the special fiber of a perfect square throughout the weighted chart, not
merely an accidental leading-order degeneracy.

The next gate is to conjugate all transformed exact operators by the same
translation (z=\psi-5u/4+u^2/2), then test whether their two-class cokernel is
constant, has a nilpotent extension, or still mixes with the quartic tail.

The executable audit is
research/voevodsky/check_soft_axis_strict_transform_square.py.
