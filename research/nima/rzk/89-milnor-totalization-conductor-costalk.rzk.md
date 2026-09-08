# Milnor totalization and conductor costalk

```rzk
#lang rzk-1
#data NimaConductorCostalkClass
  := nima-costalk-class-rank-34
  | nima-counit-image-rank-3
  | nima-counit-kernel-rank-31
#define nima-costalk-kernel-is-obstruction-lattice
  : NimaConductorCostalkClass
  := nima-counit-kernel-rank-31
#data NimaInvariantConductorCostalkClass
  := nima-invariant-costalk-rank-11
  | nima-invariant-primary-rank-1
  | nima-invariant-kernel-rank-10
#data NimaMilnorTotalizationBehavior
  := nima-structure-totalization-equivalent-to-R
  | nima-same-degree-totalization-map-group-zero
#define nima-Milnor-totalization-map-behavior : NimaMilnorTotalizationBehavior
  := nima-same-degree-totalization-map-group-zero
#data NimaConductorCostalkPhysicalStatus
  := nima-costalk-counit-does-not-select-physical-map
#define nima-conductor-costalk-physical-status : NimaConductorCostalkPhysicalStatus
  := nima-costalk-counit-does-not-select-physical-map
```
