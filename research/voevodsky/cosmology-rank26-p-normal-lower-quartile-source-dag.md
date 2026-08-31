# Lower-quartile singleton expanded to original source rows

## Issue-tree position

The minimum leaf terminated in one original p-tangent row. Depth-first traversal next reaches the lower-quartile representative, whose normalized-pivot trace has length 126.

## Result

Target:

```text
column 2962
k_pole = 0
q_levels = (1,2,2,2,2)
monomial = (7,0)
```

The normalized-pivot expansion was back-substituted through the complete pivot dependency DAG. The active closure contains:

- 571 pivot nodes;
- 3,866 traversed dependency edges;
- maximum recorded dependency depth 38.

After modular cancellation, the exact original-source identity is

\[
e_{2962}=\sum_i a_i S_i+\sum_j b_j T_j
\]

over \(\mathbb F_{32003}\), using:

- 562 original special relation rows;
- 9 original p-tangent derivative rows;
- 571 nonzero source coefficients total.

Exact reconstruction of the singleton row passed. The full coefficient list is retained in the result JSON with SHA-256 digest:

`5289d7d6e058510b16eb0594749f57d4c9634afdf4abd24d798958e2a96bbeb0`

## Meaning

No unsourced normalized pivot remains. The lower-quartile marked-wall singleton has a complete coefficient-bearing expansion in original `S` and `T` generators.

The branch remains open. This is one representative over one prime, and its 571-row expression is presentation-dependent rather than a reusable source-family template. The next depth-first leaf is the median representative; its feasibility can now be judged using the same DAG constructor.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_lower_quartile_source_dag.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_lower_quartile_source_dag.json`
