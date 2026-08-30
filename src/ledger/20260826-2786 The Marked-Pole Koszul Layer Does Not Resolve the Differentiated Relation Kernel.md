# 2786 — The Marked-Pole Koszul Layer Does Not Resolve the Differentiated Relation Kernel

## Exactness test

At the frozen generic point ((2,3,4)) and external derivative direction (x), let

\[
S:F_2\longrightarrow F_1,
\qquad
D:F_1\longrightarrow Q
\]

be respectively:

- the complete first marked-pole Koszul syzygy map from Entry 2780;
- the derivative of the complete marked-pole multiplication relation map into the finite quotient.

The labelled relation domain has dimension 25,200.

## Composition

All 21,840 source Koszul generators are composed with the full differentiated relation matrix. Every composition vanishes:

\[
DS=0.
\]

Thus the implemented sequence is a genuine complex; the following rank difference is typed homology rather than a comparison of unrelated matrices.

## Rank result

The differentiated relation map has

\[
\operatorname{rank}D=3364,
\qquad
\dim\ker D=25{,}200-3364=21{,}836.
\]

The first Koszul map has

\[
\operatorname{rank}S=14{,}295.
\]

Therefore

\[
\dim H_1
=
\dim\ker D-\operatorname{rank}S
=7541.
\]

## Narrow interpretation

The pairwise marked-pole Koszul squares do not resolve the differentiated relation kernel. Consequently they cannot by themselves make the Euler commutator preimage canonical.

The rank 7541 is not a physical coefficient rank and does not justify a new carrier object. The current complex omits independently existing relation sectors:

- Cayley--Menger multiplication relations;
- integration-by-parts relations;
- mixed syzygies among marked-pole, Cayley--Menger, and IBP families;
- possible cutoff-boundary relations of the finite presentation.

The failure therefore narrows the required constructor to the complete labelled first-syzygy complex.

## Artifacts

- `research/benincasa/check_rank26_first_syzygy_exactness.py`
- `research/benincasa/rank26-first-syzygy-exactness.json`

## Next falsifier

Adjoin only source-derived mixed syzygies involving the existing Cayley--Menger multiplication and IBP relation families. Recompute (H_1) after each predeclared family. Do not add generators selected from the 7541-dimensional residual.
