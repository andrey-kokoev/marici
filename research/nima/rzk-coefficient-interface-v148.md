# v148: true L2 integral Bockstein Smith at D20

The structured paired-lattice algorithm completes the true labelled L2
presentation at D20.

The odd target rank is 110, with 1,924 labelled columns. The u0 image has rank
71 and relation-kernel rank 1,853. The integral Bockstein image raises rank to
89, a gain of 18, again exactly matching the modular beta-rank calculation.

Original nonunit Smith factors are `2^26,4,12^6,24,840`. After the full
Bockstein image they are `2^36,6^12,12^2,24^3`; in particular the 5- and
7-primary parts of 840 disappear. Adjoining the distinguished transition
changes only `2^36` to `2^35`, so its index ratio is again two.

The transition therefore has a stable order-two integral effect at D12, D16,
and D20 while being rationally contained in the full Bockstein image. This is
distinct from comparisons against the smaller canonical generator family.

Evidence is `results/L2-bockstein-relation-smith-D20.json`.
`rzk/176-l2-integral-bockstein-smith-d20.rzk.md` passes all eight declarations
without assumptions.
