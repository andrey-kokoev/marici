# Coherent normalization-sheet extensions

```rzk
#lang rzk-1
#data NimaCoherentSheetExtensionSequence
  := nima-coherent-kernel-rank-9
  | nima-conductor-map-rank-40
  | nima-obstruction-quotient-rank-31
#data NimaCoherentSheetInvariantSequence
  := nima-invariant-kernel-rank-3
  | nima-invariant-map-rank-13
  | nima-invariant-obstruction-rank-10
#data NimaCoherentExtensionStatus
  := nima-strict-extension-only-zero
  | nima-nine-coherent-directions-with-unique-homotopies
  | nima-coherent-components-contractible
#define nima-coherent-extension-status : NimaCoherentExtensionStatus
  := nima-nine-coherent-directions-with-unique-homotopies
#data NimaRelationOnlyExtensionStatus
  := nima-all-six-relation-only-maps-obstructed
#define nima-relation-only-extension-status : NimaRelationOnlyExtensionStatus
  := nima-all-six-relation-only-maps-obstructed
```
