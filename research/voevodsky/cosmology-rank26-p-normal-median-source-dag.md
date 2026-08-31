# Median singleton expanded to original source rows

## Issue-tree position

Depth-first traversal continues from the lower-quartile leaf to the median representative.

## Result

Target:

```text
column 9560
k_pole = 1
q_levels = (2,1,1,2,1)
monomial = (3,6)
```

The normalized trace has length 186. Complete back-substitution through the pivot dependency DAG gives:

- 451 active pivot nodes;
- 3,677 traversed dependency edges;
- maximum recorded dependency depth 38;
- 439 original special rows;
- 12 original p-tangent rows;
- 451 nonzero source coefficients.

The exact identity

\[
e_{9560}=\sum_i a_iS_i+\sum_j b_jT_j
\]

was reconstructed over \(\mathbb F_{32003}\). The full coefficient list is retained with digest:

`c7039fd6f7ed828fbfadd8519e4741fb3d4276bd5ffe31de9a28e1ef72fe2b00`

## Meaning

The longer normalized trace does not force a larger source expansion: modular cancellation reduces the median representative to 451 original rows, fewer than the lower-quartile representative's 571. Both have dependency depth 38.

No unsourced pivot remains. The branch continues to the upper-quartile representative, then the maximum representative. These expressions remain single-prime and presentation-dependent rather than uniform templates.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_median_source_dag.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_median_source_dag.json`
