# Point-supported three-detector law

A physical amplitude at one selected point does not require a residue formula
for every class of the ambient supported carrier.

```rzk
#lang rzk-1
#define nima-point-supported-detectors
  (Supported Scalars : U) : U
  := Sigma (primary : Supported -> Scalars),
       Sigma (reciprocal : Supported -> Scalars), Supported -> Scalars

#define nima-point-supported-coordinate
  (Supported Scalars : U)
  (detectors : nima-point-supported-detectors Supported Scalars)
  (supported : Supported)
  : Sigma (_ : Scalars), Sigma (_ : Scalars), Scalars
  := (first detectors supported,
      (first (second detectors) supported,
       second (second detectors) supported))

#define nima-point-supported-residue-law
  (Physical Supported Scalars : U)
  (gysin : Physical -> Supported)
  (residue : Supported -> Scalars)
  (calibrate : (Sigma (_ : Scalars), Sigma (_ : Scalars), Scalars) -> Scalars)
  (detectors : nima-point-supported-detectors Supported Scalars)
  (physical : Physical)
  : U
  := residue (gysin physical)
       = calibrate
          (nima-point-supported-coordinate Supported Scalars detectors
            (gysin physical))

#define nima-point-supported-amplitude
  (Physical Supported Scalars : U)
  (gysin : Physical -> Supported)
  (residue : Supported -> Scalars)
  (physical : Physical)
  : Scalars
  := residue (gysin physical)

#define nima-point-supported-amplitude-calibrated
  (Physical Supported Scalars : U)
  (gysin : Physical -> Supported)
  (residue : Supported -> Scalars)
  (calibrate : (Sigma (_ : Scalars), Sigma (_ : Scalars), Scalars) -> Scalars)
  (detectors : nima-point-supported-detectors Supported Scalars)
  (physical : Physical)
  (law : nima-point-supported-residue-law Physical Supported Scalars
    gysin residue calibrate detectors physical)
  : nima-point-supported-amplitude Physical Supported Scalars
      gysin residue physical
    = calibrate
       (nima-point-supported-coordinate Supported Scalars detectors
         (gysin physical))
  := law

#data NimaPointSupportedDetectorStrength
  := nima-three-supported-functionals-retained
  | nima-residue-law-needed-only-on-selected-Gysin-class
  | nima-global-supported-residue-law-is-stronger-than-amplitude-inhabitance
#define nima-point-supported-detector-strength : NimaPointSupportedDetectorStrength
  := nima-residue-law-needed-only-on-selected-Gysin-class

#data NimaPointSupportedDetectorGate
  := nima-construct-primary-endpoint-detector
  | nima-construct-reciprocal-reflection-detector
  | nima-relation-detector-is-rho0
  | nima-prove-one-supported-residue-equality
#define nima-point-supported-detector-gate : NimaPointSupportedDetectorGate
  := nima-prove-one-supported-residue-equality
```
