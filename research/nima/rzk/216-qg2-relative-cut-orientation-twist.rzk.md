# qg2 relative-cut orientation twist

```rzk
#lang rzk-1
#data NimaRelativeCutOrientationLine
  := nima-oriented-interval-from-endpoint-to-conductor
  | nima-reversal-swaps-boundaries-and-negates-generator
  | nima-relative-cut-character-minus1
#define nima-relative-cut-orientation-line : NimaRelativeCutOrientationLine
  := nima-relative-cut-character-minus1
#data NimaTwistedConductorCharacter
  := nima-conductor-plus1-times-cut-minus1-equals-minus1
  | nima-twisted-conductor-line-is-reflection-odd
  | nima-character-now-matches-log-primitive
#define nima-twisted-conductor-character : NimaTwistedConductorCharacter
  := nima-character-now-matches-log-primitive
#data NimaTwistedConductorPrimitive
  := nima-strip-inverse-Euler-unit
  | nima-tensor-with-relative-cut-orientation
  | nima-result-has-detector-one-and-odd-character
#define nima-twisted-conductor-primitive : NimaTwistedConductorPrimitive
  := nima-result-has-detector-one-and-odd-character
#data NimaRelativeCutOrientationGate
  := nima-formal-character-repair-constructed
  | nima-physical-relative-cut-chain-inhabitant-required
  | nima-ambient-nearby-cycle-transport-required
#define nima-relative-cut-orientation-gate : NimaRelativeCutOrientationGate
  := nima-physical-relative-cut-chain-inhabitant-required
```
