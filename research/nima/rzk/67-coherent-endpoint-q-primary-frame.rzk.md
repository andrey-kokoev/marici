# Coherent endpoint/Q primary frame

```rzk
#lang rzk-1

#data NimaCoherentBoundaryObject
  := nima-coherent-full-Q14
  | nima-coherent-negative-endpoint-top-pair
  | nima-coherent-positive-endpoint-top-pair

#data NimaCoherentFrameModel
  := nima-coherent-448-state-fibre
  | nima-coherent-412-state-kernel
#data NimaCoherentFrameEquivalenceStatus
  := nima-coherent-fibre-contracts-to-kernel
#define nima-coherent-frame-equivalence
  : NimaCoherentFrameModel -> NimaCoherentFrameEquivalenceStatus
  := \ model -> nima-coherent-fibre-contracts-to-kernel

#data NimaCoherentSupportedMapClass12
  := nima-coherent-map-0 | nima-coherent-map-1 | nima-coherent-map-2
  | nima-coherent-map-3 | nima-coherent-map-4 | nima-coherent-map-5
  | nima-coherent-map-6 | nima-coherent-map-7 | nima-coherent-map-8
  | nima-coherent-map-9 | nima-coherent-map-10 | nima-coherent-map-11
#data NimaCoherentMapPrimaryBehavior
  := nima-coherent-map-changes-primary
#define nima-coherent-map-primary-behavior
  : NimaCoherentSupportedMapClass12 -> NimaCoherentMapPrimaryBehavior
  := \ map -> nima-coherent-map-changes-primary

#data NimaSpecifiedPrimary
  := nima-admissible-specified-primary
  | nima-obstructed-minus-beta-chi-primary
#data NimaPrimaryFixedCoherentFibreStatus
  := nima-primary-fixed-coherent-fibre-contractible
  | nima-primary-fixed-coherent-fibre-empty
#define nima-primary-fixed-coherent-fibre-status
  : NimaSpecifiedPrimary -> NimaPrimaryFixedCoherentFibreStatus
  := \ primary -> match primary
       (nima-admissible-specified-primary =>
          nima-primary-fixed-coherent-fibre-contractible
       | nima-obstructed-minus-beta-chi-primary =>
          nima-primary-fixed-coherent-fibre-empty)

#define nima-coherent-chi-framing : NimaEndpointFramingMode
  := nima-endpoint-framing-strict
#define nima-coherent-chi-is-faithful
  : nima-chi-annihilator-status nima-coherent-chi-framing
      = nima-chi-annihilator-faithful
  := refl

#data NimaCoherentFramedChiClass
  := nima-coherent-framed-chi-free-generator
#define nima-coherent-framed-chi-value
  : NimaCoherentFramedChiClass -> MariciInt
  := \ chi -> marici-int-one
#define nima-coherent-framed-chi-is-primitive
  : nima-coherent-framed-chi-value nima-coherent-framed-chi-free-generator
      = marici-int-one
  := refl
```
