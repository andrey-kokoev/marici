# Graded source-family necessity for K absorption

## Question

Which special-relation families are required to absorb all 4,224 `nx` \(K\)-derivative rows modulo the complete p-tangent relation family, while retaining pole and marked-level grading?

## Result

| basis | absorbed | residual |
|---|---:|---:|
| `T + S_K` | 4,092 | 132 |
| `T + S_K + S_IBP` | 4,158 | 66 |
| `T + S_K + S_q` | 4,224 | 0 |
| `T + all S` | 4,224 | 0 |

The residual supports against `T + S_K` and `T + S_K + S_IBP` contain 7–15 columns.

Thus special IBP relations remove half of the 132 residual rows but do not complete absorption. Special marked-\(q\) relations complete absorption without special IBP relations.

## Disposition

N3b2 is completed. The graded census identifies the essential coupling missed by the bare Jacobian test: the exact degree-14 mechanism factors through special \(K\) and marked-\(q\) relations modulo the full tangent family. Special IBP is not required for containment in this candidate comparison.

This is a family-level necessity/sufficiency result, not a homotopy formula. The next active leaf N3b3 should classify the 132 `T+S_K` residuals by pole and marked levels and extract the special marked-\(q\) lifts that kill them.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_family_necessity.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_family_necessity.json`
