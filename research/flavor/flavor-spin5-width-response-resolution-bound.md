# Spin(5) width-response resolution bound (WP898)

## Question

Can WP897's mixing-dependent total width be controlled by one independently
calibrated detector-resolution condition, rather than by fitting a separate
tau template at every mixing value?

## Conditional analytic bound

Assume the source line shape is a normalized Breit--Wigner, represented in
the mass offset by a Cauchy density of half-width
\(\gamma_i=q_i\Gamma_i^{\rm SM}/2\), and assume the calibrated local detector
response is a centered Gaussian of standard deviation \(\sigma_i\). The
Fourier transform of the convolved line is

\[
\exp(-\sigma_i^2t^2/2-\gamma_i|t|).
\]

Relative to the zero-width Gaussian, Fourier inversion for the CDF and
\(1-e^{-\gamma t}\leq\gamma t\) give

\[
\sup_x|F_{gamma_i,sigma_i}(x)-F_{0,sigma_i}(x)|
\leq
\frac{1}{\pi}\int_0^\infty
e^{-\sigma_i^2t^2/2}\frac{1-e^{-\gamma_i t}}{t}\,dt
\leq
\frac{\gamma_i}{\sigma_i\sqrt{2\pi}}.
\]

For a histogram with \(r\) finite boundaries, telescoping its bin
probabilities through those CDF values yields

\[
d_{\rm TV}(S_{gamma_i},S_0)
\leq
\frac{r\gamma_i}{\sigma_i\sqrt{2\pi}}.
\]

WP253 has six bins and five finite boundaries, so \(r=5\). Since
\(0<q_i\leq1\) on the universal-mixing slice, the worst case uses the WP897
Standard Model-like total width. For a preregistered template-drift tolerance
\(\varepsilon\), it is sufficient to calibrate

\[
\sigma_i\geq
\frac{5\Gamma_i^{\rm SM}}{2\varepsilon\sqrt{2\pi}}.
\]

At the diagnostic choice \(\varepsilon=0.01\), the sufficient resolution
floors are approximately 0.581 and 2.473 GeV at the two poles. These are
thresholds to be compared with a measured tau-response width, not claims that
the detector already satisfies them.

## Claim boundary

WP898 converts a continuum width scan into one conditional calibration gate.
It does not establish that the tau response is Gaussian, centered,
translation-invariant, or independent of event kinematics. Non-Gaussian
tails, mass-dependent efficiencies, interference, and reconstruction bias
must either be included in an enlarged calibrated kernel or falsify the model.

The smallest falsifier is a calibrated response whose CDF differs from the
declared Gaussian kernel by more than the remaining error budget. The physical
instrument gate is a same-frame resolution and tail calibration at both poles,
with uncertainty support proving the chosen \(\varepsilon\) bound.

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp898_spin5_width_response_resolution_bound.py
~~~
