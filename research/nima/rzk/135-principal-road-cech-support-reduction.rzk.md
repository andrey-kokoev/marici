# Principal road-Cech support reduction

```rzk
#lang rzk-1
#data NimaPrincipalPhysicalSupportIncidence
  := nima-D2-disjoint-from-physical-closure
  | nima-D3-disjoint-from-physical-closure
  | nima-Z12-Z13-Z23-disjoint-from-physical-closure
#define nima-principal-physical-support-incidence
  : NimaPrincipalPhysicalSupportIncidence
  := nima-Z12-Z13-Z23-disjoint-from-physical-closure
#data NimaPrincipalCechLiteralMaps
  := nima-D2-D3-and-all-incidence-maps-zero-by-support
  | nima-D1-corner-maps-zero
  | nima-D1-requires-soft-nearby-cycle
#define nima-principal-Cech-literal-maps : NimaPrincipalCechLiteralMaps
  := nima-D1-requires-soft-nearby-cycle
#data NimaPrincipalRoadCechRemainingGate
  := nima-only-soft-D1-nearby-cycle-map-remains
  | nima-analytic-continuation-not-supplied
#define nima-principal-road-Cech-remaining-gate
  : NimaPrincipalRoadCechRemainingGate
  := nima-only-soft-D1-nearby-cycle-map-remains
#data NimaPrincipalSupportReplayStatus
  := nima-packet-present
  | nima-Symbolica-replay-blocked-by-stack-overflow
#define nima-principal-support-replay-status : NimaPrincipalSupportReplayStatus
  := nima-Symbolica-replay-blocked-by-stack-overflow
```
