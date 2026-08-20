---
title: "The Four-Cycle OFPT Packet Has Twenty-Eight Terms"
date: 2026-08-20
entry: 1159
status: established-source-derived-packet
sector: cosmology
---

# 1159 — The Four-Cycle OFPT Packet Has Twenty-Eight Terms

Sequence claim: `seqclaim-d3424fb7cc9ebb78e285b96f`.

## Hard-to-vary claim

The one-loop four-cycle old-fashioned-perturbation-theory representation is
derived from the source cosmological polytope, without fitting a denominator
subset. It contains

\[
\boxed{28}
\]

physical-pole terms, partitioned into seven free cyclic orbits of size four.

## Frozen construction

For the cycle \(C_n\), use coordinates

\[
(x_1,\ldots,x_n,y_{12},\ldots,y_{n1})
\]

and the three source vertices associated to every edge \(e=(i,j)\):

\[
x_i+x_j-y_e,
\qquad
x_i+y_e-x_j,
\qquad
x_j+y_e-x_i.
\]

Their convex hull is the cosmological polytope in
\(\mathbf P^{2n-1}\). Its facet covectors are derived from the connected
source subgraphs. For \(C_4\) this gives exactly 17 facets:

- four singleton intervals;
- four two-site intervals;
- four three-site intervals;
- four all-site spanning paths \(G\setminus e\);
- the full graph \(G\).

Choose the source OFPT outer intersection

\[
\mathfrak G_\circ=\{G,g_1,g_2,g_3,g_4\}.
\]

Every simplex term must add three facets, since

\[
n_s+n_e-|\mathfrak G_\circ|=8-5=3.
\]

The admissible triples were not selected by a graph heuristic. For every
triple the checker intersects the corresponding exact facet vertex sets,
requires the expected codimension-three face on the polytope, and requires
the eight denominator covectors to have full rank.

## Source replication

Before applying the procedure at four sites, the identical algorithm was
run on the triangle. It derives its ten facets and reproduces exactly the
six printed terms of arXiv:2112.09028 and arXiv:2408.16386:

\[
\{G\setminus e,\,g_{ij}\}
\]

with the six source-compatible labelled choices.

This replication fixes the incidence convention independently of the
four-site output.

## Four-site packet

At four sites the exact census gives

\[
\boxed{
\Omega_{C_4}
=
\frac{1}{q_Gq_{g_1}q_{g_2}q_{g_3}q_{g_4}}
\sum_{a=1}^{28}
\frac{1}{q_{a_1}q_{a_2}q_{a_3}}.
}
\]

All 28 labelled triples are exported in the result packet. Cyclic rotation
acts freely:

\[
28=7\times4.
\]

Thus Entry 1158's missing physical denominator packet is now derived from
the primary canonical-function and outer-intersection rules rather than
guessed.

## Typing refinement at infinity

Each term has eight physical denominators, but \(q_G\) is independent of
the loop-edge variables. At the edge-variable infinity compactification it
is the total-energy normal parameter, not another marked hyperplane on the
projective infinity base.

Consequently a four-site term supplies seven loop-dependent marked
hyperplanes. After choosing one marked residue to obtain Entry 1154's
degree-two del Pezzo surface, six marked curves remain. This distinction is
required before applying Entry 1157's incidence calculus.

## Next falsifier

For every one of the 28 terms and each admissible marked residue pivot:

1. restrict the six remaining infinity hyperplanes to the residue plane;
2. retain all labelled coincidences rather than deduplicating equations;
3. compute pair collisions and forced triple concurrencies;
4. attach Poincare-residue orientation signs;
5. assemble the resulting elliptic/Tate Cech complex orbitwise.

A residual Hodge type outside the component elliptic systems and their Tate
incidence objects would falsify the current four-site H2 prediction.

Evidence:

- `research/benincasa/checkers/derive_polygon_ofpt_packet.py`;
- `research/benincasa/results/four-cycle-ofpt-packet.json`;
- arXiv:1709.02813, cosmological-polytope source vertices and OFPT
  connected-subgraph construction;
- arXiv:2112.09028, equations defining outer-intersection triangulations
  and the printed one-loop triangle OFPT packet.
