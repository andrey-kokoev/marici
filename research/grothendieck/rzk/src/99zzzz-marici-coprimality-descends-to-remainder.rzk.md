# Coprimality descends to a division remainder

From `x=qy+r`, any nonunit common divisor of `r` and `y` divides `qy`, hence
the sum `x`, and therefore contradicts coprimality of `x` and `y`. This descent
does not require irreducibility.

```rzk
#lang rzk-1
```

```rzk
#define marici-nat-coprime-descends-to-remainder
  ( x y quotient remainder : MariciNat)
  ( coprime : MariciNatAreCoprime x y)
  ( reconstruction : marici-add (marici-mul quotient y) remainder
    =_{MariciNat} x)
  : MariciNatAreCoprime remainder y
  := \ common →
      match common
      ( marici-nat-nonunit-common-divisor
          factor-predecessor divides-remainder divides-y ⇒
        coprime
          (marici-nat-nonunit-common-divisor x y factor-predecessor
            (marici-nat-divides-reindex-value
              (marici-succ (marici-succ factor-predecessor))
              (marici-add (marici-mul quotient y) remainder)
              x reconstruction
              (marici-nat-divides-add
                (marici-succ (marici-succ factor-predecessor))
                (marici-mul quotient y) remainder
                (marici-nat-divides-product-left
                  (marici-succ (marici-succ factor-predecessor))
                  y quotient divides-y)
                divides-remainder))
            divides-y))

#define marici-nat-coprime-division-pair-swaps
  ( x y quotient remainder : MariciNat)
  ( coprime : MariciNatAreCoprime x y)
  ( reconstruction : marici-add (marici-mul quotient y) remainder
    =_{MariciNat} x)
  : MariciNatAreCoprime y remainder
  := marici-nat-coprime-symmetric remainder y
      (marici-nat-coprime-descends-to-remainder
        x y quotient remainder coprime reconstruction)
```

## Boundary

Each Euclidean division step now transports coprimality from `(x,y)` to both
orientations of `(r,y)`. For positive nonunit `r<y`, bounded recursion may call
the induction hypothesis on `(y,r)`, use Bézout symmetry, and lift the resulting
certificate through `x=qy+r`.
