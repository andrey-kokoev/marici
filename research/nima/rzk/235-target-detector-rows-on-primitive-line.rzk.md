# Target detector rows on the primitive line

```rzk
#lang rzk-1
#data NimaTargetDetectorRows
  := nima-s-row-zero-zero-one-one-one
  | nima-W-row-one-minus-one-zero-zero-zero
  | nima-v-row-zero-zero-one-one-one
#define nima-target-detector-rows : NimaTargetDetectorRows
  := nima-W-row-one-minus-one-zero-zero-zero

#data NimaTargetDetectorRowDerivation
  := nima-s-row-forced-by-C3-invariant-Q-normalization
  | nima-W-row-forced-by-oriented-unimodular-endpoint-swap
  | nima-v-row-forced-by-rho0-D03-and-Cech-extension
#define nima-target-detector-row-derivation
  : NimaTargetDetectorRowDerivation
  := nima-v-row-forced-by-rho0-D03-and-Cech-extension

#data NimaTargetDetectorClosedness
  := nima-s-row-annihilates-all-four-d2-columns
  | nima-W-row-annihilates-all-four-d2-columns
  | nima-v-row-annihilates-all-four-d2-columns
#define nima-target-detector-closedness : NimaTargetDetectorClosedness
  := nima-s-row-annihilates-all-four-d2-columns

#data NimaPrimitiveTargetDetectorValues
  := nima-s-on-z-is-one
  | nima-W-on-z-is-one
  | nima-v-on-z-is-one
  | nima-normalized-supported-image-is-s-plus-W-plus-v
#define nima-primitive-target-detector-values
  : NimaPrimitiveTargetDetectorValues
  := nima-normalized-supported-image-is-s-plus-W-plus-v

#data NimaTargetDetectorScope
  := nima-six-point-positive-sheet-primitive
  | nima-C3-invariant-normalized-frame
  | nima-independent-symbolic-a-b-c-extension-not-asserted
#define nima-target-detector-scope : NimaTargetDetectorScope
  := nima-C3-invariant-normalized-frame
```
