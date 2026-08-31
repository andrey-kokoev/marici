# Degree-14 p-normal reduction-complexity census

## Result

The fixed `S+T` rowwise certificate was refined by source family and pivot-elimination depth over both primes.

| family | direction | rows | nonzero inputs | max pivot eliminations |
|---|---|---:|---:|---:|
| IBP | `nx` | 480 | 480 | 551 |
| IBP | `ny` | 480 | 480 | 531 |
| \(K\)-multiplication | `nx` | 4,224 | 4,224 | 580 |
| \(K\)-multiplication | `ny` | 4,224 | 4,224 | 566 |
| marked-\(q\) | `nx` | 25,200 | 10,080 | 544 |
| marked-\(q\) | `ny` | 25,200 | 10,080 | 544 |

Every row still has zero final remainder. The nonzero-input counts and maximum pivot depths agree over \(\mathbb F_{32003}\) and \(\mathbb F_{32009}\). Total pivot counts differ slightly between primes because intermediate modular cancellations differ.

## Meaning

Absorption is not explained by the derivative rows being trivial:

- every IBP derivative row is nonzero before reduction;
- every \(K\)-multiplication derivative row is nonzero;
- 10,080 marked-\(q\) rows per direction are nonzero.

The deterministic finite reducer needs at most 580 pivot eliminations per row at degree 14. This gives a concrete complexity bound for the current certificate and identifies the \(K\)-multiplication family as having the largest observed reduction depth.

Pivot depth depends on row and column order, so it is not a basis-independent homotopy length. Reduction coefficients and a uniform homotopy remain unconstructed.

## Reproducibility

- Per-prime checker: `research/voevodsky/check_cosmology_rank26_p_normal_degree14_reduction_complexity.py`
- Aggregate checker: `research/voevodsky/check_cosmology_rank26_p_normal_degree14_complexity_two_prime.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_degree14_complexity_two_prime.json`
