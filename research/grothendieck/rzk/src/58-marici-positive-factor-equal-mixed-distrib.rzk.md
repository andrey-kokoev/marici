# Positive-factor distributivity for equal mixed magnitudes

The equal-magnitude mixed-sign branch cancels before multiplication and after
multiplication. This supplies the middle comparison branch for positive-factor
mixed distributivity.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-factor-equal-mixed-left-distrib
  ( p a : MariciNat)
  : marici-int-mul (marici-int-pos p)
      (marici-int-add (marici-int-pos a) (marici-int-neg a))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul (marici-int-pos p) (marici-int-pos a))
      (marici-int-mul (marici-int-pos p) (marici-int-neg a))
  := concat MariciInt
      (marici-int-mul (marici-int-pos p)
        (marici-int-add (marici-int-pos a) (marici-int-neg a)))
      marici-int-zero
      (marici-int-add
        (marici-int-mul (marici-int-pos p) (marici-int-pos a))
        (marici-int-mul (marici-int-pos p) (marici-int-neg a)))
      (concat MariciInt
        (marici-int-mul (marici-int-pos p)
          (marici-int-add (marici-int-pos a) (marici-int-neg a)))
        (marici-int-mul (marici-int-pos p) marici-int-zero)
        marici-int-zero
        (ap MariciInt MariciInt
          (marici-int-add (marici-int-pos a) (marici-int-neg a))
          marici-int-zero
          (\ z → marici-int-mul (marici-int-pos p) z)
          (marici-int-add-pos-neg-self a))
        (marici-int-mul-zero-right (marici-int-pos p)))
      (rev MariciInt
        (marici-int-add
          (marici-int-mul (marici-int-pos p) (marici-int-pos a))
          (marici-int-mul (marici-int-pos p) (marici-int-neg a)))
        marici-int-zero
        (marici-int-add-pos-neg-self
          (marici-positive-product-predecessor p a)))
```

## Boundary

This theorem settles the equal comparison branch for a positive multiplier.
The strict branches still require paths identifying multiplication of the
already-normalized source residual with the scaled residual constructors from
modules 56 and 57.
