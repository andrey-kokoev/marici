# qg2 occurrence-labelled Leray descent

```rzk
#lang rzk-1
#data NimaQG2ToLerayCoordinate
  := nima-v-equals2-times-xi-plus1-over1-minus-kappa
  | nima-endpoint-xi-minus1-maps-to-v0
  | nima-conductor-xi-minus-kappa-maps-to-v2
#define nima-qg2-to-Leray-coordinate : NimaQG2ToLerayCoordinate
  := nima-v-equals2-times-xi-plus1-over1-minus-kappa
#data NimaQG2PulledLerayLogEdge
  := nima-pullback-is-dlog-xi-plus1-over-xi-plus-kappa
  | nima-endpoint-residue-plus1
  | nima-conductor-residue-minus1
#define nima-qg2-pulled-Leray-log-edge : NimaQG2PulledLerayLogEdge
  := nima-pullback-is-dlog-xi-plus1-over-xi-plus-kappa
#data NimaQG2CyclicOccurrenceLabel
  := nima-edge-is-G31-to-G12
  | nima-three-Leray-frame-transitions-have-cocycle-product-one
  | nima-road-class-has-source-occurrence-descent
#define nima-qg2-cyclic-occurrence-label : NimaQG2CyclicOccurrenceLabel
  := nima-road-class-has-source-occurrence-descent
#data NimaQG2OccurrenceRoadGate
  := nima-occurrence-labelled-log-road-class-constructed
  | nima-compare-with-independent-raw-physical-Cech-defect
#define nima-qg2-occurrence-road-gate : NimaQG2OccurrenceRoadGate
  := nima-compare-with-independent-raw-physical-Cech-defect
```
