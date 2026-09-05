# Cross-product order transitivity

Three positive denominators are aligned by swapping the final two factors.
Scaled integer inequalities then compose, and the common middle denominator is
reflected away.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-triple-factor-swap
  ( x y z : MariciInt)
  : marici-int-mul (marici-int-mul x y) z
    =_{MariciInt}
    marici-int-mul (marici-int-mul x z) y
  := concat MariciInt
      (marici-int-mul (marici-int-mul x y) z)
      (marici-int-mul x (marici-int-mul y z))
      (marici-int-mul (marici-int-mul x z) y)
      (marici-int-mul-assoc x y z)
      (concat MariciInt
        (marici-int-mul x (marici-int-mul y z))
        (marici-int-mul x (marici-int-mul z y))
        (marici-int-mul (marici-int-mul x z) y)
        (ap MariciInt MariciInt
          (marici-int-mul y z) (marici-int-mul z y)
          (\ u → marici-int-mul x u)
          (marici-int-mul-comm y z))
        (rev MariciInt
          (marici-int-mul (marici-int-mul x z) y)
          (marici-int-mul x (marici-int-mul z y))
          (marici-int-mul-assoc x z y)))

#define marici-int-fraction-order-cross-transitive
  ( a b c : MariciInt)
  ( d e f : MariciNat)
  ( ab : MariciIntAtMost
      (marici-int-mul a (marici-int-positive-denominator e))
      (marici-int-mul b (marici-int-positive-denominator d)))
  ( bc : MariciIntAtMost
      (marici-int-mul b (marici-int-positive-denominator f))
      (marici-int-mul c (marici-int-positive-denominator e)))
  : MariciIntAtMost
      (marici-int-mul a (marici-int-positive-denominator f))
      (marici-int-mul c (marici-int-positive-denominator d))
  := marici-int-at-most-positive-scale-right-reflects
      (marici-int-mul a (marici-int-positive-denominator f))
      (marici-int-mul c (marici-int-positive-denominator d)) e
      (marici-int-at-most-transport-both
        (marici-int-mul
          (marici-int-mul a (marici-int-positive-denominator e))
          (marici-int-positive-denominator f))
        (marici-int-mul
          (marici-int-mul a (marici-int-positive-denominator f))
          (marici-int-positive-denominator e))
        (marici-int-mul
          (marici-int-mul c (marici-int-positive-denominator e))
          (marici-int-positive-denominator d))
        (marici-int-mul
          (marici-int-mul c (marici-int-positive-denominator d))
          (marici-int-positive-denominator e))
        (marici-int-triple-factor-swap a
          (marici-int-positive-denominator e)
          (marici-int-positive-denominator f))
        (marici-int-triple-factor-swap c
          (marici-int-positive-denominator e)
          (marici-int-positive-denominator d))
        (marici-int-at-most-transitive
          (marici-int-mul
            (marici-int-mul a (marici-int-positive-denominator e))
            (marici-int-positive-denominator f))
          (marici-int-mul
            (marici-int-mul b (marici-int-positive-denominator d))
            (marici-int-positive-denominator f))
          (marici-int-mul
            (marici-int-mul c (marici-int-positive-denominator e))
            (marici-int-positive-denominator d))
          (marici-int-at-most-mul-nonnegative-right
            (marici-int-mul a (marici-int-positive-denominator e))
            (marici-int-mul b (marici-int-positive-denominator d))
            (marici-int-positive-denominator f) ab
            (marici-int-positive-denominator-nonnegative f))
          (marici-int-at-most-transport-left
            (marici-int-mul
              (marici-int-mul b (marici-int-positive-denominator f))
              (marici-int-positive-denominator d))
            (marici-int-mul
              (marici-int-mul b (marici-int-positive-denominator d))
              (marici-int-positive-denominator f))
            (marici-int-mul
              (marici-int-mul c (marici-int-positive-denominator e))
              (marici-int-positive-denominator d))
            (rev MariciInt
              (marici-int-mul
                (marici-int-mul b (marici-int-positive-denominator d))
                (marici-int-positive-denominator f))
              (marici-int-mul
                (marici-int-mul b (marici-int-positive-denominator f))
                (marici-int-positive-denominator d))
              (marici-int-triple-factor-swap b
                (marici-int-positive-denominator d)
                (marici-int-positive-denominator f)))
            (marici-int-at-most-mul-nonnegative-right
              (marici-int-mul b (marici-int-positive-denominator f))
              (marici-int-mul c (marici-int-positive-denominator e))
              (marici-int-positive-denominator d) bc
              (marici-int-positive-denominator-nonnegative d)))))
```

## Boundary

This proves the algebraic order theorem behind transitivity of canonical
rational cross-product order. The rational wrapper remains to match reduced
representatives and invoke this result.
