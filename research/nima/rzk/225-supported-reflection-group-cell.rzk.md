# Supported reflection group cell

```rzk
#lang rzk-1
#data NimaSupportedReflectionPrimitive
  := nima-W-is-normalized-ramified-branch-difference
  | nima-supported-readout-of-W-is-one
  | nima-W-survives-supported-physical-readout
#define nima-supported-reflection-primitive : NimaSupportedReflectionPrimitive
  := nima-W-survives-supported-physical-readout
#data NimaSupportedReflectionCommutator
  := nima-supported-readout-is-commutative-multiplicative
  | nima-readout-kills-r11-r00-commutator
#define nima-supported-reflection-commutator
  : NimaSupportedReflectionCommutator
  := nima-readout-kills-r11-r00-commutator
#data NimaSupportedReflectionGroupCell
  := nima-transport-native-integral-group-homotopy
  | nima-reflection-readout-of-W-is-minus-one
  | nima-supported-odd-reflection-cell-constructed
#define nima-supported-reflection-group-cell
  : NimaSupportedReflectionGroupCell
  := nima-supported-odd-reflection-cell-constructed
#data NimaSupportedReflectionBoundaryGate
  := nima-supported-cell-retains-reflection-coherence
  | nima-define-concrete-rawGroup-physical-defect
  | nima-compare-rawGroup-with-cell-boundary
#define nima-supported-reflection-boundary-gate
  : NimaSupportedReflectionBoundaryGate
  := nima-define-concrete-rawGroup-physical-defect
```
