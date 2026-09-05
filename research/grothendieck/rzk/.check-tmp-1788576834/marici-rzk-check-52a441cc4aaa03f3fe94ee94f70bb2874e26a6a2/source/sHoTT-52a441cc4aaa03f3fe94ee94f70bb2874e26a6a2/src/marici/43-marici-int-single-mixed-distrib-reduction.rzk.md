# Global distributivity reduced to one mixed-sign family

Integer addition commutativity identifies the two opposite-sign constructor
orders. Consequently the positive-plus-negative family alone suffices for both
global distributive orientations.

```rzk
#lang rzk-1
```

```rzk
#define marici-negative-positive-left-distrib-from-positive-negative
  ( positive-negative : MariciPositiveNegativeLeftDistributivity)
  : MariciNegativePositiveLeftDistributivity
  := \ x a b → concat MariciInt
      (marici-int-mul x
        (marici-int-add
          (marici-int-negate
            (marici-int-embed-nat (marici-succ a)))
          (marici-int-embed-nat (marici-succ b))))
      (marici-int-add
        (marici-int-mul x
          (marici-int-embed-nat (marici-succ b)))
        (marici-int-mul x
          (marici-int-negate
            (marici-int-embed-nat (marici-succ a)))))
      (marici-int-add
        (marici-int-mul x
          (marici-int-negate
            (marici-int-embed-nat (marici-succ a))))
        (marici-int-mul x
          (marici-int-embed-nat (marici-succ b))))
      (concat MariciInt
        (marici-int-mul x
          (marici-int-add
            (marici-int-negate
              (marici-int-embed-nat (marici-succ a)))
            (marici-int-embed-nat (marici-succ b))))
        (marici-int-mul x
          (marici-int-add
            (marici-int-embed-nat (marici-succ b))
            (marici-int-negate
              (marici-int-embed-nat (marici-succ a)))))
        (marici-int-add
          (marici-int-mul x
            (marici-int-embed-nat (marici-succ b)))
          (marici-int-mul x
            (marici-int-negate
              (marici-int-embed-nat (marici-succ a)))))
        (ap MariciInt MariciInt
          (marici-int-add
            (marici-int-negate
              (marici-int-embed-nat (marici-succ a)))
            (marici-int-embed-nat (marici-succ b)))
          (marici-int-add
            (marici-int-embed-nat (marici-succ b))
            (marici-int-negate
              (marici-int-embed-nat (marici-succ a))))
          (\ z → marici-int-mul x z)
          (marici-int-add-comm
            (marici-int-negate
              (marici-int-embed-nat (marici-succ a)))
            (marici-int-embed-nat (marici-succ b))))
        (positive-negative x b a))
      (marici-int-add-comm
        (marici-int-mul x
          (marici-int-embed-nat (marici-succ b)))
        (marici-int-mul x
          (marici-int-negate
            (marici-int-embed-nat (marici-succ a)))))
```

```rzk
#define marici-int-mul-add-left-distrib-from-single-mixed-branch
  ( positive-negative : MariciPositiveNegativeLeftDistributivity)
  ( x y z : MariciInt)
  : marici-int-mul x (marici-int-add y z)
    =_{MariciInt}
    marici-int-add (marici-int-mul x y) (marici-int-mul x z)
  := marici-int-mul-add-left-distrib-from-mixed-branches
      positive-negative
      (marici-negative-positive-left-distrib-from-positive-negative
        positive-negative)
      x y z

#define marici-int-mul-add-right-distrib-from-single-mixed-branch
  ( positive-negative : MariciPositiveNegativeLeftDistributivity)
  ( x y z : MariciInt)
  : marici-int-mul (marici-int-add y z) x
    =_{MariciInt}
    marici-int-add (marici-int-mul y x) (marici-int-mul z x)
  := marici-int-right-distrib-from-left x y z
      (marici-int-mul-add-left-distrib-from-single-mixed-branch
        positive-negative x y z)
```

## Boundary

The distributive frontier is one family: arbitrary multiplication over a
positive embedded integer plus a negative embedded integer. Equal magnitudes
are already checked by module 39; the remaining cases are unequal magnitudes
and require comparison/subtraction coherence.
