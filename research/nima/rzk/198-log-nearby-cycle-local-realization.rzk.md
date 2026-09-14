# Log nearby-cycle local realization

```rzk
#lang rzk-1
#data NimaLogNormalLinkCell
  := nima-relative-log-generator-minus-rD-plus-r1-primitive
  | nima-normal-Tor-maps-to-log-link-integrally
  | nima-log-reflection-odd
#define nima-log-normal-link-cell : NimaLogNormalLinkCell
  := nima-normal-Tor-maps-to-log-link-integrally
#data NimaLogEndpointRoadComparison
  := nima-full-endpoint-pairing-chain-map
  | nima-generic-trace-times-road-chain-map
  | nima-explicit-endpoint-comparison-homotopy
  | nima-all-coefficient-cycle-pairings-equal-road-readout
#define nima-log-endpoint-road-comparison : NimaLogEndpointRoadComparison
  := nima-explicit-endpoint-comparison-homotopy
#data NimaLogPacketIntegralStatus
  := nima-full-log-packet-integrally-contractible-off-primitive
  | nima-both-normal-grades-preserved
#define nima-log-packet-integral-status : NimaLogPacketIntegralStatus
  := nima-both-normal-grades-preserved
#data NimaLogPhysicalComparisonGate
  := nima-map-L2-relations-into-log-normal-link-packet
  | nima-single-ringed-filtered-correspondence-to-literal-Q-target
  | nima-nonzero-derived-Q-morphism-still-unproved
#define nima-log-physical-comparison-gate : NimaLogPhysicalComparisonGate
  := nima-map-L2-relations-into-log-normal-link-packet
```
