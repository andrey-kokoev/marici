# v163: global L2 Bockstein naturality

The square-zero interpretation now has a global naturality result, not just a
global column operator.

Strict A/B column projection implies that an integral A-relation at a higher
cutoff projects to an A-relation below, and its Bockstein representative
satisfies `projection(Bx)=B(projection x)`. New higher-degree source columns
have no lower target contribution. Every finite global relation and Bx therefore
occurs in some cutoff.

Hence the integral relation-to-Bockstein-representative maps form a filtered
natural system and define one global locally finite Bockstein operator. This is
the correct global coefficient object extracted from the L2 calculation.

Cokernel saturation and comparison with the geometric road-Cech boundary remain
separate; neither is inferred from naturality.

Evidence is `results/L2-global-bockstein-naturality.json` from
`checkers/check_L2_global_bockstein_naturality.py`.
`rzk/191-l2-global-bockstein-naturality.rzk.md` passes all eight declarations
without assumptions.
