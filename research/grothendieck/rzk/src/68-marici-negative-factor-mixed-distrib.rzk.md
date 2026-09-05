# Unrestricted negative-factor mixed distributivity

Simultaneous structural recursion combines the negative-factor equal and strict
zero-edge bases with the common-successor step.

```rzk
#lang rzk-1
```

```rzk
#define marici-negative-factor-mixed-left-distrib
  ( p a b : MariciNat)
  : marici-int-mul (marici-int-neg p)
      (marici-int-add (marici-int-pos a) (marici-int-neg b))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul (marici-int-neg p) (marici-int-pos a))
      (marici-int-mul (marici-int-neg p) (marici-int-neg b))
  := (match a into
        (\ a-prime → (b-prime : MariciNat) →
          marici-int-mul (marici-int-neg p)
            (marici-int-add
              (marici-int-pos a-prime) (marici-int-neg b-prime))
          =_{MariciInt}
          marici-int-add
            (marici-int-mul (marici-int-neg p)
              (marici-int-pos a-prime))
            (marici-int-mul (marici-int-neg p)
              (marici-int-neg b-prime)))
      ( marici-zero ⇒ \ q → match q
          ( marici-zero ⇒
              marici-negative-factor-equal-mixed-left-distrib
                p marici-zero
          | marici-succ j jh ⇒
              marici-negative-factor-negative-gap-left-distrib
                p marici-zero j)
      | marici-succ i ih ⇒ \ q → match q
          ( marici-zero ⇒
              marici-negative-factor-positive-gap-left-distrib
                p marici-zero i
          | marici-succ j jh ⇒
              marici-negative-factor-mixed-successor-step
                p i j (ih j)))) b
```

## Boundary

The positive-plus-negative family now distributes for every negative
multiplier and arbitrary predecessor magnitudes. Together with modules 62 and
63, every multiplier constructor is covered; assembling the constructor split
into the family required by module 43 remains.
