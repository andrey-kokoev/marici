# Independent sideband background calibration: WP656

## Signal-region obstruction

Let two labelled signal records respond to the two source log-magnitudes
\((u,v)\) and to one unknown common background normalization \(\beta\). The
linear response is

\[
J_{\mathrm{sig}}=
\begin{pmatrix}
2&0&1\\
0&2&1
\end{pmatrix}.
\]

Profiling an unconstrained \(\beta\) leaves a rank-one source Fisher matrix.
The contrast survives, but the common source-rate mode is erased. Distinct
signal templates alone therefore do not authorize two-parameter inference in
the presence of an uncalibrated common background.

## Detector-derived calibration channel

Add a background-only sideband that observes \(\beta\) independently with
Fisher precision \(\tau>0\). Profiling the now-calibrated nuisance gives

\[
\det F_{\mathrm{src}}=\frac{16\tau}{\tau+2}>0.
\]

The common-mode information is \(4\tau/(\tau+2)\). Any strictly positive
independent sideband precision restores local rank two, while the limit
\(\tau\to0\) returns the rank-one obstruction.

## Authority boundary

The sideband is a detector-derived calibration instrument only if its support
is declared independently of the target signal and its transfer factors,
efficiencies, covariance, and uncertainty are measured there. Fitting
\(\tau\) or the background response from the desired signal answer would not
authorize the calibration.

This repairs local magnitude identification, not source selection. The
smallest exact falsifier is \(\tau=0\), or sideband contamination by the same
unknown source amplitudes.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp656_sideband_background_calibration.py

Generated result: results/wp656_sideband_background_calibration.json.
