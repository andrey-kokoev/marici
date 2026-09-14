# qg2 conductor primitive normalization

```rzk
#lang rzk-1
#data NimaQG2ConductorCoefficientRing
  := nima-localize-at-p-and-kappa-minus1
  | nima-connecting-coefficient-is-a-unit
#define nima-qg2-conductor-coefficient-ring : NimaQG2ConductorCoefficientRing
  := nima-connecting-coefficient-is-a-unit
#data NimaQG2ConductorUnit
  := nima-coefficient-minus1-over32p4kappa-minus1-squared
  | nima-inverse-minus32p4kappa-minus1-squared
  | nima-product-is-one
#define nima-qg2-conductor-unit : NimaQG2ConductorUnit
  := nima-product-is-one
#data NimaQG2PrimitiveDetectorNormalization
  := nima-strip-conductor-unit-to-obtain-primitive-generator
  | nima-normalized-conductor-detector-value-one
  | nima-selected-L2-v-detector-value-one
#define nima-qg2-primitive-detector-normalization
  : NimaQG2PrimitiveDetectorNormalization
  := nima-normalized-conductor-detector-value-one
#data NimaQG2ToL2RemainingComparison
  := nima-scalar-normalizations-now-match
  | nima-identify-conductor-and-log-orientation-lines
  | nima-construct-ambient-relative-cut-chain-transport
#define nima-qg2-to-L2-remaining-comparison : NimaQG2ToL2RemainingComparison
  := nima-identify-conductor-and-log-orientation-lines
```
