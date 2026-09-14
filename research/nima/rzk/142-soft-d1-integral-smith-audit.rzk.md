# Soft D1 integral Smith audit

```rzk
#lang rzk-1
#data NimaSoftD1IntegralCutoff12
  := nima-target-rank-91
  | nima-image-rank-89
  | nima-completed-rank-90
  | nima-defect-rank-one-integrally
#define nima-soft-D1-integral-cutoff12 : NimaSoftD1IntegralCutoff12
  := nima-defect-rank-one-integrally
#data NimaSoftD1SmithSaturation
  := nima-image-has-20-nonunit-Smith-factors
  | nima-completion-has-21-nonunit-Smith-factors
  | nima-L2-completion-remains-nonsaturated
#define nima-soft-D1-Smith-saturation : NimaSoftD1SmithSaturation
  := nima-L2-completion-remains-nonsaturated
#data NimaSoftD1SmithAuditScope
  := nima-exact-integer-cutoff12-audit
  | nima-not-all-degree-Smith-theorem
  | nima-not-global-chain-map
#define nima-soft-D1-Smith-audit-scope : NimaSoftD1SmithAuditScope
  := nima-exact-integer-cutoff12-audit
```
