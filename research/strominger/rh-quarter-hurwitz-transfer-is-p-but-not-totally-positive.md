# Quarter Hurwitz transfer is P but not totally positive

## Question

Is mixed-column positivity inherited from total positivity of the endpoint transfer matrix?

## Claim boundary

The classification covers the order-eight principal Hurwitz transfer matrix associated with the order-six pencil. It does not prove the same class at arbitrary matrix size or source order.

## Disposition

Let \(C=A^{-1}B\), where \(A\) and \(B\) are the product and condensation-endpoint Hurwitz matrices. All 256 principal minors of \(C\) are strictly positive, and every column-replacement identity

\[
\det M_S=\det(A)\det C_{S,S}
\]

holds exactly. However, exhaustive testing of all 12,869 nonempty minors finds a negative entry at row zero, column two. Thus \(C\) is a P-matrix but not totally positive; a direct planar-network proof for \(C\) is excluded. The next leaf is `quarter-hurwitz-transfer-m-matrix`, testing whether \(C\) has the stronger Z-sign pattern and inverse positivity of a nonsingular M-matrix, which would explain all principal-minor signs through a different mechanism.
