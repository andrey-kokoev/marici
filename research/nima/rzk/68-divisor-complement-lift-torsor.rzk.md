# Divisor-complement local lifts and descent torsor

```rzk
#lang rzk-1

#data NimaDivisorComplementChart7
  := nima-lift-chart-common
  | nima-lift-chart-plus-13 | nima-lift-chart-plus-15
  | nima-lift-chart-plus-35
  | nima-lift-chart-minus-02 | nima-lift-chart-minus-04
  | nima-lift-chart-minus-24

#data NimaLocalGenericLift
  := nima-local-generic-unit-lift
#define nima-chart-local-lift
  : NimaDivisorComplementChart7 -> NimaLocalGenericLift
  := \ chart -> nima-local-generic-unit-lift

#data NimaLiftOverlapResidue12
  := nima-overlap-plus-subset-0 | nima-overlap-plus-subset-1
  | nima-overlap-plus-subset-2 | nima-overlap-plus-subset-01
  | nima-overlap-plus-subset-02 | nima-overlap-plus-subset-12
  | nima-overlap-minus-subset-0 | nima-overlap-minus-subset-1
  | nima-overlap-minus-subset-2 | nima-overlap-minus-subset-01
  | nima-overlap-minus-subset-02 | nima-overlap-minus-subset-12

#define NimaLiftTorsorCechOne : U := NimaZSum NimaLiftOverlapResidue12
#define nima-detected-lift-torsor-residue : NimaLiftTorsorCechOne
  := nima-sum-atom NimaLiftOverlapResidue12 nima-overlap-plus-subset-0
#define nima-lift-torsor-residue-probe : NimaLiftOverlapResidue12 -> MariciInt
  := \ residue -> match residue
       (nima-overlap-plus-subset-0 => marici-int-one
       | nima-overlap-plus-subset-1 => marici-int-zero
       | nima-overlap-plus-subset-2 => marici-int-zero
       | nima-overlap-plus-subset-01 => marici-int-zero
       | nima-overlap-plus-subset-02 => marici-int-zero
       | nima-overlap-plus-subset-12 => marici-int-zero
       | nima-overlap-minus-subset-0 => marici-int-zero
       | nima-overlap-minus-subset-1 => marici-int-zero
       | nima-overlap-minus-subset-2 => marici-int-zero
       | nima-overlap-minus-subset-01 => marici-int-zero
       | nima-overlap-minus-subset-02 => marici-int-zero
       | nima-overlap-minus-subset-12 => marici-int-zero)
#define nima-detected-lift-torsor-residue-is-primitive
  : nima-sum-eval NimaLiftOverlapResidue12 nima-lift-torsor-residue-probe
      nima-detected-lift-torsor-residue = marici-int-one
  := refl

#data NimaDetectedCechZeroCochain := nima-detected-cech-zero-cochain
#define nima-detected-cech-coboundary
  : NimaDetectedCechZeroCochain -> NimaLiftTorsorCechOne
  := \ cochain -> nima-sum-zero NimaLiftOverlapResidue12
#define nima-detected-torsor-is-not-coboundary
  (cochain : NimaDetectedCechZeroCochain)
  (boundary : nima-sum-equal NimaLiftOverlapResidue12
    (nima-detected-cech-coboundary cochain)
    nima-detected-lift-torsor-residue)
  : marici-int-zero = marici-int-one
  := boundary nima-lift-torsor-residue-probe

#data NimaLiftTorsorGlobalStatus
  := nima-local-lifts-exist-on-all-seven-charts
  | nima-global-unit-lift-does-not-exist
#define nima-local-lift-status : NimaLiftTorsorGlobalStatus
  := nima-local-lifts-exist-on-all-seven-charts
#define nima-global-lift-status : NimaLiftTorsorGlobalStatus
  := nima-global-unit-lift-does-not-exist

#define NimaDivisorComplementAnnihilatorGenerator : U
  := NimaNaturalityAnnihilatorGenerator
#define nima-divisor-complement-common-annihilator
  : NimaDivisorComplementAnnihilatorGenerator
  := nima-naturality-annihilator-common-rees

#data NimaOriginalCoefficientLiftIdeal
  := nima-original-affine-primary-ideal
  | nima-divisor-complement-secondary-ideal
#define nima-lift-ideal-after-divisor-complement
  : NimaOriginalCoefficientLiftIdeal
  := nima-divisor-complement-secondary-ideal

#data NimaDivisorComplementEndpointDiscrepancy
  := nima-positive-overlap-retains-negative-endpoint
  | nima-negative-overlap-retains-positive-endpoint

#define nima-divisor-complement-endpoint-discrepancy-value
  : NimaDivisorComplementEndpointDiscrepancy -> MariciInt
  := \ discrepancy -> marici-int-one
#define nima-positive-overlap-endpoint-is-retained
  : nima-divisor-complement-endpoint-discrepancy-value
      nima-positive-overlap-retains-negative-endpoint = marici-int-one
  := refl
#define nima-negative-overlap-endpoint-is-retained
  : nima-divisor-complement-endpoint-discrepancy-value
      nima-negative-overlap-retains-positive-endpoint = marici-int-one
  := refl
```
