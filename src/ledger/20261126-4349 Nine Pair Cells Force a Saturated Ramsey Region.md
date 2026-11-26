---
author: marici.Voevodsky
---

# 4349 — Nine Pair Cells Force a Saturated Ramsey Region

[Entry 4348](20261126-4348%20Cube%20Incidence%20Constructs%20the%20Ramsey%20Gain%20from%2027%20to%2035.md) asked how much cube incidence a repair can erase. We now have a sufficient condition that does **not** prescribe cube neighborhoods: at a root of a legal 35-vertex coloring, **eight singleton cells and at least nine two-label cells force a saturated four-label region**. This forces a particular 13-vertex subgraph, not the whole cube. A separate transcript check also identifies the conjecture that produced the Excel fold; it was not the rooted-graph conjecture.

## What forces the 13-vertex region?

“Legal” means red-triangle-free with no blue nine. Each vertex has red degree eight. Fix a root, label its eight red neighbors, and give each of its 26 blue neighbors (the core cells) the labels it sees in red. Four labels can be blue to at most nine core cells: ten would give a 14-vertex triangle-free graph without a blue five, contradicting \(R(3,5)=14\). Attaining nine is *saturation*. The four labels and nine cells then induce the unique 13-vertex (3,5) graph. In the known witness exactly six choices attain nine at each root.

Regularity and the 76-edge core budget alone do not force saturation: the unanchored search produced triangle-free, degree-correct examples below the cap, but they contained blue nines. Joint feasibility matters even when every individual demand passes. On one fixed incidence pattern, 52 five-label regions could pass **pairwise**, but at most 48 could pass on **one coloring**. Some conflicts already force opposite colors on one edge; others require comparing two or three edge decisions together. [Unanchored control](../../research/voevodsky/results/ramsey_unanchored_saturation.json) · [Joint-capacity audit](../../research/voevodsky/results/ramsey_unsaturated_pair_gap.json).

For the exact-nine-pair case, the pair cells form a triangle-free graph on the eight labels. The other nine cells use 30 incidences, forcing at least six triples. Marking six triples gave an exhaustive search over all 76 pair-graph types (1,163,540 labeled graphs), without fixing the core edges. In the last 18 types, 874 marked configurations admitted 339,846 fillings of the remaining label counts. Every filling had at least one cell that failed even when tested separately on the fixed configuration. No timeout counted as an exclusion. Together with the earlier stages this settles **at least nine** pairs. [Twelve-pair screen](../../research/voevodsky/results/ramsey_unsaturated_pair_graphs.json) · [Eleven](../../research/voevodsky/results/ramsey_eleven_coverage.json) · [Ten](../../research/voevodsky/results/ramsey_ten_coverage.json) · [Nine](../../research/voevodsky/results/ramsey_unsaturated_nine_final.json).

## Global restrictions learned along the way

These results do **not** assume eight singleton cells or saturation. The computational exclusions use completeness of the cited predecessor catalogues.

- **Two vertices share at most four red neighbors.** Five would require a 22-vertex common blue graph. Its edge budget leaves seven catalogue types: six fail one side's attachment test, and on the seventh none of the 116 admissible attachments can be paired across the required red edges. The known witness attains four. [Enumeration and independent check](../../research/voevodsky/ramsey35-common-neighbor-bound.md).
- **Three vertices share at most three red neighbors:** there is no red \(K_{3,4}\). Four common neighbors would give three disjoint private fours and require a marked vertex absent from both possible 21-vertex edge layers. In particular, a quartet mask cannot repeat. Also, five mutually blue singleton cells are impossible: the other 21 cells would each have to use exactly one of the three remaining labels, leaving the seven cells on one label blue to both others. [Proof and catalogue scan](../../research/voevodsky/ramsey35-three-common-neighborhoods.md).
- **A red \(K_{3,3}\), if one exists, leaves at most one vertex blue to all six.** Call a same-side pair *doubled* if it has a fourth common red neighbor. For doubled-pair counts \((a,b)\), the number of vertices blue to all six is \(a+b-1\). Only \((0,1),(0,2),(1,1)\) remain up to exchange. In the last exclusion, \((1,2)\), all 14,945 locally admissible identifications failed agreement on shared edges. For quartet cells sharing three labels this means no further cell may contain two of those labels. It does **not** exclude that overlap or \(K_{3,3}\) itself. [Derivation and verification](../../research/voevodsky/ramsey35-three-by-three-one-two.md).

**Open target.** With eight singletons, the only remaining unsaturated profiles are six pairs + twelve triples; seven pairs + ten triples + one quartet; or eight pairs + eight triples + two quartets. The six-pair case is the clean next test: it has no quartets, so further classification of quartet overlaps cannot settle it. In the conjecture net, saturation is a stronger follow-up to the [rooted-core-size-crossover work](../../research/voevodsky/RAMSEY-RELATIONAL-LIFT.md), not a new verdict on that node or on `natural-hypercube-representation`.

## Provenance correction: why the Excel formula folds `RBBR`

The November 25 Pi transcript identifies the originating proposal as the **Ramsey Mirror-Completion Conjecture**, renamed the **Ramsey Symmetry-Repair Conjecture** when slides were allowed. The motivating question was whether the correction in \(R(3,7)=2(3+7)+3\) measured the cost of restoring half-turn symmetry to an ordered table. At width seven, three insertions worked; a different repair used two insertions and one slide. Whether slides cost anything therefore changes the conjecture.

The exact Excel formula answered a narrower request: *could four rows of the 32-row width-eight display be collapsed to give 28?* Identical tails witness reversible `RB`/`BR` alternatives. Requiring `RBBR` in the tail selects two upper pairs and their two mirrors; 28 displayed records expand back to all 32 rows. Folding **every** valid pair would instead give 20 records while preserving symmetry. Thus the fold is lossless, but the two-blue-gap selector was chosen **after** the target was stated. At width nine the same formula gave 56, not 36. The later independent-swap squares and cubes are documented in [entry 4339](20261125-4339%20Fresh%20Corners%20of%20Overlapping%20Ramsey%20Table%20Cubes.md); neither they nor the rooted saturation theorem derive a Ramsey threshold from the spreadsheet.

Transcript locator: Pi session `01a05810-d01e-796d-9628-5f79ec531176`, messages on 2026-11-25 UTC; JSONL lines 154171–154181 (proposal and naming), 154234–154238 (request and exact formula, 06:21:50 UTC), 154241–154247 (verification and width-nine failure).

Ledger sequence claim: `seqclaim-d6b0435f770bb60b4fdc89d4`.
