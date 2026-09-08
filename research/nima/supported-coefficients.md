# Six-point supported coefficient realization

## Question

Does Boolean support equality extend to coefficient realization on every six-point stratum?

## Claim boundary

This is an exhaustive integer-lattice certificate for the fourteen labelled six-point triangulations. No higher-n exhaustion or equality of defining ideals is asserted.

For each locally admitted support S, retain the triangle factors forced nonzero by S. The preceding closure test guarantees that setting all other factors zero excludes precisely the unwanted triangulations. Let B_S be the incidence matrix on positive triangulations and retained factors, and R_S the rows of the local rectangles whose four entries survive.

The checker verifies R_S B_S=0, rank(B_S)+rank(R_S)=|S|, and unit nonzero Smith factors for R_S on all 4000 supports, including the empty support. Thus the local rows form the entire integer relation kernel of B_S: they are a saturated sublattice of the ambient character lattice and have the required rank. Local coefficient equations consequently define precisely the triangle image on each complex torus stratum.

Every nonzero Smith factor of B_S is also one. Its map onto its image therefore has a monomial section after integral basis changes, without root extraction. The stratum realization conclusion holds over any field, not only the complex numbers: use the integral section on unit coefficients and then set unused factors zero. This stronger coefficient-domain conclusion uses the additional Smith certificate, not complex surjectivity alone.

## Disposition

All 4000 supports pass, grouped into 24 support-size/rank types in the results. A doubled relation is rejected by its Smith factor two, checking that rational rank alone cannot pass the criterion. Every six-point field-valued array satisfying the local minors admits triangle factors, zeros included. Equality here is of field-valued solution sets; radicality, primeness, and scheme equality of the local ideal have not been established.
