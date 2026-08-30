# 2360 — The Soft Invariant Plane Is Exactly the Denominator-Deletion Image

## Question from Entry 2359

The \(X_1=0\) tangent connection preserves a canonical sixteen-plane
\(W_{16}\), derived as the image of the trace radical of its maximal-parabolic
algebra.  Is this a new coefficient layer, or an existing localization
operation?

## Source-derived map

On the labelled \(\mathcal G_{12}\) residue chart,

\[
q_{g_{23}}=b-X_1.
\]

Hence on \(X_1=0\),

\[
q_{g_{23}}=b.
\]

Deleting the \(g_{23}\) denominator embeds a four-mark numerator class into
the five-mark relative union by

\[
\boxed{P(a,b)\longmapsto bP(a,b).}
\]

This map is frozen before comparison with \(W_{16}\).

## Exact equality

Using every numerator monomial of degree at most five, multiplication by
\(b\) gives twenty-one candidate labelled classes.  Exact reduction in the
same degree-six rank-twenty-six presentation gives image rank

\[
\operatorname{rank}\operatorname{im}(\mathrm{Del}_{g_{23}})=16.
\]

Bidirectional containment against Entry 2359's trace-radical image gives

\[
\operatorname{im}(\mathrm{Del}_{g_{23}})/W_{16}=0,
\qquad
W_{16}/\operatorname{im}(\mathrm{Del}_{g_{23}})=0.
\]

Therefore

\[
\boxed{
W_{16}=\operatorname{im}(\mathrm{Del}_{g_{23}}).
}
\]

The four-dimensional quotient is consequently the supported soft residue
sector:

\[
0\longrightarrow
M_{16}^{\rm deleted}
\longrightarrow
M_{20}^{X_1\text{-soft}}
\longrightarrow
Q_4^{g_{23}\text{-res}}
\longrightarrow0.
\]

## Consequence for H2

The first proper supported algebra from Entry 2359 is not an undeclared
Carrier operation.  It is exactly the source-derived deletion--restriction
filtration on the existing soft wall.  H2 therefore survives this test in a
stronger form:

\[
\boxed{
\text{existing soft Carrier localization}
+
\text{sector-specific nonsplit coefficient extension}.
}
\]

## Physical gate

The physical dual is cyclic precisely when it pairs nontrivially with the
deleted image.  This can now be tested geometrically: restrict the
source-normalized physical relative cycle to the four-mark deletion sector
and evaluate one nonzero period.  If the restriction vanishes identically,
only the rank-four residue quotient is observable; if it does not, the full
rank-twenty tangent packet is recoverable.

The primary positive chain does not acquire a boundary on the five-pole
walls at generic positive energies.  At \(X_1=0\), however, the soft wall
\(q_{g_{23}}=b=0\) meets the boundary corner, so the required statement is a
supported limiting-chain calculation, not generic positivity.

## Artifacts

- `research/benincasa/check_x1_soft_parabolic_deletion_image.py`
- `research/benincasa/x1-soft-parabolic-deletion-image.json`

Sequence claim: `seqclaim-29bd6528743c15a663fca2dd`.
