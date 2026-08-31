# Upper-quartile singleton expanded to original source rows

## Issue-tree position

Depth-first traversal continues from the median to the upper-quartile representative.

## Result

Target:

```text
column 1279
k_pole = 0
q_levels = (1,1,2,2,1)
monomial = (9,4)
```

Its normalized trace length is 250. Complete source-row back-substitution gives:

- 886 active pivot nodes;
- 10,087 traversed dependency edges;
- maximum recorded depth 37;
- 877 original special rows;
- 9 original p-tangent rows;
- 886 nonzero source coefficients.

Exact reconstruction passed:

\[
e_{1279}=\sum_i a_iS_i+\sum_j b_jT_j
\]

over \(\mathbb F_{32003}\).

Coefficient digest:

`0d1ec04f621fc0e832234604ecd5c3d299edac3a06b1e1cd4fe28e55c896484f`

## Meaning

The source expansion remains bounded but grows relative to the median: 886 source generators and 10,087 dependency edges. No unsourced normalized pivot remains.

The depth-first representative sequence now has source supports of 1, 571, 451, and 886 rows from minimum through upper quartile. Normalized trace length is therefore not monotone with final source support because cancellation occurs during DAG back-substitution.

The next leaf is the maximum-trace representative. If it remains bounded, this representative subbranch is exhausted and the issue tree should be rescored toward reusable templates or a second-prime source expansion.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_upper_quartile_source_dag.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_upper_quartile_source_dag.json`
