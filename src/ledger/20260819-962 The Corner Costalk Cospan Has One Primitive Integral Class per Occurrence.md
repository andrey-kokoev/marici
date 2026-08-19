# 962 — The Corner Costalk Cospan Has One Primitive Integral Class per Occurrence

## Frozen local cospan

Entry 961 types the comparison at a compatible two-facet corner through the
common point costalk, not through direct maps between the facet and diagonal
Kummer lines.  With columns ordered as

\[
(F_m,F_n,D)
\]

and rows as the two point-costalk occurrences, the canonical integral
differential is

\[
d_{m cor}
=
\begin{pmatrix}
1&0&-1\\
0&1&-1
\end{pmatrix}:
\mathbb Z^3\longrightarrow\mathbb Z^2.
\]

## Integral calculation

The Smith invariants of \(d_{\rm cor}\) are

\[
(1,1).
\]

Consequently,

\[
\ker d_{\rm cor}=\mathbb Z\langle(1,1,1)\rangle,
\qquad
\operatorname{coker}d_{\rm cor}=0.
\]

The checker independently enumerates all sixteen choices of incidence
orientations

\[
\begin{pmatrix}
\pm1&0&\pm1\\
0&\pm1&\pm1
\end{pmatrix}.
\]

Every choice has the same Smith invariants and a primitive rank-one kernel.
Thus orientation changes alter the signed representative but neither create
torsion nor change the integral cohomology.

## Six labelled occurrences

Entry 958 found six labelled compatible corner occurrences, with
multiplicities \(1,2,1,2\) over the four composite Fitting factors.  Their
direct sum is

\[
\mathbb Z^{18}\xrightarrow{d_{\rm glob}}\mathbb Z^{12},
\]

with

\[
\operatorname{rank}d_{\rm glob}=12,
\qquad
\ker d_{\rm glob}\simeq\mathbb Z^6,
\qquad
\operatorname{coker}d_{\rm glob}=0.
\]

Hence the supported costalk comparison produces exactly one primitive
integral compatibility class per labelled corner occurrence.

## Narrow conclusion

The total kernel rank

\[
6=1+2+1+2
\]

matches the total valuation of the four composite Fitting factors.  This is
not yet an identification with the source branch columns: it is a rank and
occurrence match between a canonical supported integral complex and the
previous Fitting census.

Therefore the surviving statement is

\[
\boxed{
\text{the frozen corner-costalk calculus supplies six canonical primitive
integral classes, with no torsion or residual cokernel.}
}
\]

No new carrier stratum is required.

## Next falsifier

Construct the actual chamber-to-source comparison from these six primitive
kernel classes to the six-word de Rham/source branch lattice, preserving
residue orientation and occurrence labels.  Test whether its image is the
composite source sublattice.  Equality must be proved by the comparison
matrix, not inferred from the common rank six.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_corner_costalk_cone.rs`;
- packet:
  `research/benincasa/string-six-point-corner-costalk-cone.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_corner_costalk_cone`;
- allocator claim:
  `seqclaim-c4e79c2a257186dd6e0dafde`.
- epistemic event:
  `ev-000000000579-b6e452f0-211b-4cfe-bde5-cb195668878e`.
