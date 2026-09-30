# A uniform shared-incidence rung tower

## Rule

Use a simple undirected carrier G=(V,E). A structural edge has two directed display orientations. Identity loops are units and are excluded from the structural edge set.

Each three-rung block performs the same operations:

    flat arrows -> source indexing -> target indexing -> promotion.

Grouping preserves the carrier. Promotion makes every old undirected edge a new vertex and relates two of these vertices exactly when they share an old endpoint. The promoted carrier is L(G), the line graph. For the unsigned incidence matrix B, its adjacency is the off-diagonal support of B^T B.

This reuses the concrete shared-endpoint constructor in `minimal-line-graph-growth.md`. It replaces the preceding Cartesian-square convention and the extra completion during source grouping. There is one structural constructor, applied uniformly at 10->9, 7->6, 4->3 and 1->0.

Rung0 is the flat presentation at the start of the next block, also called next-level rung12. Renumbering 0 as 12 does not apply a second promotion.

## Two explicit initial carriers

The original directed seed [AB,BC,CA,BA,AD,DB] has five undirected supports:

    [AB,AC,BC,AD,BD].

For this undirected experiment AB and BA designate the two orientations of the same support. Exposing both orientations of all supports gives ten directed display packets. This is an explicit change from the six supplied directed occurrences to the undirected carrier convention.

Completing CD first instead gives the tetrahedral carrier with six undirected edges and twelve directed display packets. Both seeds are checked below so that completion is not silently inserted into grouping.

## Rung table

Each carrier entry is (vertices, undirected edges). Its directed two-packet count is twice the edge count.

| Rung | Operation/view | Original two triangles | Completed tetrahedron |
|---:|---|---|---|
| 12 | Flat arrows | (4,5) | (4,6) |
| 11 | Group by from | (4,5) | (4,6) |
| 10 | Group by to | (4,5) | (4,6) |
| 9 | Promote; flat arrows | (5,8) | (6,12): octahedron |
| 8 | Group by from | (5,8) | (6,12) |
| 7 | Group by to | (5,8) | (6,12) |
| 6 | Promote; flat arrows | (8,18) | (12,36) |
| 5 | Group by from | (8,18) | (12,36) |
| 4 | Group by to | (8,18) | (12,36) |
| 3 | Promote; flat arrows | (18,64) | (36,180) |
| 2 | Group by from | (18,64) | (36,180) |
| 1 | Group by to | (18,64) | (36,180) |
| 0 / next 12 | Promote; flat arrows | (64,396) | (180,1620) |

No primitive path histories are stored in this test. New vertex addresses denote actual old edge supports. Composites and orientation roles are separate from the primitive endpoint-pair identity.

## First promotion of the original seed

The new vertices are [AB,AC,AD,BC,BD]. Their eight undirected relationships are

    (AB,AC), (AB,AD), (AB,BC), (AB,BD),
    (AC,AD), (AC,BC), (AD,BD), (BC,BD).

The flat next-rung packet vector contains both directions of each pair, giving sixteen directed packets. Every pair exists because of a shared old endpoint.

For the completed tetrahedral seed, the new six vertices are [AB,AC,AD,BC,BD,CD]. All pairs are adjacent except the three opposite pairs (AB,CD), (AC,BD), (AD,BC). This is exactly the octahedral graph.

## Checks

For every promotion,

    |V_next|=|E|,
    |E_next|=sum_v binomial(degree(v),2).

Because the source graph is simple, two distinct incident edges share only one vertex, so that formula counts each new undirected edge once. All source and target indexing steps unpack to the same complete directed set.

    python research/nima/checkers/check_incidence_rung_tower.py

Fresh exact checks pass for both seeds, all rung views, four promotions and the tetrahedron-to-octahedron identification. Artifact: `results/incidence-rung-tower.json`.

This is a finite combinatorial trial. It does not assign a geometric embedding, physical energy or proton interpretation to the promoted carriers. The rule is natural under vertex relabelling once the undirected-support and unit conventions have been declared.
