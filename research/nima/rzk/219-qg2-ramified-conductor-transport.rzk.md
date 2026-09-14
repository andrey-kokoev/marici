# qg2 ramified conductor transport

```rzk
#lang rzk-1
#data NimaQG2AmbientConductorDiscriminant
  := nima-discriminant-has-generic-simple-x-factor
  | nima-conductor-root-has-square-root-x-Puiseux-order
#define nima-qg2-ambient-conductor-discriminant
  : NimaQG2AmbientConductorDiscriminant
  := nima-conductor-root-has-square-root-x-Puiseux-order
#data NimaQG2RamifiedBaseChange
  := nima-set-x-equal-h-squared
  | nima-conductor-branch-xi-minus-kappa-plus-c-h
  | nima-c-squared-equals-kappa-minus2-times-kappa-minus1-times-kappa-plus1-over2p
#define nima-qg2-ramified-base-change : NimaQG2RamifiedBaseChange
  := nima-set-x-equal-h-squared
#data NimaQG2AmbientConductorMonodromy
  := nima-h-to-minus-h-exchanges-two-conductor-branches
  | nima-ambient-conductor-orientation-character-minus1
  | nima-character-matches-log-primitive
#define nima-qg2-ambient-conductor-monodromy : NimaQG2AmbientConductorMonodromy
  := nima-character-matches-log-primitive
#data NimaQG2RamifiedTransportGate
  := nima-unramified-tubular-prism-insufficient-at-conductor-face
  | nima-ramified-nearby-cycle-cover-required
  | nima-construct-ringed-filtered-Q-map-on-double-cover
#define nima-qg2-ramified-transport-gate : NimaQG2RamifiedTransportGate
  := nima-construct-ringed-filtered-Q-map-on-double-cover
```
