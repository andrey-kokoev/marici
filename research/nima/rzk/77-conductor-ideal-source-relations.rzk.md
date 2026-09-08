# Conductor-ideal source relations

```rzk
#lang rzk-1

#data NimaConductorIdealMapClass
  := nima-strict-conductor-ideal-map-rank-16
  | nima-resolved-conductor-ideal-map-rank-40
  | nima-generator-value-image-rank-34
  | nima-higher-relation-only-map-rank-6
#data NimaConductorIdealEquivariantClass
  := nima-strict-equivariant-rank-5
  | nima-resolved-equivariant-rank-13
  | nima-higher-only-equivariant-rank-2
#data NimaInvariantGeneratorLiftStatus
  := nima-invariant-generator-lift-saturated
#define nima-invariant-generator-lift-status : NimaInvariantGeneratorLiftStatus
  := nima-invariant-generator-lift-saturated
#data NimaConductorIdealPhysicalSelection
  := nima-thirteen-equivariant-candidates-not-physically-selected
#define nima-conductor-ideal-physical-selection : NimaConductorIdealPhysicalSelection
  := nima-thirteen-equivariant-candidates-not-physically-selected
```
