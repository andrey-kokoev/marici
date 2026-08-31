# Source constructors are ambient-natural

## Question

Does multiplication by the second monomial variable squared define a rowwise source map on the `T`, `S_K`, and `Q` constructors, or does the failure of coefficient recurrence already occur at the relation-constructor level?

## Result

Every lower-ambient source descriptor was shifted by two in its second exponent. Its sparse row was transported through the corresponding column-label shift and compared with the higher-ambient row.

| inclusion | T rows | S_K rows | Q rows | failures |
|---|---:|---:|---:|---:|
| A12 to A14 | 21,964 | 2,880 | 18,720 | 0 |
| A14 to A16 | 29,904 | 4,224 | 25,200 | 0 |
| A16 to A18 | 39,076 | 5,824 | 32,640 | 0 |

All 154,188 row comparisons are coefficient-identical. Ambient multiplication commutes literally with every tested source constructor.

## Disposition

P5d2c1 is completed. The recurrence obstruction is not failure of the source differential or constructor inclusion. It lies in selecting a contracting word naturally: independently chosen exact contractions differ by coherent syzygies, but neither the words nor adjacent syzygy cells stabilize.

P5d2c2 becomes active: seek a canonical contracting homotopy or prove that the current data define only a torsor of contractions without a source-derived section.

The result is checked at the rank-26 test point across A12–A18. It does not alone prove the constructor identity symbolically for all points or all ambient degrees.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_source_constructor_ambient_naturality.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_source_constructor_ambient_naturality.json`
