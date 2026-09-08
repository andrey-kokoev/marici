# Mixed-short-edge generic attachment

```rzk
#lang rzk-1
#data NimaMixedEdgeGenericClass
  := nima-three-degree-one-edge-classes
  | nima-common-native-degree-two-class
  | nima-source-connecting-row-1-1-1
#data NimaIndividualEdgeLiftStatus
  := nima-individual-edge-has-primitive-short-transgression
  | nima-individual-edge-does-not-lift-to-endpoint-quotient
#define nima-individual-edge-lift-status : NimaIndividualEdgeLiftStatus
  := nima-individual-edge-does-not-lift-to-endpoint-quotient
#data NimaCompleteNativeCapStatus
  := nima-complete-native-cap-lifts-with-both-endpoints
  | nima-three-endpoint-preserving-short-presentations
#define nima-complete-native-cap-status : NimaCompleteNativeCapStatus
  := nima-complete-native-cap-lifts-with-both-endpoints
#data NimaMixedEdgePhysicalStatus
  := nima-Rees-Gysin-excess-transport-open
#define nima-mixed-edge-physical-status : NimaMixedEdgePhysicalStatus
  := nima-Rees-Gysin-excess-transport-open
```
