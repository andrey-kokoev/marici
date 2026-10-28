# Cross-branch coherence at the integral cellular-chain level

## Construction

Start with the retained branches from the recursive relation-promotion test.
Keep every final record ID distinct and compare its recovered geometric route.
A local comparison changes one intermediate vertex while fixing its neighbours.
It is admitted only when the old and new intermediate vertices are joined by an
elementary lattice edge. Two actual triangular faces then fill the route
difference, with their orientation checked exactly.

Choose a spanning tree of this branch-comparison graph to construct a face-chain
comparison of each route to the root route. The root/tree is a bookkeeping
choice; it does not select a physical path. For every local comparison, compare
its face witness against the two root comparisons. Their residual is a closed
2-chain. Solve for its filling by the actual tetrahedral/octahedral volume cells
of the region, retaining the integer coefficients.

## Executed results

| Endpoint separation | Branches | Local comparisons | Independent graph cycles | Volume cells | Nonzero higher fillers |
|---:|---:|---:|---:|---:|---:|
| 4 | 36 | 72 | 37 | 14 | 26 |
| 6 | 400 | 1,200 | 801 | 51 | 479 |

Both branch-comparison graphs are connected. Every tested local comparison has
an exact two-face boundary witness. Every residual between comparison routes
has a verified integral 3-chain filler. Nonzero fillers are retained rather
than calling the competing face chains equal.

The number of nonzero fillers depends on the chosen root/tree normalizations;
it is not a canonical particle or energy count. The cycle count refers to the
finite comparison graph, not a claim of nontrivial physical topology.

## Exact equations checked

For paths p and q and local face witness F_pq:

    boundary(F_pq) = q - p.

For root-route fillers F_p and F_q:

    Z = F_p + F_pq - F_q,
    boundary(Z) = 0,
    boundary(V_pq) = Z.

The checker solves the last equation over the dual volume-cell graph, anchoring
the exterior coefficient at zero, then recomputes the boundary independently.
All cells and faces belong to the constructed lattice region. This is not a
numerical tolerance fit.

## Surviving interpretation and boundary

At the **oriented integral cellular-chain level**, the 400 six-step paths form
one connected comparison system with explicit face and volume witnesses. This
advances beyond independently completed branches.

It does not identify their complete retained archives. The comparisons are on
the recovered geometric routes; no formal lifting to the native promoted-record
interfaces has yet been constructed. Chain fillings are not automatically
parametrized homotopies, nor do these additive equations establish every
nonlinear/higher coherence operation.

The remaining source binding must preserve the WG's marked endpoints, reader,
phase/coefficient and admissibility data. No particle census or Pb-208
identification follows from the 400 branches, 51 volume cells or 479 nonzero
fillers. These are different kinds of counts.

## Reproduction

```sh
python research/realization-tower/check_cross_branch_coherence.py
```

Fresh result: **PASS**. The receipt retains local face fillers, all root
comparisons, volume-cell vertices, higher filling coefficients and distinct
terminal IDs:
[results/cross-branch-coherence-v1.json](results/cross-branch-coherence-v1.json).

No proof-assistant closure, existing proof-status change or isotope assignment
was performed.
