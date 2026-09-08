# Normalization-conductor two-term roof data

This module isolates the additive coefficient content of the normalization
square.  A coefficient in the glued ring is represented by one conductor
coefficient and independent positive/negative augmentation-ideal components.
No sheet section of the conductor quotient is selected for the physical map.

```rzk
#lang rzk-1

#define NimaNormalizationB : U
  := Sigma (_ : MariciInt), Sigma (_ : MariciInt), MariciInt
#define NimaNormalizationPlus : U := Sigma (_ : MariciInt), MariciInt
#define NimaNormalizationMinus : U := Sigma (_ : MariciInt), MariciInt
#define NimaNormalizationSheets : U
  := Sigma (_ : NimaNormalizationPlus), NimaNormalizationMinus
#define NimaConductorLine : U := MariciInt

#define nima-normalization-nu : NimaNormalizationB -> NimaNormalizationSheets
  := \ (c,(p,m)) -> ((c,p),(c,m))

#define nima-normalization-rho : NimaNormalizationSheets -> NimaConductorLine
  := \ ((cp,p),(cm,m)) -> marici-int-add cp (marici-int-negate cm)

#define nima-normalization-rho-nu : (b : NimaNormalizationB) ->
  nima-normalization-rho (nima-normalization-nu b) = marici-int-zero
  := \ (c,(p,m)) -> marici-int-add-inverse-right c

#define nima-int-difference-zero-center
  (x y : MariciInt)
  (h : marici-int-add x (marici-int-negate y) = marici-int-zero)
  : x = y
  := nima-frame-concat MariciInt x
       (marici-int-add x marici-int-zero) y
       (nima-frame-rev MariciInt (marici-int-add x marici-int-zero) x
         (marici-int-add-zero-right x))
       (nima-frame-concat MariciInt
         (marici-int-add x marici-int-zero)
         (marici-int-add x (marici-int-add (marici-int-negate y) y)) y
         (nima-frame-ap MariciInt MariciInt (marici-int-add x)
           marici-int-zero (marici-int-add (marici-int-negate y) y)
           (nima-frame-rev MariciInt
             (marici-int-add (marici-int-negate y) y) marici-int-zero
             (marici-int-add-inverse-left y)))
         (nima-frame-concat MariciInt
           (marici-int-add x (marici-int-add (marici-int-negate y) y))
           (marici-int-add (marici-int-add x (marici-int-negate y)) y) y
           (nima-frame-rev MariciInt
             (marici-int-add (marici-int-add x (marici-int-negate y)) y)
             (marici-int-add x (marici-int-add (marici-int-negate y) y))
             (marici-int-add-assoc x (marici-int-negate y) y))
           (nima-frame-concat MariciInt
             (marici-int-add (marici-int-add x (marici-int-negate y)) y)
             (marici-int-add marici-int-zero y) y
             (nima-frame-ap MariciInt MariciInt (\ q -> marici-int-add q y)
               (marici-int-add x (marici-int-negate y)) marici-int-zero h)
             refl)))

#define nima-normalization-plus-center : NimaNormalizationSheets -> MariciInt
  := \ ((cp,p),(cm,m)) -> cp
#define nima-normalization-minus-center : NimaNormalizationSheets -> MariciInt
  := \ ((cp,p),(cm,m)) -> cm
#define nima-normalization-plus-ideal : NimaNormalizationSheets -> MariciInt
  := \ ((cp,p),(cm,m)) -> p
#define nima-normalization-minus-ideal : NimaNormalizationSheets -> MariciInt
  := \ ((cp,p),(cm,m)) -> m

#define nima-normalization-kernel-center
  (s : NimaNormalizationSheets)
  (closed : nima-normalization-rho s = marici-int-zero)
  : nima-normalization-plus-center s = nima-normalization-minus-center s
  := nima-int-difference-zero-center
       (nima-normalization-plus-center s) (nima-normalization-minus-center s) closed

#define nima-normalization-kernel-lift : NimaNormalizationSheets -> NimaNormalizationB
  := \ ((cp,p),(cm,m)) -> (cp,(p,m))

#define nima-normalization-lifted-plus-center (s : NimaNormalizationSheets) : MariciInt
  := nima-normalization-plus-center (nima-normalization-nu (nima-normalization-kernel-lift s))
#define nima-normalization-lifted-minus-center (s : NimaNormalizationSheets) : MariciInt
  := nima-normalization-minus-center (nima-normalization-nu (nima-normalization-kernel-lift s))
#define nima-normalization-lifted-plus-ideal (s : NimaNormalizationSheets) : MariciInt
  := nima-normalization-plus-ideal (nima-normalization-nu (nima-normalization-kernel-lift s))
#define nima-normalization-lifted-minus-ideal (s : NimaNormalizationSheets) : MariciInt
  := nima-normalization-minus-ideal (nima-normalization-nu (nima-normalization-kernel-lift s))

#define nima-normalization-kernel-lift-plus-center : (s : NimaNormalizationSheets) ->
  nima-normalization-lifted-plus-center s = nima-normalization-plus-center s
  := \ ((cp,p),(cm,m)) -> refl
#define nima-normalization-kernel-lift-plus-ideal : (s : NimaNormalizationSheets) ->
  nima-normalization-lifted-plus-ideal s = nima-normalization-plus-ideal s
  := \ ((cp,p),(cm,m)) -> refl
#define nima-normalization-kernel-lift-minus-ideal : (s : NimaNormalizationSheets) ->
  nima-normalization-lifted-minus-ideal s = nima-normalization-minus-ideal s
  := \ ((cp,p),(cm,m)) -> refl
#define nima-normalization-kernel-lift-minus-center
  (s : NimaNormalizationSheets)
  (closed : nima-normalization-rho s = marici-int-zero)
  : nima-normalization-lifted-minus-center s = nima-normalization-minus-center s
  := nima-normalization-kernel-center s closed

#define nima-normalization-rho-section : NimaConductorLine -> NimaNormalizationSheets
  := \ c -> ((c,marici-int-zero),(marici-int-zero,marici-int-zero))

#define nima-normalization-rho-surjective (c : NimaConductorLine)
  : nima-normalization-rho (nima-normalization-rho-section c) = c
  := marici-int-add-zero-right c

#data NimaNormalizationRoofObject
  := nima-normalization-roof-J
  | nima-normalization-roof-conductor
  | nima-normalization-roof-T

#define nima-physical-normalization-roof-left (p : NimaPhysicalJ) : NimaConductorLine
  := nima-physical-a-C p

#define nima-physical-normalization-roof-primitive
  : nima-physical-normalization-roof-left nima-physical-z = marici-int-one
  := nima-physical-a-z
```
