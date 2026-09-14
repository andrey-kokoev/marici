# v118: soft D1 Smith growth through D20

The exact integral Smith audit now includes cutoff `D=20`.

The target, original-image, and L2-completed ranks are `(231,229,230)`, again
leaving exactly one rational/integral rank direction. Completed Smith factors
are `1^175, 2^35, 14^13, 42^7`, with saturation index
`2^55 3^7 7^20`.

Before completion, the D20 index also contains 5- and 11-primary factors. L2
removes both, leaving the same completed prime support `{2,3,7}` observed at
D12 and D16. Thus localization at 42 clears all three tested cutoffs, while the
growing exponents reinforce that no bounded integral correction has yet been
shown.

`rzk/146-soft-d1-smith-growth-d20.rzk.md` passes all eight declarations without
assumptions.
