# Rank-one to three-packet obstruction

```rzk
#lang rzk-1
#data NimaPhysicalToPacketRanks
  := nima-current-physical-H1-rank-one
  | nima-selected-s-W-v-packet-rank-three
  | nima-linear-image-rank-at-most-one
#define nima-physical-to-packet-ranks : NimaPhysicalToPacketRanks
  := nima-linear-image-rank-at-most-one

#data NimaIndependentCoordinateNoGo
  := nima-no-linear-surjection-from-Z-to-Z-cubed
  | nima-one-generator-determines-only-one-image-column
  | nima-independent-a-b-c-cannot-come-from-current-line
#define nima-independent-coordinate-no-go : NimaIndependentCoordinateNoGo
  := nima-independent-a-b-c-cannot-come-from-current-line

#data NimaNormalizedColumnSurvival
  := nima-current-image-column-one-one-one
  | nima-integer-multiples-scale-all-three-coordinates-together
  | nima-normalized-five-direction-witness-remains-valid
#define nima-normalized-column-survival : NimaNormalizedColumnSurvival
  := nima-normalized-five-direction-witness-remains-valid

#data NimaSymbolicAmplitudeReopeningInput
  := nima-rank-three-coefficient-enriched-physical-source
  | nima-source-derived-nonlinear-three-parameter-family
  | nima-three-independent-physical-Gysin-channels
#define nima-symbolic-amplitude-reopening-input
  : NimaSymbolicAmplitudeReopeningInput
  := nima-rank-three-coefficient-enriched-physical-source
```
