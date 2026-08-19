# 925 — The Three Branches Obey an Unfilled Normal-Symbol Syzygy

## Question from Entry 924

The common coarsening

\[
F_0=(s_{14},s_{235})
\]

has zero ordinary coefficient. Its three labelled middle-channel insertions are

\[
x=s_{23},
\qquad
y=s_{35},
\qquad
z=s_{25}.
\]

The next question is whether their first nonzero filtered symbols are unrelated, or satisfy a source-derived relation.

## Common source vector

Entry 921 regularizes the diagonal and off-diagonal symbols by their inherited Cartier equations. The exact six-component source-vector audit now gives

\[
\operatorname{rank}
\begin{pmatrix}
r_x\\
r_y
\end{pmatrix}
=1,
\]

with all fifteen (2\times2) minors zero and exact proportionality

\[
\boxed{r_x=r_y=:r.}
\]

Entry 920’s strict reflection transports the (y)-branch to the (z)-branch with unit (1). After transporting the reflected source basis back to the common labelled frame, the (z)-branch carries the same row (r).

## Target directions

In the common two-dimensional target basis, the three symbols are

\[
M_x=
\begin{pmatrix}r\\-r\end{pmatrix},
\qquad
M_y=
\begin{pmatrix}0\\r\end{pmatrix},
\qquad
M_z=
\begin{pmatrix}r\\0\end{pmatrix}.
\]

They span rank two and obey the primitive exact identity

\[
\boxed{M_x+M_y-M_z=0.}
\]

Thus the three higher-normal branches are not a rank-three direct sum. They form a rank-two normal-symbol module with one syzygy.

## Why this is not yet a Koszul boundary

The three cuts (x,y,z) are pairwise incompatible: every pair intersects, and no pair is nested. Therefore the link of (F_0) on these labels consists of

\[
3\text{ vertices},
\qquad
0\text{ edges},
\qquad
0\text{ two-cells}.
\]

No frozen carrier cell has boundary (x+y-z). Consequently

\[
\boxed{
M_x+M_y-M_z=0
\text{ is a coefficient normal-symbol syzygy, not a carrier boundary.}
}
\]

Adding a two-cell to fill it would be a prohibited post hoc carrier modification.

## Narrow conclusion

The common coarsening supports a genuinely nontrivial coefficient pattern:

\[
\boxed{
\text{zero ordinary coefficient}
\longrightarrow
\text{rank-two first filtered module}
\text{ with one unfilled syzygy}.
}
\]

This is compatible with the shared-carrier architecture only if the relation belongs to coefficient/derived data rather than incidence topology. It is not evidence for a new carrier stratum.

## Next falsifier

Determine whether the syzygy is horizontal under the tangential connection on (F_0). A horizontal relation defines a rank-two coefficient local system over the existing coarsening. A nonhorizontal relation requires an extension or higher coherence term. The connection must be derived from the source transition; differentiating only the displayed target vectors is insufficient.
