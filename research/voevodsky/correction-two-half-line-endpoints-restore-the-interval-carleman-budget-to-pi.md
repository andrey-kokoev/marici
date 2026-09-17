# Correction: two half-line endpoints restore the interval Carleman budget to pi

The unitary Weil multiplier has principal logarithmic coefficient `1/2`.
Therefore one half-line cosine--sine defect has norm at most `pi/2`.

The interval has two boundary charts. Applying the triangle inequality to the
two half-line defects gives

\[
C_{\partial,\mathrm{interval}}
\le \frac\pi2+\frac\pi2=\pi.
\]

Thus replacing the earlier interval budget `pi` by `pi/2` was unjustified.
The factor `1/2` and the two endpoint charts cancel in the coarse interval
bound. A smaller constant requires a direct two-endpoint kernel estimate that
uses cancellation between the left and right boundary defects.

The threshold files using `pi/2` are sensitivity calculations, not certified
interval thresholds. The directed angular IMS calculation remains a valid
explicit route, with its stated localization cost. The next analytic target is
the exact finite-interval image kernel and its operator norm; it can improve
`pi` only through proved two-endpoint cancellation.
