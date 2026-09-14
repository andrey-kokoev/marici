# v150: true L2 integral Bockstein Smith through D28

The optimized integral relation calculation now reaches D28, completing all
cutoffs used by the modular orbit scout.

At D28 the odd target rank is 210, with 4,420 labelled columns and relation-
kernel rank 4,265. The u0 image rank is 155 and the full Bockstein image rank is
181, giving gain 26, exactly matching the modular beta rank.

The augmented nonunit Smith factors are `2^78,6^18,12^3,24,48^3`. Thus only
2- and 3-primary torsion remains, although the original image also contains
5-, 7-, 11-, and 13-primary factors. The distinguished transition changes
`2^78` to `2^77`, again with index ratio two.

Across D12,16,20,24,28 the true labelled integral beta-rank gains are
`8,14,18,22,26`; D16 onward match the modular scout exactly. Full Bockstein
torsion has support `{2,3}` at every cutoff, and the distinguished transition
consistently removes one order-two class. These conclusions replace the earlier
misattributed Cartier Smith pattern.

Evidence is `results/L2-bockstein-relation-smith-D28.json`.
`rzk/178-l2-integral-bockstein-smith-d28.rzk.md` passes all eight declarations
without assumptions.
