# Raw physical Cech definition gate

```rzk
#lang rzk-1
#data NimaRawPhysicalCechAudit
  := nima-rawCech-occurs-only-as-polymorphic-interface-parameter
  | nima-no-concrete-physical-chart-definition-found
#define nima-raw-physical-Cech-audit : NimaRawPhysicalCechAudit
  := nima-no-concrete-physical-chart-definition-found
#data NimaRawPhysicalCechCountermodel
  := nima-interface-allows-rawCech-equal-selected-target
  | nima-interface-also-allows-rawCech-equal-zero
  | nima-road-data-do-not-distinguish-these-models
#define nima-raw-physical-Cech-countermodel : NimaRawPhysicalCechCountermodel
  := nima-road-data-do-not-distinguish-these-models
#data NimaRawPhysicalCechEqualityStatus
  := nima-road-boundary-selected-class-comparison-constructed
  | nima-raw-physical-equality-not-derivable-from-current-interface
#define nima-raw-physical-Cech-equality-status : NimaRawPhysicalCechEqualityStatus
  := nima-raw-physical-equality-not-derivable-from-current-interface
#data NimaRawPhysicalCechRequiredInput
  := nima-define-occurrence-labelled-local-qG12-raw-defect-formula
  | nima-value-formula-in-ramified-filtered-Q-target
  | nima-then-compare-formula-with-branch-difference
#define nima-raw-physical-Cech-required-input : NimaRawPhysicalCechRequiredInput
  := nima-define-occurrence-labelled-local-qG12-raw-defect-formula
```
