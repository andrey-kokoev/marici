# qg2-to-log orientation character gate

```rzk
#lang rzk-1
#data NimaQG2ConductorCharacter
  := nima-normalized-wall-Kummer-character-plus1
  | nima-conductor-line-locally-even
#define nima-qg2-conductor-character : NimaQG2ConductorCharacter
  := nima-normalized-wall-Kummer-character-plus1
#data NimaLogPrimitiveCharacter
  := nima-log-normal-link-reflection-character-minus1
  | nima-log-primitive-line-odd
#define nima-log-primitive-character : NimaLogPrimitiveCharacter
  := nima-log-normal-link-reflection-character-minus1
#data NimaQG2LogEquivariantComparison
  := nima-intertwiner-equation-t-equals-minus-t
  | nima-characteristic-zero-forces-t-zero
  | nima-no-nonzero-equivariant-line-identification
#define nima-qg2-log-equivariant-comparison : NimaQG2LogEquivariantComparison
  := nima-no-nonzero-equivariant-line-identification
#data NimaQG2LogOrientationRepair
  := nima-relative-cut-chain-must-carry-sign-local-system
  | nima-tensoring-conductor-line-by-sign-makes-character-odd
  | nima-scalar-unit-normalization-alone-insufficient
#define nima-qg2-log-orientation-repair : NimaQG2LogOrientationRepair
  := nima-relative-cut-chain-must-carry-sign-local-system
```
