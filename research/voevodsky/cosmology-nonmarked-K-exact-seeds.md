# Exact rational nonmarked K seeds

## Result

All 248 A12 nonmarked seed systems have exact rational `T+S_K` contractions:

- two K poles;
- 31 nonmarked level patterns;
- four parity seeds per pole and pattern.

Every reconstructed target agrees coefficientwise over the rationals. The largest selected system has 12 source rows and 13 equations. The maximum coefficient denominator is 50,112.

Closures were selected with the `F_32003` pivot order and coefficients reconstructed from four primes, but each final identity was checked by complete exact rational reconstruction. Modular membership was not used as the conclusion.

## Disposition

The exact-seed leaf is completed. Together with the orbit census and uniform constructor naturality, these seeds transport to every nonmarked K target at every even ambient degree at least 12.

The next leaf combines this result with the already proved marked-residual quotient colimit to state and verify the full K-family characteristic-zero absorption theorem. It must retain the distinction between representative contractions and canonical quotient classes.

## Verification

- `research/voevodsky/check_cosmology_nonmarked_K_exact_seeds.py`
- `research/voevodsky/results/cosmology_nonmarked_K_exact_seeds_a12.json`
