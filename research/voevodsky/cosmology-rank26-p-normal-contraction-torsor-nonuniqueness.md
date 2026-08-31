# Exact contraction torsor is nontrivial

## Result

Every overlap syzygy is nonzero as a source coefficient word while evaluating to zero. Acting on either transported contraction by rational multiples of this syzygy produces distinct contractions of the same target.

| inclusion | overlap targets | nonzero actions | syzygy support |
|---|---:|---:|---:|
| A12 to A14 | 36 | 36 | 64–116 |
| A14 to A16 | 48 | 48 | 75–137 |
| A16 to A18 | 60 | 60 | 90–158 |

For every overlap target, coefficients 0, 1, and 2 along the syzygy direction give three explicitly distinct rational source words with the same image. Hence the contraction space is not a singleton.

## Disposition

P5d2c2c is completed with an obstruction: the admitted exact source data does not select a unique contraction. A canonical section would require an additional source-derived normalization, symmetry, universal property, or homotopy selector. Nonuniqueness does not prove that no such extra datum can exist; none is currently supplied.

P5d2 is completed as a classification. Source constructors and their two-monomial cover are natural, and contractions carry coherent exact descent cells, but the natural object is a nontrivial contraction torsor rather than a canonical coefficient word.

P5d3 becomes active: determine whether quotienting contractions by exact source syzygies produces a canonical ambient-compatible class and whether that class admits a colimit interpretation.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_contraction_torsor_nonuniqueness.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_contraction_torsor_nonuniqueness.json`
