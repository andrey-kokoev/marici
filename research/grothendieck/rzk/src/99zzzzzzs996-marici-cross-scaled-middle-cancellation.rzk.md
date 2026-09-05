# Cross-scaled middle terms cancel

After commuting the two right scale factors in each endpoint, the two
cross-scaled positive differences share an identical middle term and compose by
exact cancellation.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-cross-scaled-middle-cancel
  ( a b c d e f : MariciInt)
  : marici-int-add
      (marici-int-add
        (marici-int-mul (marici-int-mul a e) f)
        (marici-int-negate (marici-int-mul (marici-int-mul b d) f)))
      (marici-int-add
        (marici-int-mul (marici-int-mul b f) d)
        (marici-int-negate (marici-int-mul (marici-int-mul c e) d)))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul (marici-int-mul a f) e)
      (marici-int-negate (marici-int-mul (marici-int-mul c d) e))
  := concat MariciInt
      (marici-int-add
        (marici-int-add
          (marici-int-mul (marici-int-mul a e) f)
          (marici-int-negate (marici-int-mul (marici-int-mul b d) f)))
        (marici-int-add
          (marici-int-mul (marici-int-mul b f) d)
          (marici-int-negate (marici-int-mul (marici-int-mul c e) d))))
      (marici-int-add
        (marici-int-add
          (marici-int-mul (marici-int-mul a f) e)
          (marici-int-negate (marici-int-mul (marici-int-mul b f) d)))
        (marici-int-add
          (marici-int-mul (marici-int-mul b f) d)
          (marici-int-negate (marici-int-mul (marici-int-mul c d) e))))
      (marici-int-add
        (marici-int-mul (marici-int-mul a f) e)
        (marici-int-negate (marici-int-mul (marici-int-mul c d) e)))
      (marici-int-add-congruent
        (marici-int-add
          (marici-int-mul (marici-int-mul a e) f)
          (marici-int-negate (marici-int-mul (marici-int-mul b d) f)))
        (marici-int-add
          (marici-int-mul (marici-int-mul a f) e)
          (marici-int-negate (marici-int-mul (marici-int-mul b f) d)))
        (marici-int-add
          (marici-int-mul (marici-int-mul b f) d)
          (marici-int-negate (marici-int-mul (marici-int-mul c e) d)))
        (marici-int-add
          (marici-int-mul (marici-int-mul b f) d)
          (marici-int-negate (marici-int-mul (marici-int-mul c d) e)))
        (marici-int-add-congruent
          (marici-int-mul (marici-int-mul a e) f)
          (marici-int-mul (marici-int-mul a f) e)
          (marici-int-negate (marici-int-mul (marici-int-mul b d) f))
          (marici-int-negate (marici-int-mul (marici-int-mul b f) d))
          (marici-int-commute-right-scales a e f)
          (ap MariciInt MariciInt
            (marici-int-mul (marici-int-mul b d) f)
            (marici-int-mul (marici-int-mul b f) d)
            marici-int-negate
            (marici-int-commute-right-scales b d f)))
        (marici-int-add-congruent
          (marici-int-mul (marici-int-mul b f) d)
          (marici-int-mul (marici-int-mul b f) d)
          (marici-int-negate (marici-int-mul (marici-int-mul c e) d))
          (marici-int-negate (marici-int-mul (marici-int-mul c d) e))
          refl
          (ap MariciInt MariciInt
            (marici-int-mul (marici-int-mul c e) d)
            (marici-int-mul (marici-int-mul c d) e)
            marici-int-negate
            (marici-int-commute-right-scales c e d))))
      (marici-int-add-positive-differences
        (marici-int-mul (marici-int-mul a f) e)
        (marici-int-mul (marici-int-mul b f) d)
        (marici-int-mul (marici-int-mul c d) e))
```

## Boundary

The cross-scaled middle numerator now cancels exactly. The remaining
three-denominator identity wraps this theorem with the two distributivity paths.
