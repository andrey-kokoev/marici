# Primitive conormal replay and input audit

```rzk
#lang rzk-1
#data NimaPrimitiveConormalColumn
  := nima-target-side-column-zero-one
  | nima-column-primitive
#define nima-primitive-conormal-column : NimaPrimitiveConormalColumn
  := nima-target-side-column-zero-one
#data NimaPrimitiveConormalExtBehavior
  := nima-native-Ext-ranks-1-6-24-92-354-1362-5240
  | nima-beta-zero-doubles-ranks
  | nima-beta-inversion-removes-torsion
#define nima-primitive-conormal-Ext-behavior : NimaPrimitiveConormalExtBehavior
  := nima-beta-inversion-removes-torsion
#data NimaPrimitiveConormalInputStatus
  := nima-complete-framed-physical-source-missing
  | nima-physical-covectors-unset
  | nima-control-cohomology-unset
  | nima-physical-b-map-not-constructed
#define nima-primitive-conormal-input-status : NimaPrimitiveConormalInputStatus
  := nima-physical-b-map-not-constructed
#data NimaPrimitiveConormalReplayStatus
  := nima-recovered-checker-passed-80087
#define nima-primitive-conormal-replay-status : NimaPrimitiveConormalReplayStatus
  := nima-recovered-checker-passed-80087
```
