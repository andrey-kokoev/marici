# The rank-1000 gamma-floor scout localizes the Schur loss

The gamma-floor lower operator was extended from Legendre rank 670 to 1000.
The rank-670 compression has minimum `2.6070751e-8`; the full rank-1000
minimum is `2.6067400e-8`. Eliminating modes 670--999 gives Schur minimum
`2.6067399e-8`.

Although the unweighted cross-block norm is `0.27085`, the finite tail block
has minimum `1.59673`, and the near-null low vector couples only at the scale
needed to change its eigenvalue by about `3.35e-12`. Therefore a scalar
`||B||^2/delta` estimate is catastrophically pessimistic. The required
certificate must retain the range-compatible Schur matrix or a residual bound
on the few low eigenvectors.

This supplies the next finite architecture:

1. certify the rank-1000 gamma-floor matrix;
2. eliminate modes 670--999 by a preconditioned interval Schur complement;
3. bound coupling beyond mode 999 using the Legendre logarithmic floor and a
   residual estimate, not the full cross-block norm.
