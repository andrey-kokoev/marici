# Rooted residual forest completes the filtered Morse matching

## Question

After reserving same-grade positive-dimensional pairs, do the unused edges form a forest whose rooted orientation completes the global cell matching?

## Claim boundary

This is a bounded test in distinct-shell multiplicative degrees two through five at grade 20000. It establishes a constructor on those materialized complexes, not yet an all-dimensional proof that every residual graph is a forest.

## Constructor

First retain the successful phase:

- process positive dimensions upward;
- match each unmatched positive-dimensional cell to its least same-grade coface.

Let \(G_{\mathrm{res}}\) contain every vertex and every edge not consumed by that phase. Test whether each connected component of \(G_{\mathrm{res}}\) is a tree. In each component choose the least vertex as root. Orient tree edges toward the root and match every nonroot vertex with its parent edge.

This pairs every residual edge exactly once and leaves one critical vertex per component. A gradient path in the residual graph strictly approaches its root.

## Bold conjecture

In every tested sector, the residual graph is a spanning forest with the same components as the full one-skeleton. Adding its rooted matching to the same-grade higher matching pairs every positive-dimensional cell, leaves exactly \(\beta_0\) critical vertices, and preserves global gradient acyclicity.

## Rivals

1. Same-grade reservations leave a cycle among unused edges.
2. Removing paired edges disconnects a full one-skeleton component.
3. Each phase is separately acyclic but their union creates a mixed-dimensional gradient cycle.

## Test

For multiplicative degrees two through five, record residual vertices, edges, components, forest Euler identity, agreement with full absolute \(H_0\), complete cell pairing, critical vertices, and acyclicity of the full reversed Hasse graph.

## Computed result

The residual graphs are forests in all four sectors. Their edge/component counts are respectively

\[
(927,445),\ (1422,502),\ (1116,278),\ (682,130)
\]

for multiplicative degrees two through five. Each component count equals absolute \(\beta_0\). Rooting these forests pairs every remaining edge, leaves exactly one vertex per component, introduces no cross-grade positive pair, and preserves acyclicity of the full mixed-dimensional gradient graph.

## Disposition

The bounded constructor succeeds completely. Same-grade higher matching followed by rooted residual-forest matching pairs every positive-dimensional cell and leaves exactly the absolute connected-component generators. The remaining theorem gate is to prove, for every degree and cutoff, that the same-grade reservation leaves a spanning forest and that the combined gradient remains acyclic.
