# Explicit qg2 relative cut chain

```rzk
#lang rzk-1
#data NimaQG2RelativeCutChainFormula
  := nima-xi-of-t-equals-minus1-plus-t-times1-minus-kappa
  | nima-t0-is-endpoint-minus1
  | nima-t1-is-conductor-minus-kappa
#define nima-qg2-relative-cut-chain-formula : NimaQG2RelativeCutChainFormula
  := nima-xi-of-t-equals-minus1-plus-t-times1-minus-kappa
#data NimaQG2RelativeCutInterior
  := nima-kappa-not1-makes-endpoints-distinct
  | nima-interior-avoids-endpoint-and-conductor-poles
#define nima-qg2-relative-cut-interior : NimaQG2RelativeCutInterior
  := nima-interior-avoids-endpoint-and-conductor-poles
#data NimaQG2RelativeCutBoundary
  := nima-boundary-is-conductor-minus-endpoint
  | nima-reversal-negates-oriented-chain
  | nima-orientation-character-minus1
#define nima-qg2-relative-cut-boundary : NimaQG2RelativeCutBoundary
  := nima-boundary-is-conductor-minus-endpoint
#data NimaQG2RelativeCutTransportGate
  := nima-wall-relative-chain-inhabited
  | nima-ambient-tubular-nearby-cycle-map-required
  | nima-map-boundary-to-selected-log-road-generator
#define nima-qg2-relative-cut-transport-gate : NimaQG2RelativeCutTransportGate
  := nima-ambient-tubular-nearby-cycle-map-required
```
