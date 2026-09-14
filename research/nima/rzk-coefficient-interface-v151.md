# v151: canonical plus L2 integral completion at D16

The true integral checker now presents the canonical generator family and the
distinguished L2 transition inside the same target lattice as the full
relation/Bockstein computation.

At D16 the canonical family raises rank by 13. Adding
`3a^3+3a^3b` raises it by 14, reaching the full Bockstein rational rank, exactly
as in the modular scout.

Integrally, the canonical image has nonunit factors `2^15,12^5`; canonical plus
L2 has `2^14,6,12^5`. The full relation-derived Bockstein lattice instead has
`2^21,6^9,12^4`. Thus equal rank does not identify the integer lattices. In
particular, the externally written canonical vectors have not yet been proved
to lie in the integral relation-derived Bockstein image.

The next integral gate is to compute inclusion/intersection indices between the
canonical-plus-L2 lattice and the full relation-image lattice. Smith rank
completion alone is insufficient.

Evidence is the refreshed `results/L2-bockstein-relation-smith-D16.json`.
`rzk/179-l2-canonical-integral-completion-d16.rzk.md` passes all eight
declarations without assumptions.
