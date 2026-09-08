# First-conductor coherent component ranks

```rzk
#lang rzk-1

#data NimaFirstConductorComponentRank
  := nima-first-conductor-rank-7
  | nima-first-conductor-rank-9
  | nima-first-conductor-rank-19
#define nima-first-conductor-component-rank
  : NimaFirstConductorDirection -> NimaFirstConductorComponentRank
  := \ direction -> match direction
       (nima-first-conductor-X02 => nima-first-conductor-rank-9
       | nima-first-conductor-X04 => nima-first-conductor-rank-9
       | nima-first-conductor-X24 => nima-first-conductor-rank-9
       | nima-first-conductor-X13 => nima-first-conductor-rank-7
       | nima-first-conductor-X15 => nima-first-conductor-rank-7
       | nima-first-conductor-X35 => nima-first-conductor-rank-19)

#data NimaCoherentFirstConductorTotalRank
  := nima-primary-fixed-total-rank-60
  | nima-comparison-only-kernel-rank-24
  | nima-forgetful-image-rank-36
  | nima-ordinary-supported-total-rank-72

#data NimaCoherentFirstConductorComponentShape
  := nima-component-contractible
#define nima-first-conductor-component-shape
  (direction : NimaFirstConductorDirection)
  : NimaCoherentFirstConductorComponentShape
  := nima-component-contractible

#data NimaFirstConductorGlobalShape
  := nima-sixty-components-not-contractible-total-space
#define nima-first-conductor-global-shape : NimaFirstConductorGlobalShape
  := nima-sixty-components-not-contractible-total-space

#data NimaPrimaryComparisonRetention
  := nima-primary-comparison-retained
  | nima-primary-comparison-forgotten
#data NimaO02DifferenceStatus
  := nima-O02-difference-nonzero-primary-framed
  | nima-O02-difference-ordinary-nullhomotopic
#define nima-O02-status
  : NimaPrimaryComparisonRetention -> NimaO02DifferenceStatus
  := \ retention -> match retention
       (nima-primary-comparison-retained =>
          nima-O02-difference-nonzero-primary-framed
       | nima-primary-comparison-forgotten =>
          nima-O02-difference-ordinary-nullhomotopic)
```
