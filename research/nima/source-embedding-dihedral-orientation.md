# Dihedral and coordinate orientation in embedding comparison

## Question

Which signs must accompany orientation-reversing coordinate maps or dihedral relabellings of a five-point source embedding?

## Claim boundary

The calculation concerns labelled embedding equivalence. It does not authorize forgetting labels or infer source provenance.

For the cyclic logarithmic form

\[
\Omega_5=\sum_i d\log a_i\wedge d\log a_{i+1},
\]

a cyclic rotation of facet labels preserves every oriented edge and hence preserves the form. A dihedral reflection reverses every cyclic edge. Wedge antisymmetry therefore gives the character

\[
\chi(\text{rotation})=+1,\qquad
\chi(\text{reflection})=-1.
\]

The checker enumerates all ten elements of `D5` and verifies this action on the antisymmetric edge coefficient matrix.

An affine coordinate map `x'=Mx+t` independently changes the coordinate volume by `det(M)`. When `det(M)<0`, transformed facet Jacobians and the scalar top-form coefficient reverse sign. The geometric differential form is preserved only when this coordinate-orientation sign is retained. An exact reflection `x'=-x,y'=y` sends all five reference cyclic Jacobians from `+1` to `-1`.

Thus comparison data must contain both the labelled dihedral map and the coordinate determinant. Their signs are distinct and multiply. A simultaneous coordinate reflection and facet reflection can preserve the displayed coefficient, but this cancellation does not erase either orientation transport.

## Disposition

The conformance interface now accepts orientation-reversing presentations without ambiguity: transport uses `sign(det M)` times the cyclic-orientation character of the label map. Unlabelled numerical agreement is still insufficient.
