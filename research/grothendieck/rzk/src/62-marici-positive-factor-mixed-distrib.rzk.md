# Unrestricted positive-factor mixed distributivity

Simultaneous structural recursion on the two predecessor magnitudes combines
the zero-edge strict cases, the equal zero case, and the common-successor step.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-factor-mixed-left-distrib
  ( p a b : MariciNat)
  : marici-int-mul (marici-int-pos p)
      (marici-int-add (marici-int-pos a) (marici-int-neg b))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul (marici-int-pos p) (marici-int-pos a))
      (marici-int-mul (marici-int-pos p) (marici-int-neg b))
  := (match a into
        (\ a-prime → (b-prime : MariciNat) →
          marici-int-mul (marici-int-pos p)
            (marici-int-add
              (marici-int-pos a-prime) (marici-int-neg b-prime))
          =_{MariciInt}
          marici-int-add
            (marici-int-mul (marici-int-pos p)
              (marici-int-pos a-prime))
            (marici-int-mul (marici-int-pos p)
              (marici-int-neg b-prime)))
      ( marici-zero ⇒ \ q → match q
          ( marici-zero ⇒
              marici-positive-factor-equal-mixed-left-distrib
                p marici-zero
          | marici-succ j jh ⇒
              marici-positive-factor-negative-gap-left-distrib
                p marici-zero j)
      | marici-succ i ih ⇒ \ q → match q
          ( marici-zero ⇒
              marici-positive-factor-positive-gap-left-distrib
                p marici-zero i
          | marici-succ j jh ⇒
              marici-positive-factor-mixed-successor-step
                p i j (ih j)))) b
```

## Boundary

This theorem proves the positive-plus-negative mixed family for every positive
multiplier and arbitrary predecessor magnitudes. The zero and negative
multiplier constructors remain before the full mixed family can be supplied to
the global reduction of module 43.
