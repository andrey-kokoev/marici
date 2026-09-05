# Second positive power is the positive self-product

The recursive positive-power predecessor at exponent two reduces to the
positive-product predecessor of the base with itself after transporting the
exponent-one predecessor identity.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-power-predecessor-two
  ( k : MariciNat)
  : marici-positive-power-predecessor k marici-two
    =_{MariciNat}
    marici-positive-product-predecessor k k
  := ap MariciNat MariciNat
      (marici-positive-power-predecessor k marici-one) k
      (\ predecessor →
        marici-positive-product-predecessor k predecessor)
      (marici-positive-power-predecessor-one k)
```

## Boundary

Exponent-two Dirichlet denominators now reduce to encoded squares of their
positive bases. The Cauchy proof still requires a telescoping upper bound for
finite tails and its promotion through rational finite sums.
