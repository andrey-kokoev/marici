# qG12 raw physical Cech road equality

```rzk
#lang rzk-1
#data NimaQG12RawPhysicalCechDefinition
  := nima-raw-defect-is-dlog-n12-over-n31
  | nima-labelled-transition-is-G31-to-G12-X3-over-X2
  | nima-definition-comes-from-source-Leray-frames
#define nima-qG12-raw-physical-Cech-definition
  : NimaQG12RawPhysicalCechDefinition
  := nima-raw-defect-is-dlog-n12-over-n31
#data NimaQG12RawPhysicalCechFormula
  := nima-qG12-chart-transition-minus-v-over-v-minus2
  | nima-qg2-pullback-dlog-xi-plus1-over-xi-plus-kappa
#define nima-qG12-raw-physical-Cech-formula : NimaQG12RawPhysicalCechFormula
  := nima-qg2-pullback-dlog-xi-plus1-over-xi-plus-kappa
#data NimaQG12RoadBoundaryFormula
  := nima-ramified-relative-road-boundary-dlog-xi-plus1-over-xi-plus-kappa
  | nima-selected-road-boundary-is-Cech-v
#define nima-qG12-road-boundary-formula : NimaQG12RoadBoundaryFormula
  := nima-ramified-relative-road-boundary-dlog-xi-plus1-over-xi-plus-kappa
#data NimaQG12RawRoadEquality
  := nima-raw-physical-Cech-equals-road-boundary
  | nima-local-Cech-direction-killed-by-road-correction
  | nima-equality-local-to-one-labelled-wall-sector
#define nima-qG12-raw-road-equality : NimaQG12RawRoadEquality
  := nima-raw-physical-Cech-equals-road-boundary
```
