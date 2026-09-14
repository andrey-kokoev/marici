# v146: distinguished L2 transition at D12

The true integral L2 Smith checker now separately adjoins the distinguished
transition `3a^3+3a^3b` to the full relation/Bockstein image.

At D12 it adds no rational rank: both matrices have rank 27. Integrally,
however, it divides the saturation index by two. The nonunit Smith factors
change from `2^8,6^8,12` by multiplicity to `2^7,6^8,12`. Thus the labelled
transition kills a specific order-two torsion class at this cutoff.

This is distinct from its rank-completing role observed modularly at D16 and
above. A direct saturated-Hermite D16 calculation exceeded the five-minute
budget, so the next executable task is structured kernel reduction rather than
blindly increasing the timeout.

Evidence is the refreshed `results/L2-bockstein-relation-smith-D12.json`.
`rzk/174-l2-distinguished-transition-integral-effect-d12.rzk.md` passes all
eight declarations without assumptions.
