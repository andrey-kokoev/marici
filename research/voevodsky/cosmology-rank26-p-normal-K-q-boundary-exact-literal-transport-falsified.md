# Exact boundary source words do not transport literally

## Test

The exhaustive exact boundary solver now retains every nonzero rational coefficient keyed by its typed `T`, `S_K`, or `Q` descriptor. Each lower-degree word was shifted through the admitted vertical descriptor map and compared coefficientwise with the independently solved higher-degree word for the shifted target.

## Result

| inclusion | targets | literal matches | difference support |
|---|---:|---:|---:|
| A12 to A14 | 48 | 0 | 40–65 terms |
| A14 to A16 | 60 | 0 | 40–65 terms |
| A12 to A16 | 48 | 0 | 53–85 terms |

Thus literal representative transport is falsified for every tested target. This does not falsify ambient coherence: both words reconstruct the same shifted target, so their difference is expected to be an exact source syzygy when the descriptor transport preserves row evaluation.

## Disposition

N5b3b is falsified. N5b3c becomes active.

The next test must evaluate each rational coefficient difference against the exact higher-ambient source rows, verify that it is a zero source relation, and compare the direct A12-to-A16 difference with the sum of the transported A12-to-A14 and A14-to-A16 differences. Equality of reconstructed targets alone is insufficient unless the descriptor transport itself is checked against exact row transport.

## Reproducibility

- Exact-word producer: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_exact_all_solves.py`
- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_exact_literal_transport.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_boundary_exact_literal_transport.json`
