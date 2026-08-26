# Covariance-support selector obstruction (WP289)

## Equal moments, unequal selection

Let the calibrated local selector margin be

\[
m_i=h_i-\sum_jJ_{ij}.
\]

Strict robust selection requires positive margin throughout the admitted
support. Mean and covariance do not determine that property. Consider two
exact laws:

\[
P_{\mathrm{safe}}(m=1)=P_{\mathrm{safe}}(m=3)=\frac12,
\]

and

\[
P_{\mathrm{unsafe}}(m=-1)=\frac1{12},\qquad
P_{\mathrm{unsafe}}(m=2)=\frac23,\qquad
P_{\mathrm{unsafe}}(m=3)=\frac14.
\]

Both have mean 2 and variance 1. The first has positive support and zero
selector-failure probability. The second crosses the boundary and fails with
probability $1/12$.

## Consequence

A calibrated covariance matrix does not supply the support requested by
WP288. Any Gaussian or compact-support completion is an added modeling
assumption. It must be independently source-authorized, and a nonzero tail
must be judged against a failure tolerance declared before flavor readout.

This is a contextual-equivalence kernel: moment probes place the two laws in
one equivalence class, while a support-sensitive or tail-event probe separates
them. Algebraic access to moments is not an instrument for the tail event.

## Classification

Neither packet selects a `physical16` point by itself. The result closes
covariance-only calibration as sufficient selector authority. The remaining
instrument must measure or certify support or tails in the common source frame.

Run `uv run --with sympy python
research/flavor/checkers/wp289_covariance_support_selector.py` to regenerate
the exact moment and failure-probability audit.
