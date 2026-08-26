# Moment-tail selector bound (WP290)

## What moments can certify

For a local selector margin $m$ with calibrated mean $\mu>0$ and variance
$\sigma^2$, Cantelli's one-sided inequality gives

\[
P(m\leq0)\leq\frac{\sigma^2}{\sigma^2+\mu^2}.
\]

This is a probabilistic selector certificate, not a support theorem. At every
finite signal-to-uncertainty ratio, the upper bound remains positive.

## Exact sharp packet

For mean 2 and variance 1, the bound is $1/5$. It is attained exactly by

\[
P(m=0)=\frac15,\qquad P(m=5/2)=\frac45.
\]

The neutral-margin event already defeats strict selection. Therefore no
stronger distribution-free conclusion follows from those two moments.

For a predeclared one-percent failure tolerance, the necessary Cantelli
certificate is

\[
\frac{\mu}{\sigma}\geq\sqrt{99}.
\]

Meeting this threshold certifies the probability bound; it still does not
establish compact positive support.

## Classification

Moment calibration can authorize a conservative probabilistic branch selector
when its sampling law and failure tolerance are independently declared. It
cannot authorize a deterministic selector or a `physical16` point. The
physical gate remains a calibrated margin instrument, source-derived dynamics,
and the branch-to-flavor map.

Run `uv run --with sympy python
research/flavor/checkers/wp290_moment_tail_selector_bound.py` to regenerate the
exact sharpness and one-percent audit.
