# v145: true L2 integral Bockstein Smith presentation at D12

A first exact integral Smith presentation has now been computed for the actual
labelled L2 relation matrix, correcting the Cartier-matrix provenance issue.
The calculation uses the all-degree lattice with u1 generator `u/2` and obtains
a saturated integer relation kernel via a unimodular row-Hermite transform.

At D12 the odd target rank is 42. There are 452 labelled columns; the u0 map has
rank 19 and a saturated relation kernel of rank 433. Applying the u1 map to that
kernel and adjoining its Bockstein image raises rank to 27, an integral rank
gain of 8.

The original u0 image has nonunit Smith factors `2^6,6,12^2` by multiplicity.
The image augmented by the true Bockstein relation image has nonunit factors
`2^8,6^8,12`. Unlike the earlier a2-product tables, these factors genuinely
belong to the labelled L2 presentation.

Evidence is `results/L2-bockstein-relation-smith-D12.json` from
`checkers/check_L2_bockstein_relation_smith.py`.
`rzk/173-l2-integral-bockstein-smith-d12.rzk.md` passes all eight declarations
without assumptions. Higher cutoffs and the distinguished transition quotient
remain to be computed.
