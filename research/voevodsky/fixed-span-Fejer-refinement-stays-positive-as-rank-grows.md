# Fixed-span Fejér refinement stays positive as rank grows

## Correct refinement schedule

To avoid collapse of the sampled real-line span, halve spacing while approximately doubling rank:

\[
(h,N)
=
(0.25,13),
\quad
(0.125,25),
\quad
(0.0625,49).
\]

Each packet covers physical separation

\[
h(N-1)=3.
\]

The Gaussian width remains \(0.005\).

## Results

Using 1,048,576 angle samples, derivative interpolation bounds, and the inherited coefficient allowances gives conditional global Fejér lower bounds of approximately:

\[
0.00867,
\qquad
0.000558,
\qquad
0.000308.
\]

All three correctly scaled refinements remain positive.

## Significance

Unlike the fixed-rank spacing experiment, this sequence retains a nonzero observation span as \(h\) decreases. The rank-49 packet is the first test combining:

- smaller spacing;
- proportionally larger rank;
- source-derived coefficients at 49 lattice positions;
- global angle interpolation;
- accumulated coefficient uncertainty.

The positive margin decreases but remains larger than the declared total error.

## Scope

Three refinements with fixed physical span do not prove an infinite sequence. Recovering arbitrary compact real-line tests ultimately requires the physical span itself to grow, not merely remain equal to three. Thus a complete schedule needs

\[
h_j\to0,
\qquad
N_jh_j\to\infty.
\]

This packet establishes the first finite fixed-span precursor to that two-parameter limit.

## Verification

```text
python research/voevodsky/checkers/scout_fixed_span_fejer_refinement.py
```

Artifacts:

- `research/voevodsky/checkers/scout_fixed_span_fejer_refinement.py`
- `research/voevodsky/results/fixed_span_fejer_refinement.json`
