# Canonical marked-q lifts for K residuals

## Result

Exact q-only provenance was retained while reducing the canonical monomial residual at marked levels

```text
(g1,g2,g3,g23,g31) = (1,1,2,1,1)
```

against `T + S_K + S_q`.

For pole 0, the target plus 7 special marked-\(q\) rows lies in `T + S_K`. All 7 rows are `g1` rows: 3 at q-pole 0 and 4 at q-pole 1.

For pole 1, the target plus 11 special marked-\(q\) rows lies in `T + S_K`. All 11 rows are `g1` rows: 3 at q-pole 0, 4 at q-pole 1, and 4 at q-pole 2.

Both identities were reconstructed exactly over \(\mathbb F_{32003}\). The complete pivot-order-dependent coefficient lists and digests are retained in the result JSON.

## Interpretation

Although the unresolved K targets occupy the `g3`-level-2 stratum, their canonical special-wall correction is carried entirely by `g1` multiplication rows. The correction reaches one q-pole above the K target pole.

This is an explicit finite lift, not yet a uniform formula. The next leaf tests whether multiplying these two canonical identities by every retained monomial reproduces the 132 residual identities without boundary loss or coefficient changes.

## Disposition

N3b3b is completed. N3b3c becomes active.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_canonical_q_lifts.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_canonical_q_lifts.json`
