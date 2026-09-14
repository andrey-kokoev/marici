# First Gauss-Manin Cech continuation

```rzk
#lang rzk-1
#data NimaPhysicalNormalGaussManinLift
  := nima-three-local-normal-lifts-tangent-to-Cayley-Menger-boundary
  | nima-explicit-K-denominators-cancel
  | nima-no-new-denominator-support
#define nima-physical-normal-Gauss-Manin-lift : NimaPhysicalNormalGaussManinLift
  := nima-no-new-denominator-support
#data NimaFirstGaussManinWallTransport
  := nima-three-transported-Cech-components-zero
  | nima-three-derivative-denominators-coprime-to-Q
  | nima-no-quartic-supported-first-transition
#define nima-first-Gauss-Manin-wall-transport : NimaFirstGaussManinWallTransport
  := nima-three-transported-Cech-components-zero
#data NimaGaussManinPhysicalScope
  := nima-contact-weighted-adapter-on-main-boundary
  | nima-absolute-lift-not-selected
  | nima-all-signed-minor-tangencies-unproved
  | nima-period-rank-and-tensor-polarization-unproved
#define nima-Gauss-Manin-physical-scope : NimaGaussManinPhysicalScope
  := nima-absolute-lift-not-selected
#data NimaRoadCechCompletionProgress
  := nima-local-and-first-transport-Cech-terms-close
  | nima-higher-localization-extension-gluing-still-open
#define nima-road-Cech-completion-progress : NimaRoadCechCompletionProgress
  := nima-local-and-first-transport-Cech-terms-close
```
