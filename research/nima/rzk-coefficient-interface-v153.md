# v153: canonical-L2/relation lattice incomparability at D20

The integral lattice comparison now extends to D20. The canonical family has
rank gain 17 and canonical plus L2 has gain 18, reaching the full Bockstein
rational rank.

Canonical plus L2 has nonunit factors `2^26,12^7,24,840`. The sum with the full
relation-derived Bockstein lattice has `2^31,4^2,8,24`. The sum-over-canonical
index is `7348320 = 2^5 3^8 5 7`; the sum-over-full-Bockstein index is
`45137758519296 = 2^20 3^16`.

Again neither lattice contains the other. The sum removes the canonical
5- and 7-primary obstructions while exposing a large 2/3-primary mismatch with
the relation lattice. This confirms that D16 incomparability was not a boundary
artifact.

Evidence is the refreshed `results/L2-bockstein-relation-smith-D20.json`.
`rzk/181-l2-lattice-incomparability-d20.rzk.md` passes all eight declarations
without assumptions.
