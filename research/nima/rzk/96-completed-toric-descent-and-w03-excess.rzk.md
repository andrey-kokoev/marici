# Completed toric descent and W03 excess

```rzk
#lang rzk-1
#data NimaCompletedToricDescentStatus
  := nima-proper-trace-equivalence-on-completed-dual
  | nima-complete-Cartier-endpoint-pair-descends
#data NimaCompletedCentralRestriction
  := nima-four-free-generic-dual-lines-degree-3
  | nima-no-derived-limit-one-term
  | nima-normalized-generic-trace-zero
  | nima-six-upper-endpoint-terms-persist
#define nima-completed-central-restriction : NimaCompletedCentralRestriction
  := nima-normalized-generic-trace-zero
#data NimaW03CostalkGenerator
  := nima-W03-primary-generator-degree-2
  | nima-W03-excess-generator-degree-3
  | nima-W03-residual-generator-degree-3
#data NimaW03MapDecomposition
  := nima-W03-map-beta-primary-plus-excess
  | nima-W03-excess-nonzero-zero-primary
#define nima-W03-map-decomposition : NimaW03MapDecomposition
  := nima-W03-map-beta-primary-plus-excess
#data NimaW03CartierBehavior
  := nima-source-shifted-X03-Cartier-preserves-excess
  | nima-identifying-native-and-occurrence-35-deletes-class
#define nima-W03-Cartier-behavior : NimaW03CartierBehavior
  := nima-source-shifted-X03-Cartier-preserves-excess
#data NimaCompletedToricPhysicalStatus
  := nima-full-physical-supported-comparison-not-yet-identified
#define nima-completed-toric-physical-status : NimaCompletedToricPhysicalStatus
  := nima-full-physical-supported-comparison-not-yet-identified
```
