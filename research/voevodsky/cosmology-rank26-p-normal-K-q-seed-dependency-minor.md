# Canonical seed dependency minors

## Result

The canonical targets were traced through a basis containing `T`, `S_K`, and the fixed selected q rows. Only active pivot dependencies were retained.

| K pole | selected q rows | active/source rows | retained columns | T rows | special K rows | q rows | maximum depth |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 7 | 27 | 27 | 17 | 3 | 7 | 3 |
| 1 | 11 | 45 | 45 | 28 | 6 | 11 | 3 |

Both closures reconstruct their targets exactly over \(\mathbb F_{32003}\). The source generator indices and retained column indices are materialized in the result JSON.

## Disposition

N5c2a is completed. The full rank-11,603 quotient problem reduces to square candidate minors of sizes 27 and 45, making exact rational elimination bounded.

N5c2b becomes active. It must rebuild these rows over exact integers/rationals, verify that modular signed lifts match source-derived integer coefficients, solve each square system, and reconstruct the complete target identity. The minor is modularly selected, so exact nonsingularity must be checked rather than assumed.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_seed_dependency_minor.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_seed_dependency_minor.json`
