# First-conductor framed deformations

```rzk
#lang rzk-1

#data NimaFirstConductorCycle9
  := nima-first-conductor-cycle-0 | nima-first-conductor-cycle-1
  | nima-first-conductor-cycle-2 | nima-first-conductor-cycle-3
  | nima-first-conductor-cycle-4 | nima-first-conductor-cycle-5
  | nima-first-conductor-occurrence-cycle-0
  | nima-first-conductor-occurrence-cycle-1
  | nima-first-conductor-occurrence-cycle-2

#data NimaFixedRegulatorMapClass6
  := nima-fixed-regulator-map-class-0 | nima-fixed-regulator-map-class-1
  | nima-fixed-regulator-map-class-2 | nima-fixed-regulator-map-class-3
  | nima-fixed-regulator-map-class-4 | nima-fixed-regulator-map-class-5

#data NimaFirstConductorProjectionStatus
  := nima-first-conductor-endpoint-zero
  | nima-first-conductor-Q-zero

#define nima-first-conductor-endpoint-status
  : NimaFirstConductorCycle9 -> NimaFirstConductorProjectionStatus
  := \ cycle -> nima-first-conductor-endpoint-zero
#define nima-first-conductor-Q-status
  : NimaFirstConductorCycle9 -> NimaFirstConductorProjectionStatus
  := \ cycle -> nima-first-conductor-Q-zero

#data NimaY02MapAnnihilatorGenerator
  := nima-Y02-annihilator-beta
  | nima-Y02-annihilator-X13
  | nima-Y02-annihilator-X15
  | nima-Y02-annihilator-X35

#data NimaY02Carrier
  := nima-Y02-two-term-first-flip-cycle
#define nima-Y02-carrier-value : NimaY02Carrier -> MariciInt
  := \ y -> marici-int-one
#define nima-Y02-is-primitive
  : nima-Y02-carrier-value nima-Y02-two-term-first-flip-cycle
      = marici-int-one
  := refl

#data NimaFirstConductorFrameLevel
  := nima-frame-occurrence-weight-zero
  | nima-frame-first-negative-conductor-degree
#data NimaPrimaryFixedRigidityStatus
  := nima-primary-fixed-rigid
  | nima-primary-fixed-has-six-map-directions
#define nima-primary-fixed-rigidity-by-degree
  : NimaFirstConductorFrameLevel -> NimaPrimaryFixedRigidityStatus
  := \ level -> match level
       (nima-frame-occurrence-weight-zero => nima-primary-fixed-rigid
       | nima-frame-first-negative-conductor-degree =>
          nima-primary-fixed-has-six-map-directions)
```
