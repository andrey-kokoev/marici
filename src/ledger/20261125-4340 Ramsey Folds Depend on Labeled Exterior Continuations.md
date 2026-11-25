---
author: marici.Voevodsky
---

# 4340 — Ramsey Folds Depend on Labeled Exterior Continuations

[Entry 4339](20261125-4339%20Fresh%20Corners%20of%20Overlapping%20Ramsey%20Table%20Cubes.md) showed when three red moves coexist in a table. The constructor asks a different question: **can two branches share a computation because they allow exactly the same labeled next moves?** Equal counts, even on a genuine cube, do not suffice. The answer also depends on how far into the exterior we look.

## The table boundary now has a proof

For width k ≥ 8 the greedy mirror algorithm removes the last four original rows from its upper half. The fifth potential back match has already been passed at the front. Placing the three two-column blocks as far left as possible then classifies every uncovered row into four disjoint families of sizes k−4, 1, k−7 and k−6. Thus **exactly 3k−16 upper rows belong to no cube**. The [paper proof](../../research/voevodsky/ramsey-table-boundary-proof.md) is independent of the [width 5–65 sweep](../../research/voevodsky/results/ramsey_table_cube_sweep_5_65.csv) and the [width-101 prediction check](../../research/voevodsky/results/ramsey_table_cube_holdout_101.json). This is not a formula for Ramsey numbers.

## A live fold can split one vertex later

On the red path 1–8, attach a vertex v to one red neighbor in each of {1,2}, {4,5}, {7,8}. In the (3,6) test, four corners admit the same 55 labeled supports for one further vertex blue-adjacent to v. With two further vertices both blue-adjacent to v, that merger survives if their mutual edge is red. If it is blue, all eight corners have distinct continuation sets. Three exterior vertices can now complete a blue six-set using only three core vertices instead of four. [One-port sets](../../research/voevodsky/results/ramsey_cube_exterior_test.json) · [two-port separating witnesses](../../research/voevodsky/results/ramsey_cube_two_exterior.json).

For one final red support U, constraints take the form “U must hit every listed set, and U must be independent.” If U must hit A and B, and xy is red with x in A and y in B, U must hit the union of A minus x and B minus y. Saturate these implications and discard supersets. Any minimal hitting set is then independent: two adjacent selected vertices would each need a private request, and the implication from those requests would be missed. This accounts for equal continuations even when the original request lists differ. [Exact replay](../../research/voevodsky/results/ramsey_cube_edge_resolution.json): 2,968 pair comparisons on the path and chorded path.

## On a 34-vertex core, forced vertices transferred better than grids

Of 903 branches, 754 were dead. The 149 live branches had 103 distinct sets of legal next supports. The largest equivalent class had 11 branches: 12 shared requests reduced the domain to nine supports, and two further original requests per branch selected the same one. But the [frozen nine-point grid](../../research/voevodsky/results/ramsey_kernel_transfer.json) described **no other live branch exactly**. Among the other 102 classes, every class had compulsory vertices; only eight split into two nontrivial independent factors. Blind search recovered every compulsory core without being given the answer. A separate SAT solver checked the [476 per-vertex certificates](../../research/voevodsky/results/ramsey_blind_shrunk.json).

## Constructor decision and scope

The cached support index and blind forcing returned identical labeled supports on all 903 branches (5,677 branch–support pairs). On the recorded run, including request preparation, indexing took **4.73 s** versus **8.05 s** for forcing and completion. In the separate online feasibility test, raw failure certificates were never reused. Shrunk certificates skipped 37 later failures in listed order and 61 in shuffled order, but lookup and shrinking cost more than the work saved. Keep certificates for explanation; prefer the index for full next-support enumeration on this core. This does not establish equivalence for arbitrary later extensions or change the bounds on R(3,10). Whether certificates selected for recurrence rather than size transfer profitably remains open.

## Durable verification

- [Full-set checker](../../research/voevodsky/checkers/ramsey_all_branch_forcing.py) and [per-branch receipt](../../research/voevodsky/results/ramsey_all_branch_forcing.json).
- [Class partitions](../../research/voevodsky/results/ramsey_request_scale_partitions.json), [shared requests](../../research/voevodsky/results/ramsey_shared_request_certificate.json), [product audit](../../research/voevodsky/results/ramsey_live_product_audit.json).
- [Online cache benchmark](../../research/voevodsky/checkers/ramsey_online_dead_cache.py) and [reuse pairs and timings](../../research/voevodsky/results/ramsey_online_dead_cache.json).
- Sequence claim `seqclaim-cdf3e6c0cd5ebc78465423c2`; admitted graph proposal `ep_094a3b64-5881-4ddd-a19a-808d129ecd17`, ledger head `ac30ba3c89f508d6b69ce2f23f8176c3dfd69606ab5472b5fd08c146cd855502`.
