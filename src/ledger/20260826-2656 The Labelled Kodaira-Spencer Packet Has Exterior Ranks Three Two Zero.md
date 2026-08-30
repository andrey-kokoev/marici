# 2656 — The Labelled Kodaira--Spencer Packet Has Exterior Ranks Three, Two, Zero

## Construction

Using Entry 2654's conormal basis, define the three source-labelled sections

\[
\kappa_j=(\partial_jg_1,\ldots,\partial_jg_4)\in I/I^2\simeq R^4.
\]

Their polynomial coefficients are reduced in the seven-dimensional quotient,
while all four generator labels are retained. The checker forms the three pair
wedges and the triple wedge in the conormal exterior algebra.

## Replicated result

At A, B, and HOMA, with two-prime replication at A:

\[
\operatorname{rank}\langle\kappa_1,\kappa_2,\kappa_3\rangle=3,
\]

\[
\operatorname{rank}\langle
\kappa_1\wedge\kappa_2,
\kappa_1\wedge\kappa_3,
\kappa_2\wedge\kappa_3
\rangle=2,
\]

and

\[
\kappa_1\wedge\kappa_2\wedge\kappa_3=0
\]

termwise in all four labelled (Lambda^3R^4) components.

Each run has one unique kinematics-dependent relation among the three pair
wedges.

## Narrow conclusion

The base motion is three-dimensional over the ground field but has conormal
rank two over (R). Therefore the first and only nontrivial higher
Kodaira--Spencer grade is the two-dimensional pair-wedge packet. There is no
independent triple-grade class.

The mixed curvature from Entry 2648 is a two-form and now has a correctly
typed possible target. The next finite gate is to derive the primitive/Koszul
map from the visible curvature into this pair-wedge packet and test whether
the total cone curvature is nullhomotopic. Matching dimensions alone is not
evidence.

## Artifacts

- `research/benincasa/cm-conormal-kodaira-spencer-ranks.md`
- `research/benincasa/checkers/check_cm_conormal_kodaira_spencer.py`
- `research/benincasa/results/cm-conormal-kodaira-spencer.json`
- `research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs`

Ledger sequence claim: `seqclaim-c97a30665a08a9083d4d3a5d`.

Epistemic event: `ev-000000004035-6208f091-0160-4ce0-acf3-26abc864cfa6`.
