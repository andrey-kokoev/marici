# CP-bias finite-sample resolution (WP334)

## Detector-level information

For the thermal branch probability

\[
p(\epsilon)=\frac{1}{1+e^{-2\beta\epsilon c_0}},
\]

the calibrated detector observes

\[
q(\epsilon)=\alpha+(1-\alpha-\delta)p(\epsilon).
\]

The checker derives the exact Bernoulli Fisher information for \(\epsilon\). At
zero bias, a perfect detector supplies information \(\beta^2c_0^2\) per
independent domain trial. For symmetric confusion \(\alpha=\delta=r\), this
becomes

\[
I_\epsilon(0)=\beta^2c_0^2(1-2r)^2.
\]

Independent trials add information linearly. At zero detector contrast, the
information vanishes for every sample count, so repetition cannot repair the
instrument kernel.

## Interpretation

WP333 proves local identifiability at zero bias. WP334 adds the distinct
statistical statement: any finite sample leaves overlapping outcome
distributions, with variance bounded below by the inverse total information.
No confidence claim is admitted until sample independence, calibration
uncertainty, nuisance uncertainty in \((\beta,c_0)\), and a confidence and power
criterion are declared.

This remains an instrument-resolution result. It neither selects the bias nor
proves that cosmological domains can be independently prepared and repeated.

Run `uv run --with sympy python
research/flavor/checkers/wp334_cp_bias_finite_sample_resolution.py` to
regenerate the exact information audit.
