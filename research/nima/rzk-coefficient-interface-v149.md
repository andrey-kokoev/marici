# v149: true L2 integral Bockstein Smith at D24

The structured integral relation calculation now reaches D24.

The odd target rank is 156, with 3,044 labelled columns and relation-kernel rank
2,935. The u0 image rank is 109; adjoining the full integral Bockstein image
raises it to 131, a gain of 22 matching the modular beta rank exactly.

Original nonunit factors are `2^39,6,12^11,60,120,27720`. The full Bockstein
image reduces these to `2^51,6^19,12^6`, removing all 5-, 7-, and 11-primary
parts. The distinguished transition again removes exactly one order-two factor,
leaving `2^50,6^19,12^6`.

Across the true labelled presentations D12, D16, D20, and D24, the full
Bockstein cokernel has only 2- and 3-primary torsion. The distinguished
transition has saturation-index ratio two at every cutoff. This replaces the
incorrect Cartier-derived `{2,3,7}` attribution with actual L2 evidence.

Evidence is `results/L2-bockstein-relation-smith-D24.json`.
`rzk/177-l2-integral-bockstein-smith-d24.rzk.md` passes all eight declarations
without assumptions.
