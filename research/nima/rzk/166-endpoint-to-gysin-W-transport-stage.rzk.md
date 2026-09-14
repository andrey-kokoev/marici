# Endpoint-to-Gysin W transport stage

```rzk
#lang rzk-1
#data NimaEndpointGysinIntegralComparison
  := nima-sixteen-line-Gysin-cases-checked
  | nima-line-and-Gysin-H0-rank-one
  | nima-comparison-cones-acyclic
  | nima-comparison-fibres-retain-H0-rank-one
#define nima-endpoint-Gysin-integral-comparison : NimaEndpointGysinIntegralComparison
  := nima-comparison-cones-acyclic
#data NimaEndpointGysinCoverage
  := nima-plus-and-minus-endpoints
  | nima-three-pairs-and-one-triple
  | nima-central-and-noncentral-faces
#define nima-endpoint-Gysin-coverage : NimaEndpointGysinCoverage
  := nima-central-and-noncentral-faces
#data NimaWTransportRemainingStage
  := nima-endpoint-to-coefficient-Gysin-stage-complete
  | nima-coefficient-Gysin-to-physical-supported-stage-open
#define nima-W-transport-remaining-stage : NimaWTransportRemainingStage
  := nima-coefficient-Gysin-to-physical-supported-stage-open
```
