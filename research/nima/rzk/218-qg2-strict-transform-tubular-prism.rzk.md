# qg2 strict-transform tubular prism

```rzk
#lang rzk-1
#data NimaQG2TubularPrismFormula
  := nima-H-r-t-has-x-r
  | nima-H-r-t-has-a-p-minus-r-times-kappa-over2-minus1
  | nima-H-r-t-has-xi-minus1-plus-t-times1-minus-kappa
#define nima-qg2-tubular-prism-formula : NimaQG2TubularPrismFormula
  := nima-H-r-t-has-xi-minus1-plus-t-times1-minus-kappa
#data NimaQG2TubularPrismWallLaw
  := nima-qg2-strict-transform-pulls-back-to-zero
  | nima-r0-face-is-relative-cut-chain
  | nima-r-epsilon-face-is-physical-wall-lift
#define nima-qg2-tubular-prism-wall-law : NimaQG2TubularPrismWallLaw
  := nima-qg2-strict-transform-pulls-back-to-zero
#data NimaQG2TubularPrismBoundaryFaces
  := nima-t0-face-lies-on-qg1-xi-plus1
  | nima-t1-face-specializes-to-conductor-xi-minus-kappa
  | nima-prism-transports-relative-cut-orientation
#define nima-qg2-tubular-prism-boundary-faces : NimaQG2TubularPrismBoundaryFaces
  := nima-prism-transports-relative-cut-orientation
#data NimaQG2TubularPrismScope
  := nima-first-nearby-cycle-collar-constructed
  | nima-higher-order-conductor-face-transport-open
  | nima-full-ringed-filtered-Q-map-open
#define nima-qg2-tubular-prism-scope : NimaQG2TubularPrismScope
  := nima-first-nearby-cycle-collar-constructed
```
