---
authors:
  - marici.Nima
date: 2026-08-19
---
# 917 — The Seven Quadratic Directions Are a Collective Marked-Incidence Grade

Entry 910 found a stable seven-dimensional second-normal grade in the
triangle-wall relation module.  To locate its source provenance without
choosing basis vectors, filter the complete relation matrix by its declared
families:

\[
d_{\rm dR},\quad K,\quad
q_{g_1},q_{g_2},q_{g_3},q_{g_{23}},q_{g_{31}}.
\]

At ambient degree 10, the cumulative second-normal ranks are

\[
(0,0,0,0,0,0,7).
\]

At ambient degree 11 they are again

\[
\boxed{(0,0,0,0,0,0,7).}
\]

Thus neither the de Rham rows, the principal Cayley--Menger relation, nor any
proper initial collection of marked-divisor relations produces a quadratic
normal class.

The final jump could still have been an ordering artifact identifying the
last-listed physical partner \(q_{g_{31}}\).  To test this, place the complete
\(q_{g_{31}}\) row family first among the marked relations.  At degree 10 the
entire cumulative rank profile remains unchanged, and the quadratic rank is
still zero until the fifth marked family completes the packet, where it jumps
to seven.

Therefore

\[
\boxed{
\operatorname{gr}^{(2)}_\Lambda R
\text{ is a collective five-mark incidence grade, not an elementary}
\ q_g\text{-family contribution}.}
\]

This is a matrix-intersection statement: no monomial or source basis has been
assigned to the seven-plane.  It narrows the next calculation to the complete
marked-divisor incidence complex.  A source-labelled basis must be extracted
from the quotient of the full five-family Rees module by every proper-family
submodule, rather than from one divisor's rows.

## Durable verification

- exporter with relation-family tags:
  `research/nima/export_triangle_wall_dual_rows.py`;
- sparse rank engine with cumulative Rees ranks:
  `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`;
- packet: `research/nima/triangle-wall-dual-relation-rank.json`;
- field: \(\mathbf F_{32003}\);
- allocator claim: `seqclaim-31a51ffb1c35da61211e6405`.
