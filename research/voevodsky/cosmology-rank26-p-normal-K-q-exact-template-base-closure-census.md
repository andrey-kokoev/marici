# Interior base-correction dependency census

## Result

Fresh `T+S_K` dependency closures were extracted for every corrected interior target at ambient degrees 12, 14, and 16 over \(\mathbb F_{32003}\).

| degree | pole | shifts | source-row range | retained-column range | maximum depth |
|---:|---:|---:|---:|---:|---:|
| 12 | 0 | 21 | 20–45 | 27–52 | 5 |
| 12 | 1 | 21 | 34–94 | 45–109 | 5 |
| 14 | 0 | 36 | 20–58 | 27–65 | 5 |
| 14 | 1 | 36 | 34–129 | 45–146 | 5 |
| 16 | 0 | 55 | 20–72 | 27–80 | 5 |
| 16 | 1 | 55 | 34–170 | 45–191 | 5 |

All 224 corrected targets reduce exactly in their modular base closures. Maximal closures occur near the interior cutoff, with pole 1 consistently larger.

## Disposition

N5c3c2a is completed. Exact solving remains bounded: the largest observed system has 170 source unknowns across 191 retained equations.

N5c3c2b becomes active. First solve exact rational representative closures at the canonical, median, and maximal-size shifts for each ambient degree and pole. If their integer systems are nonsingular or consistent with full reconstruction, extend to all shifts; otherwise type the exact obstruction before further sampling.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_exact_template_base_closure_census.py`
- Results: corresponding `..._a12.json`, `..._a14.json`, and `..._a16.json` files.
