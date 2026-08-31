# Target-typed envelope for tangent corrections

## Issue-tree position

The stable special tri-complex core leaves a sample-dependent p-tangent correction. This leaf tests whether that correction is constrained by the target singleton's pole level and marked-wall levels.

## Result

Across the five representative source expansions, three support rules hold:

1. every p-tangent source row has \(K\)-pole level no greater than the target column's pole level;
2. every p-tangent marked-\(q\) row belongs to `g1`;
3. a p-tangent marked-\(q\) correction is present exactly when the target's `g1` level is 2.

| sample | target pole | target `g1` level | tangent poles | tangent families | tangent marked walls |
|---|---:|---:|---|---|---|
| minimum | 0 | 2 | 0 | \(q\) | `g1` |
| lower quartile | 0 | 1 | 0 | IBP, \(K\) | none |
| median | 1 | 2 | 0–1 | IBP, \(K\), \(q\) | `g1` |
| upper quartile | 0 | 1 | 0 | IBP | none |
| maximum | 2 | 2 | 0–2 | IBP, \(K\), \(q\) | `g1` |

## Meaning

The tangent correction is not arbitrary. Its pole support lies beneath the target pole, and its marked-wall component is controlled by the target `g1` level. This refines the support template into a target-typed envelope.

The result is a five-sample rule, not a universal theorem. It does not predict IBP or \(K\) multiplicities, coefficients, or monomial shifts.

The next depth-first leaf is falsification on additional non-quantile singleton columns. Promotion to a reusable conjecture requires those tests; failure would exhaust this tangent-envelope branch and trigger tree rescoring.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_tangent_envelope.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_tangent_envelope.json`
