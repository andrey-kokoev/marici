# Relative mixed-operation fibre

```rzk
#lang rzk-1
#data NimaRelativeHopfKernel
  := nima-free-associative-on-49-primitive-commutators
  | nima-generator-degrees-2-through-6
  | nima-positive-part-generates-nine-relation-ideal
#define nima-relative-Hopf-kernel : NimaRelativeHopfKernel
  := nima-free-associative-on-49-primitive-commutators
#data NimaRelativeOperationSymmetry
  := nima-dihedral-action-labelled
  | nima-reflection-has-nonlinear-commutator-correction
#define nima-relative-operation-symmetry : NimaRelativeOperationSymmetry
  := nima-reflection-has-nonlinear-commutator-correction
#data NimaMomentAngleFibre
  := nima-homotopy-Sigma-T3-smash-T3
  | nima-sphere-multiplicities-9-18-15-6-1
  | nima-pi5-Whitehead-free-rank-36
  | nima-Hurewicz-kills-rank-36-subgroup
#define nima-moment-angle-fibre : NimaMomentAngleFibre
  := nima-homotopy-Sigma-T3-smash-T3
#data NimaRelativeOperationPhysicalStatus
  := nima-coefficient-combinatorial-not-physical-endpoint-connector
#define nima-relative-operation-physical-status
  : NimaRelativeOperationPhysicalStatus
  := nima-coefficient-combinatorial-not-physical-endpoint-connector
```
