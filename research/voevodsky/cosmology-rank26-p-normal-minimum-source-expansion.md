# Minimum marked-wall singleton back-substitutes to one source row

## Issue-tree position

This continues the explicit-expansion branch depth-first. The normalized-pivot minimum representative is back-substituted to original `S`/`T` generators.

## Result

The minimum-trace target is the labelled basis column

```text
column 3420
k_pole = 0
q_levels = (2,1,1,2,1)
monomial = (0,0)
```

Its normalized expansion used one p-tangent pivot. Re-reading the original derivative rows shows that p-tangent row 4914 is already the singleton

\[
T_{4914}=-e_{3420}
\]

over \(\mathbb F_{32003}\). Therefore

\[
e_{3420}=-T_{4914}.
\]

The row belongs to the marked-\(q\) multiplication family, local index 210, for the active mark `g1`. Exact reconstruction passed.

## Meaning

For this representative, normalized-pivot back-substitution terminates immediately. No special relation, nested pivot, or fitted coefficient is needed: the singleton target is directly one original p-tangent derivative generator up to the integral unit sign.

This resolves the first leaf of the explicit-expansion branch. The branch itself remains open because the quartile, median, and maximum representatives have longer traces and may require genuine source-row DAG expansion.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_minimum_source_expansion.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_minimum_source_expansion.json`
