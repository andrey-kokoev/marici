# Soft D1 Smith growth through D16

```rzk
#lang rzk-1
#data NimaSoftD1IntegralCutoff16
  := nima-D16-target153-image151-completed152
  | nima-D16-integral-defect-rank-one
#define nima-soft-D1-integral-cutoff16 : NimaSoftD1IntegralCutoff16
  := nima-D16-integral-defect-rank-one
#data NimaSoftD1CompletedSmithD16
  := nima-D16-completed-ones116-twos20-fourteens11-fortytwos5
#define nima-soft-D1-completed-Smith-D16 : NimaSoftD1CompletedSmithD16
  := nima-D16-completed-ones116-twos20-fourteens11-fortytwos5
#data NimaSoftD1SaturationGrowth
  := nima-D12-index-2pow21-3pow4-7pow12
  | nima-D16-index-2pow36-3pow5-7pow16
  | nima-torsion-exponents-grow-with-cutoff
  | nima-prime-support-stable-2-3-7
#define nima-soft-D1-saturation-growth : NimaSoftD1SaturationGrowth
  := nima-torsion-exponents-grow-with-cutoff
#data NimaSoftD1LocalizationQualification
  := nima-invert42-clears-both-tested-cutoffs
  | nima-no-fixed-integral-finite-correction-established
#define nima-soft-D1-localization-qualification : NimaSoftD1LocalizationQualification
  := nima-no-fixed-integral-finite-correction-established
```
