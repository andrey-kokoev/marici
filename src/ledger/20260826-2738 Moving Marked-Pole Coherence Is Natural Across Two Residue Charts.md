# 2738 — Moving Marked-Pole Coherence Is Natural Across Two Residue Charts

## Frozen square

Use the independently derived residue-chart transition

\[
G_{12}\longrightarrow G_{31}
\]

induced by the site permutation (sigma_{23}), with fiber-coordinate exchange and Poincaré-residue sign (-1).

For a complete labelled marked-pole multiplication family, compare:

1. differentiate its raw relation map in the (G_{12}) chart and then transport it;
2. transport its generator labels and then differentiate the independently constructed (G_{31}) relation map.

The comparison is performed before quotient reduction or span formation.

## Fixed-axis representative

For the complete (q_{\mathcal G_1}) family and the fixed external (x)-direction:

- 2640 source generators are captured;
- transported keys agree bijectively with 2640 target generators;
- raw derivative-map failures: (0);
- Poincaré-orientation failures: (0).

## Hostile swapped-axis representative

For the distinct (q_{\mathcal G_{23}}) family, transport the external derivative (y\to z). Again:

- 2640 generator keys map bijectively;
- raw derivative-map failures: (0);
- Poincaré-orientation failures: (0).

## Result

The moving marked-pole relation derivative is a strict natural transformation on two geometrically distinct occurrence families, including one nontrivial external-axis permutation. The residue orientation multiplies both sides by the same sign and introduces no defect.

This supplies a canonical relation-map-level coherence cell despite Entry 2734's nonunique span witnesses. The canonical object is the full labelled map and its naturality, not a selected absorbing occurrence subspace.

The remaining three occurrence families and the second cyclic chart transition are not yet audited.

## Artifacts

- `research/benincasa/check_rank26_moving_relation_chart_naturality.py`
- `research/benincasa/rank26-moving-relation-chart-naturality.json`
- `research/benincasa/rank26-moving-relation-chart-naturality-g23-axis-1.json`

## Next falsifier

Complete the five-occurrence audit under the (G_{12}\to G_{31}) transition and one generator family under the next cyclic chart transition. Then assemble the corrected finite adapter and rerun the differentiated Euler identity without choosing an occurrence projector.
