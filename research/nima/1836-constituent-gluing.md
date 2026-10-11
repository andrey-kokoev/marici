# Exact four-piece support accounting of the 1836 arrows

## Question

Does the retained L/G/N graph support the proposed four-constituent inclusion-exclusion formula, and what do its shared terms actually represent?

## Source labels and claim boundary

Read all 1836 stage-typed arrows from `results/twelve-triangle-1836-arrows.json` and the twelve triangle placements from `results/twelve-triangle-positive-geometry.json`. Each small triangle has one parent face ABC, ABD, ACD or BCD. That face also labels a proposed center-to-face constituent tetrahedron. Each face owns three small triangles and nine coordinate ports per stage.

This owner map labels existing boundary-supported data. It does not construct internal-center ports, shared-face maps or standalone constituent tetrahedra. Two support conventions below are distinguished rather than conflated.

## Within-piece and bridging arrows

Enumerating source and target ownership gives:

| Support | L | G | N | Total |
|---|---:|---:|---:|---:|
| Within one piece | 27 | 27 | 81 | 135 |
| Between one unordered pair of pieces, both directions | 0 | 54 | 162 | 216 |

All four pieces and all six pairs have the displayed counts. These sets partition every source arrow exactly once:

    1836 = 4*135 + 6*216.

Keeping only within-piece arrows gives 540 and omits 1296 cross-piece arrows. The latter number happens to equal the global N support size, but the cross-piece set consists of 324 G arrows and 972 N arrows, not all N arrows.

The equal share of the full network attributed to one piece is 135 + 3*(216/2) = 459, if each bridge is shared equally by its two endpoints. This is an allocation rule on the retained graph, not the independently computed cost of an isolated constituent.

## Overlapping incident-arrow cover

Instead define A_i as every arrow with at least one endpoint owned by piece i. Then

- |A_i| = 135+3*216 = 783;
- |A_i intersection A_j| = 216 for each distinct pair;
- all triple and quadruple intersections are empty.

Thus the actual arrow sets satisfy

    1836 = 4*783 - 6*216 + 4*0 - 0.

This is the requested inclusion-exclusion pattern for an incident-arrow cover. The pair overlap is the bridge set, not a proved geometric shared-face kernel. The higher intersections vanish because each primitive coefficient arrow has at most two parent-face owners. A common geometric vertex need not support a common primitive coefficient arrow.

The strict within-piece sets, by contrast, are disjoint and do not cover the bridging arrows. Therefore the same coefficients cannot be described interchangeably as internal costs, incident costs and shared-face costs.

## Collective normalization

Each face-restricted N block has trace 1/4, as checked directly from the retained coefficients. The four blocks distribute the global collective line's norm across four face sectors. A restricted block is not itself the full normalized collective identity of a newly constructed constituent. Independent constituent normalization would be an additional operation.

## Disposition and verification

The source really admits four symmetric sectors and six symmetric pair couplings. It supports both exact accounting formulas above. It does not yet supply nonzero triple-edge or central-vertex arrow costs, nor identify incident sectors as standalone quark structures.

`python research/nima/checkers/check_1836_constituent_gluing.py` passed via structured-command execution `structured_command_execution:e_32876_1791218991311241000_13`. The checker verifies all arrows, both covers, every intersection, the missing-cross-arrow control, the duplicate-count control and collective face traces. Results: `results/1836-constituent-gluing.json`, with source and geometry SHA-256 values. No mass assignment, new Agda theorem, commit or publication is claimed.
