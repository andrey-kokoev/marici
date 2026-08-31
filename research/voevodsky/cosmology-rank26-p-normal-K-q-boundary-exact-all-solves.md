# Exact rational identities for every cutoff-boundary target

## Result

Every top-three-degree K target was solved using its full `T+S_K+Q` source closure reconstructed over the integers by four-prime CRT.

| ambient degree | targets | largest exact system | maximum denominator | full reconstructions |
|---:|---:|---:|---:|---:|
| 12 | 48 | 73-by-73 | 13,716,864 | 48 |
| 14 | 60 | 91-by-91 | 1,524,096 | 60 |
| 16 | 72 | 110-by-110 | 169,344 | 72 |

All 180 square systems are nonsingular over the rationals and reconstruct their complete targets.

Combined with the 224 exact interior identities, every K-derivative target on the marked stratum `(1,1,2,1,1)` has an exact rational source identity at ambient degrees 12, 14, and 16.

## Disposition

N5b2 is completed. The characteristic-zero result is a finite ambient theorem at the three tested degrees.

N5b3 remains open: compare exact boundary source words under A12-to-A14-to-A16 descriptor transport and test direct versus composite rational correction cells. The one-prime 48/48 composition result does not prove this exact coherence.

No unbounded ambient theorem, surviving p-normal quotient line, horn comparison, relative Bockstein, contour, or physical period follows from the finite-degree identities.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_exact_all_solves.py`
- Results: corresponding `...boundary_exact_all_a12.json`, `...a14.json`, and `...a16.json` files.
