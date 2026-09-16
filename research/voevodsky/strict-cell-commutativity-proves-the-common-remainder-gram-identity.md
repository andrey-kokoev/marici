# Strict cell commutativity proves the common-remainder Gram identity

## Cell at one lattice coordinate

Fix a regulated lattice coordinate \(\alpha\). Let

\[
\mathcal T_\alpha^T,
\qquad
\mathcal T_\alpha^0
\]

be the two differently polarized sub-tetrahedra of the same positive cell.

Write their physical feature maps as

\[
X_{phys,\alpha}^T:E_\alpha\to\mathcal K_{phys,\alpha}^T,
\]

\[
X_{phys,\alpha}^0:E_\alpha\to\mathcal K_{phys,\alpha}^0.
\]

The polarized boundary-face maps are

\[
\widehat X_\alpha^T:E_\alpha\to\widehat{\mathcal K}_\alpha^T,
\qquad
\widehat X_\alpha^0:E_\alpha\to\widehat{\mathcal K}_\alpha^0.
\]

## Orthogonal face decomposition

A positive cell records its faces by orthogonal feature summands. Hence each polarized tetrahedron has a decomposition

\[
U_\alpha^T X_{phys,\alpha}^T
=
B_\alpha^T\oplus\widehat X_\alpha^T,
\]

\[
U_\alpha^0 X_{phys,\alpha}^0
=
B_\alpha^0\oplus\widehat X_\alpha^0,
\]

where \(U_\alpha^{T,0}\) are the cell's target isometries and \(B_\alpha^{T,0}\) are the two route presentations of the face opposite the polarized boundary leg.

This is not a Jordan decomposition of a signed form. It is the face decomposition already present in the positive lattice cell.

## Commuting common-face square

Let

\[
r_T:\mathcal T_\alpha^T\to\mathcal F_\alpha,
\qquad
r_0:\mathcal T_\alpha^0\to\mathcal F_\alpha
\]

be the two routes to their common face. Strict lattice-cell commutativity says

\[
\boxed{
r_T\circ X_{phys,\alpha}^T
=
r_0\circ X_{phys,\alpha}^0.
}
\]

Denote this common composite by

\[
\boxed{
B_\alpha
:=r_T X_{phys,\alpha}^T
=r_0X_{phys,\alpha}^0.
}
\]

Therefore

\[
B_\alpha^T=B_\alpha=B_\alpha^0
\]

as source-labelled feature maps, or up to the canonical target isometry if the two face carriers are retained separately.

## Gram calculation

Define

\[
G_{phys,\alpha}^T
=(X_{phys,\alpha}^T)^*X_{phys,\alpha}^T,
\qquad
G_{phys,\alpha}^0
=(X_{phys,\alpha}^0)^*X_{phys,\alpha}^0,
\]

and

\[
\widehat G_\alpha^T
=(\widehat X_\alpha^T)^*\widehat X_\alpha^T,
\qquad
\widehat G_\alpha^0
=(\widehat X_\alpha^0)^*\widehat X_\alpha^0.
\]

Because the decompositions are orthogonal and \(U_\alpha^{T,0}\) are isometries,

\[
G_{phys,\alpha}^T
=(B_\alpha^T)^*B_\alpha^T+
\widehat G_\alpha^T,
\]

\[
G_{phys,\alpha}^0
=(B_\alpha^0)^*B_\alpha^0+
\widehat G_\alpha^0.
\]

Strict common-face commutativity now gives

\[
\boxed{
G_{phys,\alpha}^T-
\widehat G_\alpha^T
=
B_\alpha^*B_\alpha
=
G_{phys,\alpha}^0-
\widehat G_\alpha^0.
}
\]

Since every feature Gram is positive,

\[
\boxed{
G_{phys,\alpha}^T-
\widehat G_\alpha^T
=
G_{phys,\alpha}^0-
\widehat G_\alpha^0
\succeq0.
}
\]

## Relation to the analytic chart equations

For source charts \(S_i\) with inverses \(R_i\) on essential images, every route is

\[
C_{ij}=S_jR_i.
\]

Thus the two routes to the common face reduce to the same source-rooted map. Schematically,

\[
r_TX_{phys,\alpha}^T
=S_F R_*S_*R_E
=S_FR_E,
\]

\[
r_0X_{phys,\alpha}^0
=S_F R_{*'}S_{*'}R_E
=S_FR_E.
\]

This is the analytic reason that \(B_\alpha^T\) and \(B_\alpha^0\) are the same feature rather than merely two features with equal scalar traces.

## Strength of the conclusion

The proof is feature-level if the positive lattice cell retains:

1. the source-labelled face maps;
2. the orthogonal summand inclusions;
3. the target isometries.

If only the signed Hermitian readouts are retained, the proof descends only to equality of signed differences and the common Gram cannot be recovered. The asserted full positive lattice-cell structure supplies exactly the missing information.

## External realizations

The theorem concerns two polarized sub-tetrahedra of the same lattice cell. It makes no assertion about a separately constructed external prolate/Widom feature unless that feature has first been installed as one of the cell's positive presentations by an isometric comparison.

## Disposition

The common-remainder identity is the Gram shadow of the strict common-face equation

\[
\boxed{
r_TX_{phys,\alpha}^T
=r_0X_{phys,\alpha}^0.}
\]

Accordingly, for the internal polarized lattice cell, the identity is proved formally from cell commutativity and orthogonal face decomposition. No regulator limit, trace asymptotic, Douglas estimate, or packetwise positivity argument is required.
