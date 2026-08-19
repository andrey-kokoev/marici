# 1037 — The Source-Selected Loaded Cousin Diagram Is a Two-Component Forest

## Source-derived incidences

Entry 1030 factors each of the six source character columns occurrencewise as

\[
p_iq_i.
\]

This supplies the codimension-two incidences that Entry 1036 requires.  After
removing Laurent units, introduce four pivot walls

\[
\begin{aligned}
P_1&=(A_3B_{34})^2-1,&
P_2&=A_3^2-1,\\
P_3&=(A_2B_{24})^2-1,&
P_4&=A_2^2-1,
\end{aligned}
\]

and four loaded walls

\[
\begin{aligned}
Q_1&=(ZA_2)^2-1,&
Q_2&=(ZA_2B_{24})^2-1,\\
Q_3&=(A_3/Z)^2-1,&
Q_4&=(A_3B_{34}/Z)^2-1.
\end{aligned}
\]

The six labelled source products give exactly

\[
\boxed{
(P_1Q_2, P_2Q_2, P_3Q_4, P_4Q_4, P_2Q_1, P_4Q_3).
}
\]

No pair incidence is added merely because two wall equations can be solved
simultaneously.

## Incidence graph

Orient every edge from a pivot wall to a loaded wall.  The graph decomposes as

\[
P_1-Q_2-P_2-Q_1
\]

and

\[
P_3-Q_4-P_4-Q_3.
\]

Thus it is a disjoint union of two four-vertex paths.  Exact incidence
reduction gives

\[
\operatorname{rank}\partial=6,
\qquad
\operatorname{rank}H_0=2,
\qquad
\boxed{\operatorname{rank}H_1=0.}
\]

## Pochhammer corner grade

The source-derived codimension-two coefficients are

\[
\frac1{P_1Q_2},quad
\frac1{P_2Q_2},quad
\frac1{P_3Q_4},quad
\frac1{P_4Q_4},quad
\frac1{P_2Q_1},quad
\frac1{P_4Q_3}.
\]

They are precisely the products required by the generalized Pochhammer rule
on the six declared intersections.  Because the incidence graph is a forest,
there is no cycle on which a codimension-two Čech coherence class could live.

## Narrow result

\[
\boxed{
\text{the source-selected loaded Cousin diagram has no first coherence
obstruction.}
}
\]

The two surviving (H_0) components are the two independent labelled
character chains, not an obstruction or new carrier support.

This is stronger than a determinant match but still deliberately limited:
the source products determine the selected first incidence graph; they do not
prove that every deeper geometric intersection is absent.

## Next falsifier

Compute the codimension-three source grade.  A triple term is admissible only
if a frozen source column or a derived bar/Koszul relation contains three
compatible wall factors.  If no such term exists, the forest closes the
static occurrence regularization.  If one exists, attach it to the labelled
path and test whether it creates torsion or an extension at the common pivot
vertices (P_2) or (P_4).

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_loaded_cousin_forest.rs`;
- packet:
  `research/benincasa/string-six-point-loaded-cousin-forest.json`;
- allocator claim:
  `seqclaim-f000a5fd42e180391654fa5f`.
- epistemic event:
  `ev-000000000656-15493945-f115-480d-939c-2b5ca0a9e32e`.
