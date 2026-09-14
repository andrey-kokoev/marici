# Five-direction normalized physical amplitude

```rzk
#lang rzk-1
#define nima-five-direction-normalized-amplitude
  (FiveLift Physical Supported Scalars : U)
  (physical-point : FiveLift -> Physical)
  (gysin : Physical -> Supported)
  (residue : Supported -> Scalars)
  (s W v : Supported)
  (add : Supported -> Supported -> Supported)
  (beta one : Scalars)
  (scalar-add scalar-multiply : Scalars -> Scalars -> Scalars)
  (scalar-negate : Scalars -> Scalars)
  : U
  := Sigma (lift : FiveLift),
       Sigma
         (_ : gysin (physical-point lift) = add s (add W v)),
         residue (gysin (physical-point lift))
           = scalar-negate
               (scalar-multiply beta
                 (scalar-add one (scalar-add one one)))

#define nima-five-direction-normalized-amplitude-point
  (FiveLift Physical Supported Scalars : U)
  (physical-point : FiveLift -> Physical)
  (gysin : Physical -> Supported)
  (residue : Supported -> Scalars)
  (s W v : Supported)
  (add : Supported -> Supported -> Supported)
  (beta one : Scalars)
  (scalar-add scalar-multiply : Scalars -> Scalars -> Scalars)
  (scalar-negate : Scalars -> Scalars)
  (witness : nima-five-direction-normalized-amplitude
    FiveLift Physical Supported Scalars physical-point gysin residue
    s W v add beta one scalar-add scalar-multiply scalar-negate)
  : Physical
  := physical-point (first witness)

#define nima-five-direction-normalized-amplitude-residue
  (FiveLift Physical Supported Scalars : U)
  (physical-point : FiveLift -> Physical)
  (gysin : Physical -> Supported)
  (residue : Supported -> Scalars)
  (s W v : Supported)
  (add : Supported -> Supported -> Supported)
  (beta one : Scalars)
  (scalar-add scalar-multiply : Scalars -> Scalars -> Scalars)
  (scalar-negate : Scalars -> Scalars)
  (witness : nima-five-direction-normalized-amplitude
    FiveLift Physical Supported Scalars physical-point gysin residue
    s W v add beta one scalar-add scalar-multiply scalar-negate)
  : residue (gysin (physical-point (first witness)))
      = scalar-negate
          (scalar-multiply beta
            (scalar-add one (scalar-add one one)))
  := second (second witness)

#define nima-assemble-five-direction-normalized-amplitude
  (FiveLift Physical Supported Scalars : U)
  (physical-point : FiveLift -> Physical)
  (gysin : Physical -> Supported)
  (residue : Supported -> Scalars)
  (s W v : Supported)
  (add : Supported -> Supported -> Supported)
  (beta one : Scalars)
  (scalar-add scalar-multiply : Scalars -> Scalars -> Scalars)
  (scalar-negate : Scalars -> Scalars)
  (lift : FiveLift)
  (image-law : gysin (physical-point lift) = add s (add W v))
  (residue-law : residue (gysin (physical-point lift))
    = scalar-negate
        (scalar-multiply beta (scalar-add one (scalar-add one one))))
  : nima-five-direction-normalized-amplitude
      FiveLift Physical Supported Scalars physical-point gysin residue
      s W v add beta one scalar-add scalar-multiply scalar-negate
  := (lift, (image-law, residue-law))

#data NimaFiveDirectionNormalizedWitnessStatus
  := nima-road-group-corrected-five-lift-retained
  | nima-primitive-pullback-image-is-s-plus-W-plus-v
  | nima-pointwise-residue-is-minus-beta-times-three
  | nima-normalized-selected-amplitude-witness-assembled
#define nima-five-direction-normalized-witness-status
  : NimaFiveDirectionNormalizedWitnessStatus
  := nima-normalized-selected-amplitude-witness-assembled
```
