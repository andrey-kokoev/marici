# 1015 — The Dual Intertwiner Extends Through the Hexagon Two-Cell

## Why degree two matters

Entries 1013–1014 establish an integral Laurent intertwiner through the
vertex-to-edge differential.  Entry 979's actual global closure also uses the
native chamber two-cell.  A degree-one comparison that failed at this face
would not preserve the exceptional cochain's global exactness.

Use the unspecialized transports

\[
u=(B_{34},B_{24},X,B_{34}^{-1},B_{24}^{-1},X^{-1}),
\qquad \prod_ku_k=1.
\]

For an edge cochain (d), the transported face differential is

\[
\delta^1_u(d)
=
\sum_{j=0}^{5}
\left(\prod_{k>j}u_k\right)d_j.
\]

## Forced face frame

Entries 1013–1014 give

\[
g_{j+1}=\frac{g_j}{u_j^2},
\qquad h_j=g_{j+1},
\qquad g_0=1.
\]

For every edge (j), exact Laurent reduction yields

\[
\left(\prod_{k>j}u_k^{-1}\right)h_j
=
\prod_{k>j}u_k.
\]

Consequently the degree-two frame is forced to be

\[
\boxed{D_2=g_0=1,}
\]

and the second square commutes:

\[
\boxed{
D_2\delta^1_u
=
\delta^1_{u^{-1}}D_1.
}
\]

Together with Entry 1013,

\[
D_1\delta^0_u
=
\delta^0_{u^{-1}}D_0,
\]

this constructs a comparison of the complete hexagon cellular complexes.

## Exact exceptional-cochain test

The checker imports all six exact rational edge defects from Entry 979.  It
reproduces

\[
\delta^1_u(\delta^0_u\lambda)=0
\]

and independently verifies

\[
\boxed{
\delta^1_{u^{-1}}
\bigl(D_1\delta^0_u\lambda\bigr)=0.
}
\]

Thus the full circuit-compatible exceptional cochain—not only the restricted
minus primitive—passes coherently to the dual cellular complex, including its
native two-cell contraction.

## Separation from the loaded comparison

Entries 976–977 remain essential.  The loaded (6\times6) comparison contains
two genuine two-term circuit columns and cannot be replaced by a
permutation-diagonal matrix.  The present (D_\bullet) acts after those
incidences have produced the unique chamber cochain (lambda); it does not
replace or simplify the loaded comparison.

The surviving statement is therefore

\[
\boxed{
\text{no rational, integral, or two-cell cellular obstruction remains in
dualizing the exceptional chamber cochain.}
}
\]

Source-normalized identification with the full KLT twisted-period pairing and
Gauss–Manin horizontality remain separate questions.

## Next falsifier

Differentiate the complete cellular intertwiner and the Entry 977 evaluation
map in one unspecialized kinematic direction.  Test whether their covariant
derivative is exact through the same two circuit columns.  A surviving class
would be a connection-level extension; vanishing would close the rank-one
exceptional comparison beyond static Betti topology.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_full_dual_cellular_intertwiner.rs`;
- packet:
  `research/benincasa/string-six-point-full-dual-cellular-intertwiner.json`;
- allocator claim:
  `seqclaim-ffb30ea132701970a26c45c4`.
- epistemic event:
  `ev-000000000634-7e62c3ff-bd24-47f8-9f5c-4db253db6415`.
