# Primitive endpoint audit of the two-body candidate

## Result

The current 24-triangle pair does not produce 1836+1 under the earlier dense three-stage convention. That convention gives

    1836 + 1836 + 3456 = 7128.

The retained geometric cell graph independently shows that the second body contributes 24 new directed edges beyond the shared core.

These are explicit, different endpoint ledgers. They are not silently added into a claimed total cost for compiling the entire construction from the seed. The coordinate-record and operator-coefficient construction still needs a primitive execution trace to obtain that total.

## Same convention as the original 1836 graph

Retain exactly the original definition: a primitive coefficient-transfer arrow is a nonzero map entry between distinct typed ports (stage, triangle, coordinate). The stages are local mode selection, full frame averaging, and dense collective feedback.

The actual pair has two sets of twelve triangle positions and three coordinates per triangle. The counts are:

| Stage | Count | Value |
|---|---|---:|
| Local selection | 2*12*3² | 216 |
| Full frame alignment | (2*12)²*3 | 1728 |
| Collective feedback | (2*12)²*3² | 5184 |
| Total | | 7128 |

Partitioning by actual source and destination bodies gives:

| Endpoint class | Unique arrows |
|---|---:|
| Both endpoints in body A | 1836 |
| Both endpoints in body B | 1836 |
| Endpoints in different bodies | 3456 |
| Total | 7128 |

Thus the increment over one body's internal support is 5292. In the coupled protocol, averaging normalizations differ from those of a standalone body; the table compares endpoint supports rather than claiming unchanged isolated dynamics.

The checker verifies GL=LG=N block by block. There are 5184 positive-weight closed three-step cycles, one for each feedback arrow. Their union covers every one of the 7128 directed arrows. Their weights sum to one.

This is an explicit extension of the earlier dense protocol. The pair's previously specified sparse seed-comparison transition is recorded separately below.

## Existing seed-comparison transition

The original pair construction specified M=I-L/6 on the 24 generated triangle positions. Counting its ordered endpoints gives:

- 60 arrows within each body, including twelve self-loops;
- 24 directed arrows between bodies;
- 144 arrows altogether, or 120 when self-loops are excluded.

The previously reported twelve cross-exchange edges were **undirected pairs**. They represent twenty-four directed arrows.

Collapsing each body to one coarse node leaves two directed cross-arrows, or one undirected link. That quotient merges twelve different endpoint pairs. Its link count cannot replace the primitive ledger.

## Retained geometric assembly ledger

The shared positive cell refinement has eight core tetrahedra and four tips per body. Record both directed orientations of every edge used in any retained cell; canceling an internal face does not erase an interaction that was already used.

| Cell support | Directed geometric arrows |
|---|---:|
| Shared core | 36 |
| Complete body A | 60 |
| Complete body B | 60 |
| Union, shared arrows counted once | 84 |
| Added by B beyond A | 24 |

Each of the four new apex vertices has three midpoint neighbors. Both arrow orientations occur in the closed face assembly. The contribution is therefore

    4*3*2 = 24.

Every geometric arrow is assigned an explicit three-step closed walk on an oriented face of a positive retained tetrahedron. All sixteen cell-addition stages are rerun; each retains a positive volume and a closed manifold boundary.

The 84-edge ledger concerns the retained positive cell complex. It does not automatically include every intermediate coordinate calculation, every alternative centroid-fan presentation, or the formation of every spectral coefficient.

## Conclusion for the proposed pair

The current construction gives two extended, congruent bodies coupled across a shared octahedral core. Its additional branch has multiple new primitive endpoints and arrows. One common identity eigenline does not turn those arrows into a single primitive interaction.

The explicit ledgers reject 1836+1 for this candidate. A total seed-to-operator construction count is a further compilation task, not one of the numbers above.

## Reproduction

    python research/nima/checkers/check_twenty_four_triangle_shared_seed.py
    python research/nima/checkers/check_pair_arrow_ledger.py

Artifacts:

- `results/pair-arrow-ledger.json`: partitioned counts and all geometric stage increments.
- `results/pair-dense-7128-arrows.json`: all directed coefficient arrows and their exact complex weights.
- `results/pair-geometric-arrows.json`: all retained geometric arrows and closed-walk witnesses.
