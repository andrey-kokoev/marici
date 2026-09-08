# All-degree comparison, endpoint classes, and scalar pairing

```rzk
#lang rzk-1
#data NimaAllDegreeConductorImage
  := nima-image-exterior-coalgebra-on-six-occurrences
  | nima-image-zero-above-degree-six
#data NimaYonedaRestrictionKernel
  := nima-two-sided-ideal-of-nine-mixed-anticommutators
#define nima-Yoneda-restriction-kernel : NimaYonedaRestrictionKernel
  := nima-two-sided-ideal-of-nine-mixed-anticommutators
#data NimaSupportedEndpointClass
  := nima-eight-generic-classes-primitive-nonzero
  | nima-eight-plus-minus-endpoint-classes-nullhomotopic
  | nima-compatible-endpoint-lift-spaces-contractible
#define nima-supported-endpoint-class : NimaSupportedEndpointClass
  := nima-eight-generic-classes-primitive-nonzero
#data NimaTangentialScalarPairing
  := nima-both-excess-traces-pair-to-minus-beta-unit
  | nima-general-pairing-minus-beta-a-plus-b-plus-c-diagonal
  | nima-scalar-readout-kills-trace-difference
#define nima-tangential-scalar-pairing : NimaTangentialScalarPairing
  := nima-scalar-readout-kills-trace-difference
#data NimaScalarPairingPhysicalStatus
  := nima-coefficient-pairing-not-physical-PC-operation
#define nima-scalar-pairing-physical-status : NimaScalarPairingPhysicalStatus
  := nima-coefficient-pairing-not-physical-PC-operation
```
