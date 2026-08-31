# Fixed-support coefficient uniqueness gate

## Result

For each canonical target, the common selected q rows were adjoined directly to the full `T + S_K` basis. Rank additions were measured before adjoining the target.

Over both \(\mathbb F_{32003}\) and \(\mathbb F_{32009}\):

| K pole | selected q rows | quotient rank added | coefficient-kernel dimension | target rank addition |
|---:|---:|---:|---:|---:|
| 0 | 7 | 7 | 0 | 0 |
| 1 | 11 | 11 | 0 | 0 |

Stored coefficient certificates also reconstruct exactly. Thus each field has a unique coefficient solution on the fixed descriptor support; field variation is not gauge freedom inside that support.

An intermediate implementation ranked separately reduced quotient representatives and incorrectly reported a pole-1 target rank addition. This contradicted a directly verified certificate. Recomputing rank in the full source space repaired the defect and restored consistency.

## Disposition

N5c1 is completed. The failed four-prime bounded reconstruction reflects coefficient height beyond the tested uniqueness range, not a positive-dimensional fixed-support solution family.

N5c2 becomes active: solve the 7-variable and 11-variable constrained systems directly over exact rational arithmetic. A viable implementation should project against a source-derived independent row/column minor rather than perform unrestricted rational elimination on the full 11,000-rank base.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_seed_support_uniqueness.py`
- Results: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_seed_support_uniqueness_p32003.json` and `...p32009.json`.
