# The coarse undilated tail bound is already small enough for the first Gram minor

## Tail budget

At the existing split `N=3`, the directed Hurwitz bound gives

`sum_(n>=3)(n+1/4)^(-8) <= 9.2110177077e-5`.

Multiplying by the correct undilated variation `5184` gives the coarse absolute tail error

`epsilon_tail <= 0.4774991580`.

This uses no signed-atom cancellation.

## Comparison with scouted margins

The coherent `c=1` values are

`d approximately 2.12511464`,

`c_1 approximately -0.84666022`.

Even if independent symmetric errors of size `epsilon_tail` are assigned to both cells, one obtains the conservative ranges

`d >= 1.64761548`,

`|c_1| <= 1.32415938`.

Hence

`d^2-|c_1|^2 > 0.95`.

The exact lower bound must include all finite-prefix interval widths, but those were tiny in the former checker relative to this order-one reserve. Therefore the coarse total-variation tail should already certify positivity of the first two-translate Gram minor; a signed-atomic rebuild is not prerequisite for rank two.

## Rank-three limitation

For the three-translate matrix, entrywise errors accumulate in an operator-norm bound. A crude row-sum penalty from three uncertain Toeplitz cells exceeds the scouted minimum eigenvalue `0.62048`. Rank three may therefore require signed atoms, a later split `N`, or direct interval eigenvalue assembly with correlated errors.

## Disposition

Implement the coarse `5184` enclosure first and target a certified rank-two theorem. Optimize the tail only after that certificate passes; do not delay the first repaired result for a sharper remainder that rank two does not need.
