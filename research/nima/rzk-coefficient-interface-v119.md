# v119: soft D1 Smith growth through D24

The exact integer Smith audit now reaches cutoff `D=24`.

Ranks `(target,image,completed)` are `(325,323,324)`. Completed Smith factors
are `1^246, 2^54, 14^16, 42^8`, and the saturation index is
`2^78 3^8 7^24`.

Across D12, D16, D20, and D24 the completed prime support remains exactly
`{2,3,7}`. For `D=4n`, the sampled 2-primary exponent follows
`n(2n+1)` and the 7-primary exponent equals `D`. These are observed finite
patterns, not promoted to all-degree theorems.

The growing indices strengthen the derived-tower diagnosis: localization at 42
uniformly clears every tested truncation, while an integral completion requires
unbounded torsion-aware data unless a later theorem changes the pattern.

`rzk/147-soft-d1-smith-growth-d24.rzk.md` passes all eight declarations without
assumptions.
