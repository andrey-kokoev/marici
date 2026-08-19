# 1014 — The Dual Cellular Intertwiner Is Laurent-Unimodular

## Lattice question

Entry 1013 constructs the unique diagonal cellular intertwiner up to a global
scalar.  Could its diagonal frames hide a nontrivial integral index even
though they are invertible over the rational function field?

Use the frozen Laurent coefficient ring

\[
R=\mathbb Z[A_2^{\pm1},A_3^{\pm1},Z^{\pm1},X^{\pm1}].
\]

With (g_0=1), Entry 1013 gives

\[
D_0=\operatorname{diag}\left(
1,
\frac{A_3^2}{Z^2},
A_3^2A_2^2,
\frac{A_3^2A_2^2}{X^2},
\frac{Z^2A_2^2}{X^2},
\frac1{X^2}
\right).
\]

The edge frame (D_1) is its cyclic shift.  Therefore

\[
\boxed{
\det D_0=det D_1
=\frac{A_2^6A_3^6}{X^6}.
}
\]

This determinant is a unit of (R).  Every individual diagonal entry is also
a Laurent unit, so both maps are integral Laurent-lattice isomorphisms.

## Occurrence transport

Entry 974's frozen occurrence-to-dense map is a permutation of determinant
(+1).  Conjugating or relabelling (D_0,D_1) by this map preserves their
determinants and Laurent unimodularity.  Hence

\[
\boxed{
\text{the diagonal dual cellular comparison has finite lattice index }1.
}
\]

The minus primitive is therefore exact not only over the rational function
field but over the generic integral Laurent lattice defined by the frozen
transport variables.

## Remaining qualification

This does not prove that the diagonal comparison is the source-normalized
twisted period pairing used by the KLT construction.  Entry 974 fixes support
and labels but explicitly does not prove the complete rational transition, and
Entry 908 exposes only its mixed-corner contraction.

What is now excluded is narrower and useful: a hidden nonunit index cannot be
the obstruction.  Any mismatch with the source intersection pairing must be a
Laurent-unit gauge, orientation convention, or a genuinely nondiagonal mixing
of chamber frames.

## Next falsifier

Compute the complete rational occurrence transition, not only its support
permutation.  Test whether it conjugates the source intersection pairing to
the diagonal frames of Entry 1013 up to one global Laurent unit.  A required
nondiagonal term would reopen the comparison; agreement would close the
minus-recombination arc at the source-normalized Betti level.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_dual_intertwiner_lattice.rs`;
- packet:
  `research/benincasa/string-six-point-dual-intertwiner-lattice.json`;
- allocator claim:
  `seqclaim-0edd1d9e4adcc72564fe1e3e`.
- epistemic event:
  `ev-000000000633-1b3553a1-3501-4b5f-b074-1e528e0c6124`.
