# General homogeneous linear assignments retain fiber degree five

Conjecture: a nondegenerate assignment `s_i=a_i*A+b_i*B` can make the Gysin
denominator base-only.

The denominator is homogeneous of degree five in the `s_i`. Its pullback is
either zero or homogeneous of degree five in `A,B`. Fiber scaling gives
`F(t*A,t*B)=t^5*F(A,B)`, incompatible with a base function unless `F=0`.
The zero case is a degenerate divisor pullback, not a support comparison.

Thus every nondegenerate homogeneous linear assignment is falsified. An
exhaustive bounded test of 480 rank-two matrices with nonzero rows found a
nonzero degree-five polynomial in every case.

The next test adds base-dependent affine constants and checks whether they can
cancel the degree-five leading term.
