---
author: marici.Benincasa
date: 2026-08-25
---

# 2430 — The Gram Wall Splits Interaction Transport into Two Tangent Directions and One Nearby Cycle

## Question

Entries 2424, 2426, and 2429 transport the generic six-scale interaction
normals along the open Cayley--Menger contour boundary and its three
loop-distance endpoints. The remaining contour degeneration is the external
triangle divisor

\[
\Lambda(P_1,P_2,P_3)=0.
\]

At this divisor an arbitrary interaction normal need not remain tangent. The
correct test is therefore whether its transverse part enters an already
frozen nearby-cycle channel or forces new Carrier support.

## Labelled resolved normals

Write

\[
f_1=P_1-P_2-P_3,
\qquad
f_2=P_1-P_2+P_3,
\qquad
f_3=P_1+P_2-P_3.
\]

For $P_i^2=X_i^2+\nu_i$, each physical Heron component has normal
covector

\[
d_\nu f_j
=
\left(
\frac{\partial_{P_1}f_j}{2P_1},
\frac{\partial_{P_2}f_j}{2P_2},
\frac{\partial_{P_3}f_j}{2P_3}
\right).
\]

At generic nonsoft kinematics this row has rank one. Its kernel has rank two;
for signs $s_i=\partial_{P_i}f_j$, an exact labelled basis is

\[
(s_1P_1,-s_2P_2,0),
\qquad
(s_1P_1,0,-s_3P_3).
\]

Thus two interaction-normal combinations transport tangentially along every
physical Gram component. The remaining combination is the resolved linear
smoothing normal $f_j$.

## Elliptic degeneration

The generic infinity boundary is

\[
W^2=F_P(t),
\qquad
F_P(t)=P_1^2t^4-(P_1^2+P_2^2-P_3^2)t^2+P_2^2,
\]

with discriminant

\[
\Delta_F=16P_1^2P_2^2\Lambda^2.
\]

Exact specialization gives a perfect square on each physical wall. For
example,

\[
f_3=0
\quad\Longrightarrow\quad
F_P(t)=(P_1t^2+P_2)^2.
\]

The other two labelled walls behave identically up to their source signs.
Consequently the resolved normal $f_j$ is linear, while the coarse
elliptic discriminant has

\[
\operatorname{gr}^{(1)}_{f_j}\Delta_F=0,
\qquad
\operatorname{gr}^{(2)}_{f_j}\Delta_F\ne0
\]

away from soft support. The perfect-square fiber is the standard nodal
elliptic degeneration. Its rank-one unipotent Picard--Lefschetz operator

\[
\operatorname{rank}N=1,
\qquad
N^2=0
\]

is inferred from that standard nodal model; it is not a newly computed
physical-cycle pairing.

## Classification

\[
\boxed{
0\longrightarrow
\mathbb Q^2_{\rm tangent}
\longrightarrow
\mathbb Q^3_{\nu}
\xrightarrow{\ d_\nu f_j\ }
\mathbb Q_{\rm Gram\ normal}
\longrightarrow0
}
\]

at every generic physical Heron component. No canonical splitting is
asserted. The transverse direction lands
in the existing external-triangle/Gram coefficient support already carried
by the Cayley--Menger geometry. It does not define a new Carrier divisor.

Entry 193 proves that intersections of distinct physical Heron components
force soft support and resolve as products of existing soft and orientation
normals. Hence no additional nonsoft multiple-Gram audit is required.

## Scope

This entry establishes the coefficient-side normal decomposition and the
standard nodal nearby-cycle type. It does not establish that the physical
relative cycle pairs nontrivially with the rank-one vanishing cycle, nor
does it prove recovery of the complete rank-seven interaction module after
period integration.

## Durable evidence

- `research/benincasa/check_interaction_normals_at_gram_wall.py`;
- `research/benincasa/interaction-normals-at-gram-wall.json`;
- Entry 794 for the generic infinity quartic and discriminant;
- Entry 193 for physical multi-Gram/soft intersections;
- sequence claim `seqclaim-517c94bdcc2f4cfa6c1d60da`.

## Next falsifier

Compute the physical relative-cycle specialization at one generic Heron
wall and its pairing with the rank-one elliptic vanishing cycle. A zero
pairing closes Gram activation while preserving coefficient monodromy; a
nonzero pairing must then be tested for score-port recoverability. No new
Carrier structure is admissible in either outcome.
