# Translated-fraction cross-product cancellation

The translated numerator cancellation is stable under the remaining target
denominator factor. Multiplication associativity and commutativity then align
the surviving product with the denominator product on the untranslated
fraction.

```rzk
#lang rzk-1
```

```rzk
#define marici-translated-fraction-cross-product-cancellation
  ( a b d e : MariciInt)
  : marici-int-mul
      (marici-int-add
        (marici-int-mul
          (marici-int-add
            (marici-int-mul a e)
            (marici-int-mul b d)) d)
        (marici-int-negate
          (marici-int-mul a (marici-int-mul e d))))
      e
    =_{MariciInt}
    marici-int-mul b
      (marici-int-mul (marici-int-mul d e) d)
  := concat MariciInt
      (marici-int-mul
        (marici-int-add
          (marici-int-mul
            (marici-int-add
              (marici-int-mul a e)
              (marici-int-mul b d)) d)
          (marici-int-negate
            (marici-int-mul a (marici-int-mul e d)))) e)
      (marici-int-mul
        (marici-int-mul (marici-int-mul b d) d) e)
      (marici-int-mul b
        (marici-int-mul (marici-int-mul d e) d))
      (ap MariciInt MariciInt
        (marici-int-add
          (marici-int-mul
            (marici-int-add
              (marici-int-mul a e)
              (marici-int-mul b d)) d)
          (marici-int-negate
            (marici-int-mul a (marici-int-mul e d))))
        (marici-int-mul (marici-int-mul b d) d)
        (\ numerator → marici-int-mul numerator e)
        (marici-translated-fraction-numerator-cancellation a b d e))
      (concat MariciInt
        (marici-int-mul
          (marici-int-mul (marici-int-mul b d) d) e)
        (marici-int-mul b
          (marici-int-mul d (marici-int-mul d e)))
        (marici-int-mul b
          (marici-int-mul (marici-int-mul d e) d))
        (concat MariciInt
          (marici-int-mul
            (marici-int-mul (marici-int-mul b d) d) e)
          (marici-int-mul
            (marici-int-mul b d) (marici-int-mul d e))
          (marici-int-mul b
            (marici-int-mul d (marici-int-mul d e)))
          (marici-int-mul-assoc
            (marici-int-mul b d) d e)
          (marici-int-mul-assoc b d (marici-int-mul d e)))
        (ap MariciInt MariciInt
          (marici-int-mul d (marici-int-mul d e))
          (marici-int-mul (marici-int-mul d e) d)
          (\ denominator → marici-int-mul b denominator)
          (marici-int-mul-comm d (marici-int-mul d e))))
```

## Boundary

The integer cross-product equality for translated-fraction cancellation is now
proved. Transporting encoded positive-product denominators to these explicit
integer products yields the raw equivalence `((p + q) - p) ~ q`.
