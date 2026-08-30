---
author: marici.Benincasa
date: 2026-08-25
---

# 2386 — The Labelled Gauss--Manin Adapter Staircase Is Strictly Flat

## Question

Do Entry 2385's direction-dependent adapters compose independently of path,
or is an additional coherence cell required?

Sequence claim: `seqclaim-52329b481ab8bc931cb60283`.

Epistemic graph: `ev-000000003269-e142cdad-c9ca-4853-a5cf-f745570b1f87`.

## Predeclared composition

Starting from

\[
C_{D,d_K,\mathbf d_q},
\]

each derivative applies

\[
(D,d_K,\mathbf d_q)
\longmapsto
(D+4,d_K+1,\mathbf d_q+\mathbf 1_{\partial_\mu q\ne0}).
\]

For each unordered pair of directions, both routes were embedded into their
least common labelled target. No quotient representative or residual-dependent
cell was chosen.

## Exhaustive source-column test

Every one of the \(8736\) labelled source columns was transported around each
mixed square:

\[
(x,y),\qquad(x,z),\qquad(y,z).
\]

At \((x,y,z)=(2,3,-4)\), all three literal commutators vanish:

\[
\boxed{
[\nabla_x,\nabla_y]
=[\nabla_x,\nabla_z]
=[\nabla_y,\nabla_z]
=0
}
\]

before reduction by exact relations. The same \(3\times8736\) tests pass at
the independent point \((3,5,-7)\).

The least common occurrence depths are additive. For example,

\[
\mathbf d_q^{xy}
=
\mathbf d_q+(1,1,0,1,1)
\]

in the ordered labels \((g_1,g_2,g_3,g_{23},g_{31})\).

## Result

\[
\boxed{
\text{the denominator-incidence adapters form a strict flat differential}
\text{ staircase on the complete labelled source presentation.}
}
\]

No mixed homotopy is needed at this grade. The earlier rank growth came from
placing repeated derivatives inside one fixed cutoff presentation rather than
from curvature of the source connection.

## Classification

- Carrier: unchanged;
- coefficient transport: a filtered, direction-dependent labelled colimit;
- mixed curvature: zero before quotient;
- coherence cell: unnecessary at second order;
- new support: none.

## Durable verification

- `research/benincasa/check_directional_adapter_mixed_paths.py`;
- `research/benincasa/directional-adapter-mixed-paths.json`;
- `research/benincasa/directional-adapter-mixed-paths-point-3-5-m7.json`.

## Next falsifier

Transport the frozen score, polarization, marked-wall, and physical-cycle maps
through the flat staircase. Test their naturality before aggregation. Then use
the complete score/Mobius tower to distinguish route loss from destructive
interference and determine whether the physical observer family is jointly
faithful.
