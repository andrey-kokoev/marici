# Candidate group/reflection split

```rzk
#lang rzk-1
#data NimaCandidateAlgebraicGroupCoherence
  := nima-group-operation-comparison-closed
  | nima-group-operation-comparison-zero-class
  | nima-group-operation-integral-homotopy
  | nima-native-bar-and-endpoint-group-equivariant
#define nima-candidate-algebraic-group-coherence : NimaCandidateAlgebraicGroupCoherence
  := nima-group-operation-integral-homotopy
#data NimaCandidateReflectionFormula
  := nima-reflection-W-is-minus-W-plus-r11-r00-commutator
#define nima-candidate-reflection-formula : NimaCandidateReflectionFormula
  := nima-reflection-W-is-minus-W-plus-r11-r00-commutator
#data NimaCandidatePhysicalReflectionGate
  := nima-endpoint-labels-reflection-exchanged
  | nima-no-physical-parity-selected
  | nima-physical-parity-transport-only-remaining-group-gate
#define nima-candidate-physical-reflection-gate : NimaCandidatePhysicalReflectionGate
  := nima-physical-parity-transport-only-remaining-group-gate
```
