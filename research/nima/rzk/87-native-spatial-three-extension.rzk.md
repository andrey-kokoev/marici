# Native spatial three-extension

```rzk
#lang rzk-1
#data NimaNativeSpatialThreeExtensionTerm
  := nima-short-face-ring
  | nima-three-long-facet-link-rings
  | nima-three-mixed-pair-rings
  | nima-conductor-ring
#data NimaNativeSpatialExtensionStatus
  := nima-exact-polynomial-three-extension
  | nima-native-nonsplit-attachment-realized
#define nima-native-spatial-extension-status : NimaNativeSpatialExtensionStatus
  := nima-native-nonsplit-attachment-realized
#data NimaNativeSpatialEndpointRequirement
  := nima-both-endpoint-triangles-essential
#define nima-native-spatial-endpoint-requirement
  : NimaNativeSpatialEndpointRequirement
  := nima-both-endpoint-triangles-essential
#data NimaNativeSpatialEquivariance
  := nima-polynomial-comparison-coherently-equivariant
#define nima-native-spatial-equivariance : NimaNativeSpatialEquivariance
  := nima-polynomial-comparison-coherently-equivariant
#data NimaNativeSpatialPhysicalStatus
  := nima-occurrence-realization-not-normal-Rees-PC-identification
#define nima-native-spatial-physical-status : NimaNativeSpatialPhysicalStatus
  := nima-occurrence-realization-not-normal-Rees-PC-identification
```
