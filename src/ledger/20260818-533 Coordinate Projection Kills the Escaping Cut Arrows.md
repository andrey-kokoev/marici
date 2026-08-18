---
id: 533
date: 2026-08-18
title: Coordinate Projection Kills the Escaping Cut Arrows
---

# Coordinate Projection Kills the Escaping Cut Arrows

This entry corrects Entry 532. That entry identified (7320) radial arrows
which leave a common Cut overlap and incorrectly concluded that they obstruct
the coordinate projection from being a chain map.

Let

\[
p_{D,D'}:C_D\longrightarrow C_{DD'}
\]

retain precisely the loaded faces compatible with both Cuts. If a retained
source acquires a diagonal crossing (D'), its target is discarded. Then
(p d) kills that target, while (d p) contains no such overlap arrow. Both
sides are zero. An obstruction would instead be an arrow from a discarded
source into a retained target.

The complete census gives

\[
\boxed{\text{entering arrows}=0},
\qquad
\boxed{\text{killed escaping arrows}=7320}.
\]

Thus the discarded sector is a subcomplex, the common-link complex is the
corresponding coordinate quotient, and (p_{D,D'}) is a chain map. The
(7200) arrows internal to the retained sector agree with the overlap
differential including their integral signs. All remaining projected-away
arrows are killed on both sides.

Tensoring these twelve quotient maps with the native Thom-twisted oriented
Čech incidence gives the full totalization. It contains

\[
8\cdot1075=8600
\]

chart generators and

\[
12\cdot125=1500
\]

pair-overlap generators. Since the physical Cut nerve has dimension one,
there is no further Čech differential. With the standard totalization sign,

\[
\boxed{D_{\rm tot}^2=0}
\]

cell by cell.

The constant eight-chart coefficient is primitive and restricts equally on
all (1500) overlap cells. Consequently the primitive scalar section of
Entry 446 lifts to the full loaded Cut system:

\[
\boxed{\text{full eight-point Thom-twisted Cut descent exists in the
cellular fs/Kato sector}.}
\]

Entry 532 remains useful only as the census of escaping arrows; its claimed
chain-map obstruction is withdrawn. No Cut-collar homotopy is needed to
define these quotient restrictions.

The executable audit is
`research/voevodsky/check_n8_full_twisted_cut_cech_lift.py`.
