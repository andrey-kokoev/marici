# No nonzero diagonal rescaling removes fiber dependence

Conjecture: rational rescalings
`(s1,s2,s3)=(a*A,b*B,c*(A+B))` can make the q-based Gysin denominator a base
function.

The coefficients of `Lambda_P` are `(a-c)^2` on `A^2`, `(b-c)^2` on `B^2`,
and `2*(c^2-a*b-a*c-b*c)` on `A*B`. If all vanish, the square coefficients
force `a=c` and `b=c`; the cross coefficient then gives `-4*c^2=0`. Thus only
`a=b=c=0` annihilates `Lambda_P`.

For nonzero `a,b,c`, the denominator is a nonzero homogeneous fiber polynomial
of degree five. Setting a coefficient to zero makes the denominator degenerate,
not base-only. The conjecture is falsified for every rational diagonal
rescaling; 512 bounded nonzero triples also passed the deliberate-failure test.

The next test extends the homogeneity obstruction to arbitrary homogeneous
linear assignments of the two fiber functions.
