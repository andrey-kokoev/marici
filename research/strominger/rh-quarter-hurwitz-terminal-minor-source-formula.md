# Quarter Hurwitz terminal-minor source formula

## Question

Can terminal bordered minors of the transfer \(C=A^{-1}B\) be reduced directly to endpoint Hurwitz minors?

## Claim boundary

The formula is an all-size determinant identity. Its exact sign verification here is bounded to the order-eight transfer; no all-order cancellation theorem is proved.

## Disposition

Jacobi's complementary-minor identity followed by Cauchy--Binet gives

\[
\det(A)\det C[R,S]
=
\sum_{|K|=|R|}(-1)^{\sum R+\sum K}
\det A[K^c,R^c]\det B[K,S].
\]

Exact arithmetic verifies this identity for all 12,869 nonempty order-eight minors and the expected orientation for all 3,584 terminal bordered minors. The source expansion is not sign-coherent: already for empty base, \(i=0\), and \(j=1\), two nonzero summands are positive and one is negative. Endpoint minor sign-regularity alone therefore cannot prove the terminal rule termwise. The next leaf is `quarter-hurwitz-source-sum-cancellation`, seeking a pairing, recurrence, or determinant condensation that controls this mixed-sign sum without assuming the Schur-sign conclusion.
