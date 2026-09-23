# Bosonized Y0 regularity reduces to eight quotient-coordinate polynomiality

## Exact covariance

Write external six-vectors as `Z=[z|h]`, with `z` eight-by-four and `h` eight-by-two. For an invertible ambient parabolic `W=[[L,M],[0,R]]`, the sourced target chart changes by `U'=(UM+R)^-1 UL`. The full row-major eight-form Jacobian, WITHOUT assuming `det W=1`, is

    det(dU'/dU) = det(W)^2 / det(UM+R)^6.

Consequently at `Y0`, the complete two-sheet coefficient obeys

    omega_U(Y0;Z W) = det(R)^6 / det(W)^2 * omega_U(Y0;Z).

Three consequences are exact: (1) for `L=R=I`, changing `h` by `zM` leaves the coefficient unchanged; (2) scaling `h -> λh` multiplies it by `λ^8`; (3) scaling `z -> λz` multiplies it by `λ^-8`. The checker tests ALL THREE identities on each algebraic sheet of TWO distinct positive rank-six Y0 targets. The transformations retain positive maximal minors when their determinant is positive.

## The sharp nilpotent test

Select any four external rows `I` with `det z_I != 0` and eliminate the redundant bottom coordinates. The invariant variables are the four-by-two matrix

    Q = h_rest - z_rest z_I^-1 h_I.

Unipotent covariance proves the Y0 coefficient depends on `h` only through these EIGHT quotient coordinates; uniform scaling makes it a homogeneous RATIONAL function of degree eight in `Q` (for fixed generic `z`). The next global-trace calculation must cancel all denominators vanishing at `Q=0`. If the resulting rational function is regular at that origin, its homogeneous degree-eight Taylor expansion is exactly a degree-eight POLYNOMIAL, which can then be evaluated at nilpotent `h=φ·η` before Berezin extraction. Merely observing degree eight is NOT sufficient: `x^9/y` has degree eight and is undefined at the origin. Two rank-six witnesses or a nonzero scaling limit likewise do not prove polynomiality. This criterion is stronger and more executable than comparing positive-data densities with super-components pointwise.

Checker: `research/nima/checkers/check_four_mass_bosonization_quotient_weights.py`; result: `research/nima/results/four-mass-bosonization-quotient-weights.json`.
