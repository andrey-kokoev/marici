# Uniform framed-metric Markov completion

## Question

Does the framed GL equipment fragment admit a bounded one-sided completion?

## Claim boundary

Normalized transfers satisfy \(\lVert A_i\rVert\le\rho<1\). Frames satisfy \(\sup_i\lVert R_i\rVert\le C<\infty\). Completed GL gauge arrows additionally require uniformly bounded \(S_i\) and \(S_i^{-1}\). No metric-only descent is asserted.

## Completed kernel

Let \(K^0\) be the normalized completed Markov operator and let

\[
R=\bigoplus_iR_i.
\]

The uniform frame bound makes \(R\) bounded. Define

\[
K=RK^0R^T.
\]

Then \(K\) is bounded and positive, with

\[
\lVert K\rVert
\le C^2\frac{1+\rho}{1-\rho}.
\]

Its finite principal block compressions are exactly the finite framed kernels.

## Completed GL arrows

A family \(S_i\) with uniform bounds on \(S_i\) and \(S_i^{-1}\) defines a bounded invertible direct-sum operator \(S\). Frame transport completes as

\[
K\longmapsto SKS^T.
\]

The companion witness is \(S\), the conjoint witness is \(S^{-1}\), and their triangle equations remain inverse identities. Composition, contiguous Beck–Chevalley, and finite-to-closed comparison cells paste strictly.

## Hostile boundary

Finite invertibility at every vertex is insufficient. Frames \(R_i=iI\) have unbounded direct sum and produce diagonal metric blocks \(i^2I\), so the completed covariance is unbounded even when every normalized edge vanishes. Similarly, a gauge family with unbounded inverse does not supply a bounded conjoint.

## Disposition

The framed-metric GL equipment has a uniformly bounded completion fragment. Completion requires separate uniform certificates for normalized transfers, frames, gauges, and inverse gauges. Metric-only descent remains independent.

## Verification

- `research/voevodsky/checkers/check_framed_metric_markov_completion.py`
- `research/voevodsky/results/framed_metric_markov_completion.json`
