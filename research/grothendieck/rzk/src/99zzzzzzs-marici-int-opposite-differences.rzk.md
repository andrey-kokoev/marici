# Opposite integer differences

Swapping the endpoints of an additive difference negates the original
difference. This is the integer identity required for rational distance
symmetry.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-opposite-differences
  ( x y : MariciInt)
  : marici-int-add y (marici-int-negate x)
    =_{MariciInt}
    marici-int-negate
      (marici-int-add x (marici-int-negate y))
  := rev MariciInt
      (marici-int-negate
        (marici-int-add x (marici-int-negate y)))
      (marici-int-add y (marici-int-negate x))
      (concat MariciInt
        (marici-int-negate
          (marici-int-add x (marici-int-negate y)))
        (marici-int-add
          (marici-int-negate x)
          (marici-int-negate (marici-int-negate y)))
        (marici-int-add y (marici-int-negate x))
        (marici-int-negate-add x (marici-int-negate y))
        (concat MariciInt
          (marici-int-add
            (marici-int-negate x)
            (marici-int-negate (marici-int-negate y)))
          (marici-int-add (marici-int-negate x) y)
          (marici-int-add y (marici-int-negate x))
          (marici-int-add-congruent
            (marici-int-negate x) (marici-int-negate x)
            (marici-int-negate (marici-int-negate y)) y
            refl (marici-int-negate-involutive y))
          (marici-int-add-comm (marici-int-negate x) y)))
```

## Boundary

This is an integer identity. Lifting it to raw fractions also requires the
scaling-negation paths and commutativity of product denominators.
