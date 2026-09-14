# Physical-to-coefficient amplitude bridge

A bridge identifies the supported physical residue with the calibrated
coefficient formula pointwise.  This is the exact remaining comparison datum;
it is exposed as an inhabitance problem rather than assumed.

```rzk
#lang rzk-1

#define nima-amplitude-coordinates : U
  := Sigma (_ : MariciInt), Sigma (_ : MariciInt), MariciInt

#define nima-amplitude-coordinate-a
  (x : nima-amplitude-coordinates) : MariciInt
  := first x

#define nima-amplitude-coordinate-b
  (x : nima-amplitude-coordinates) : MariciInt
  := first (second x)

#define nima-amplitude-coordinate-c
  (x : nima-amplitude-coordinates) : MariciInt
  := second (second x)

#define nima-calibrated-coordinate-amplitude
  (beta : MariciInt) (x : nima-amplitude-coordinates) : MariciInt
  := marici-int-negate
       (marici-int-mul beta
         (marici-int-add (nima-amplitude-coordinate-a x)
           (marici-int-add (nima-amplitude-coordinate-b x)
             (nima-amplitude-coordinate-c x))))

#define nima-physical-coefficient-amplitude-bridge
  (Physical Supported : U)
  (beta : MariciInt)
  (gysin : Physical -> Supported)
  (residue : Supported -> MariciInt)
  : U
  := Sigma (coordinates : Physical -> nima-amplitude-coordinates),
       (x : Physical) -> residue (gysin x)
         = nima-calibrated-coordinate-amplitude beta (coordinates x)

#define nima-physical-amplitude-coordinates
  (Physical Supported : U)
  (beta : MariciInt)
  (gysin : Physical -> Supported)
  (residue : Supported -> MariciInt)
  (bridge : nima-physical-coefficient-amplitude-bridge
    Physical Supported beta gysin residue)
  : Physical -> nima-amplitude-coordinates
  := first bridge

#define nima-physical-amplitude-calibration
  (Physical Supported : U)
  (beta : MariciInt)
  (gysin : Physical -> Supported)
  (residue : Supported -> MariciInt)
  (bridge : nima-physical-coefficient-amplitude-bridge
    Physical Supported beta gysin residue)
  (x : Physical)
  : residue (gysin x)
    = nima-calibrated-coordinate-amplitude beta
       (nima-physical-amplitude-coordinates Physical Supported beta
         gysin residue bridge x)
  := second bridge x

#define nima-comparison-filling-calibrated-amplitude
  (Coefficient Physical Comparison Supported : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (beta : MariciInt)
  (gysin : Physical -> Supported)
  (residue : Supported -> MariciInt)
  (bridge : nima-physical-coefficient-amplitude-bridge
    Physical Supported beta gysin residue)
  (filling : Sigma (coefficient : Coefficient),
    Sigma (physical : Physical), difference coefficient physical = zero)
  : MariciInt
  := nima-calibrated-coordinate-amplitude beta
       (nima-physical-amplitude-coordinates Physical Supported beta
         gysin residue bridge (first (second filling)))

#define nima-comparison-filling-physical-equals-calibration
  (Coefficient Physical Comparison Supported : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (beta : MariciInt)
  (gysin : Physical -> Supported)
  (residue : Supported -> MariciInt)
  (bridge : nima-physical-coefficient-amplitude-bridge
    Physical Supported beta gysin residue)
  (filling : Sigma (coefficient : Coefficient),
    Sigma (physical : Physical), difference coefficient physical = zero)
  : residue (gysin (first (second filling)))
    = nima-comparison-filling-calibrated-amplitude
       Coefficient Physical Comparison Supported zero difference beta
       gysin residue bridge filling
  := second bridge (first (second filling))

#data NimaPhysicalCoefficientBridgeStatus
  := nima-pointwise-bridge-type-constructed
  | nima-concrete-bridge-inhabitant-missing
#define nima-physical-coefficient-bridge-status
  : NimaPhysicalCoefficientBridgeStatus
  := nima-pointwise-bridge-type-constructed
```
