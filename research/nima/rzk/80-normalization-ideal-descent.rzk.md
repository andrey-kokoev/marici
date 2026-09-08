# Normalization-ideal descent

```rzk
#lang rzk-1

#data NimaNormalizationIdealComparisonClass
  := nima-normalization-ideal-derived-maps-rank-40
  | nima-normalization-ideal-generator-images-rank-34
  | nima-normalization-ideal-relation-only-rank-6
  | nima-normalization-ideal-strict-maps-rank-16
#data NimaNormalizationIdealEquivariantClass
  := nima-normalization-ideal-equivariant-rank-13
  | nima-normalization-symbol-values-rank-11
  | nima-normalization-equivariant-relation-only-rank-2
#data NimaNormalizationSymbolDetection
  := nima-six-term-symbol-does-not-detect-relation-homotopies
#define nima-normalization-symbol-detection : NimaNormalizationSymbolDetection
  := nima-six-term-symbol-does-not-detect-relation-homotopies
#data NimaNormalizationIdealPhysicalStatus
  := nima-no-selected-physical-conductor-morse-map
#define nima-normalization-ideal-physical-status : NimaNormalizationIdealPhysicalStatus
  := nima-no-selected-physical-conductor-morse-map
```
