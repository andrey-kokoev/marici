# Global integer distributivity reduced to two mixed-sign families

All homogeneous branches are now checked. The global theorem is therefore
reduced exactly to the two unequal opposite-sign constructor orders, with
strictly positive magnitudes represented by successors.

```rzk
#lang rzk-1

#define MariciPositiveNegativeLeftDistributivity
  : U
  := ( x : MariciInt)
  → ( a b : MariciNat)
  → marici-int-mul x
      (marici-int-add
        (marici-int-embed-nat (marici-succ a))
        (marici-int-negate
          (marici-int-embed-nat (marici-succ b))))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul x
        (marici-int-embed-nat (marici-succ a)))
      (marici-int-mul x
        (marici-int-negate
          (marici-int-embed-nat (marici-succ b))))

#define MariciNegativePositiveLeftDistributivity
  : U
  := ( x : MariciInt)
  → ( a b : MariciNat)
  → marici-int-mul x
      (marici-int-add
        (marici-int-negate
          (marici-int-embed-nat (marici-succ a)))
        (marici-int-embed-nat (marici-succ b)))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul x
        (marici-int-negate
          (marici-int-embed-nat (marici-succ a))))
      (marici-int-mul x
        (marici-int-embed-nat (marici-succ b)))
```

```rzk
#define marici-int-mul-add-left-distrib-from-mixed-branches
  ( positive-negative : MariciPositiveNegativeLeftDistributivity)
  ( negative-positive : MariciNegativePositiveLeftDistributivity)
  ( x y z : MariciInt)
  : marici-int-mul x (marici-int-add y z)
    =_{MariciInt}
    marici-int-add (marici-int-mul x y) (marici-int-mul x z)
  := match y
      ( marici-int-zero ⇒ match z
          ( marici-int-zero ⇒
              marici-int-mul-add-left-distrib-arbitrary-by-embedded
                x marici-zero marici-zero
          | marici-int-pos b ⇒
              marici-int-mul-add-left-distrib-arbitrary-by-embedded
                x marici-zero (marici-succ b)
          | marici-int-neg b ⇒
              marici-int-mul-add-left-distrib-arbitrary-by-negated
                x marici-zero (marici-succ b))
      | marici-int-pos a ⇒ match z
          ( marici-int-zero ⇒
              marici-int-mul-add-left-distrib-arbitrary-by-embedded
                x (marici-succ a) marici-zero
          | marici-int-pos b ⇒
              marici-int-mul-add-left-distrib-arbitrary-by-embedded
                x (marici-succ a) (marici-succ b)
          | marici-int-neg b ⇒ positive-negative x a b)
      | marici-int-neg a ⇒ match z
          ( marici-int-zero ⇒
              marici-int-mul-add-left-distrib-arbitrary-by-negated
                x (marici-succ a) marici-zero
          | marici-int-pos b ⇒ negative-positive x a b
          | marici-int-neg b ⇒
              marici-int-mul-add-left-distrib-arbitrary-by-negated
                x (marici-succ a) (marici-succ b)))

#define marici-int-mul-add-right-distrib-from-mixed-branches
  ( positive-negative : MariciPositiveNegativeLeftDistributivity)
  ( negative-positive : MariciNegativePositiveLeftDistributivity)
  ( x y z : MariciInt)
  : marici-int-mul (marici-int-add y z) x
    =_{MariciInt}
    marici-int-add (marici-int-mul y x) (marici-int-mul z x)
  := marici-int-right-distrib-from-left x y z
      (marici-int-mul-add-left-distrib-from-mixed-branches
        positive-negative negative-positive x y z)
```

## Boundary

Global left and right distributivity now require exactly two source theorems:
positive-plus-negative and negative-plus-positive, each with unequal or equal
positive magnitudes handled by the same normalized comparison operation. The
branch reduction does not assume those theorems or hide their subtraction
coherence obligation.
