# Full-family DNC factorization gate

## Result

At ambient degree 14, the K-derivative family has 4,224 rows. Modulo `T+S_K` over `F_32003`, 4,092 are absorbed and 132 remain. All 132 residual rows lie on the single marked level `(1,1,2,1,1)`.

The residual family is now handled exactly over the rationals for every even ambient degree at least 12. The unresolved core is the other 4,092 rows: their `T+S_K` containment is still a finite-field, degree-14 result. No complete exact rational seed family has been materialized for them.

Uniform constructor naturality transports exact identities but does not prove seed existence. Therefore the full characteristic-zero DNC absorption theorem cannot yet be claimed.

## Disposition

The factorization gap is reduced to one bounded task: classify the nonmarked rows by level, pole, and exponent orbit; exact-solve one seed per natural orbit over the rationals; then prove monomial-shift coverage. If those seeds exist, the marked and nonmarked results combine into the full K-family theorem.

## Verification

- `research/voevodsky/check_cosmology_DNC_full_family_factorization_gate.py`
- `research/voevodsky/results/cosmology_DNC_full_family_factorization_gate.json`
