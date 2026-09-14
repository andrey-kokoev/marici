# Physical pullback basis reconstruction

```rzk
#lang rzk-1
#data NimaPhysicalPullbackC1Basis
  := nima-C1-conductor-plus
  | nima-C1-conductor-minus
  | nima-C1-road-D03
  | nima-C1-road-D25
  | nima-C1-road-D14
#define nima-physical-pullback-C1-basis : NimaPhysicalPullbackC1Basis
  := nima-C1-road-D03

#data NimaPhysicalPullbackBlockDecomposition
  := nima-first-d2-column-supported-on-two-conductor-slots
  | nima-last-three-d2-columns-are-oriented-road-triangle
  | nima-road-order-is-D03-D25-D14
  | nima-ordered-block-labeling-is-unique
#define nima-physical-pullback-block-decomposition
  : NimaPhysicalPullbackBlockDecomposition
  := nima-ordered-block-labeling-is-unique

#data NimaPhysicalPullbackCanonicalRows
  := nima-conductor-row-one-minus-one-zero-zero-zero
  | nima-road-row-zero-zero-one-one-one
  | nima-d1-is-conductor-row-minus-road-row
  | nima-both-rows-evaluate-z-to-plus-one
#define nima-physical-pullback-canonical-rows
  : NimaPhysicalPullbackCanonicalRows
  := nima-both-rows-evaluate-z-to-plus-one

#data NimaPostBasisReconstructionGate
  := nima-restrict-global-Q-functional-to-C1-basis
  | nima-restrict-global-endpoint-functional-to-C1-basis
  | nima-restrict-road-relation-functional-to-C1-basis
  | nima-compare-restricted-rows-with-canonical-two-row-lattice
#define nima-post-basis-reconstruction-gate
  : NimaPostBasisReconstructionGate
  := nima-restrict-global-Q-functional-to-C1-basis
```
