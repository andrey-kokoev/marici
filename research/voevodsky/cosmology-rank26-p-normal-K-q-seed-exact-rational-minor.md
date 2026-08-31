# Exact rational canonical seed identities

## Result

The modularly selected dependency closures were rebuilt entrywise over the integers using four-prime CRT. The largest reconstructed integer row entry is 3,888, far below half the modulus product. Exact Fraction elimination was then performed on the 27-by-27 and 45-by-45 source minors.

Both minors are nonsingular over the rationals, and both solutions reconstruct the complete target rows across all ambient columns.

| K pole | minor | full reconstruction | largest source numerator | largest denominator |
|---:|---:|---|---:|---:|
| 0 | 27 | yes | 78,732 | 1,134 |
| 1 | 45 | yes | 78,732 | 1,111,065,984 |

The large pole-1 denominator explains why four-prime symmetric rational reconstruction failed. The exact 7 and 11 q coefficients and source-word digests are retained in the result JSON.

## Disposition

N5c2b is completed. Canonical degree-14 seed identities now hold over exact rational arithmetic; they are no longer finite-field-only observations.

This does not yet prove the ambient family or unbounded theorem. N5c remains active through N5c3: verify the same rational source coefficients directly at ambient degrees 12 and 16, then establish the interior monomial-shift identities over the rationals through degree \(A-7\).

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_seed_exact_rational_minor.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_seed_exact_rational_minor.json`
