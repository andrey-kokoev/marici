# v128: road/group independence countermodel

A finite countermodel now proves that oriented road correction cannot
parametrically supply physical group/reflection coherence.

Use a singleton road cell with additive integer Cech target: residual `1`,
boundary `-1`, and identity detector. Every oriented correction field holds.
Independently choose a two-point group target with zero `0` and candidate
difference `1`; the group-zero equality fails.

Therefore the bridge of module 155 necessarily needs independent group
geometry. The work split is strict: construct the unit-oriented nearby-cycle
cell, compute reflection/group coherence separately at the same physical point,
and only then assemble module 132.

Evidence is `results/road-correction-group-independence.json` from
`checkers/check_road_correction_group_independence.py`.
`rzk/156-road-correction-group-independence.rzk.md` passes all six declarations
without assumptions.
