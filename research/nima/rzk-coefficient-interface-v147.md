# v147: true L2 integral Bockstein Smith at D16

The relation-kernel algorithm was restructured as a row-Hermite intersection of
the paired lattice `(A x, B x)`. Rows with zero A-block directly generate
`B(ker_Z A)`, avoiding the prohibitively large unimodular transformation. It
reproduces D12 exactly and completes D16 within budget.

At D16 the odd target rank is 72, with 1,060 labelled columns. The u0 image has
rank 41 and integral relation-kernel rank 1,019. The full relation Bockstein
image raises rank to 55, giving rank gain 14, exactly matching the modular
beta-rank result.

The u0 image has nonunit factors `2^15,12^5`. After adjoining the full integral
Bockstein image they are `2^21,6^9,12^4`. The distinguished transition remains
rationally dependent in the full Bockstein image but removes one order-two
factor, yielding `2^20,6^9,12^4`.

Evidence is `results/L2-bockstein-relation-smith-D16.json`.
`rzk/175-l2-integral-bockstein-smith-d16.rzk.md` passes all eight declarations
without assumptions.
