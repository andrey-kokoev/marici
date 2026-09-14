# Target detector input gate

```rzk
#lang rzk-1
#data NimaPullbackMatrixExport
  := nima-d3-d2-d1-matrices-exported
  | nima-primitive-z-exported
  | nima-road-augmentation-exported
#define nima-pullback-matrix-export : NimaPullbackMatrixExport
  := nima-d3-d2-d1-matrices-exported

#data NimaMissingPullbackBasisSemantics
  := nima-C1-basis-labels-not-exported
  | nima-s-detector-row-not-exported
  | nima-W-detector-row-not-exported
  | nima-v-detector-row-not-exported
#define nima-missing-pullback-basis-semantics
  : NimaMissingPullbackBasisSemantics
  := nima-C1-basis-labels-not-exported

#data NimaLiteralSignatureControl
  := nima-generic-Q-plus-one-is-print-literal
  | nima-Cartier-residue-plus-one-is-print-literal
  | nima-literals-are-not-row-evaluations-on-z
#define nima-literal-signature-control : NimaLiteralSignatureControl
  := nima-literals-are-not-row-evaluations-on-z

#data NimaFirstUndefinedDetectorGenerator
  := nima-first-undefined-generator-is-C1-basis-labels
  | nima-next-required-data-are-three-target-detector-rows
#define nima-first-undefined-detector-generator
  : NimaFirstUndefinedDetectorGenerator
  := nima-first-undefined-generator-is-C1-basis-labels
```
