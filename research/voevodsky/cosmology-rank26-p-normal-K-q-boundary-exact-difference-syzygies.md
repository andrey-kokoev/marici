# Exact boundary transport differences are source syzygies

## Result

Each lower-ambient exact word was transported through the typed descriptor map, subtracted from the independently solved higher-ambient word, and evaluated against exact higher-ambient `T`, `S_K`, and `Q` rows reconstructed by four-prime CRT.

| inclusion | difference cells | exact zero evaluations | support range |
|---|---:|---:|---:|
| A12 to A14 | 48 | 48 | 40–65 |
| A14 to A16 | 60 | 60 | 40–65 |
| A12 to A16 | 48 | 48 | 53–85 |

All 156 differences evaluate to zero over the rationals. The failure of literal representative transport is therefore an exact source-syzygy effect, not a target mismatch.

## Disposition

N5b3c1 is completed. N5b3c2 becomes active.

The remaining coherence test is coefficient-level composition: for each A12 boundary coordinate, compare the direct A12-to-A16 difference cell with the A14-to-A16 transport of the A12-to-A14 cell plus the local A14-to-A16 cell. This equality is algebraically expected from functorial descriptor shift, but must be checked on the retained exact dictionaries rather than inferred.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_exact_difference_syzygies.py`
- Results: corresponding `...difference_syzygies_a14.json` and `...a16.json` files.
