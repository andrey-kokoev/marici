# Green-orthogonalized observers outperform raw moment ladders

## Stability metric

For finite Green coefficient states with norm

\[
\|u\|_K^2=u^TKu,
\]

observer covectors carry the dual metric

\[
\langle a,b\rangle_{K^{-1}}=a^TK^{-1}b.
\]

Normalize every candidate observer in this metric. The eigenvalues of its observer Gram matrix measure complementary-observer stability independently of row scaling.

## Ten-context experiment

Use ten uniformly spaced contexts in \([-1,1]\). Compare:

1. the endpoint-first schedule
   \[
   -1,+1,0,+2,-2,\ldots;
   \]
2. greedy selection from integer exponents \([-8,8]\), maximizing the next smallest Gram eigenvalue;
3. Green-metric Gram--Schmidt combinations of the selected covectors.

Representative condition numbers are:

| observers | endpoint-first | adaptive pure moments | orthogonalized |
|---:|---:|---:|---:|
| 2 | 1.15 | 1.15 | 1 |
| 4 | 22.4 | 2.67 | 1 |
| 6 | 351 | 36.2 | 1 |
| 8 | 9,226 | 643 | 1 |
| 10 | 587,384 | 40,481 | 1 |

The greedy schedule begins

\[
-1,+1,-8,+8,0,+4,-5,-3,+6,+2.
\]

Large positive and negative exponents are selected early because they separate opposite ends of the context interval.

## Conclusions

### Endpoint stability is exceptional at rank two

The original pair \(q_{-1},q_{+1}\) is already well conditioned. Instability appears when nearby raw moments are added.

### Algebraic independence is not stable complementarity

Every distinct Laurent exponent adds exact rank, but consecutive raw moments rapidly become nearly dependent on a bounded context interval.

### Adaptive moments help but do not solve full recovery

Greedy exponent selection improves conditioning by more than an order of magnitude at moderate rank, yet full raw Vandermonde recovery remains severely ill conditioned.

### Orthogonalized combinations are the stable completion

Green-dual Gram--Schmidt produces condition number one at every stage. These observers are linear combinations of moments rather than single exponentials. Stable observation therefore requires synthesized covectors once the endpoint pair is exhausted.

## Design principle

```text
first two channels:
  use canonical endpoint moments

additional channels:
  choose by innovation against the Green dual metric

full reconstruction:
  use orthogonalized combinations, not a raw moment Vandermonde
```

This turns observer growth into a frame-design problem rather than only a rank census.

## Verification

```text
python research/coherence/check_observer_ladder_stability.py
```

The checker uses dependency-free Gaussian elimination and Jacobi symmetric eigensolving. Results are numerical rather than exact and should be treated as a reproducible finite experiment.

Artifacts:

- `check_observer_ladder_stability.py`
- `observer-ladder-stability.v1.json`
