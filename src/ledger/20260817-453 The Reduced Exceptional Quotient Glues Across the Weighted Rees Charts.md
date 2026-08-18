---
id: 453
date: 2026-08-17
title: The Reduced Exceptional Quotient Glues Across the Weighted Rees Charts
---

# The Reduced Exceptional Quotient Glues Across the Weighted Rees Charts

Entry 452 found a surviving quotient on the (a^2)-chart of the weighted Rees
space.  The complementary (u)-chart shows that this is not a chart artifact.

The coordinate ring of the second chart is

\[
\mathbb Q[u,a,t,b]/(a^2-ut).
\]

Put

\[
H=a^2+\frac u2(1-b^2).
\]

The controlling Newton equation is globally (H^2).  Moreover,

\[
\partial_a(H^2)=4aH,
\qquad
\partial_b(H^2)=-2ubH.
\]

These identities imply before either chart is chosen that every weighted
initial exact operator is divisible by (H).  Thus the common factor found in
Entry 452 is intrinsic to the weighted normal cone.

On the two charts,

\[
H=a^2\phi,
\quad
\phi=1+\frac s2(1-b^2),
\]

and

\[
H=u\psi,
\quad
\psi=t+\frac12(1-b^2).
\]

On the overlap (t=s^{-1}), so

\[
\phi=s\psi.
\]

Because (s) is invertible there, the two quotients obtained by removing one
of the two (H)-layers glue.  We therefore have a global (H)-reduced
exceptional quotient on the weighted Rees space, not merely an affine-chart
class.

The missing directions from Entry 452 now appear.  At (b=\pm1), the section
is (psi=t), hence meets the exceptional divisor at (t=0).  Its local ring
also retains

\[
a^2=0,
\]

the residual thickening of the nonreduced center.  Consequently “reduced” here
means reduced in the (H)-direction only; it does not authorize discarding the
(a)-nilpotent boundary structure.

The next gate is categorical rather than another rank count: identify this
glued quotient as a relative nearby-cycle/local-cohomology object, specify its
extension across the (a^2=0) boundary, and only then ask for its physical
pushforward.

The executable audit is
research/voevodsky/check_soft_axis_weighted_second_chart_gluing.py.
