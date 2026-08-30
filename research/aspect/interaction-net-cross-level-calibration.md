# Cross-level calibration gate

The pro-context tower becomes an instrument only if adjacent physical levels
agree without sharing a fit to the test packet.

For each adjacent pair, calibrate one common gain on the complete packet and
coordinate offsets from independent standards. Independent per-channel gains
are not an admissible chart change.
Then acquire the same preregistered source preparation by two routes:

1. direct acquisition at the lower level;
2. acquisition at the higher level followed by the frozen transfer map.

The transfer map first inverts the high-level calibration, applies the source
saturation law, and then applies the low-level calibration. The naturality
residual is the difference between the two raw lower-level records.

On every open saturation stratum, the same square must close to first order.
Its diagonal Jacobian is the common low-level to high-level gain ratio on
unsaturated coordinates and zero on clipped coordinates. At a clipping kink,
the packet declares a one-sided stratum instead of pretending a two-sided
derivative exists.

Accept a square only when its full-covariance residual statistic is below the
frozen threshold. Calibration standards, covariance, exclusions, apparatus
identities, and levels all precede the test packet.

This construction exposes the next real falsifier. A level-dependent gain or
offset change after calibration breaks the square. So does the wrong clipping
law. Keeping the value map while dropping its derivative transport also fails.
Refitting either calibration on the test packet can force closure and is
therefore prohibited.

The included fixture proves that the checker accepts the exact ideal family
and rejects wrong clipping and post-standard gain drift. It does not close the
physical square. That requires an independently calibrated optical packet.
