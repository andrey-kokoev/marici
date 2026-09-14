# D35 strict input gate

```rzk
#lang rzk-1
#data NimaD35InputGate
  := nima-18-unconditional-inputs-requested
  | nima-11-inputs-available
  | nima-7-inputs-missing
  | nima-zero-new-spatial-calculations
#define nima-D35-input-gate : NimaD35InputGate
  := nima-7-inputs-missing
#data NimaD35ComparisonStatus
  := nima-spatial-comparison-not-tested
  | nima-input-stop-not-mathematical-no-go
#define nima-D35-comparison-status : NimaD35ComparisonStatus
  := nima-input-stop-not-mathematical-no-go
#data NimaStrictPullbackRequirement
  := nima-component-complex-equations-required
  | nima-q-and-pi-chain-map-equations-required
  | nima-native-actions-and-maps-must-intertwine
#define nima-strict-pullback-requirement : NimaStrictPullbackRequirement
  := nima-q-and-pi-chain-map-equations-required
#data NimaD35MissingBlockPolicy
  := nima-unavailable-matrices-not-replaced-by-zero
#define nima-D35-missing-block-policy : NimaD35MissingBlockPolicy
  := nima-unavailable-matrices-not-replaced-by-zero
```
