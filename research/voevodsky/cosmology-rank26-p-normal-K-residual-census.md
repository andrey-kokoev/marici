# Graded K-residual quotient census

## Result

Modulo `T + S_K`, the 132 nonabsorbed `nx` K-family rows have quotient rank 72. They are exactly:

- 66 rows at pole level 0 and 66 at pole level 1;
- one row for every retained monomial of total degree at most 10 at each pole;
- one marked-level pattern only:

```text
(g1,g2,g3,g23,g31) = (1,1,2,1,1).
```

After adjoining special IBP relations, the pole-0 copy disappears. The remaining 66 rows have quotient rank 38 and are exactly the pole-1 copy of the same monomial family and marked-level pattern.

## Interpretation

The apparent 132 unrelated failures are two monomial-shift families supported on a single marked stratum: `g3` is at level 2 while every other wall is at level 1. Special IBP removes the entire lower-pole family but not the upper-pole family.

This sharply localizes the marked-\(q\) mechanism. The next leaf need not search all 25,200 special wall rows: it should extract lifts for the canonical monomial at pole levels 0 and 1 on the `(1,1,2,1,1)` stratum, then test whether monomial shifts generate the remaining rows within the degree cutoff.

## Disposition

N3b3a is completed. N3b3 remains active through child N3b3b, explicit canonical marked-\(q\) lifts.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_residual_census.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_residual_census.json`
