# Selected L2-to-log-line comparison

```rzk
#lang rzk-1
#data NimaL2IntegralSelectedLogMap
  := nima-class-f-maps-to-rho0-f-times-gamma
  | nima-A-image-maps-to-zero
  | nima-distinguished-transition-maps-to-three-gamma
#define nima-L2-integral-selected-log-map : NimaL2IntegralSelectedLogMap
  := nima-distinguished-transition-maps-to-three-gamma
#data NimaL2IntegralLogImage
  := nima-image-is-index-three-sublattice-of-primitive-log-line
#define nima-L2-integral-log-image : NimaL2IntegralLogImage
  := nima-image-is-index-three-sublattice-of-primitive-log-line
#data NimaL2PrimitiveLogNormalizationChoices
  := nima-invert-three
  | nima-adjoin-integral-divided-transition-cell
  | nima-accept-index-three-line-if-physical-normalization-allows
#define nima-L2-primitive-log-normalization-choices
  : NimaL2PrimitiveLogNormalizationChoices
  := nima-adjoin-integral-divided-transition-cell
#data NimaL2SelectedLogComparisonScope
  := nima-rank-one-local-log-comparison-constructed
  | nima-full-filtered-Q-correspondence-open
#define nima-L2-selected-log-comparison-scope : NimaL2SelectedLogComparisonScope
  := nima-rank-one-local-log-comparison-constructed
```
