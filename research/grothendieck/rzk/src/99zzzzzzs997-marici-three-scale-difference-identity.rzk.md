# Three-scale difference identity

Distributing the two adjacent differences, cancelling their aligned middle
term, and reversing distribution on the outer difference proves the numerator
identity used by the rational triangle inequality.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-three-scale-difference-identity
  ( a b c d e f : MariciInt)
  : marici-int-add
      (marici-int-mul
        (marici-int-add
          (marici-int-mul a e)
          (marici-int-negate (marici-int-mul b d))) f)
      (marici-int-mul
        (marici-int-add
          (marici-int-mul b f)
          (marici-int-negate (marici-int-mul c e))) d)
    =_{MariciInt}
    marici-int-mul
      (marici-int-add
        (marici-int-mul a f)
        (marici-int-negate (marici-int-mul c d))) e
  := concat MariciInt
      (marici-int-add
        (marici-int-mul
          (marici-int-add
            (marici-int-mul a e)
            (marici-int-negate (marici-int-mul b d))) f)
        (marici-int-mul
          (marici-int-add
            (marici-int-mul b f)
            (marici-int-negate (marici-int-mul c e))) d))
      (marici-int-add
        (marici-int-add
          (marici-int-mul (marici-int-mul a e) f)
          (marici-int-negate (marici-int-mul (marici-int-mul b d) f)))
        (marici-int-add
          (marici-int-mul (marici-int-mul b f) d)
          (marici-int-negate (marici-int-mul (marici-int-mul c e) d))))
      (marici-int-mul
        (marici-int-add
          (marici-int-mul a f)
          (marici-int-negate (marici-int-mul c d))) e)
      (marici-int-add-congruent
        (marici-int-mul
          (marici-int-add
            (marici-int-mul a e)
            (marici-int-negate (marici-int-mul b d))) f)
        (marici-int-add
          (marici-int-mul (marici-int-mul a e) f)
          (marici-int-negate (marici-int-mul (marici-int-mul b d) f)))
        (marici-int-mul
          (marici-int-add
            (marici-int-mul b f)
            (marici-int-negate (marici-int-mul c e))) d)
        (marici-int-add
          (marici-int-mul (marici-int-mul b f) d)
          (marici-int-negate (marici-int-mul (marici-int-mul c e) d)))
        (marici-int-positive-difference-scale-right
          (marici-int-mul a e) (marici-int-mul b d) f)
        (marici-int-positive-difference-scale-right
          (marici-int-mul b f) (marici-int-mul c e) d))
      (concat MariciInt
        (marici-int-add
          (marici-int-add
            (marici-int-mul (marici-int-mul a e) f)
            (marici-int-negate (marici-int-mul (marici-int-mul b d) f)))
          (marici-int-add
            (marici-int-mul (marici-int-mul b f) d)
            (marici-int-negate (marici-int-mul (marici-int-mul c e) d))))
        (marici-int-add
          (marici-int-mul (marici-int-mul a f) e)
          (marici-int-negate (marici-int-mul (marici-int-mul c d) e)))
        (marici-int-mul
          (marici-int-add
            (marici-int-mul a f)
            (marici-int-negate (marici-int-mul c d))) e)
        (marici-int-cross-scaled-middle-cancel a b c d e f)
        (rev MariciInt
          (marici-int-mul
            (marici-int-add
              (marici-int-mul a f)
              (marici-int-negate (marici-int-mul c d))) e)
          (marici-int-add
            (marici-int-mul (marici-int-mul a f) e)
            (marici-int-negate (marici-int-mul (marici-int-mul c d) e)))
          (marici-int-positive-difference-scale-right
            (marici-int-mul a f) (marici-int-mul c d) e)))
```

## Boundary

The full three-scale numerator identity is proved. Converting positive
natural-denominator predecessors to these integer scales and aligning the raw
denominator constructors remain before the rational triangle inequality.
