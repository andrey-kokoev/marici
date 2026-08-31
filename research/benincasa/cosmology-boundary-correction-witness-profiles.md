# Boundary correction provenance has one size profile per K pole

All 48 degree-12-to-14 boundary correction cells were replayed against one
retained `T+S_K` basis.

For each of the 24 pole-0 rows, the difference has raw support 30 and an exact
30-node witness comprising 25 tangent and 5 special-K nodes with 21 target
steps. Each of the 24 pole-1 rows has raw support 45 and an exact 50-node
witness comprising 40 tangent and 10 special-K nodes with 33 target steps.

Thus support and provenance size are determined solely by K pole. Raw pivot
skeletons nevertheless split into four classes per pole, with multiplicities
`4,4,7,9`. This profile regularity is evidence for a stratified operator but
not its formula. Descriptor-normalized coefficients must still be compared
across monomials and adjacent ambient inclusions.
