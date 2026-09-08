# Six-point scale-invariant triangulation-weight relations

## Question

What complete finite test determines whether fourteen six-point triangulation coefficients can be absorbed into nine channel-facet scales?

## Claim boundary

The recorded basis uses a declared ordering of channels and triangulations. Other primitive bases define the same rational kernel. The positive-real factorability test does not supply source provenance.

Let `A` be the `14 by 9` triangulation-channel incidence matrix. It has rank nine, so its left kernel has dimension five. A primitive integer basis `z^(r)` gives five binomial tests

\[
\prod_{T=1}^{14} w_T^{z_T^{(r)}}=1,
\qquad r=1,\ldots,5.
\]

For positive weights these conditions are sufficient and necessary: logarithms turn them into orthogonality to the complete left kernel, hence `log w` lies in the column image of `A` and equals `A log lambda` for channel scales `lambda`.

The checker records all triangulation channel sets and every nonzero exponent in a canonical nullspace basis, verifies the relation matrix has rank five, and verifies its product with `A` vanishes exactly. Unit weights pass all five relations. A deliberate single-weight deformation to two is assigned to a triangulation detected by the largest number of displayed basis rows; every resulting nonunit power of two is recorded.

## Disposition

The six-point acceptance criterion is now executable without fitting facet scales. An owner coefficient packet must preserve the declared ordering or provide an explicit permutation, then pass all five binomials. Failure is a scale-invariant obstruction to canonical-form comparison, not a coordinate convention.
