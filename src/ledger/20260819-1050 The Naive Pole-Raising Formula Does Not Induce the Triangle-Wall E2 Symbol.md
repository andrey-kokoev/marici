# 1050 — The Naive Pole-Raising Formula Does Not Induce the Triangle-Wall E2 Symbol

## Question

Entries 1046 and 1049 leave a typed frontier:

\[
\theta_T:
E_2^{K\le3}/E_2^{K\le2}
\longrightarrow
E_2^{K\le4}/E_2^{K\le3}.
\]

Test the smallest candidate construction: on each source-relation
representative, retain only the degree-plus-one Cayley--Menger pole term

\[
r_k\longmapsto (\gamma-k)T(K)r_{k+1},
\]

then reduce its normal two-jet in the complete depth-four exact-valuation
presentation.

## Frozen representatives and target

The depth-three grade has its intrinsic one-plus-five representatives

\[
722;qquad
15362,15363,15364,15365,15370.
\]

They were transported for both triangle-wall tangents

\[
T_1=\partial_{X_1}+\partial_{X_3},
\qquad
T_2=\partial_{X_2}+\partial_{X_3}.
\]

All twelve images were reduced in one shared exact batch over
\(\mathbf F_{32003}\) against Entry 1049's depth-four packet, whose
exact-valuation-two rank is nineteen.

## Result

Every candidate image has a nonzero remainder:

\[
\boxed{
12/12\text{ provisional images fail the depth-four }E_2\text{ typing gate.}
}
\]

Each reduction nevertheless has eighteen tracked coordinates in the
nineteen-dimensional target basis.  Those coordinates are not a symbol
matrix: the surviving remainder prevents descent to the quotient.

Therefore the formula

\[
r_k\mapsto(\gamma-k)T(K)r_{k+1}
\]

does not by itself define the map proposed in Entry 1046.  In particular,
one may not project away the remainders and read a fitted \(6\times6\)
connection.

## Interpretation

Entry 1049 proves the injective pole-depth tower

\[
7\hookrightarrow13\hookrightarrow19,
\]

but an inclusion of exact-valuation spaces is not a Gauss--Manin comparison
between consecutive grades.  The missing datum is a chain-level filtered
connection together with its coherence on the de Rham and principal
relations.  The derivative of the pole factor alone is insufficient.

This does **not** falsify existence of a typed symbol \(\theta_T\), nor the
filtered-tower interpretation.  It falsifies only the minimal relation-wise
pole-raising construction.

## Next finite test

Construct the complete tangential derivative of the labelled exact complex,
including derivative terms in every relation family and a homotopy witnessing
compatibility with the relation differential.  Only after that chain map is
verified may its associated-grade map be reduced modulo the depth-three
inclusion.

## Durable verification

- provisional image exporter:
  `research/benincasa/export_triangle_wall_pole_symbol_images.py`;
- twelve source images:
  `research/benincasa/triangle-wall-depth3-to4-symbol-images.json`;
- shared exact reduction:
  `research/benincasa/triangle-wall-depth3-to4-reduction.json`;
- batch-probe support:
  `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`;
- allocator claim: `seqclaim-b8e865fbd3007ec0c227c687`.
- epistemic graph event:
  `ev-000000000681-5ab68441-5942-4a7d-9962-3da79fc52e38`.
