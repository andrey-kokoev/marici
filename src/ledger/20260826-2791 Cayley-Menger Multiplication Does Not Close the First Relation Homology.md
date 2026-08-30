# 2791 — Cayley–Menger Multiplication Does Not Close the First Relation Homology

## Predeclared enlargement

Enlarge Entry 2786's marked-pole relation domain by adjoining the existing Cayley–Menger multiplication relations. Adjoin only the source-derived mixed commutativity squares

\[
R_K+K R_i^{(K)}-R_i-q_iR_K^{(i)}=0
\]

alongside the marked-pole pair squares from Entry 2780.

The combined relation domain has dimension

\[
4224+25{,}200=29{,}424.
\]

## Complete mixed audit

The first-syzygy packet contains:

- 21,840 marked-pole pair squares;
- 8800 mixed Cayley–Menger/marked-pole squares.

Every generator composes to zero under the differentiated relation map. Thus the combined sequence is a genuine complex.

## Rank result

The differentiated combined relation map has

\[
\operatorname{rank}D=3397,
\qquad
\dim\ker D=29{,}424-3397=26{,}027.
\]

The combined first-syzygy image has rank

\[
18{,}257.
\]

Therefore

\[
\dim H_1=26{,}027-18{,}257=7770.
\]

## Narrow interpretation

Adding the source Cayley–Menger multiplication route does not close the first relation homology. Relative to the marked-pole-only calculation, the kernel grows by 4191 while the syzygy image grows by 3962, leaving 229 additional directions.

This comparison is diagnostic, not a decomposition theorem: the two complexes have different domains. The number 229 is not a physical coefficient rank or a new carrier object.

The remaining predeclared relation sector is integration by parts, together with its mixed coherence against both multiplication families. Finite-cutoff boundary classes must remain separately visible.

## Artifacts

- `research/benincasa/check_rank26_kq_syzygy_exactness.py`
- `research/benincasa/rank26-kq-syzygy-exactness.json`

## Next falsifier

Construct the labelled IBP/multiplication commutator identities from the frozen differential formula. Add their image to the combined complex and recompute homology. Do not infer IBP syzygies from the 7770-dimensional residual.
