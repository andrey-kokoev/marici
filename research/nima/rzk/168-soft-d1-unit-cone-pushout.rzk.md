# Soft D1 unit-cone pushout

```rzk
#lang rzk-1
#data NimaSoftD1UnitConeAttachment
  := nima-map-cone-unit-to-closed-residual-r
  | nima-new-road-cell-has-boundary-minus-r
#define nima-soft-D1-unit-cone-attachment : NimaSoftD1UnitConeAttachment
  := nima-new-road-cell-has-boundary-minus-r
#data NimaSoftD1UnitConeChainCondition
  := nima-r-closed-implies-new-boundary-squares-zero
  | nima-detector-r-one-implies-new-boundary-detector-minus-one
#define nima-soft-D1-unit-cone-chain-condition : NimaSoftD1UnitConeChainCondition
  := nima-r-closed-implies-new-boundary-squares-zero
#data NimaSoftD1UnitConePushoutEffect
  := nima-new-column-independent-modulo-old-image
  | nima-free-detector-class-killed
  | nima-integral-torsion-remains
#define nima-soft-D1-unit-cone-pushout-effect : NimaSoftD1UnitConePushoutEffect
  := nima-free-detector-class-killed
#data NimaSoftD1UnitConeQualification
  := nima-standalone-cone-contractible
  | nima-pushout-kills-r-and-need-not-be-contractible
  | nima-geometric-map-from-cone-unit-to-r-required
#define nima-soft-D1-unit-cone-qualification : NimaSoftD1UnitConeQualification
  := nima-geometric-map-from-cone-unit-to-r-required
```
