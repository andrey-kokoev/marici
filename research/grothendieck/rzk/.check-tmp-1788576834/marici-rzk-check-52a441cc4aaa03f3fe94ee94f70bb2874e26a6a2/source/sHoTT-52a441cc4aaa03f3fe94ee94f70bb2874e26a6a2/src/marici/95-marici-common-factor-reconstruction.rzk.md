# Reconstructing a raw fraction from its common-factor certificate

The denominator equation first descends through successor injectivity to the
stored predecessor formula. Constructor congruence then identifies positive
scaling of the extracted cofactor fraction with the original raw fraction.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-factor-predecessor-equation
  ( d r f : MariciNat)
  ( e : marici-mul (marici-succ r) (marici-succ f)
      =_{MariciNat} marici-succ d)
  : marici-positive-product-predecessor r f =_{MariciNat} d
  := marici-succ-injective
      (marici-positive-product-predecessor r f) d
      (concat MariciNat
        (marici-succ (marici-positive-product-predecessor r f))
        (marici-mul (marici-succ r) (marici-succ f))
        (marici-succ d)
        (marici-succ-positive-product r f) e)

#define marici-raw-fraction-component-path
  ( x y : MariciInt)
  ( d e : MariciNat)
  ( p : x =_{MariciInt} y)
  ( q : d =_{MariciNat} e)
  : marici-raw-fraction x d =_{MariciRawFraction}
      marici-raw-fraction y e
  := concat MariciRawFraction
      (marici-raw-fraction x d)
      (marici-raw-fraction y d)
      (marici-raw-fraction y e)
      (ap MariciInt MariciRawFraction x y
        (\ z → marici-raw-fraction z d) p)
      (ap MariciNat MariciRawFraction d e
        (\ n → marici-raw-fraction y n) q)

#define marici-common-factor-reconstruction
  ( a : MariciInt)
  ( d f : MariciNat)
  ( c : MariciRawComponentsCommonPositiveFactor a d f)
  : marici-raw-fraction-scale-positive
      (marici-common-factor-reduced-fraction a d f c) f
    =_{MariciRawFraction} marici-raw-fraction a d
  := match c
      ( marici-raw-components-common-positive-factor q r eq-num eq-den ⇒
          marici-raw-fraction-component-path
            (marici-int-mul q (marici-int-positive-denominator f)) a
            (marici-positive-product-predecessor r f) d
            eq-num
            (marici-positive-factor-predecessor-equation d r f eq-den))
```

## Boundary

Every supplied common-factor certificate reconstructs the original raw
fraction exactly by positive scaling of its extracted cofactor fraction.
Transporting positive-scaling equivalence across this path to obtain direct
relation preservation is the next step; factor selection and coprimality remain
open.
