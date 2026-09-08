# Native conductor dual endpoint attachment

```rzk
#lang rzk-1

#data NimaNativeConductorDualGrade
  := nima-native-branch-cohomology-degree-3
  | nima-native-conductor-cohomology-degree-5
#data NimaNativeDualAttachmentStatus
  := nima-native-branch-conductor-attachment-nonsplit
#define nima-native-dual-attachment-status : NimaNativeDualAttachmentStatus
  := nima-native-branch-conductor-attachment-nonsplit

#data NimaNativeEndpointGysinAttachment
  := nima-minus-Gysin-X0-X2-X4
  | nima-plus-Gysin-X1-X3-X5
#data NimaResidualPairFactorization
  := nima-minus-attachment-is-X0-times-old-X2-X4-factor
#define nima-residual-pair-factorization : NimaResidualPairFactorization
  := nima-minus-attachment-is-X0-times-old-X2-X4-factor

#data NimaNativePrimitiveComparisonTest
  := nima-five-variable-packet-hom-differential-injective-28
  | nima-conductor-line-section-hom-differential-injective-49
#data NimaNativePrimitiveComparisonResult
  := nima-no-five-variable-primitive-map
  | nima-no-primitive-conductor-section
#define nima-native-primitive-comparison-result
  : NimaNativePrimitiveComparisonTest -> NimaNativePrimitiveComparisonResult
  := \ test -> match test
       (nima-five-variable-packet-hom-differential-injective-28 =>
          nima-no-five-variable-primitive-map
       | nima-conductor-line-section-hom-differential-injective-49 =>
          nima-no-primitive-conductor-section)

#data NimaNativeCollarStatus
  := nima-collar-weights-match-labelled-threefold-occurrences
  | nima-raw-collar-conductor-specializations-zero
  | nima-spatial-connector-identification-absent
#define nima-native-collar-physical-status : NimaNativeCollarStatus
  := nima-spatial-connector-identification-absent
```
