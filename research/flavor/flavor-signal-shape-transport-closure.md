# Signal-shape transport closure (WP255)

## Hostile leave-one-out test

Before using the finite grid at the physical pole masses, test the simplest
candidate transport without fitting it: normalize each raw signal column and
predict 140 GeV by linear interpolation between 130 and 160 GeV,

\[
\widehat S_{140}=\frac23 S_{130}+\frac13 S_{160}.
\]

The exact residual is nonzero in every occupied central bin. Its total-variation
norm is

\[
d_{\rm TV}(S_{140},\widehat S_{140})
=\frac{23108773}{354073635}\approx0.0653.
\]

The largest discrepancy lies in 110–140 GeV: about `-0.04249`. A diagnostic
variance formed from independent multinomial bin variances at all three masses
gives a standardized residual around `-3.26`; this is recorded as a diagnostic,
not promoted to a calibrated global significance.

## Disposition

WP255 rejects **exact piecewise-linear transport** of the normalized visible-mass
response. Therefore WP254's finite-grid rank cannot be transported mechanically
to 133.774 and 151.287 GeV. An approximate morphing model needs an independently
derived response law and correlated uncertainty calibration, or the actual pole
masses must be simulated directly. Interpolation chosen merely to preserve rank
would be a degenerating repair.

Run `uv run --with sympy python
research/flavor/checkers/wp255_signal_shape_transport_closure.py` for the exact
residuals, total variation, and deliberate zero-residual failure.
