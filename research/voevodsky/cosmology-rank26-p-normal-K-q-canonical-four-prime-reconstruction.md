# Four-prime reconstruction exposes pivot dependence

## Result

Prime 32029 was verified and sampled. Standard rational reconstruction was applied to descriptor-paired canonical coefficients across primes 32003, 32009, 32027, and 32029. The modulus product is

```text
1050805741917077141
```

with symmetric uniqueness bound 724,846,791.

| K pole | coefficients | reconstructed | unresolved |
|---:|---:|---:|---:|
| 0 | 7 | 7 | 0 |
| 1 | 11 | 9 | 2 |

One pole-1 coefficient reconstructed from three primes is contradicted by the fourth residue, reducing the stable count from 10 to 9. Therefore the deterministic finite-field representatives cannot be treated as reductions of one common small rational coefficient word merely because their source supports coincide.

## Disposition

N5a3 is falsified as a complete four-prime rational reconstruction. Repeated prime sampling is no longer the highest-value route: it risks fitting field-dependent pivot representatives.

Tree rescoring selects N5c, a direct characteristic-zero constrained solve. It must fix the common 7-row and 11-row source descriptor supports, formulate membership modulo `T + S_K` over exact rational arithmetic, and solve for coefficients without importing finite-field pivot choices. Until that passes, no rational or characteristic-zero source identity is claimed.

## Reproducibility

- Fourth-prime extractor: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_canonical_ambient_signature.py`
- Reconstruction checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_canonical_four_prime_reconstruction.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_canonical_four_prime_reconstruction.json`
