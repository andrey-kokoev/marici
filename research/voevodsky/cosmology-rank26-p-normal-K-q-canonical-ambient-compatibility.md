# Ambient compatibility of canonical q lifts

## Result

Canonical q-lift coefficient lists were independently extracted at ambient degrees 12, 14, and 16, then compared by source descriptors rather than row indices.

The pole-0 lift contains 7 rows at every degree and has the identical descriptor-coefficient digest

```text
206b994eb6385d038a8f16d9801e52088a18bb63ac06dc6ed1aaa4191792dcdb
```

The pole-1 lift contains 11 rows at every degree and has the identical digest

```text
81abd0f74f88174a36cd67ae019f33c99c00cacd4690be9f8cc939195e13fc44
```

Thus the two interior seed identities are exactly compatible under the tested ambient inclusions. Their coefficients and typed q-row descriptors do not depend on the ambient cutoff.

## Disposition

N3b5a is completed. This upgrades invariant lift sizes to exact descriptor-level coefficient compatibility across three degrees.

It does not establish source-natural uniqueness: the compatible representative was selected by deterministic elimination. N3b5 remains active through N3b5b, which must define the boundary transition operator on the three top monomial degrees and verify compatibility with these fixed interior seeds.

## Reproducibility

- Extractor: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_canonical_ambient_signature.py`
- Comparator: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_canonical_ambient_compatibility.py`
- Results: `cosmology_rank26_p_normal_K_q_canonical_signature_a12.json`, `a14.json`, `a16.json`, and `cosmology_rank26_p_normal_K_q_canonical_ambient_compatibility.json` under `research/voevodsky/results/`.
