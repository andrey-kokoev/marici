# 2913 — The Bridge Double Residue Is the Join of Two Triangle Facets and One Vertex

## Ordered face

Take the ordered codimension-two residue along

\[
q_L=X_1+X_2+X_3+y_{34}=0,
\]

then

\[
q_R=X_4+X_5+X_6+y_{34}=0.
\]

The common zero set inside Entry 2911's twenty-one labelled source vertices
contains exactly thirteen vertices.

## Canonical partition

The thirteen vertices split without choices into:

1. six left-triangle vertices: types two and three on edges
   \(12,23,31\);
2. the unique type-one bridge vertex on \(34\);
3. six right-triangle vertices: types two and three on edges
   \(45,56,64\).

Each six-vertex triangle block has affine rank four, exactly the total-energy
facet of the frozen triangle source.  The common face has affine rank ten and
satisfies

\[
10=4+0+4+2,
\]

the projective join dimension formula.  Hence the face is

\[
F_L * v_{34}^{(1)} * F_R.
\]

## Normalization and orientation

Writing

\[
E_L=X_1+X_2+X_3,
\qquad
E_R=X_4+X_5+X_6,
\]

gives

\[
q_L=E_L+y_{34},
\qquad
q_R=E_R+y_{34}.
\]

At fixed \(y_{34}\), the normal Jacobian from \((E_L,E_R)\) to
\((q_L,q_R)\) is one.  The ordered canonical-form residue therefore has unit
coefficient.  Reversing the two residue operations changes only the derived
orientation sign.

## Result

At Carrier level, the bridge double residue is canonically the join of the two
triangle total-energy facets and one unique bridge normal vertex.  The scale
ambiguity exhibited in Entry 2906 is absent for the canonical form itself:
source residue normalization fixes it to one.

This does not yet prove that the pointed Kummer finite parts sew with unit
scale.  Their moving-fiber pushforwards and affine origins must still be
transported through this residue map.

## Next finite calculation

Push the two source-normalized triangle relative cycles through the join
residue.  Retain the bridge type-one contour variable and compare the composite
pointing with \(F_L(2)=F_R(2)=0\).  Compute any resulting affine mismatch
before quotienting the bridge occurrence.

## Durable artifacts

- `research/benincasa/check_double_triangle_bridge_double_residue.py`
- `research/benincasa/double-triangle-bridge-double-residue.json`
