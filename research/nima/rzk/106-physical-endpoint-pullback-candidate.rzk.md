# Physical endpoint pullback candidate

```rzk
#lang rzk-1
#data NimaBareQPullbackStatus
  := nima-fixed-generic-class-lift-contractible
  | nima-endpoint-composites-exact
#data NimaEndpointDualityFrame
  := nima-three-normal-frame-endpoint-acyclic
  | nima-conormal-frame-has-primitive-endpoint-class
  | nima-conormal-frame-loses-degree-four-generic-class
#define nima-endpoint-duality-frame : NimaEndpointDualityFrame
  := nima-conormal-frame-has-primitive-endpoint-class
#data NimaEndpointPullbackObstruction
  := nima-Euler-source-comparison-nullhomotopic
  | nima-primitive-endpoint-differences-obstruct-by-pair-one-one
#define nima-endpoint-pullback-obstruction : NimaEndpointPullbackObstruction
  := nima-primitive-endpoint-differences-obstruct-by-pair-one-one
#data NimaEndpointMixedOperationAction
  := nima-nine-independent-nonzero-actions-each-endpoint
  | nima-unit-preserving-exterior-augmentation-source-impossible
  | nima-endpoint-to-scalar-augmentation-compatible
#define nima-endpoint-mixed-operation-action : NimaEndpointMixedOperationAction
  := nima-nine-independent-nonzero-actions-each-endpoint
#data NimaEndpointCandidateStatus
  := nima-typed-candidate-not-physical-identification
#define nima-endpoint-candidate-status : NimaEndpointCandidateStatus
  := nima-typed-candidate-not-physical-identification
```
