# Source-expansion template census

## Issue-tree position

After exhausting representative back-substitution, the issue tree selected reusable template extraction. The first leaf tests whether one relation family alone explains the nontrivial expansions.

## Result

Each original source coefficient was decoded back to its source constructor, pole level, marked wall, and monomial shift.

| sample | IBP rows | \(K\) rows | marked-\(q\) rows | S rows | T rows |
|---|---:|---:|---:|---:|---:|
| minimum | 0 | 0 | 1 | 0 | 1 |
| lower quartile | 115 | 58 | 398 | 562 | 9 |
| median | 118 | 55 | 278 | 439 | 12 |
| upper quartile | 228 | 99 | 559 | 877 | 9 |
| maximum | 143 | 154 | 765 | 1,002 | 60 |

Every nonminimum expansion uses all three source constructors: IBP, \(K\)-multiplication, and marked-\(q\) multiplication. Every nonminimum expansion also uses both special and p-tangent source rows.

The number of distinct family-relative monomial shifts is 103, 101, 235, and 120 from lower quartile through maximum. Thus the longer identities do not collapse to a mark-only or single-shift rule.

## Disposition

The single-family-template leaf fails. This is a typed failure, not branch exhaustion: it redirects template extraction to a tri-complex template coupling all three relation constructors.

The next depth-first leaf should test whether the coupling has a stable block form by pole level and mark, rather than fitting individual coefficient vectors. If no common block form survives, the issue tree should move to second-prime comparison or the independent \(K\)-absorption branch.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_source_template_census.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_source_template_census.json`
