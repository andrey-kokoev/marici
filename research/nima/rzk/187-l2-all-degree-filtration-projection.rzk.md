# L2 all-degree filtration projection

```rzk
#lang rzk-1
#data NimaL2AllDegreeSupportShifts
  := nima-every-labelled-column-shifts-degree-by-2-through7
  | nima-no-labelled-column-preserves-or-lowers-degree
#define nima-L2-all-degree-support-shifts : NimaL2AllDegreeSupportShifts
  := nima-every-labelled-column-shifts-degree-by-2-through7
#data NimaL2SupportShiftProof
  := nima-derivatives-lower-source-degree-by-one
  | nima-fixed-L1-L2-k-multipliers-determine-shifts
  | nima-monomial-translation-preserves-shift-list
#define nima-L2-support-shift-proof : NimaL2SupportShiftProof
  := nima-monomial-translation-preserves-shift-list
#data NimaL2GlobalFilteredProjection
  := nima-new-higher-degree-sources-have-no-lower-target-output
  | nima-cutoff-projections-strict-in-all-degrees
#define nima-L2-global-filtered-projection : NimaL2GlobalFilteredProjection
  := nima-cutoff-projections-strict-in-all-degrees
```
