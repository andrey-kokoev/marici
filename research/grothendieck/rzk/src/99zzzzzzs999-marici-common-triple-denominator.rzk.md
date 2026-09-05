# Common triple denominator predecessor

Associativity and commutativity align all three nested positive-product
denominator predecessors with the ordering `(d e) f`.

```rzk
#lang rzk-1
```

```rzk
#define marici-common-triple-denominator-predecessor
  ( d e f : MariciNat)
  : MariciNat
  := marici-positive-product-predecessor
      (marici-positive-product-predecessor d e) f

#define marici-triple-denominator-middle-first
  ( d e f : MariciNat)
  : marici-positive-product-predecessor
      (marici-positive-product-predecessor e f) d
    =_{MariciNat}
    marici-common-triple-denominator-predecessor d e f
  := concat MariciNat
      (marici-positive-product-predecessor
        (marici-positive-product-predecessor e f) d)
      (marici-positive-product-predecessor e
        (marici-positive-product-predecessor f d))
      (marici-common-triple-denominator-predecessor d e f)
      (marici-positive-product-predecessor-assoc e f d)
      (concat MariciNat
        (marici-positive-product-predecessor e
          (marici-positive-product-predecessor f d))
        (marici-positive-product-predecessor e
          (marici-positive-product-predecessor d f))
        (marici-common-triple-denominator-predecessor d e f)
        (ap MariciNat MariciNat
          (marici-positive-product-predecessor f d)
          (marici-positive-product-predecessor d f)
          (\ inner → marici-positive-product-predecessor e inner)
          (marici-positive-product-predecessor-comm f d))
        (concat MariciNat
          (marici-positive-product-predecessor e
            (marici-positive-product-predecessor d f))
          (marici-positive-product-predecessor
            (marici-positive-product-predecessor e d) f)
          (marici-common-triple-denominator-predecessor d e f)
          (rev MariciNat
            (marici-positive-product-predecessor
              (marici-positive-product-predecessor e d) f)
            (marici-positive-product-predecessor e
              (marici-positive-product-predecessor d f))
            (marici-positive-product-predecessor-assoc e d f))
          (ap MariciNat MariciNat
            (marici-positive-product-predecessor e d)
            (marici-positive-product-predecessor d e)
            (\ pair → marici-positive-product-predecessor pair f)
            (marici-positive-product-predecessor-comm e d))))

#define marici-triple-denominator-outer-first
  ( d e f : MariciNat)
  : marici-positive-product-predecessor
      (marici-positive-product-predecessor d f) e
    =_{MariciNat}
    marici-common-triple-denominator-predecessor d e f
  := concat MariciNat
      (marici-positive-product-predecessor
        (marici-positive-product-predecessor d f) e)
      (marici-positive-product-predecessor d
        (marici-positive-product-predecessor f e))
      (marici-common-triple-denominator-predecessor d e f)
      (marici-positive-product-predecessor-assoc d f e)
      (concat MariciNat
        (marici-positive-product-predecessor d
          (marici-positive-product-predecessor f e))
        (marici-positive-product-predecessor d
          (marici-positive-product-predecessor e f))
        (marici-common-triple-denominator-predecessor d e f)
        (ap MariciNat MariciNat
          (marici-positive-product-predecessor f e)
          (marici-positive-product-predecessor e f)
          (\ inner → marici-positive-product-predecessor d inner)
          (marici-positive-product-predecessor-comm f e))
        (rev MariciNat
          (marici-common-triple-denominator-predecessor d e f)
          (marici-positive-product-predecessor d
            (marici-positive-product-predecessor e f))
          (marici-positive-product-predecessor-assoc d e f)))
```

## Boundary

All scaled directed-difference denominators now align with one common triple
predecessor. Numerator absolute-value bounds can now be assembled in one raw
fraction order comparison.
