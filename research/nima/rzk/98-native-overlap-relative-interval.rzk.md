# Native overlap and relative interval extension

```rzk
#lang rzk-1
#data NimaBranchConormalModel
  := nima-native-three-occurrence-conormals-per-sheet
  | nima-universal-one-coordinate-conormal-per-sheet
#data NimaUniversalFactorizationStatus
  := nima-equivariant-image-only-cyclic-diagonal
  | nima-native-six-term-symbol-does-not-factor
  | nima-native-top-punctured-residue-not-carried
#define nima-universal-factorization-status : NimaUniversalFactorizationStatus
  := nima-native-six-term-symbol-does-not-factor
#data NimaW03RelativeTraceStatus
  := nima-two-excess-classes-preserved-by-minus-beta-identity
  | nima-scalar-projection-row-1-1
  | nima-relation-only-difference-killed-by-scalar-projection
#define nima-W03-relative-trace-status : NimaW03RelativeTraceStatus
  := nima-two-excess-classes-preserved-by-minus-beta-identity
#data NimaOccurrenceExtensionStatus
  := nima-occurrence-complex-primitive-nonsplit-two-extension
  | nima-occurrence-Postnikov-class-one
#define nima-occurrence-extension-status : NimaOccurrenceExtensionStatus
  := nima-occurrence-complex-primitive-nonsplit-two-extension
#data NimaRelativeIntervalPhysicalStatus
  := nima-relative-projection-not-physical-PC-trace
#define nima-relative-interval-physical-status : NimaRelativeIntervalPhysicalStatus
  := nima-relative-projection-not-physical-PC-trace
```
