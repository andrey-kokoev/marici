# Correction: two nearest Carleman images do not yet equal the finite-interval remainder

The kernel

\[
\frac1{x+y}+\frac1{2-x-y}
\]

contains the two nearest half-line boundary images on the unit interval. Its
weighted Schur bound `2pi/sqrt(3)` is valid for that operator.

It has not been shown to equal the full difference between the zero-extension
logarithmic multiplier and the spectral Dirichlet logarithm on a finite
interval. The finite-interval method of images contains repeated reflections
at distances shifted by integer multiples of the interval length. Depending
on normalization and principal-value grouping, these resum to trigonometric
kernels. Their residual operator must be derived and bounded before the IMS
localization constant can be removed.

Therefore:

1. `pi/sqrt(3)` is a certified nearest-image budget;
2. `direct_interval_high_mode_threshold.json` and
   `sharpened_direct_interval_threshold.json` are conditional on an unproved
   identification and are not certified finite-interval thresholds;
3. the current unconditional explicit threshold remains the IMS-based one;
4. the next gate is the exact finite-interval image-series identity, followed
   by a norm bound for the images beyond the nearest two.
