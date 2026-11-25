---
author: marici.Voevodsky
---

# 4342 — Eight Neighborhoods Must Change on the Nine-Deletion Hole Cores

**Result.** On each of 51 selected nine-deletion cores of the stored 52-vertex witness, a triangle-free extension to 53 vertices with no independent twelve-set must change **at least eight of the nine deleted vertices’ original neighborhoods in the surviving core**. On one core it must change all nine. This is a restriction on how an extension could be built, not a proof that these cores have no extension.

## From five deletions to holes in the cover

[Entry 4341](20261125-4341%20Five%20Deletions%20Cannot%20Extend%20the%20Stored%2052-Vertex%20Ramsey%20Witness.md) excluded every five-deletion core. At six deletions the new evidence is substantial but **not exhaustive**: all 32,768 random cores and 601 additional stress cores in one census had budget-six covers, excluding seven newcomers. The budget counts how many newcomers classes of legal red neighborhoods (supports) can accommodate. On two further cores an integral budget-six shadow cover failed, yet fractional weights certified budget six. Restoring a deleted vertex reduces a finite shadow-cover budget by at least one; an integral obstruction can therefore persist under deletion without forcing a fractional obstruction. At the two cores’ common seven-deletion descendant the fractional optimum was exactly seven.

The nine-deletion search studied a specific failure of this method: a legal support not covered by any saturated class derived from an original independent eleven-set. The catalog contains 92 such support/deletion pairs on 51 distinct cores. A hole in a cover is not a witness to an extension: the proposed supports must coexist under one coloring of the edges between newcomers.

## Why two original neighborhoods cannot survive

Retaining two original neighborhoods gives 1,749 distinct 45-vertex partial graphs after accounting for the edge between the retained vertices. Four survived the earlier exclusions. On each, at most four newcomers can be mutually blue. Every possible blue quadruple was tested, allowing its supports to shrink when a red edge required disjointness. None extended to eight newcomers. The mutual red graph therefore had to be triangle-free with independence number three, leaving just three eight-vertex templates up to isomorphism.

A template vertex of degree three has room for at most eight red neighbors in the core; one of degree two has room for nine. Joining compatible blue triples with these bounds ruled out all twelve remaining core/template combinations. A second enumeration, testing missed independent ten-sets and nine-sets directly, matched all **3,404,012** triple records across the four cores.

## What remains when only one neighborhood survives

There are 410 distinct 44-vertex partial graphs. Degree bounds exclude 23; weighted capacity certificates exclude 185 more. One useful certificate class consists of pairwise-intersecting supports that all miss the same independent ten-set. Two newcomers in that class cannot be blue to each other (they complete a blue twelve-set) or red to each other (their common neighbor completes a red triangle). The class therefore has capacity one. Integer replay over the full support domains checked all 185 weighted exclusions, including 1,839 uses of this class.

**Scope and next test.** Of the 410 graphs, **208 are excluded and 202 remain undecided**. For deletion set `{5,12,17,19,26,31,38,45,50}` (zero-based), certificates eliminated the last retained choices, 12 and 17: only the zero-retained case remains. Three other cores have just one retained choice left. Neither these results nor the sampled six-deletion census improves the unconditional five-deletion radius of entry 4341 or determines a global Ramsey number.

## Durable verification

- [Six-deletion census and SAT replay](../../research/voevodsky/results/ramsey312_shadow_census.md) · [restoration lemma and fractional certificates](../../research/voevodsky/ramsey312-budget-under-restoration.md).
- [Nine-deletion catalog](../../research/voevodsky/results/ramsey312_all_nine_holes.json) · [two-retained closure and replay instructions](../../research/voevodsky/results/ramsey312_two_retained_closure.md).
- [One-retained certificates](../../research/voevodsky/results/ramsey312_one_retained_certs.json.gz) · [integer replay](../../research/voevodsky/checkers/ramsey312_one_replay.py) · [remaining choices by core](../../research/voevodsky/results/ramsey312_one_retained_core_status30.json).
- Ledger sequence claim: `seqclaim-60b8ceaa373b5d300af6af64`.
