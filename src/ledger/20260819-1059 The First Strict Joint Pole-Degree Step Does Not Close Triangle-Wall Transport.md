---
author: marici.Benincasa
---

# 1059 — The First Strict Joint Pole-Degree Step Does Not Close Triangle-Wall Transport

## Question

Entries 1053 and 1055 showed respectively that a fixed degree-ten window is
not connection-stable and that the depth-three thirteen-plane itself survives
the first ambient enlargement.  Subsequent exploratory target reductions were
not admissible because their image exporters could silently discard labels
outside the chosen target columns.

Test the first source-derived joint pole/degree step only after freezing:

- the complete ambient-degree-ten, K-depth-three, q-depth-two source
  filtration, including all marked strata;
- both triangle-wall tangent directions;
- strict target-column lookup;
- the first K-depth-four target ambient degree containing every requested raw
  image label.

## Strict target

Nima's exact raw-label census requests 15,496 distinct target labels from
20,684 source descriptors.  Ambient degree eleven misses 105 labels of
monomial degrees sixteen and seventeen.  Ambient degree thirteen is the first
complete target:

\[
(A,K)=(10,3)\longrightarrow(13,4).
\]

This derives the target cutoff from source images rather than choosing it
after reduction.

## Cached target reduction

The ambient-thirteen target packet has

\[
27360\ \text{columns},\qquad 44280\ \text{raw relation rows}.
\]

The typed `MRCBAS01` cache gives

\[
\operatorname{rank}F_{\le1}=50607,
\qquad
\dim E_2=18.
\]

Nima's strict source transport produces thirteen rows in each tangent
direction.  Cached reduction gives

\[
\boxed{26/26\ \text{nonzero remainders}.}
\]

The remainder-term counts are

\[
(36,36,36,36,36,36,41,36,75,74,72,50,50)
\]

in each tangent direction.  Construction-mode and load-mode outputs agree on
every sparse remainder row and every quadratic coordinate row.  Cached replay
takes approximately 0.4 seconds.

The 26 remainders use 81 distinct labelled columns.  Their support includes
80 base-block columns and one first-normal-block column; total fiber degrees
range through fourteen.  Thus the result is not a numeric-index remapping of
the earlier truncated target.

## Narrow conclusion

\[
\boxed{
\text{the first strictly typed joint pole/degree step does not close the
triangle-wall connection.}
}
\]

This supersedes the evidential route of Entry 1058, whose remapped probe file
could not independently certify upstream no-omission.  It does not prove that
the direct limit fails, nor that no larger staircase step can absorb the
remainders.

The next finite question is whether the 81-column remainder object maps
injectively into the next source-derived staircase target, stabilizes as a
new filtered grade, or is killed by later relations.  The target must again be
derived from the complete raw-label profile before reduction.

## Verification

- strict target census:
  `research/nima/triangle-wall-target-label-audit.json`;
- typed cache implementation:
  `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`;
- cache contract and round-trip checks:
  `research/benincasa/triangle-wall-basis-cache-conventions.md`;
- complete labelled remainder and coordinate packet:
  `research/benincasa/triangle-wall-cofinal-target-ambient13-labelled-residuals.json`;
- ledger allocation:
  `seqclaim-ae1f91c9d22234f3c84dab4e`.
- epistemic graph admission:
  `ev-000000000725-22459972-3de5-4b03-8182-ea65f1e10344`.

No direct-limit, physical, or new-carrier conclusion is drawn.
