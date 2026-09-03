# Quadratic Gram sign lifting needs one anchor per component

## Question

What orientation data minimally lift quadratic Gram sign ambiguity, and does the complementary-minor source formula supply them independently?

## Claim boundary

For nonzero coordinates whose observed quadratic products form a graph `H`, relative signs are fixed within each connected component. One source-derived nonvanishing orientation anchor per component is necessary and sufficient; with `c` components there are `2^c` unanchored lifts. A full rank-one Gram needs one anchor, while entrywise squares need one per coordinate. The quarter-source formula has an explicit parity prefactor, but its two determinant factors still require a sign theorem. Treating their signs as anchors would assume the all-order sign law being sought. Zeros require separate support handling.

## Disposition

Orientation anchors are additional linear source data, not consequences of Gram positivity. The complementary-minor formula does not presently provide independent anchors because determinant signs are the unresolved content. Next perform the bounded `k=8` anchor census: build the quadratic-product connectivity of retained signed terms, count required components, and test whether any existing source-labelled nonzero probes orient them without using the target sign conclusion.
