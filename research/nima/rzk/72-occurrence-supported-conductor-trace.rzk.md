# Occurrence-supported trace and conductor specialization

```rzk
#lang rzk-1

#data NimaOccurrenceTraceOutput
  := nima-polynomial-ring-output
  | nima-local-cohomology-H2-X2-X4-output
#data NimaOccurrenceReverseMapBehavior
  := nima-proper-ideal-image
  | nima-supported-isomorphism
#define nima-occurrence-reverse-behavior
  : NimaOccurrenceTraceOutput -> NimaOccurrenceReverseMapBehavior
  := \ output -> match output
       (nima-polynomial-ring-output => nima-proper-ideal-image
       | nima-local-cohomology-H2-X2-X4-output => nima-supported-isomorphism)

#data NimaPrimitiveOccurrenceResidue
  := nima-ordered-double-pole-X2-X4
#data NimaSupportedTraceFibreShape
  := nima-fixed-homogeneous-trace-fibre-contractible
  | nima-ungraded-trace-fibre-K-A-mod-I-1
#define nima-supported-trace-fibre-by-frame
  : NimaPrimaryComparisonRetention -> NimaSupportedTraceFibreShape
  := \ framing -> match framing
       (nima-primary-comparison-retained =>
          nima-fixed-homogeneous-trace-fibre-contractible
       | nima-primary-comparison-forgotten =>
          nima-ungraded-trace-fibre-K-A-mod-I-1)

#data NimaConductorSpecializingOccurrenceMap
  := nima-free-generic-residue-map
  | nima-whole-occurrence-koszul-gysin-map
#data NimaConductorSpecializationStatus
  := nima-specializes-to-zero
  | nima-primitive-bottom-component-survives
#define nima-occurrence-conductor-specialization
  : NimaConductorSpecializingOccurrenceMap -> NimaConductorSpecializationStatus
  := \ map -> match map
       (nima-free-generic-residue-map => nima-specializes-to-zero
       | nima-whole-occurrence-koszul-gysin-map =>
          nima-primitive-bottom-component-survives)

#data NimaOccurrenceGysinFrame
  := nima-codimension-two-ordered-conormal-determinant
#define nima-occurrence-gysin-frame : NimaOccurrenceGysinFrame
  := nima-codimension-two-ordered-conormal-determinant
```
