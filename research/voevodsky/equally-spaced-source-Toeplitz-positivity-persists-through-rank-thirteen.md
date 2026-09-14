# Equally spaced source Toeplitz positivity persists through rank thirteen

## Ladder

Fix

\[
\sigma=0.005,
\qquad h=0.25.
\]

Using source-side kernel values at separations

\[
h,2h,\ldots,12h,
\]

form the equally spaced Toeplitz Gram packet at every rank from two through thirteen.

Every packet passes numerical Cholesky positivity.

## Pivot behavior

The last Cholesky pivots begin as

\[
0.05799,
\quad0.05799,
\quad0.05616,
\quad0.01903,
\quad0.000458.
\]

At the largest ranks they decrease to

\[
2.37\times10^{-5},
\quad7.34\times10^{-7},
\quad3.87\times10^{-7}.
\]

The rank-thirteen determinant is approximately

\[
6.74\times10^{-42}.
\]

## Interpretation

The absence of a negative pivot through rank thirteen is positive evidence for this one-width lattice family. However, the rapidly shrinking pivots reveal an increasingly ill-conditioned moment problem.

The existing \(10^{-6}\) entrywise evaluation allowance is already larger than the final rank-twelve and rank-thirteen pivots. Consequently the previous coarse perturbation method cannot certify these ranks. Higher-rank work requires either:

- substantially higher precision with directed rounding;
- a structured Toeplitz determinant identity;
- a positive source factorization valid for the full lattice family.

Simply extending double-precision Cholesky to larger ranks will cease to be informative.

## Scope

This is not an all-rank theorem and uses only one width and one spacing. No zero locations were used; all kernel entries came from the endpoint, gamma, and prime source formula.

## Verification

```text
python research/voevodsky/checkers/scout_equal_spacing_toeplitz_rank_ladder.py
```

Artifacts:

- `research/voevodsky/checkers/scout_equal_spacing_toeplitz_rank_ladder.py`
- `research/voevodsky/results/equal_spacing_toeplitz_rank_ladder.json`
