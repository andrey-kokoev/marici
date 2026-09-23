# Seven cyclic minors may control admitted fibres—but not arbitrary targets

A new exact halfspace census points to a sharper potential coverage theorem. A subsequent universal telescoping theorem proves that the seven cyclic halfspaces form a compact polygon whenever the seven source cyclic minors are strictly positive; see `the-seven-cyclic-halfspaces-always-form-a-bounded-fibre-polygon.md`. Compactness does NOT prove noncyclic redundancy. At each of 245 strictly positive seven-column source samples spanning seven sign gauges, ONLY the seven cyclic ordered minors among the 21 source minors support edges of the fixed-target positive fibre polygon. The other fourteen may vanish at vertices but support no sampled polygon edge. A separate 350-target test constructs both exact polygons—using seven cyclic inequalities and using all 21 inequalities—and checks they are bounded with identical vertex sets at every strictly-positive-source target.

This is NOT a universal redundancy theorem. In particular **cyclic positivity alone is false without the admitted-positive-target precondition**. A deliberately constructed source matrix with rows

    (1,1,0,-1,-1,-1,2),
    (0,1,1,1,0,-2,1)

has all seven ordered cyclic minors strictly positive but six noncyclic minors negative. Its cyclic-only fibre polygon has three vertices, while the full positive fibre is empty. The cyclic polygon is bounded, so the empty full vertex set genuinely rules out an admitted positive lift. This example does not refute the restricted conjecture for `Y` already known to lie in the positive image; it demonstrates why that provenance must not be dropped.

**Precise next proof target:** for every `Y=CZ` with a strictly positive rank-two source `C` and fixed strictly positive moment-curve `Z`, show that each noncyclic minor inequality is valid over the compact polygon cut out by the seven cyclic minor inequalities. One possible certificate is a rational nonnegative combination of those seven inequalities with coefficients permitted to depend on the admitted target `Y`. Then the active-set coverage theorem reduces from 21 potential facet inequalities to seven. Pointwise finite Farkas certificates would not suffice without an all-positive-source argument, and this still would not prove physical history-form matching.

Run:

    python research/nima/checkers/check_seven_point_fibre_facet_census.py
    python research/nima/checkers/check_seven_point_cyclic_fibre_reduction_probe.py

Artifacts: `research/nima/results/seven-point-fibre-facet-census.json` and `research/nima/results/seven-point-cyclic-fibre-reduction-probe.json`.
