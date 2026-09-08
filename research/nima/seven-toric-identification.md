# Seven-point integral toric identification

## Question

Does coordinate saturation identify the seven-point local ideal with the triangle toric ideal once the integral relation lattice is checked?

## Claim boundary

Use the same 42 labelled triangulations, 35 triangles, and 63 local quadrics as the prior Groebner certificate. The statement concerns polynomial ideals over any field, not surjectivity of triangle parameterization on all boundary points.

Let B be the 42-by-35 triangle incidence matrix and R the 63-by-42 matrix of local exponent differences. The checker verifies RB=0. Both matrices have rank 21, and every nonzero Smith factor of R is one. Hence the row lattice of R is saturated in Z^42 and equals the full kernel of B-transpose. Doubling R preserves rational rank but produces Smith factors two, rejecting that nonprimitive rival.

In the Laurent polynomial ring, local binomials generate the lattice ideal of their exponent differences. Integer lattice equality therefore identifies their Laurent ideal with the triangle monomial kernel. The preceding 42 coordinate-regularity certificates show that the local polynomial ideal equals the contraction of this Laurent ideal. The triangle toric ideal is also its Laurent contraction. Thus the two polynomial ideals are equal.

## Disposition

The seven-point local ideal is prime and equals the triangle toric ideal over every field. Its dimension is 21. All nonzero Smith factors of B are also one, so the unit-locus monomial image has no coefficient-field root obstruction. This does not supply boundary pointwise surjectivity: an affine monomial map can have an image smaller than the points of its scheme-theoretic image. Seven-point zero-support closure and supported coefficient lifting remain separate from ideal equality.
