# 2659 — Curvature Does Not Factor Through the Kodaira–Spencer Pair-Wedge Packet

## Frozen question

Can the three visible curvature components

\[
(F_{12},F_{13},F_{23})
\]

factor base-linearly through the labelled conormal pair-wedge packet

\[
(\kappa_1\wedge\kappa_2,\kappa_1\wedge\kappa_3,\kappa_2\wedge\kappa_3)?
\]

Such a factorization must preserve every relation among the three base two-form labels. This is a necessary condition, not a sufficient construction of a Koszul cone.

## Exact finite test

The source-labelled Kodaira–Spencer pair wedges have rank two and one kinematics-dependent relation at every tested run. The corresponding three curvature matrices were flattened without changing their base labels and tested for the same relation, for both curvature-sign conventions.

Across points A, B, and HOMA and primes 32003 and 65521:

\[
\operatorname{rank}\langle\kappa_1\wedge\kappa_2,
\kappa_1\wedge\kappa_3,
\kappa_2\wedge\kappa_3\rangle=2,
\]

while

\[
\operatorname{rank}\langle F_{12},F_{13},F_{23}\rangle=3
\]

for both signs.

## Narrow result

Therefore no base-linear map from the tested Kodaira–Spencer pair-wedge packet can produce the visible curvature triple. The unique relation in the proposed source packet would have to survive, but the target triple has no relation.

This rejects the proposed direct factorization and blocks construction of a large cone based on it. It does not reject the full conormal/Koszul object, nor does it prove that curvature lacks a derived home. Any surviving construction must contain an additional typed coherence operation that breaks the pair-wedge relation only after passing through a larger complex; it cannot be inferred from the three pair wedges alone.

## Artifacts

- `research/benincasa/checkers/check_cm_curvature_ks_relation.py`
- `research/benincasa/results/cm-curvature-ks-relation.json`

## Next falsifier

Inventory the source-defined operations adjoining the principal generator and Koszul degree-one/degree-two cells, and test whether their actual differential supplies a third independent base-two-form channel. Do not add a free curvature cell merely to repair this rank mismatch.
