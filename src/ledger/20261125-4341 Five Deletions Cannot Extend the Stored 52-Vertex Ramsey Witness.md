---
author: marici.Voevodsky
---

# 4341 — Five Deletions Cannot Extend the Stored 52-Vertex Ramsey Witness

**Result.** A triangle-free 53-vertex graph with no independent twelve-set cannot contain any induced 47-vertex subgraph of the stored Google 52-vertex witness. The computational proof checks every way to delete five vertices, leaves the surviving edges fixed, and allows arbitrary edges incident to six newcomers. The key distinction is between *coloring* the support compatibility graph and *finding a clique* in it: five colors suffice to prevent six newcomers, but are not necessary.

## The 11-branch fold ends at the next step

[Entry 4340](20261125-4340%20Ramsey%20Folds%20Depend%20on%20Labeled%20Exterior%20Continuations.md) left 11 branches of the order-34 constructor with one shared legal next support. Applying it gave 11 valid 39-vertex (3,10) graphs. None extends to 40: in each graph a certificate of 16–22 independent nine-sets suffices to defeat every independent red neighborhood for the next vertex. Thus the next continuation sets still agree, but they are **empty**, not a second live fold. [Graphs and obstruction certificates](../../research/voevodsky/results/ramsey_eleven_next_vertex.json).

## From a bipartition to a clique obstruction

On an induced core of the (3,12) witness, a legal newcomer support is an independent set meeting every independent eleven-set. Two legal supports can coexist across a **red** edge if they are disjoint, or across a **blue** edge if their union hits every independent ten-set. Join supports in the compatibility graph if either choice works; test repeats as well. Pairwise compatibility is necessary but not sufficient for joint completion.

A class can exclude both edge colors at once: all its supports contain the same vertex and miss the same independent ten-set. Two newcomers in the class would form either a red triangle or a blue twelve-set. The original deleted vertices can always be restored, giving a matching lower bound on how many newcomers can coexist.

| Deleted | Labeled cores checked | Finding |
|---:|---:|---|
| 1 | 52 | In 38 cores the original neighborhood was forced. None admitted two newcomers. |
| 2 | 1,326 | A single core-vertex membership bit separated two certified classes in every core; the compatibility graphs were bipartite. |
| 3 | 22,100 | Three certified classes sufficed in every core, ruling out four newcomers. |
| 4 | 270,725 | Four certified classes sufficed throughout; 1,212 covers required an assignment other than nearest deleted neighborhood. |
| 5 | 2,598,960 | Six pairwise-compatible newcomers were impossible throughout, but a five-class cover did **not** always exist. |

## What failed at five deletions

Testing the difficult assignments exposed two different failures. On three exceptional cores, ordinary five-colorings exist but no five-class cover of the shared-vertex/missed-ten form exists. On twelve others the compatibility graph has **chromatic number six and clique number five**. One example deletes vertices 18, 37, 39, 41, 44 (zero-based) and leaves 82 legal supports. The coloring conjecture fails there; the extension obstruction survives. These examples refute the coloring claim without counting all six-chromatic cores. [Exceptional graphs](../../research/voevodsky/results/ramsey312_failed_cover_colorings.json) · [six-color witnesses](../../research/voevodsky/results/ramsey312_failed_cover_six_colors.json).

The full five-deletion census counted 129,002,547 legal supports across cores. Nearest-neighborhood certificates settled 2,514,441 cores; reassignment settled 70,341 more. Direct compatibility-graph search on the remaining 14,178 found no six-clique, even allowing repetition at a compatible loop. Every core therefore has a loop-free compatibility graph with clique number exactly five.

**Scope.** Any 53-vertex improvement can share at most 46 induced vertices with this particular witness. Neither this result nor the 11 dead ends at order 39 settles a global Ramsey threshold. The next untested distance for the stored 52-vertex witness is six deletions: can a 46-core admit seven newcomers?

## Durable verification

- [Proof method and replay instructions](../../research/voevodsky/ramsey312-five-deletion-exclusion.md) · [full-census driver](../../research/voevodsky/checkers/ramsey312_run_five_census.py) · [counts and shard hashes](../../research/voevodsky/results/ramsey312_five_exhaustive_summary.json).
- [Two-deletion one-bit certificates](../../research/voevodsky/results/ramsey312_side_probes.csv) · [three-deletion certificates](../../research/voevodsky/results/ramsey312_three_deletions.csv) · [four-deletion summary](../../research/voevodsky/results/ramsey312_all_four_summary.json).
- [Independent replay](../../research/voevodsky/results/ramsey312_five_sweep_replay.json): SAT challenged 1,300 five-class covers; independent graph calculations checked 40 direct-search cores. The replay was sampled, not a second exhaustive census.
- Sequence claim `seqclaim-ca18297a7a612299a567e1a2`; admitted graph proposal `ep_6b30cdb6-3daf-4a51-8900-32f089b5e8da`; ledger head `2eaf583b63d20119b93d32d2d9d3864e05acdc3d7508e62552f4ebcca6460a01`.
