# Principal wall functions do not define Gysin base variables

Conjecture: assigning `s_i=q_gi` makes the Gysin variables rational functions
of `u` on the principal divisor.

The sourced `q_g1,q_g2,q_g3` are affine functions in two fiber coordinates;
each retains nonconstant fiber monomials. The identity
`-q_g1-q_g2+q_g3=p` cancels those monomials only in that linear combination.
On `p=0` it gives `q_g3=q_g1+q_g2`, not three functions on the base `u`.
No sourced fiber section removes the remaining variables.

The conjecture is falsified by typing, so the Gysin denominator still has no
pullback to the `u` line. This deliberate candidate does not authorize an
identification.

The next test substitutes `q_g3=q_g1+q_g2` into the full Gysin denominator to
check whether an accidental cancellation removes all fiber dependence.
