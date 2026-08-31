# Explicit lower-edge boundary correction words

## Result

Representative correction cells at the lower boundary coordinate were back-substituted completely to original p-tangent and special K source rows for both adjacent ambient inclusions.

| K pole | inclusion | trace length | source rows | T rows | special K rows |
|---:|---|---:|---:|---:|---:|
| 0 | 12 to 14 | 21 | 30 | 25 | 5 |
| 0 | 14 to 16 | 21 | 30 | 25 | 5 |
| 1 | 12 to 14 | 33 | 50 | 40 | 10 |
| 1 | 14 to 16 | 33 | 50 | 40 | 10 |

Every identity reconstructs exactly over \(\mathbb F_{32003}\). The source-row counts and trace lengths are invariant across the two inclusions. Raw coefficient digests differ because row indices change with ambient degree.

## Disposition

N3b5b3a is completed. Correction-cell existence now has original-source witnesses rather than only quotient reductions.

N3b5b3 remains active through N3b5b3b: decode the T and special-K row indices into source descriptors, normalize exponents by the boundary coordinate, and compare coefficients across inclusions. Matching normalized signatures would establish transport of these representative source words; differing signatures would retain only invariant complexity counts.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_correction_source_words.py`
- Results:
  - `research/voevodsky/results/cosmology_rank26_p_normal_K_q_boundary_correction_words_A12_to_A14.json`
  - `research/voevodsky/results/cosmology_rank26_p_normal_K_q_boundary_correction_words_A14_to_A16.json`
