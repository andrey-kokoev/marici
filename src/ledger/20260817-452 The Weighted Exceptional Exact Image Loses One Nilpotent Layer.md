---
id: 452
date: 2026-08-17
title: The Weighted Exceptional Exact Image Loses One Nilpotent Layer
---

# The Weighted Exceptional Exact Image Loses One Nilpotent Layer

Entries 450--451 leave a precise combined question: what becomes of the full
exact image after pulling it to the Newton-adapted chart (u=a^2s)?  The
answer begins with filtration shifts that are forced by total-transform order,
not selected afterward.  In sector ((s_a,s_b)), put (e_b=2-s_b).  The two
exact operators have shifts

\[
\nu_a(p)=e_b+4=6-s_b,
\qquad
\nu_a(q)=e_b+3=5-s_b.
\]

Write

\[
\phi=1+\frac{s}{2}(1-b^2).
\]

The exceptional Cayley--Menger equation is (phi^2=0).  A crucial point is
that the original (a)-derivative is taken at fixed (u).  On the weighted
chart,

\[
\partial_a|_u=\partial_a|_s-\frac{2s}{a}\partial_s,
\]

and hence, for (K_{\rm in}=a^4phi^2),

\[
(\partial_aK)_{\rm in}/a^3=4phi,
\qquad
(\partial_bK)_{\rm in}/a^4=-2sbphi.
\]

After dividing each transformed exact operator by its derived shift, every
exceptional initial operator is divisible by (phi).  More explicitly, for
(f=a^ib^j), both transformed coefficients have the form

\[
p_{i,j}=phi P_{i,j},
\qquad
q_{i,j}=phi Q_{i,j}.
\]

Therefore on the doubled exceptional support

\[
R_E=\mathbb Q[s,b]/(phi^2)
\]

the exact image is contained in the nilradical ((phi)).  The entire reduced
exceptional restriction (R_E/(phi)) is invisible to the initial exact
image and consequently survives in the transformed cokernel.  This is the
first geometrically derived relative quotient in the soft-axis calculation;
it is stronger than merely observing persistence of the two Euler generators.

This does not yet prove global flatness or a physical class.  At (b=\pm1),
(phi=1), so the doubled section has no point in this affine chart.  Those
directions belong to the other weighted chart (or its refinement), and the
surviving reduced quotient must be glued there before a nearby-cycle claim is
admissible.

The executable audit is
research/voevodsky/check_soft_axis_weighted_exceptional_exact_complex.py.
