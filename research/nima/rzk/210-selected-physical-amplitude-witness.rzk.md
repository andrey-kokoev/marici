# Selected physical amplitude witness

```rzk
#lang rzk-1
#define nima-selected-physical-amplitude-witness
  (Lift Physical Supported Scalars : U)
  (pointOf : Lift -> Physical)
  (gysin : Physical -> Supported)
  (residue : Supported -> Scalars)
  (calibrate : (Sigma (_ : Scalars), Sigma (_ : Scalars), Scalars) -> Scalars)
  : U
  := Sigma (lift : Lift),
       Sigma (detectors : nima-point-supported-detectors Supported Scalars),
         nima-point-supported-residue-law Physical Supported Scalars
           gysin residue calibrate detectors (pointOf lift)

#define nima-selected-amplitude-physical-point
  (Lift Physical Supported Scalars : U)
  (pointOf : Lift -> Physical)
  (gysin : Physical -> Supported)
  (residue : Supported -> Scalars)
  (calibrate : (Sigma (_ : Scalars), Sigma (_ : Scalars), Scalars) -> Scalars)
  (witness : nima-selected-physical-amplitude-witness
    Lift Physical Supported Scalars pointOf gysin residue calibrate)
  : Physical
  := pointOf (first witness)

#define nima-selected-amplitude-value
  (Lift Physical Supported Scalars : U)
  (pointOf : Lift -> Physical)
  (gysin : Physical -> Supported)
  (residue : Supported -> Scalars)
  (calibrate : (Sigma (_ : Scalars), Sigma (_ : Scalars), Scalars) -> Scalars)
  (witness : nima-selected-physical-amplitude-witness
    Lift Physical Supported Scalars pointOf gysin residue calibrate)
  : Scalars
  := residue (gysin (pointOf (first witness)))

#define nima-selected-amplitude-calibrated
  (Lift Physical Supported Scalars : U)
  (pointOf : Lift -> Physical)
  (gysin : Physical -> Supported)
  (residue : Supported -> Scalars)
  (calibrate : (Sigma (_ : Scalars), Sigma (_ : Scalars), Scalars) -> Scalars)
  (witness : nima-selected-physical-amplitude-witness
    Lift Physical Supported Scalars pointOf gysin residue calibrate)
  : nima-selected-amplitude-value Lift Physical Supported Scalars
      pointOf gysin residue calibrate witness
    = calibrate
       (nima-point-supported-coordinate Supported Scalars
         (first (second witness))
         (gysin (pointOf (first witness))))
  := second (second witness)

#define nima-five-lift-and-point-law-to-selected-amplitude
  (Lift Physical Supported Scalars : U)
  (pointOf : Lift -> Physical)
  (gysin : Physical -> Supported)
  (residue : Supported -> Scalars)
  (calibrate : (Sigma (_ : Scalars), Sigma (_ : Scalars), Scalars) -> Scalars)
  (lift : Lift)
  (detectors : nima-point-supported-detectors Supported Scalars)
  (law : nima-point-supported-residue-law Physical Supported Scalars
    gysin residue calibrate detectors (pointOf lift))
  : nima-selected-physical-amplitude-witness
      Lift Physical Supported Scalars pointOf gysin residue calibrate
  := (lift, (detectors, law))

#data NimaSelectedAmplitudeCompletionInputs
  := nima-road-and-group-corrected-five-lift
  | nima-three-supported-functionals
  | nima-one-Gysin-class-residue-law
#define nima-selected-amplitude-completion-inputs
  : NimaSelectedAmplitudeCompletionInputs
  := nima-one-Gysin-class-residue-law

#data NimaSelectedAmplitudeRemainingPhysicalData
  := nima-two-cell-boundary-comparisons
  | nima-primary-and-reciprocal-supported-comparisons
  | nima-supported-residue-equals-minus-beta-a-plus-b-plus-c-at-point
#define nima-selected-amplitude-remaining-physical-data
  : NimaSelectedAmplitudeRemainingPhysicalData
  := nima-two-cell-boundary-comparisons
```
