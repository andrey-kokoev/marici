# Rank-two source positivity holds on an open separation interval

## Result

Fix

\[
\sigma=0.005.
\]

The two eigenvalue enclosures at \(d=0.25\) can be transported using an explicit derivative bound in the separation parameter.

For both eigenvalues, the endpoint, gamma-constant, gamma-integral, and finite-prime derivative contributions give the common Lipschitz bound

\[
312.568.
\]

On the interval

\[
0.24998\leq d\leq0.25002,
\]

the maximum loss from the center bounds is therefore at most

\[
0.006252.
\]

The resulting uniform eigenvalue bounds are

\[
K_\sigma(0)-K_\sigma(d)>0.01315
\]

and

\[
K_\sigma(0)+K_\sigma(d)>0.00958.
\]

Hence every two-translate Gram matrix in this nonempty separation interval is positive definite under the inherited floating model.

## Meaning

The source-side result is no longer confined to one isolated parameter point. Continuity has been made quantitative directly from the endpoint, digamma, and prime formulas.

The interval is intentionally small because the gamma-integral derivative estimate uses the very coarse global majorant \(21+2u\). Sharper local digamma bounds could enlarge it substantially.

## Scope

The width remains fixed. The result does not cover all separations, width variation, or higher Gram ranks. It inherits the elementary-function rounding assumptions of the center enclosures.

## Verification

```text
python research/voevodsky/checkers/check_rank_two_positive_d_neighborhood.py
```

Artifacts:

- `research/voevodsky/checkers/check_rank_two_positive_d_neighborhood.py`
- `research/voevodsky/results/rank_two_positive_d_neighborhood.json`
