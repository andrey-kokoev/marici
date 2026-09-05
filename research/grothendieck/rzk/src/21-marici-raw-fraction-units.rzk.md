# Raw-fraction multiplicative units and zero representatives

The raw constructor has a strict multiplicative unit. Zero, by contrast, has
one raw representative at every positive denominator; those representatives
are related but are not identified as constructor terms.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-mul-one-right
  ( p : MariciRawFraction)
  : marici-raw-fraction-mul p marici-raw-one
    =_{MariciRawFraction} p
  := match p
      ( marici-raw-fraction a d ⇒
          concat MariciRawFraction
            (marici-raw-fraction
              (marici-int-mul a marici-int-one)
              (marici-positive-product-predecessor d marici-zero))
            (marici-raw-fraction a
              (marici-positive-product-predecessor d marici-zero))
            (marici-raw-fraction a d)
            (ap MariciInt MariciRawFraction
              (marici-int-mul a marici-int-one) a
              (\ n → marici-raw-fraction n
                (marici-positive-product-predecessor d marici-zero))
              (marici-int-mul-one-right a))
            (ap MariciNat MariciRawFraction
              (marici-positive-product-predecessor d marici-zero) d
              (\ e → marici-raw-fraction a e)
              (marici-positive-product-one-right d)))

#define marici-raw-fraction-mul-one-left
  ( p : MariciRawFraction)
  : marici-raw-fraction-mul marici-raw-one p
    =_{MariciRawFraction} p
  := concat MariciRawFraction
      (marici-raw-fraction-mul marici-raw-one p)
      (marici-raw-fraction-mul p marici-raw-one)
      p
      (marici-raw-fraction-mul-comm marici-raw-one p)
      (marici-raw-fraction-mul-one-right p)
```

```rzk
#define marici-raw-zero-at
  ( d : MariciNat)
  : MariciRawFraction
  := marici-raw-fraction marici-int-zero d

#define marici-raw-zero-at-equivalent
  ( d e : MariciNat)
  : marici-raw-fraction-equivalent
      (marici-raw-zero-at d) (marici-raw-zero-at e)
  := refl
```

## Boundary

The multiplicative unit is strict because multiplying a positive denominator
by one preserves its predecessor. Zero representatives with different stored
denominators are only related. A canonical rational zero therefore requires a
normalization or quotient/retract construction; raw syntax alone does not
identify it.
