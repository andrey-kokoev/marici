# Coprimality descends to divisors

If `x` has no nonunit common divisor with `y`, then it has none with any divisor
of `y`. A proposed common divisor of `x` and the smaller value composes through
divisibility transitivity to become a forbidden common divisor of `x` and `y`.

```rzk
#lang rzk-1
```

```rzk
#define marici-nat-coprime-symmetric
  ( x y : MariciNat)
  ( coprime : MariciNatAreCoprime x y)
  : MariciNatAreCoprime y x
  := \ common → match common
      ( marici-nat-nonunit-common-divisor f divides-y divides-x ⇒
          coprime
            (marici-nat-nonunit-common-divisor
              x y f divides-x divides-y))

#define marici-nat-coprime-descends-right-divisor
  ( x y divisor : MariciNat)
  ( coprime : MariciNatAreCoprime x y)
  ( divides-y : MariciNatDivides divisor y)
  : MariciNatAreCoprime x divisor
  := \ common → match common
      ( marici-nat-nonunit-common-divisor
          f divides-x divides-divisor ⇒
        coprime
          (marici-nat-nonunit-common-divisor
            x y f divides-x
            (marici-nat-divides-transitive
              (marici-succ (marici-succ f))
              divisor y divides-divisor divides-y)))

#define marici-nat-coprime-descends-left-divisor
  ( x y divisor : MariciNat)
  ( coprime : MariciNatAreCoprime x y)
  ( divides-x : MariciNatDivides divisor x)
  : MariciNatAreCoprime divisor y
  := marici-nat-coprime-symmetric y divisor
      (marici-nat-coprime-descends-right-divisor
        y x divisor
        (marici-nat-coprime-symmetric x y coprime)
        divides-x)
```

## Boundary

Coprimality now descends along either divisibility coordinate. This is the
induction transport needed to reduce Euclid for a composite divisor to Euclid
for its proper factors; the factorization and recombination steps remain.
