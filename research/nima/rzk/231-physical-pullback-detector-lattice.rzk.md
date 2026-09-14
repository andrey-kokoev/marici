# Physical pullback detector lattice

```rzk
#lang rzk-1
#data NimaPhysicalPullbackCocycleLattice
  := nima-cocycles-generated-by-endpoint-and-road-rows
  | nima-coboundary-is-endpoint-minus-road
  | nima-dual-H1-detector-line-is-primitive-rank-one
#define nima-physical-pullback-cocycle-lattice
  : NimaPhysicalPullbackCocycleLattice
  := nima-dual-H1-detector-line-is-primitive-rank-one

#data NimaPrimitivePullbackDetectorValue
  := nima-endpoint-detector-of-z-is-plus-one
  | nima-road-detector-of-z-is-plus-one
  | nima-every-oriented-primitive-H1-detector-of-z-is-plus-one
#define nima-primitive-pullback-detector-value
  : NimaPrimitivePullbackDetectorValue
  := nima-every-oriented-primitive-H1-detector-of-z-is-plus-one

#data NimaTargetDetectorDescentGate
  := nima-primary-s-detector-descends-to-pullback-H1
  | nima-reciprocal-W-detector-descends-to-pullback-H1
  | nima-relation-v-detector-descends-to-pullback-H1
  | nima-three-descended-orientations-match-log-orientation
#define nima-target-detector-descent-gate : NimaTargetDetectorDescentGate
  := nima-primary-s-detector-descends-to-pullback-H1

#data NimaDetectorCoordinateConsequence
  := nima-descended-oriented-detector-coordinate-is-plus-one
  | nima-normalized-primitive-image-has-coordinates-one-one-one
  | nima-arbitrary-coefficient-multiple-scales-all-three-coordinates-together
#define nima-detector-coordinate-consequence : NimaDetectorCoordinateConsequence
  := nima-descended-oriented-detector-coordinate-is-plus-one
```
