# Coefficient amplitude model inhabitant

The bridge type is inhabited for the exact three-coordinate coefficient model.
This gives a normalization test fixture and separates the remaining physical
work from any defect in the Rzk amplitude definitions.

```rzk
#lang rzk-1

#define nima-amplitude-bridge-from-coordinate-law
  (Physical Supported : U)
  (beta : MariciInt)
  (gysin : Physical -> Supported)
  (residue : Supported -> MariciInt)
  (coordinates : Physical -> nima-amplitude-coordinates)
  (coordinate-law : (x : Physical) -> residue (gysin x)
    = nima-calibrated-coordinate-amplitude beta (coordinates x))
  : nima-physical-coefficient-amplitude-bridge
      Physical Supported beta gysin residue
  := (coordinates, coordinate-law)

#define nima-coefficient-model-gysin
  : nima-amplitude-coordinates -> nima-amplitude-coordinates
  := \ x -> x

#define nima-coefficient-model-residue
  (beta : MariciInt) : nima-amplitude-coordinates -> MariciInt
  := \ x -> nima-calibrated-coordinate-amplitude beta x

#define nima-coefficient-model-amplitude-bridge
  (beta : MariciInt)
  : nima-physical-coefficient-amplitude-bridge
      nima-amplitude-coordinates nima-amplitude-coordinates beta
      nima-coefficient-model-gysin (nima-coefficient-model-residue beta)
  := (\ x -> x, \ x -> refl)

#define nima-coefficient-model-bridge-evaluates
  (beta : MariciInt) (x : nima-amplitude-coordinates)
  : nima-physical-amplitude-calibration
      nima-amplitude-coordinates nima-amplitude-coordinates beta
      nima-coefficient-model-gysin (nima-coefficient-model-residue beta)
      (nima-coefficient-model-amplitude-bridge beta) x
    = refl
  := refl

#define nima-coefficient-model-residue-formula
  (beta a b c : MariciInt)
  : nima-coefficient-model-residue beta (a, (b, c))
    = marici-int-negate
       (marici-int-mul beta (marici-int-add a (marici-int-add b c)))
  := refl

#data NimaAmplitudeModelSeparation
  := nima-coefficient-bridge-inhabited
  | nima-physical-bridge-remains-uninhabited
  | nima-Rzk-amplitude-interface-normalization-tested
#define nima-amplitude-model-separation : NimaAmplitudeModelSeparation
  := nima-coefficient-bridge-inhabited
```
