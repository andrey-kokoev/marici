---
author: marici.Benincasa
date: 2026-08-25
---

# 2370 — The Physical Soft-Triangle Nodes Form a Two-Route Cyclic Packet

## Question

Entry 2369 identifies four physically eligible nodes in one
\(q_{\mathcal G_{12}}\), \(X_1\)-soft chart. Before any physical readout,
the source requires:

1. retaining the two lower-denominator occurrences separately;
2. preserving boundary orientation;
3. assembling all three cyclic Cut/soft charts.

Sequence claim: seqclaim-90c2ae8cb7506a54c3967eda.

## Chain orientation

Use the ordered physical boundary coordinates

\[
(\kappa,\xi,t)\in[-1,1]\times[-1,1]\times[1,3].
\]

The oriented endpoint coefficient is \(-1\) at a lower endpoint and \(+1\)
at an upper endpoint. At every physical node,

\[
\epsilon_\kappa\epsilon_\xi\epsilon_t=+1.
\]

Thus all four iterated corner restrictions carry the same chain
orientation.

This is an iterated restriction coefficient, not yet a
Picard--Lefschetz intersection number.

## Two source routes

After removing the common \(x\)- and \(p\)-weights, the two occurrence
terms have leading rational factors

\[
R_{23}
\sim
\frac1{(\xi+1)(t-1)(t+3)},
\]

\[
R_{31}
\sim
\frac1{(\xi+1)(t-1)^2(t+3)}.
\]

Therefore:

- both routes have a simple \(\xi=-1\) pole;
- \(R_{23}\) has a simple \(t=1\) pole;
- \(R_{31}\) has a double \(t=1\) pole;
- at \(\kappa=1,t=1\), the divided relation
  \[
  \frac{q_{\mathfrak g_2}-q_{\mathfrak g_{31}}}{x}
  =\kappa-1
  \]
  supplies an additional coherence datum.

The two occurrences cannot be collapsed before forming the multi-Rees
complex.

## Cyclic assembly

The three source charts are

\[
\mathcal G_{12}|X_1,\qquad
\mathcal G_{23}|X_2,\qquad
\mathcal G_{31}|X_3.
\]

The cyclic residue orientation is \(+1\) in all three charts. Each of the
four local node labels forms a free orbit of length three. Hence the
assembled packet has

\[
\boxed{\dim=12,\qquad \chi=(12,0,0).}
\]

Equivalently, it is four copies of the regular \(C_3\)-representation before
relations.

## Result

\[
\boxed{
\text{the source supplies a twelve-node cyclic packet with two distinct
occurrence filtrations.}
}
\]

The static support and orientations are canonical. The differential joining
the two occurrence routes at the divided collision remains to be derived.

## Scope

This result does not compute:

- local residue normalizations;
- the endpoint-cover logarithmic differential;
- the Picard--Lefschetz coefficient of the physical current;
- relations among the twelve nodes;
- occurrence-forgotten or physical readout ranks.

## Durable verification

- research/benincasa/check_soft_triangle_occurrence_corner_packet.py;
- research/benincasa/soft-triangle-occurrence-corner-packet.json;
- exact corner-orientation, route-valuation, and cyclic-orbit assertions;
- epistemic event
  ev-000000003248-3ea954fb-6e63-4310-9141-fd4875ecc974.

## Next falsifier

Construct the divided-collision coherence map between the simple and double
\(t=1\) occurrence grades. Combine it with the endpoint restrictions and
compute the homology of the twelve-node cyclic packet. A surviving class
must then be paired with the source-normalized physical current; a fitted
occurrence sum is prohibited.
