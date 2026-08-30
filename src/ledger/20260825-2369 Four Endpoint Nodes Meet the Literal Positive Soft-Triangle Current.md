---
author: marici.Benincasa
date: 2026-08-25
---

# 2369 — Four Endpoint Nodes Meet the Literal Positive Soft-Triangle Current

## Question

Entry 2368 finds eight algebraic \(A_1\) nodes. Physical activation cannot
be inferred from their existence. The finite incidence test must retain all
three source triangle inequalities.

Sequence claim: seqclaim-08404639bfd28bb281bf91e5.

## Three exceptional intervals

The physical weighted chart gives:

\[
-1\leq\kappa\leq1
\]

from the fixed external triangle and

\[
-1\leq\xi\leq1
\]

from the collapsing \((c,b,X_1)\) triangle.

For the remaining \((c,a,X_2)\) face, setting \(t=a/p\) gives

\[
\boxed{
F_{ca}^{\rm exc}
=(t^2-1)(t^2-9).
}
\]

The positive loop-length chamber therefore selects

\[
\boxed{1\leq t\leq3.}
\]

## Physical node census

Exactly four of Entry 2368's eight nodes lie in this positive exceptional
closure:

\[
\begin{array}{c|c|c|l}
\kappa&\xi&t&\text{marked support}\\ \hline
-1&-1&3&q_{\mathfrak g_1}\text{ endpoint}\\
-1& 1&1&q_{\mathfrak g_2}/q_{\mathfrak g_{31}}\text{ collision}\\
 1&-1&1&q_{\mathfrak g_1}\text{ endpoint and }
          q_{\mathfrak g_2}/q_{\mathfrak g_{31}}\text{ collision}\\
 1& 1&3&\text{none; pure Cayley--Menger corner}.
\end{array}
\]

Their marked-incidence profile is consequently

\[
\boxed{(0,1,1,2).}
\]

The four negative-\(t\) nodes are signed analytic companions and do not
meet the literal positive current.

## Result

Before relations, orientations, or thimble coefficients, the physically
eligible local Milnor packet has rank four. Every eligible node lies on
existing Cayley--Menger endpoints; three also lie on existing marked
support.

This is an incidence theorem only:

\[
\Gamma_{\rm phys}^{\rm exc}\cap\operatorname{Supp}(\phi)
\ne\varnothing
\]

does not yet prove a nonzero intersection number with the corresponding
vanishing cycle.

## Classification

- algebraic node packet: rank eight;
- literal positive incidence packet: rank four;
- support: existing soft, triangle, signed-face, and marked incidence;
- source-selected coefficients: uncomputed;
- new Carrier datum: none.

## Scope

The result does not compute local orientations, Picard--Lefschetz
coefficients, relations among nodes, occurrence sewing, or the physical
period map.

## Durable verification

- research/benincasa/check_soft_triangle_physical_node_incidence.py;
- research/benincasa/soft-triangle-physical-node-incidence.json;
- exact three-face factorizations and labelled node census;
- epistemic event
  ev-000000003247-e79506e2-21e8-4bb1-b90a-acc6ba9161ec.

## Next falsifier

Derive the source orientation and local Picard--Lefschetz coefficient at
each of the four eligible nodes. Assemble the two occurrence summands
before any physical readout. A zero sewn packet closes physical activation;
a nonzero packet must then be tested against the existing endpoint/Gysin
complex.
