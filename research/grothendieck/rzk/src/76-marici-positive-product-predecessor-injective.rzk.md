# Positive-product predecessor injectivity

For a fixed positive factor, equality of positive-product predecessors implies
equality of the other predecessor payloads. Adding a successor converts the
encoded products to full natural products, where module 73 cancels the factor.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-product-predecessor-injective
  ( p a b : MariciNat)
  ( e : marici-positive-product-predecessor p a
      =_{MariciNat} marici-positive-product-predecessor p b)
  : a =_{MariciNat} b
  := marici-succ-injective a b
      (marici-mul-positive-left-injective p
        (marici-succ a) (marici-succ b)
        (concat MariciNat
          (marici-mul (marici-succ p) (marici-succ a))
          (marici-succ (marici-positive-product-predecessor p a))
          (marici-mul (marici-succ p) (marici-succ b))
          (rev MariciNat
            (marici-succ (marici-positive-product-predecessor p a))
            (marici-mul (marici-succ p) (marici-succ a))
            (marici-succ-positive-product p a))
          (concat MariciNat
            (marici-succ (marici-positive-product-predecessor p a))
            (marici-succ (marici-positive-product-predecessor p b))
            (marici-mul (marici-succ p) (marici-succ b))
            (ap MariciNat MariciNat
              (marici-positive-product-predecessor p a)
              (marici-positive-product-predecessor p b)
              marici-succ e)
            (marici-succ-positive-product p b))))
```

## Boundary

The encoded positive-product operation is injective in either payload for a
fixed positive factor. Lifting this through the positive and negative integer
constructors, with module 75 handling mixed constructors, remains.
