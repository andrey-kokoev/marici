# CPLEAR common-knob complex calibration (WP407)

## Empirical packet

The CPLEAR collaboration performed dedicated neutral-kaon regeneration data
taking with a 2.5 cm graphite absorber. Tagged $K^0$ and $\bar K^0$ decay rates
after the absorber were compared through their interference with the inherent
$K_S$ amplitude. The published Table 2 reports both $\operatorname{Re}\Delta f$
and $\operatorname{Im}\Delta f$, their standard errors, and their correlation
in five momentum intervals from 250 to 750 MeV/$c$.

The exact checker reconstructs each reported two-by-two covariance matrix. All
five determinants are positive, hence every bin has a rank-two uncertainty
ellipse. Both central response components are nonzero in every bin. The carbon
intervention therefore has empirical evidence for the same physical setting
producing resolvable dispersive and absorptive shifts; this is no longer only
the formal identity Jacobian of WP406.

Primary sources are the [CPLEAR paper and Table 2](https://doi.org/10.1016/S0370-2693(97)01193-3)
and its [CERN record](https://cds.cern.ch/record/336319). The later
[dispersion analysis](https://arxiv.org/abs/hep-ex/9905007) explicitly combines
the correlated real and imaginary measurements and relates independent total
cross-section information to the imaginary part by the optical theorem.

## What the experiment does not yet prove

The published dedicated operation supplies absorber absent and one fixed carbon
thickness. With the vacuum intercept fixed, those two settings calibrate an
affine response, but their two-row design has rank two on the intercept, linear,
and quadratic columns. It cannot exclude a quadratic density correction.

Adding a third certified density makes the quadratic design full rank. A fourth
density can then be withheld. This is a genuine experimental successor rather
than a reanalysis of momentum bins: momentum changes the forward amplitude and
cannot substitute for independently varied carbon column density.

The largest reported correlations, 0.96 and 0.99, also warn that formal rank is
not uniform robustness. A successor must propagate material-density,
composition, momentum, geometry, decay-width, and detector uncertainties and
predeclare a smallest-singular-value acceptance threshold.

## Disposition

WP407 closes the existence, executability, and common-knob two-component
calibration gates for a real flavor system. It leaves the completion and
withheld-test gates open: at least three independently certified carbon column
densities are needed to test the first nonlinear correction, followed by a
fourth no-refit displacement measurement.

Run `uv run --with sympy python
research/flavor/checkers/wp407_cplear_common_knob_calibration.py` to regenerate
the JSON result.
