# Four-prime validation of exact rational q-template shifts

## Result

Only the exact rational q-coefficient templates were shifted. For each target, the shifted q word was subtracted from the K derivative target and reduced against a freshly built `T+S_K` basis.

Every interior shift passed at all four primes 32003, 32009, 32027, and 32029:

| ambient degree | shifts per pole | total prime-pole-shift reductions |
|---:|---:|---:|
| 12 | 21 | 168 |
| 14 | 36 | 288 |
| 16 | 55 | 440 |

No shifted q descriptor crosses the graded cutoff in this corrected formulation, and every corrected target lies in the finite-field base span.

## Disposition

N5c3c1 is completed. The exact rational q template has the correct reductions throughout the full tested interior family.

This remains modular validation of base membership, not an exact rational correction word. N5c3c2 becomes active: extract fresh `T+S_K` dependency closures for corrected targets and solve them over the rationals. A bounded representative census should first measure closure sizes and select extremal shifts before attempting all 224 rational identities.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_exact_template_shift_four_prime.py`
- Results: corresponding `..._a12.json`, `..._a14.json`, and `..._a16.json` files under `research/voevodsky/results/`.
