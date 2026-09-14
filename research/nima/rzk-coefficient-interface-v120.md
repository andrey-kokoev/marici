# v120: soft D1 Smith growth through D28

The exact integer Smith audit now reaches the largest cutoff used by the
original modular scout, `D=28`.

Ranks `(target,image,completed)` are `(435,433,434)`. Completed Smith factors
are `1^329, 2^77, 14^19, 42^9`, with saturation index
`2^105 3^9 7^28`.

Across all five exact cutoffs D12--D28, every completed invariant factor is one
of `1,2,14,42`. The number of nonunit factors equals the 2-primary exponent,
and the 7-primary exponent equals D. This is strong finite evidence that 42 is
the uniform localization denominator for the completed tower, but it remains a
pattern rather than an all-degree proof.

`rzk/148-soft-d1-smith-growth-d28.rzk.md` passes all eight declarations without
assumptions.
