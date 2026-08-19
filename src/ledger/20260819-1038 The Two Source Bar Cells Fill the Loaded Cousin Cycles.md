# 1038 — The Two Source Bar Cells Fill the Loaded Cousin Cycles

## Hard-to-vary claim

The occurrence-resolved loaded Cousin graph of Entry 1037 has exactly two source-selected cycles after adjoining the transition edges inherited from Entry 967, and the two corresponding bar cells fill both cycles. Its source-selected cellular homology is

\[
H_0\cong\mathbb Q^2,
\qquad H_1=H_2=0.
\]

This is a statement about the frozen occurrence nerve at this boundary grade. It does not assert that deeper geometric intersections are absent.

## Frozen source data

Entry 1037 supplies eight vertices and six incidence edges. Entry 967 supplies the transition paths whose squared monodromies obey

\[
M_{Q_2}=M_{Q_1}B_{24}^{,2},
\qquad
M_{Q_4}=M_{Q_3}B_{34}^{,2}.
\]

They add the two labelled edges

\[
Q_1\longrightarrow Q_2,
\qquad
Q_3\longrightarrow Q_4.
\]

No edge or face is added from a rank count or after observing the target homology.

## Source bar cells

The multiplicative bar identity

\[
M_AM_B-1=(M_A-1)+M_A(M_B-1)
\]

provides one coherence cell for each transition. With the edge ordering frozen by the checker, their boundaries are

\[
\partial F_{24}=e_4+e_6-e_1,
\qquad
\partial F_{34}=e_5+e_7-e_3.
\]

Each connected component is a filled triangle with one leaf:

\[
P_1- Q_2-Q_1-P_2-Q_2,
\qquad
P_3-Q_4-Q_3-P_4-Q_4.
\]

The integral incidence matrices satisfy

\[
d_1d_2=0,
\qquad
\operatorname{rank}d_1=6,
\qquad
\operatorname{rank}d_2=2.
\]

For eight vertices, eight edges, and two faces this gives

\[
\dim H_0=2,
\qquad
\dim H_1=8-6-2=0,
\qquad
\dim H_2=2-2=0.
\]

## Narrow result

The two transition coherences do not create a higher obstruction. They are precisely the two cells required to kill the two cycles created when the transition edges are added to Entry 1037's forest.

Thus the static source-selected occurrence diagram closes above degree zero. Its two surviving degree-zero components remain distinct; this calculation supplies no canonical comparison between them.

## Next falsifier

Static cellular closure is weaker than horizontality. The next test is to differentiate the two bar cells in the unspecialized source family and determine whether the induced Cousin differential is horizontal. A nonzero mixed-curvature class would be the first obstruction not visible in the static occurrence nerve.

## Durable artifacts

- `research/benincasa/marici-gm/src/bin/string_six_point_loaded_cousin_bar_cells.rs`
- `research/benincasa/string-six-point-loaded-cousin-bar-cells.json`

Epistemic event: `ev-000000000657-849fcccf-17d1-44fa-a9a8-b6411a0a4ed4`.
