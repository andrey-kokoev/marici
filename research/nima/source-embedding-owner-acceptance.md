# Source-embedding owner acceptance bundle

## Question

In what order should a source-owned embedding packet be tested without allowing downstream algebra to substitute for provenance?

## Claim boundary

This bundle orders existing gates and binds their results by digest. It does not authenticate a source or supply missing coefficients, normalization, or physical maps.

The acceptance order is:

1. **Source object.** Supply `E_n=(K_n,iota_n,{X_c},P_n,nu_n)` with source locators, formulas, labelled channels, support constants, channel scales or coefficient-weight transport, and orientation.
2. **Five-point geometry.** Run the conformance harness for dimension, distinct facets, dissection incidence, boundary recursion, simple poles, infinity regularity, and Jacobian weights. Coordinate-equivalent packets must supply the affine and dihedral transports.
3. **Coefficient group.** Declare positive-real, signed-real, or complex coefficients. Apply magnitude binomials, `F2` sign parities, or integer characters and retain the Smith root branch.
4. **Six-point gluing.** Run all five global weight binomials and all facet rank-one tests. Local tests alone miss two nonlocal classes.
5. **Normalization.** Supply the oriented point scalar, or source-authorized adjacent-size comparisons that determine it through normalization descent.
6. **Physical promotion.** Supply the sector map and any boundary-value, contour, or readout normalization required by the claimed interpretation.

Testing stops at the first failed gate. In particular, the reference fixture passes its algebraic five-point checks but remains nonpromotable because gate 1 and the base normalization are absent. Positive rival slices show why that ordering is necessary.

## Disposition

All local acceptance machinery is assembled and digest-bound. The first reopening condition is an owner packet satisfying gate 1; repeated fixture computation cannot advance that authority boundary.
