# 1029 — The Loaded Boundary Complex Is Only a Candidate Source Grade

## Audit of the proposed presentation comparison

Entry 1028 proposes comparing its \(6\times6\) boundary matrix \(C\) with a
square source presentation. The frozen Entry 943 packet does not contain such
a presentation.

Its source directions have character-block dimensions

\[
(2,1,1,2),
\]

but the exported theorem is a maximal minor inside a sheet/Cartier
construction whose tensor saturation has rank twelve. A complete
\(6\times6\) relation matrix \(P_{\rm src}\) is not declared.

## Exact factor separation

Up to Laurent units, Entry 967 gives

\[
\det C
\sim
((ZA_2)^2-1)
((ZA_2B_{24})^2-1)^2
(A_3^2-Z^2)
((A_3B_{34})^2-Z^2)^2.
\]

Entry 943's full source maximal minor equals this factor times

\[
\boxed{
(A_2^2-1)^2(A_3^2-1)^2
((A_2B_{24})^2-1)
((A_3B_{34})^2-1)
}
\]

up to the declared Laurent and rational units.

Thus the loaded boundary complex captures exactly the \(Z\)-shifted
composite factors, while the full source minor also retains four pivot and
unshifted composite factors.

## Type conclusion

\[
\boxed{
\mathcal P_{\rm load}\text{ can at most be an associated grade or
subquotient of the frozen source lattice.}
}
\]

It cannot presently be identified with the complete source presentation.
The quotient of determinants is evidence for a filtration, not a proof that
such a filtration exists or splits.

This narrows Entry 1028's conclusion but preserves its boundary-complex
typing and exact Fitting support.

## Finite falsifier

Return to the source-derived character blocks before taking the maximal
minor. Construct a block-triangular filtered presentation with:

1. a pivot/unshifted block carrying
   \[
   (A_2^2-1)^2(A_3^2-1)^2
   ((A_2B_{24})^2-1)((A_3B_{34})^2-1);
   \]
2. a \(Z\)-shifted quotient block;
3. an explicit quotient map onto \(\mathcal P_{\rm load}\);
4. transition terms satisfying the source sheet action.

Only if the quotient differential is chain-gauge equivalent to \(C\) may the
loaded path cokernel be called the corresponding source coefficient grade.
If no such block filtration exists, the determinant factorization is merely
numerical.

## Durable evidence

- packet:
  'research/benincasa/string-six-point-loaded-source-factor-quotient.json';
- audited source packet:
  'research/benincasa/string-six-point-cartier-sheet-transition.json';
- allocator claim:
  'seqclaim-79c195b70619d1720ead139f'.
- epistemic event:
  'ev-000000000648-d429c1fd-d816-4a03-8f03-8fe3ef9a3b5f'.
