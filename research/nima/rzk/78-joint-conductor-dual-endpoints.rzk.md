# Joint conductor dual and endpoint test

```rzk
#lang rzk-1

#data NimaJointNodeDualClass
  := nima-two-branch-Ext-degree-3
  | nima-coupled-conductor-Ext-degree-5
#data NimaConductorResiduePairing
  := nima-primitive-ordered-sixfold-residue
#define nima-conductor-residue-pairing : NimaConductorResiduePairing
  := nima-primitive-ordered-sixfold-residue
#data NimaFivefoldNodePullbackBehavior
  := nima-supported-map-nonzero
  | nima-support-counit-zero
  | nima-derived-conductor-specialization-zero
#data NimaJointSourceComparisonStatus
  := nima-complete-sheet-maps-and-joint-homotopy-constructed
  | nima-spatial-collar-identification-absent
#define nima-joint-source-comparison-status : NimaJointSourceComparisonStatus
  := nima-complete-sheet-maps-and-joint-homotopy-constructed
#define nima-joint-physical-comparison-status : NimaJointSourceComparisonStatus
  := nima-spatial-collar-identification-absent
```
