# Maximum-trace singleton expanded to original source rows

## Issue-tree position

This is the final leaf in the five-representative source-expansion subbranch.

## Result

Target:

```text
column 16699
k_pole = 2
q_levels = (2,1,2,2,2)
monomial = (13,0)
```

The maximum normalized trace length is 544. Complete source back-substitution gives:

- 1,062 active pivot nodes;
- 4,969 traversed dependency edges;
- maximum recorded depth 38;
- 1,002 original special rows;
- 60 original p-tangent rows;
- 1,062 nonzero source coefficients.

Exact reconstruction passed:

\[
e_{16699}=\sum_i a_iS_i+\sum_j b_jT_j
\]

over \(\mathbb F_{32003}\).

Coefficient digest:

`fabc75da2b88ff25e81b61818c8ae2e7242752672d02652b73c35ddb38049f95`

## Representative-subbranch disposition

All five sampled leaves now have complete original-source dispositions:

| sample | normalized trace | source rows | S rows | T rows |
|---|---:|---:|---:|---:|
| minimum | 1 | 1 | 0 | 1 |
| lower quartile | 126 | 571 | 562 | 9 |
| median | 186 | 451 | 439 | 12 |
| upper quartile | 250 | 886 | 877 | 9 |
| maximum | 544 | 1,062 | 1,002 | 60 |

The representative back-substitution subbranch is exhausted. Every sampled normalized expansion reaches original source rows without an unsourced pivot.

## Issue-tree reevaluation

The next highest-value depth-first branch is reusable template extraction: determine whether source coefficients organize by pole level, mark level, and monomial shift. A second-prime coefficient comparison is next if no compact template exists. The IBP and \(K\)-multiplication absorption mechanisms remain separate high-value branches.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_maximum_source_dag.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_maximum_source_dag.json`
