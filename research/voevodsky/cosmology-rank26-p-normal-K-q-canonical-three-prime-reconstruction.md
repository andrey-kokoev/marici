# Three-prime rational reconstruction

## Test

A third prime, 32027, was verified by trial division and used for an independent degree-14 canonical seed extraction. Coefficients were paired by typed source descriptor across primes 32003, 32009, and 32027.

Rational reconstruction used the symmetric uniqueness bounds

\[
|n|\le 4{,}000{,}000,
\qquad
1\le d\le 4{,}000{,}000,
\]

which remain below the three-modulus uniqueness threshold.

## Result

| K pole | coefficients | reconstructed | unresolved |
|---:|---:|---:|---:|
| 0 | 7 | 7 | 0 |
| 1 | 11 | 10 | 1 |

The third residue resolves five of the six two-prime failures, but one pole-1 coefficient still has no rational candidate inside the maximal practical symmetric uniqueness range.

## Disposition

N5a2 is incomplete as a full characteristic-zero lift. Promotion remains withheld.

N5 remains active through N5a3: sample the independently verified prime 32029 and perform four-modulus reconstruction. The larger modulus product permits a substantially wider unique rational range and directly tests whether the last coefficient is a large rational or a field-dependent pivot artifact.

## Reproducibility

- Seed extractor: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_canonical_ambient_signature.py`
- Reconstruction checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_canonical_three_prime_reconstruction.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_canonical_three_prime_reconstruction.json`
