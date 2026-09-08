# Morse Q-filling coordinates and lower-support attachment

This module records the finite integral consequence of the new filling-torsor
calculation.  A variation is represented by its three long-facet coefficients;
the diagonal variation is already null in the Q-filling torsor.

```rzk
#lang rzk-1

#define NimaMorseFillingVariation : U
  := Sigma (_ : MariciInt), Sigma (_ : MariciInt), MariciInt

#define NimaMorseFillingCoordinates : U
  := Sigma (_ : MariciInt), MariciInt

#define nima-morse-filling-coordinates
  : NimaMorseFillingVariation -> NimaMorseFillingCoordinates
  := \ (c03,(c14,c25)) ->
       (marici-int-add c03 (marici-int-negate c25),
        marici-int-add c14 (marici-int-negate c25))

#define NimaShortBoundaryAttachment5 : U
  := Sigma (_ : MariciInt), Sigma (_ : MariciInt), Sigma (_ : MariciInt),
       Sigma (_ : MariciInt), MariciInt

#define nima-morse-short-boundary-attachment
  : NimaMorseFillingVariation -> NimaShortBoundaryAttachment5
  := \ (c03,(c14,c25)) ->
       (marici-int-add (marici-int-negate c03) c14,
       (marici-int-add c03 (marici-int-negate c25),
       (marici-int-add c03 (marici-int-negate c25),
       (marici-int-add (marici-int-negate c03) c14,
        marici-int-add (marici-int-negate c14) c25))))

#define nima-morse-diagonal-first-coordinate-zero (c : MariciInt)
  : marici-int-add c (marici-int-negate c) = marici-int-zero
  := marici-int-add-inverse-right c

#define nima-morse-diagonal-second-coordinate-zero (c : MariciInt)
  : marici-int-add c (marici-int-negate c) = marici-int-zero
  := marici-int-add-inverse-right c

#define nima-morse-zero-coordinates-force-diagonal
  (c03 c14 c25 : MariciInt)
  (first-zero : marici-int-add c03 (marici-int-negate c25) = marici-int-zero)
  (second-zero : marici-int-add c14 (marici-int-negate c25) = marici-int-zero)
  : Sigma (_ : c03 = c25), c14 = c25
  := (nima-int-difference-zero-center c03 c25 first-zero,
      nima-int-difference-zero-center c14 c25 second-zero)

#define nima-morse-attachment-kernel-diagonal
  (c03 c14 c25 : MariciInt)
  (row0 : marici-int-add (marici-int-negate c03) c14 = marici-int-zero)
  (row1 : marici-int-add c03 (marici-int-negate c25) = marici-int-zero)
  (row4 : marici-int-add (marici-int-negate c14) c25 = marici-int-zero)
  : Sigma (_ : c03 = c25), c14 = c25
  := (nima-int-difference-zero-center c03 c25 row1,
      nima-frame-rev MariciInt c25 c14
        (nima-int-difference-zero-center c25 c14
          (nima-frame-concat MariciInt
            (marici-int-add c25 (marici-int-negate c14))
            (marici-int-add (marici-int-negate c14) c25)
            marici-int-zero
            (marici-int-add-comm c25 (marici-int-negate c14)) row4)))

#define nima-morse-fixed-attachment-unique-class
  (c03 c14 c25 : MariciInt)
  (first-coordinate-zero : marici-int-add c03 (marici-int-negate c25) = marici-int-zero)
  (second-coordinate-zero : marici-int-add c14 (marici-int-negate c25) = marici-int-zero)
  : Sigma (_ : c03 = c25), c14 = c25
  := nima-morse-zero-coordinates-force-diagonal c03 c14 c25
       first-coordinate-zero second-coordinate-zero
```
