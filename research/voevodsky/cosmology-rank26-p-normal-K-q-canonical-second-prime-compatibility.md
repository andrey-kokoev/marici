# Canonical interior seeds at a second prime

## Result

The canonical pole-0 and pole-1 q lifts were independently extracted over \(\mathbb F_{32009}\) at ambient degrees 12, 14, and 16.

At the second prime:

- the pole-0 lift has 7 rows and one identical descriptor-coefficient digest across all three degrees;
- the pole-1 lift has 11 rows and one identical digest across all three degrees.

The typed source descriptor supports are identical to those over \(\mathbb F_{32003}\). Coefficient hashes differ between primes, as expected for field-valued coefficients.

| pole | rows | \(p=32003\) ambient-compatible | \(p=32009\) ambient-compatible | same descriptor support |
|---:|---:|---|---|---|
| 0 | 7 | yes | yes | yes |
| 1 | 11 | yes | yes | yes |

## Disposition

N4a is completed. Canonical seed compatibility is not a one-prime artifact at the level of support and ambient transport.

No integral coefficient lift is claimed. N4 remains active through N4b: rerun adjacent boundary source words and full direct-versus-composite coherence over \(\mathbb F_{32009}\).

## Reproducibility

- Extractor: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_canonical_ambient_signature.py`
- Comparator: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_canonical_second_prime_compatibility.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_canonical_second_prime_compatibility.json`
