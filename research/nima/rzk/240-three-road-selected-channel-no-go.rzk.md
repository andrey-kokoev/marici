# Three roads do not split the selected channel packet

```rzk
#lang rzk-1
#data NimaThreeRoadSelectedReadoutMatrix
  := nima-s-values-one-one-one
  | nima-W-values-one-one-one
  | nima-v-values-one-one-one
#define nima-three-road-selected-readout-matrix
  : NimaThreeRoadSelectedReadoutMatrix
  := nima-W-values-one-one-one

#data NimaThreeRoadSelectedReadoutRank
  := nima-selected-readout-rank-one
  | nima-no-road-to-s-W-v-permutation
  | nima-road-augmentation-ideal-killed-by-all-selected-rows
#define nima-three-road-selected-readout-rank
  : NimaThreeRoadSelectedReadoutRank
  := nima-road-augmentation-ideal-killed-by-all-selected-rows

#data NimaSymbolicSelectedPacketInput
  := nima-three-independent-target-typed-boundary-maps
  | nima-character-enriched-readout-retaining-augmentation-ideal
  | nima-source-derived-nonlinear-selected-channel-family
#define nima-symbolic-selected-packet-input : NimaSymbolicSelectedPacketInput
  := nima-three-independent-target-typed-boundary-maps
```
