# Exact rational base corrections for all interior shifts

## Result

The exact rectangular solver was run for every corrected interior target at ambient degrees 12, 14, and 16.

| ambient degree | targets solved | maximum source rows | maximum equations | full reconstructions |
|---:|---:|---:|---:|---:|
| 12 | 42 | 94 | 109 | 42 |
| 14 | 72 | 129 | 146 | 72 |
| 16 | 110 | 170 | 191 | 110 |

All 224 systems have exact rational `T+S_K` corrections and reconstruct their complete corrected targets. The maximum denominator remains 1,111,065,984; no new denominator appears away from the canonical seed.

## Disposition

N5c3c2b and the rational interior branch N5c3 are completed. The exact q templates generate the complete interior family through degree \(A-7\) at all three tested ambient degrees, with fresh graded base corrections.

This is still a finite ambient theorem at degrees 12, 14, and 16. It does not establish an unbounded ambient identity.

The highest-value remaining branch is N5b: reconstruct the top-three-degree boundary correction templates over the rationals and test their direct/composite ambient coherence.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_exact_base_representative_solves.py` with `MARICI_ALL_SHIFTS=1`.
- Results: corresponding `...exact_base_all_shifts_a12.json`, `...a14.json`, and `...a16.json` files.
