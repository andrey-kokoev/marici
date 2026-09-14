# Explicit L2 transition detector

```rzk
#lang rzk-1
#data NimaL2ExplicitDetector
  := nima-rho0-extracts-u0-a3-b0-coefficient
#define nima-L2-explicit-detector : NimaL2ExplicitDetector
  := nima-rho0-extracts-u0-a3-b0-coefficient
#data NimaL2ExplicitDetectorLaw
  := nima-rho0-vanishes-on-all-A-image-columns
  | nima-rho0-of-3a3-plus-3a3b-is3
#define nima-L2-explicit-detector-law : NimaL2ExplicitDetectorLaw
  := nima-rho0-of-3a3-plus-3a3b-is3
#data NimaL2AllDegreeDetectorReason
  := nima-u0-image-has-a-order-at-least4
  | nima-da-k-a3-term-always-gains-positive-L2-a-factor
#define nima-L2-all-degree-detector-reason : NimaL2AllDegreeDetectorReason
  := nima-u0-image-has-a-order-at-least4
#data NimaL2LogSelectorNormalization
  := nima-rho0-over3-pairs-transition-to-log-unit
  | nima-defined-over-Z-one-third
  | nima-no-integral-unit-pairing-for-this-transition
#define nima-L2-log-selector-normalization : NimaL2LogSelectorNormalization
  := nima-rho0-over3-pairs-transition-to-log-unit
```
