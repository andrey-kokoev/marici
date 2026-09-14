# Vanishing spacing requires shrinking error or growing rank

## Conditioning theorem

As spacing \(h\) tends to zero at fixed rank, the sampled kernel values coalesce. For an even smooth kernel,

\[
K(mh)=K(0)+O(m^2h^2).
\]

Consequently the nonconstant Gram and Fejér directions generally have margins on the scale \(h^2\) at fixed order.

## Exact hostile

Consider the signed real-line measure

\[
2\delta_0-
\delta_1.
\]

Its rank-two lattice kernel has

\[
k_0=1,
\qquad
k_1=2-e^{-ih}.
\]

The determinant is exactly

\[
1-|k_1|^2
=4(\cos h-1)
=-2h^2+O(h^4).
\]

The negative atom is detected for every nonzero spacing, but the numerical margin collapses quadratically.

## Correction to the spacing experiment

Positivity through rank thirteen at

\[
h=0.25,
\qquad0.125,
\qquad0.0625
\]

is evidence at three finite scales. It is not a uniform approximation to the vanishing-spacing theorem under one fixed coefficient-error allowance.

A valid computational refinement must use at least one of:

- coefficient errors shrinking faster than \(h^2\) at fixed rank;
- rank growing as spacing decreases;
- an analytic factorization proving circle positivity without resolving collapsing minors numerically.

## Implication

The all-spacing theorem remains mathematically correct in exact arithmetic. What fails is the idea that a fixed-rank, fixed-precision sequence can establish it computationally.

## Verification

```text
python research/voevodsky/checkers/check_vanishing_spacing_fixed_rank_conditioning.py
```

Artifacts:

- `research/voevodsky/checkers/check_vanishing_spacing_fixed_rank_conditioning.py`
- `research/voevodsky/results/vanishing_spacing_fixed_rank_conditioning.json`
