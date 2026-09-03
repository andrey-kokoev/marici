# Quarter Hurwitz source-sum cancellation groupings

## Question

Can mixed Jacobi--Cauchy--Binet summands be made sign-coherent by grouping them with a single natural index statistic?

## Claim boundary

The test covers eight specified grouping rules over all 3,584 order-eight terminal cases. It does not exclude multivariate pairings, sign-reversing involutions, or determinant condensation.

## Disposition

No tested grouping is sign-coherent. The rules group by \(\sum K\), \(\min K\), \(\max K\), intersection size with the base, symmetric-difference size from the row set, and counts below, inside, or above the terminal interval. Every rule has a negative oriented group; seven already fail with empty base. Therefore one-statistic grouping does not control the cancellation and this branch is rejected. The next leaf is `quarter-terminal-dodgson-condensation-source-induction`, testing whether Desnanot--Jacobi condensation yields a noncircular source induction whose factors have previously certified principal signs.
