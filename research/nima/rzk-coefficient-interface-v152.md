# v152: canonical-L2/relation lattice incomparability at D16

The integral checker now computes the sum of the canonical-plus-L2 lattice and
the full relation-derived Bockstein lattice.

At D16 the sum lattice has nonunit Smith factors `2^17,4^2,12`, hence index
`2^23*3`. Its index over canonical-plus-L2 is `972=2^2*3^5`; its index over the
full Bockstein lattice is `17414258688=2^15*3^12`.

Neither lattice contains the other. They are commensurable at the same rational
rank but differ substantially in both 2- and 3-primary directions. Equivalently,
their intersection has the corresponding reciprocal finite indices in each.

Thus the integral road map cannot be closed by treating the canonical
transition family as an integral basis for the relation Bockstein image.
Explicit 2- and 3-primary saturation/comparison maps are required.

Evidence is the refreshed `results/L2-bockstein-relation-smith-D16.json`.
`rzk/180-l2-lattice-incomparability-d16.rzk.md` passes all eight declarations
without assumptions.
