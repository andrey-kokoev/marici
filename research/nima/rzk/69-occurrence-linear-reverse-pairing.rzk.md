# Occurrence-linear reverse pairing obstruction

```rzk
#lang rzk-1

#data NimaResidualOccurrencePairIdeal6
  := nima-residual-pair-X2-X4 | nima-residual-pair-X3-X5
  | nima-residual-pair-X0-X4 | nima-residual-pair-X1-X5
  | nima-residual-pair-X0-X2 | nima-residual-pair-X1-X3

#data NimaOccurrenceReverseCovector2
  := nima-occurrence-reverse-X2-covector
  | nima-occurrence-reverse-X4-covector

#data NimaOccurrenceReverseImageStatus
  := nima-occurrence-reverse-image-proper-pair-ideal
  | nima-occurrence-reverse-image-unit-ideal
#define nima-occurrence-linear-reverse-image-status
  : NimaOccurrenceReverseImageStatus
  := nima-occurrence-reverse-image-proper-pair-ideal

#data NimaOccurrenceSupportedCokernel
  := nima-occurrence-supported-class-mod-X2-X4
#define nima-occurrence-supported-class-value
  : NimaOccurrenceSupportedCokernel -> MariciInt
  := \ residue -> marici-int-one
#define nima-occurrence-supported-class-is-primitive
  : nima-occurrence-supported-class-value
      nima-occurrence-supported-class-mod-X2-X4 = marici-int-one
  := refl

#data NimaOccurrenceTraceLinearity
  := nima-integer-homogeneous-slice-trace
  | nima-polynomial-occurrence-linear-trace
#data NimaOccurrenceUnitTraceStatus
  := nima-unit-trace-exists
  | nima-unit-trace-obstructed
#define nima-occurrence-unit-trace-status
  : NimaOccurrenceTraceLinearity -> NimaOccurrenceUnitTraceStatus
  := \ linearity -> match linearity
       (nima-integer-homogeneous-slice-trace => nima-unit-trace-exists
       | nima-polynomial-occurrence-linear-trace => nima-unit-trace-obstructed)

#data NimaOccurrencePrincipalOpenTrace
  := nima-X2-inverted-local-trace | nima-X4-inverted-local-trace
#data NimaOccurrenceOverlapHomotopyStatus
  := nima-local-traces-agree-up-to-koszul-homotopy
#define nima-occurrence-overlap-homotopy
  : NimaOccurrencePrincipalOpenTrace -> NimaOccurrenceOverlapHomotopyStatus
  := \ trace -> nima-local-traces-agree-up-to-koszul-homotopy

#data NimaOccurrencePhysicalPromotionStatus
  := nima-occurrence-polynomial-promotion-not-physical-comparison
#define nima-occurrence-physical-promotion-status
  : NimaOccurrencePhysicalPromotionStatus
  := nima-occurrence-polynomial-promotion-not-physical-comparison
```
