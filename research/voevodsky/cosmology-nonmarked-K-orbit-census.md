# Nonmarked K-family orbit census

## Result

The 4,092 nonmarked degree-14 rows factor as:

- 31 nonmarked five-level patterns;
- two K poles;
- 66 monomial exponents of total degree at most ten.

Under the two axis-square maps, the natural orbit key is `(K pole, level pattern, exponent parity pair)`. There are 248 orbits. Their minimal exponent seeds are `(0,0)`, `(0,1)`, `(1,0)`, and `(1,1)` for each pole and level pattern.

Hence the unresolved modular core reduces to 248 exact rational A12 seed tests. If those identities exist, unchanged inclusions and square-monomial naturality reach every nonmarked K target at every even ambient degree at least 12.

## Verification correction

The first checker run incorrectly expected parity-orbit sizes 15 and 18. It failed. Direct counting gives size 21 for even-even exponents and size 15 for each other parity; the corrected checker passes with 62 orbits of size 21 and 186 of size 15.

## Disposition

No exact seed identity is inferred from the census. The next leaf is to solve all 248 seed systems over the rationals and record failures and denominator bounds without modular promotion.

## Reproducibility

- `research/voevodsky/check_cosmology_nonmarked_K_orbit_census.py`
- `research/voevodsky/results/cosmology_nonmarked_K_orbit_census.json`
