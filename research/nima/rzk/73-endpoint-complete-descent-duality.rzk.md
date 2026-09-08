# Endpoint-complete descent and coefficient duality

```rzk
#lang rzk-1

#data NimaEndpointCompleteBoundaryFamily14
  := nima-endpoint-complete-old-residue
       (residue : NimaLiftOverlapResidue12)
  | nima-endpoint-complete-positive-endpoint
  | nima-endpoint-complete-negative-endpoint

#data NimaBaseScalarMixedPole3
  := nima-scalar-pole-02-35-u14
  | nima-scalar-pole-04-13-u25
  | nima-scalar-pole-24-15-u03
#data NimaBaseScalarDetectionStatus
  := nima-base-scalars-have-nonzero-joint-blind-kernel
#define nima-base-scalar-detection-status : NimaBaseScalarDetectionStatus
  := nima-base-scalars-have-nonzero-joint-blind-kernel

#data NimaRelativeDualizingCohomologyDegree
  := nima-dualizing-branch-degree-minus-3
  | nima-dualizing-conductor-degree-minus-1
#data NimaDualizingAttachmentStatus
  := nima-branch-conductor-attachment-nonsplit
#define nima-relative-dualizing-attachment : NimaDualizingAttachmentStatus
  := nima-branch-conductor-attachment-nonsplit

#data NimaConductorOrientationCharacter
  := nima-conductor-orientation-sheet-exchange-odd
#define nima-conductor-orientation : NimaConductorOrientationCharacter
  := nima-conductor-orientation-sheet-exchange-odd

#data NimaSupportedDescentDualStatus
  := nima-complete-cyclic-obstruction-retained-with-T-conormal-shift
#define nima-supported-descent-dual-status : NimaSupportedDescentDualStatus
  := nima-complete-cyclic-obstruction-retained-with-T-conormal-shift

#data NimaDescentDualPhysicalStatus
  := nima-coefficient-dual-not-native-physical-dual
#define nima-descent-dual-physical-status : NimaDescentDualPhysicalStatus
  := nima-coefficient-dual-not-native-physical-dual
```
