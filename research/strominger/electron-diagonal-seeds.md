# Electron five-cycle: all ten directed diagonal additions

## Experiment

Operator conjecture: take the electron seed and add BD or DB; run both through the assembler. Baseline is A->B->C->D->E->A with the existing `relative-electron.json` metric and attachment pole unchanged.

The relative assembler takes affine generators, not raw arrows. This experiment explicitly uses the existing arrow-seed convention: every simple directed cycle acts as its cyclic vertex permutation, fixing other vertices. The adapter retains all resulting generators, with the original five-cycle first in the schedule. No particle label or requested geometry selects a result.

## Fresh results

| Input | Additional cycle | Additional determinant | Generated permutation group | Shared assembly | Scheduled return |
|---|---|---:|---:|---|---:|
| Baseline, 5 arrows | none | — | 5 | regular four-simplex | 5 applications |
| +BD, 6 arrows | B->D->E->A->B | -1 | 120 | rejected | not constructed |
| +DB, 6 arrows | B->C->D->B | +1 | 60 | same regular four-simplex | 10 applications |

The +BD group count is a permutation calculation before admission, not an assembled geometry. Its new four-cycle reverses orientation on the supplied four-dimensional affine span. The unchanged shared assembler rejects it with `Generator is not orientation preserving`. Dropping that cycle would silently discard the mutation and merely replay the baseline; that is not counted as an assembly of +BD.

The +DB triangle is a proper isometry. Together with the five-cycle it generates A5 (60 permutations). The generated vertices, supporting facets, attachment, center cones, metric and distances are exactly equal to baseline. It still has five vertices, five supporting tetrahedral facets and five center cones. All five facet centroids are active. Its new two-generator schedule has word order five, hence ten individual applications per scheduled word return. The entire reversed centroid history recovers exactly.

Both mutations have six primitive occurrences and incidence-kernel dimension two, versus five occurrences and kernel dimension one in the baseline. They therefore change retained arrow data even when one geometrically completes to the same shape.

## AD/DA follow-up

Freshly reran baseline and all four single-arrow additions with the same metric,
attachment pole and cycle adapter.

| Addition | New cycle | Determinant | Result | Scheduled return |
|---|---|---:|---|---:|
| AD | A->D->E->A | +1 | same four-simplex, group order 60 | 10 applications |
| DA | A->B->C->D->A | -1 | orientation rejection, permutation group order 120 | not constructed |

AD and DB have equal completed geometry and return-step count, but different
labelled centroid traces. The new triangle ADE includes the marked seed A,
whereas BCD does not. No equivalence of their entire marked histories is claimed.
The contrast again follows the length/parity of the newly closed cycle, not
whether the added arrow points toward or away from a chosen vertex.

## AC/CA follow-up

The same run now covers baseline and all six single-arrow mutations. AC closes
A->C->D->E->A, a determinant -1 four-cycle, and is rejected. CA closes
A->B->C->A, a determinant +1 triangle, and is accepted. CA gives the same
four-simplex, group order 60 and ten-application scheduled return as AD/DB,
with its own distinct labelled centroid trace and verified reverse recovery.
No source metric, attachment mark or admission rule changed.

## EC/CE/EB/BE: completion of the diagonal census

| Addition | New cycle | Result |
|---|---|---|
| EC | C->D->E->C | accepted |
| CE | A->B->C->E->A | orientation rejection |
| EB | B->C->D->E->B | orientation rejection |
| BE | A->B->E->A | accepted |

Both new accepted cases retain the same complete geometry, group order 60,
ten-application schedule and exact reverse recovery. This exhausts the ten
directed diagonals (not reverse copies of perimeter edges or loops). Five
triangle-closing directions are admitted: DB, AD, CA, EC, BE. The five opposite
directions close four-cycles and are rejected. A k-cycle has determinant
(-1)^(k-1) in the supplied simplex representation; the observed split follows
from the proper-isometry rule rather than a particle-specific filter.

## Disposition

Direction matters under the declared cycle-isometry interpretation. DB is admitted and enlarges the action without changing the completed carrier. BD is rejected by the existing orientation requirement; no metric or rule was changed to accommodate it.

The ten-step schedule is a measure of the supplied generator-list procedure, not a derived physical period. This experiment runs the geometric assembler and its full centroid-cycle wrapper, not the separate four-face electron spinor producer; no new coefficient-transfer count or particle identification is inferred.

## Verification

```sh
python research/strominger/checkers/check_electron_diagonal_seeds.py
```

All 50 checks passed, including exact baseline replay, all ten added-cycle lists, exhaustive directed-diagonal coverage, determinant controls, accepted-case geometric equality and inverse recovery. Receipt: `research/strominger/results/electron_diagonal_seeds.json`, containing the primitive arrows, adapted sources, complete accepted cycle traces, rejection reason and source hashes. Shared constructor code and established stores were not changed.
