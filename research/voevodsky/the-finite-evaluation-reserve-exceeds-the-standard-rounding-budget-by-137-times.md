# The finite-evaluation reserve exceeds the standard rounding budget by 137 times

## Question

Is the \(10^{-6}\) finite-evaluation allowance in the elementary rank-two enclosure quantitatively conservative?

## Gamma accumulation

The absolute accumulated midpoint integral is approximately

\[
1.35738.
\]

Using the standard floating forward-error factor with forty elementary operations per panel and 1,200,000 panels gives a gamma accumulation bound of approximately

\[
7.24\times10^{-9}.
\]

## Prime accumulation

There are 93,192 nonzero von Mangoldt terms through the selected cutoff. Their normalized absolute accumulation is approximately

\[
0.005091.
\]

Even charging fifty operations at every integer through the full cutoff gives a prime accumulation bound below

\[
3.40\times10^{-11}.
\]

## Combined budget

The combined standard bound is approximately

\[
7.27\times10^{-9}.
\]

The declared reserve \(10^{-6}\) is therefore larger by a factor of approximately

\[
137.6.
\]

Thus the reserve is not an arbitrary decimal cushion under the stated floating model.

## Remaining qualification

This forward-error calculation assumes that elementary transcendental evaluations are within a small fixed number of units in the last place. Python's standard library does not contractually provide directed interval enclosures, so the result remains conditional on the platform `libm` behavior.

A publication-grade certificate should replace each elementary call by outward-rounded intervals. No change to the analytic lower-bound argument is required.

## Verification

```text
python research/voevodsky/checkers/check_rank_two_floating_error_budget.py
```

Artifacts:

- `research/voevodsky/checkers/check_rank_two_floating_error_budget.py`
- `research/voevodsky/results/rank_two_floating_error_budget.json`
