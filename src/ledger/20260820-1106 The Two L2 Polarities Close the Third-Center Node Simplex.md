# 1106 — The Two L2 Polarities Close the Third-Center Node Simplex

## Record

Entry 1105 derived the doubled branch and its first smoothing at the third
rank-twelve exceptional center.  The normalization and associated-grade
Gysin simplex are now checked independently.

Sequence claim: `seqclaim-a243158df8c70831e79d9667`.

## Normalized node

For

\[
W^2=16B^2+pK_3+O(p^2),
\]

set

\[
X=W-4B,
\qquad
Y=W+4B.
\]

At first nontrivial normal grade,

\[
XY
=p\,u\,L_2^+L_2^-,
\]

where \(u\) is the source-fixed nonzero scalar unit.  The three labelled
smoothing factors are therefore

\[
\boxed{(p,L_2^+,L_2^-)}.
\]

The nodal vanishing cycle is again rank one and anti-invariant under the deck
map \((X,Y)\mapsto(-Y,-X)\).

## Independent simplex calculation

The face map is

\[
d_0=(1,1,1).
\]

With the displayed factor order, the oriented edge and triple maps are

\[
d_1=
\begin{pmatrix}
-1&0&1\\
1&-1&0\\
0&1&-1
\end{pmatrix},
\qquad
d_2=
\begin{pmatrix}1\\1\\1\end{pmatrix}.
\]

The third-center checker independently verifies

\[
d_0d_1=0,
\qquad
d_1d_2=0,
\]

and

\[
(\operatorname{rank}d_0,operatorname{rank}d_1,operatorname{rank}d_2)
=(1,2,1).
\]

Hence the augmented homology vanishes in every degree.

## Deutsch--Popperian verdict

The conjecture that the two \(L_2\) polarities leave an unmatched local
vanishing-cycle class is falsified at the first nontrivial normal grade.  The
existing occurrence-resolved support and its overlap coherences generate the
node line exactly.

Thus the third center closes locally as

\[
\boxed{
\text{existing }(p,L_2^+,L_2^-)\text{ carrier simplex}
+
\text{one anti-invariant Tate coefficient}.
}

No new carrier or associated-grade coefficient excess survives.

## Scope

This is an associated-grade statement.  It does not identify the complete
higher-order normalized connection or a physical integration-chain pairing.

## Evidence

- `research/benincasa/marici-gm/src/bin/rank12_u2v4_node_simplex.rs`;
- `research/benincasa/rank12-u2-v4-joint-newton.json`.

Epistemic graph admission:
`ev-000000000805-d984b94e-7dea-4d8d-a4b1-b75484c32658`.

## Next falsifier

Proceed to the conductor--energy tangency center \((u,v)=(1,2)\).  Derive its
Newton polyhedron and source-form lattice without assuming either quartic or
doubled-node behavior.
