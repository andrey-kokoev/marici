# v113: soft D1 L2 defect completion

The orbit-completed rank calculation was freshly replayed through cutoffs
`D=12,16,20,24,28`.

`rzk/141-soft-d1-l2-defect-completion.rzk.md` records the stable one-generator
defect. At cutoffs 16,20,24,28 the odd Bockstein ranks are `(14,18,22,26)`,
while the canonical generator ranks are `(13,17,21,25)`. Adding the single L2
transition raises each canonical rank by one and reaches the full Bockstein
rank.

The residual is traced to the labelled minus-q source `s11`, with target
combination `3 a^3 + 3 a^3 b`. This identifies a concrete candidate for the
rank-one plus-side extension rather than merely its dimension.

The calculation is modular/truncated and the total cokernel is not flat.
Integral Smith data and a global chain-map realization of the L2 transition are
still required before road-Cech closure.

The Rzk module passes all eight declarations with no assumptions.
