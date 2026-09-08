# W03 Cech support and trace descent

```rzk
#lang rzk-1
#data NimaW03SupportedHomStatistic
  := nima-supported-Hom-degree-minus-1-rank-9
  | nima-supported-Hom-degree-0-rank-66
  | nima-supported-Hom-degree-1-rank-151
  | nima-supported-first-differential-rank-9
  | nima-supported-second-differential-rank-55
  | nima-supported-cohomology-rank-2
#data NimaW03SupportedTraceClass
  := nima-supported-reciprocal-trace-E
  | nima-supported-reciprocal-trace-R
#data NimaW03SupportLiftStatus
  := nima-two-independent-local-cohomology-counit-lifts
#define nima-W03-support-lift-status : NimaW03SupportLiftStatus
  := nima-two-independent-local-cohomology-counit-lifts
#data NimaMixedOccurrenceLocalizationStatus
  := nima-simultaneous-opposite-sheet-localization-zero-ring
  | nima-separate-localizations-and-fibre-nonzero
#define nima-mixed-occurrence-localization-status
  : NimaMixedOccurrenceLocalizationStatus
  := nima-simultaneous-opposite-sheet-localization-zero-ring
#data NimaW03TracePhysicalStatus
  := nima-supported-traces-not-physical-scalar-trace
#define nima-W03-trace-physical-status : NimaW03TracePhysicalStatus
  := nima-supported-traces-not-physical-scalar-trace
```
