# Native short-face comparison

```rzk
#lang rzk-1
#data NimaNativeShortFaceComparison
  := nima-canonical-short-face-ring-quotient
  | nima-complete-derived-dual-face-inclusion
  | nima-polynomial-naturality-homotopy
#data NimaMixedShortEdgeAttachment
  := nima-three-mixed-edges-attach-conductor
  | nima-connecting-row-1-1-1
  | nima-bridge-kernel-rank-2
#define nima-mixed-short-edge-attachment : NimaMixedShortEdgeAttachment
  := nima-three-mixed-edges-attach-conductor
#data NimaNativeShortFacePhysicalStatus
  := nima-face-model-not-full-support-PC-Rees-diagram
#define nima-native-short-face-physical-status : NimaNativeShortFacePhysicalStatus
  := nima-face-model-not-full-support-PC-Rees-diagram
```
