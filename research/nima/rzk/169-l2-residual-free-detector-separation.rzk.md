# L2 residual and free-detector separation

```rzk
#lang rzk-1
#data NimaL2LabelledResidual
  := nima-s11-minus-q-target-is-3a3-plus-3a3b
#define nima-L2-labelled-residual : NimaL2LabelledResidual
  := nima-s11-minus-q-target-is-3a3-plus-3a3b
#data NimaL2ResidualDetectorPairing
  := nima-alternating-a0-detector-of-L2-residual-is-zero
#define nima-L2-residual-detector-pairing : NimaL2ResidualDetectorPairing
  := nima-alternating-a0-detector-of-L2-residual-is-zero
#data NimaFreeComplementDetectorPairing
  := nima-alternating-a0-detector-of-constant-one-is-one
#define nima-free-complement-detector-pairing : NimaFreeComplementDetectorPairing
  := nima-alternating-a0-detector-of-constant-one-is-one
#data NimaResidualSeparationCorrection
  := nima-L2-residual-is-not-free-unit-class
  | nima-unit-cone-route-is-conditional-on-geometric-unit-residual
  | nima-no-road-unit-realization-yet
#define nima-residual-separation-correction : NimaResidualSeparationCorrection
  := nima-unit-cone-route-is-conditional-on-geometric-unit-residual
```
