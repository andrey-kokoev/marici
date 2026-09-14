# v117: soft D1 Smith growth through D16

The independent integral Smith checker was extended to cutoff `D=16`.

The target, image, and L2-completed ranks are `(153,151,152)`, confirming the
rank-one defect integrally at a second cutoff. The completed Smith factors are
`1^116, 2^20, 14^11, 42^5`, with saturation index
`2^36 3^5 7^16`.

Compared with D12's `2^21 3^4 7^12`, the prime support remains exactly
`{2,3,7}` but torsion exponents grow. Thus localization at 42 clears both tested
cutoffs, while no fixed finite integral correction has been established. This
makes a torsion-aware derived tower more plausible than a single saturated
integral column.

`rzk/145-soft-d1-smith-growth-d16.rzk.md` passes all eight declarations without
assumptions.
