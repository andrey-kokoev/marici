# Representative explicit expansions of marked-wall singleton columns

## Issue-tree position

This follows the highest-scored branch: retain explicit `S+T` expansion coefficients for active marked-\(q\) singleton columns. The first bounded subproblem is to retain and verify representative normalized-basis expansions before attempting all 9,450 columns or source-row back-substitution.

## Result

Over \(\mathbb F_{32003}\) at ambient degree 14, all 9,450 distinct active marked-wall singleton columns were reduced against the fixed normalized `S+T` basis. Trace lengths have:

- minimum: 1;
- median: 186;
- maximum: 544;
- total: 1,816,384 across 9,450 columns.

Five exact expansions were retained at minimum, lower-quartile, median, upper-quartile, and maximum trace length. Each satisfies the checked identity

\[
e_c=\sum_j a_j b_j,
\]

where \(e_c\) is the singleton labelled column and the \(b_j\) are fixed normalized pivots introduced by special (`S`) or p-tangent (`T`) rows.

| sample | trace length | `S` pivots | `T` pivots |
|---|---:|---:|---:|
| minimum | 1 | 0 | 1 |
| lower quartile | 126 | 118 | 8 |
| median | 186 | 176 | 10 |
| upper quartile | 250 | 242 | 8 |
| maximum | 544 | 489 | 55 |

Every retained expansion was reconstructed exactly. Full coefficient lists and labelled target columns are stored in the result JSON.

## Meaning

This crosses from rank/zero-remainder evidence to explicit coefficient-bearing identities. It also shows that most marked-wall singleton containment is mediated primarily by special exact pivots with a smaller p-tangent contribution, while one simplest column is itself a p-tangent pivot.

The branch is not exhausted. These are normalized-pivot expansions, not coefficients against the original source rows. Only five representative expansions are retained, and only one prime is covered. The next depth-first subproblem is back-substitution from normalized pivots to original `S` and `T` generators for a bounded representative, then expansion to templates if sparsity permits.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_marked_q_expansion_samples.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_marked_q_expansion_samples.json`
