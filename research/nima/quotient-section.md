# Faithful six-point quotient coordinates

## Question

Can arbitrary values of the two saturated quotient characters be represented without roots, and does dropping primitivity lose information?

## Claim boundary

The quotient is the complex torus L/C with labelled triangulations and the character ordering in results/local_global_torus_lattice.json. This is not a physical quotient or a claim over arbitrary coefficient fields.

For prescribed nonzero coordinates (a,b), assign triangle weights h_013=b^(-1), h_024=b/a, and every other triangle weight one. Let s(a,b) be their triangulation products. The checker constructs the integral exponent matrix S for this assignment and verifies D S=I, where D contains the two quotient character rows. Thus the construction is a monomial section for every complex unit pair, not just the numerical sample (2,3).

The preceding saturation certificate identifies the two character classes as a basis of X*(L/C). Consequently two points of L have equal coordinates exactly when their ratio belongs to C. The section splits L as C times (C*)^2; it does not choose unique channel parameters, whose finite root kernel remains.

## Disposition

An explicit channel-image multiplication preserves the coordinates of the sample while changing its triangulation weights. The competing pair of characters (chi_1^2,chi_2) is rationally independent but identifies the distinct quotient points (2,3) and (-2,3). Its missing mu_2 distinction demonstrates why rational rank cannot replace integral primitivity. All targeted checks passed.
