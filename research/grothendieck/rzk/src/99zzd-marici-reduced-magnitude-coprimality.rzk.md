# Reducedness excludes nonunit magnitude common factors

The signed numerator's magnitude supplies the natural-number side of the
coprime argument. Any nonunit positive factor shared by that magnitude and the
denominator lifts back to signed integer divisibility with the source sign,
contradicting raw-component reducedness.

```rzk
#lang rzk-1
```

```rzk
#data MariciMagnitudeNonunitCommonPositiveFactor
  ( numerator : MariciInt)
  ( denominator-predecessor : MariciNat)
  := marici-magnitude-nonunit-common-positive-factor
      ( factor-predecessor : MariciNat)
      ( magnitude-cofactor-predecessor : MariciNat)
      ( denominator-cofactor-predecessor : MariciNat)
      ( magnitude-equation : marici-mul
          (marici-succ magnitude-cofactor-predecessor)
          (marici-succ (marici-succ factor-predecessor))
        =_{MariciNat} marici-int-magnitude numerator)
      ( denominator-equation : marici-mul
          (marici-succ denominator-cofactor-predecessor)
          (marici-succ (marici-succ factor-predecessor))
        =_{MariciNat} marici-succ denominator-predecessor)

#define marici-magnitude-common-factor-gives-raw-common-factor
  ( a : MariciInt)
  ( d : MariciNat)
  ( common : MariciMagnitudeNonunitCommonPositiveFactor a d)
  : MariciRawComponentsNonunitCommonPositiveFactor a d
  := match common
      ( marici-magnitude-nonunit-common-positive-factor
          f q r magnitude-equation denominator-equation ⇒
            marici-raw-components-nonunit-common-positive-factor
              a d f
              (match (marici-magnitude-factorization-lifts-to-int
                a q (marici-succ f) magnitude-equation)
                ( marici-int-right-positive-divides-witness
                    signed-cofactor numerator-equation ⇒
                      marici-raw-components-common-positive-factor
                        a d (marici-succ f)
                        signed-cofactor r
                        numerator-equation denominator-equation)))

#define marici-reduced-components-have-coprime-magnitude
  ( a : MariciInt)
  ( d : MariciNat)
  ( reduced : MariciRawComponentsAreReduced a d)
  : MariciMagnitudeNonunitCommonPositiveFactor a d → MariciEmpty
  := \ common → reduced
      (marici-magnitude-common-factor-gives-raw-common-factor
        a d common)
```

## Boundary

Raw reducedness now supplies the exact natural coprimality input required by a
Euclid argument: no structurally nonunit positive factor is shared by the
numerator magnitude and denominator. The remaining bridge must use
cross-product equality to show that the denominator divides the opposite
denominator under this coprimality condition.
