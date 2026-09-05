# Raw-fraction addition has associative numerators

Positive-product denominator encodings expand to integer products. After those
two endpoint transports, the three-scale integer sum identity proves equality
of the numerators produced by the two raw-addition bracketings.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-add-associativity-numerator
  ( a b c : MariciInt)
  ( d e f : MariciNat)
  : marici-int-add
      (marici-scale-by-positive-denominator
        (marici-int-add
          (marici-scale-by-positive-denominator a e)
          (marici-scale-by-positive-denominator b d)) f)
      (marici-scale-by-positive-denominator c
        (marici-positive-product-predecessor d e))
    =_{MariciInt}
    marici-int-add
      (marici-scale-by-positive-denominator a
        (marici-positive-product-predecessor e f))
      (marici-scale-by-positive-denominator
        (marici-int-add
          (marici-scale-by-positive-denominator b f)
          (marici-scale-by-positive-denominator c e)) d)
  := concat MariciInt
      (marici-int-add
        (marici-scale-by-positive-denominator
          (marici-int-add
            (marici-scale-by-positive-denominator a e)
            (marici-scale-by-positive-denominator b d)) f)
        (marici-scale-by-positive-denominator c
          (marici-positive-product-predecessor d e)))
      (marici-int-add
        (marici-int-mul
          (marici-int-add
            (marici-int-mul a (marici-int-positive-denominator e))
            (marici-int-mul b (marici-int-positive-denominator d)))
          (marici-int-positive-denominator f))
        (marici-int-mul c
          (marici-int-mul
            (marici-int-positive-denominator d)
            (marici-int-positive-denominator e))))
      (marici-int-add
        (marici-scale-by-positive-denominator a
          (marici-positive-product-predecessor e f))
        (marici-scale-by-positive-denominator
          (marici-int-add
            (marici-scale-by-positive-denominator b f)
            (marici-scale-by-positive-denominator c e)) d))
      (ap MariciInt MariciInt
        (marici-int-positive-denominator
          (marici-positive-product-predecessor d e))
        (marici-int-mul
          (marici-int-positive-denominator d)
          (marici-int-positive-denominator e))
        (\ denominator → marici-int-add
          (marici-scale-by-positive-denominator
            (marici-int-add
              (marici-scale-by-positive-denominator a e)
              (marici-scale-by-positive-denominator b d)) f)
          (marici-int-mul c denominator))
        (marici-positive-denominator-product d e))
      (concat MariciInt
        (marici-int-add
          (marici-int-mul
            (marici-int-add
              (marici-int-mul a (marici-int-positive-denominator e))
              (marici-int-mul b (marici-int-positive-denominator d)))
            (marici-int-positive-denominator f))
          (marici-int-mul c
            (marici-int-mul
              (marici-int-positive-denominator d)
              (marici-int-positive-denominator e))))
        (marici-int-add
          (marici-int-mul a
            (marici-int-mul
              (marici-int-positive-denominator e)
              (marici-int-positive-denominator f)))
          (marici-int-mul
            (marici-int-add
              (marici-int-mul b (marici-int-positive-denominator f))
              (marici-int-mul c (marici-int-positive-denominator e)))
            (marici-int-positive-denominator d)))
        (marici-int-add
          (marici-scale-by-positive-denominator a
            (marici-positive-product-predecessor e f))
          (marici-scale-by-positive-denominator
            (marici-int-add
              (marici-scale-by-positive-denominator b f)
              (marici-scale-by-positive-denominator c e)) d))
        (marici-int-three-scale-sum-associativity a b c
          (marici-int-positive-denominator d)
          (marici-int-positive-denominator e)
          (marici-int-positive-denominator f))
        (ap MariciInt MariciInt
          (marici-int-mul
            (marici-int-positive-denominator e)
            (marici-int-positive-denominator f))
          (marici-int-positive-denominator
            (marici-positive-product-predecessor e f))
          (\ denominator → marici-int-add
            (marici-int-mul a denominator)
            (marici-scale-by-positive-denominator
              (marici-int-add
                (marici-scale-by-positive-denominator b f)
                (marici-scale-by-positive-denominator c e)) d))
          (rev MariciInt
            (marici-int-positive-denominator
              (marici-positive-product-predecessor e f))
            (marici-int-mul
              (marici-int-positive-denominator e)
              (marici-int-positive-denominator f))
            (marici-positive-denominator-product e f))))
```

## Boundary

The two raw-addition bracketings now have equal numerators. Combining this path
with `marici-positive-product-predecessor-assoc` yields a path, hence an
equivalence, between the bracketed raw sums.
