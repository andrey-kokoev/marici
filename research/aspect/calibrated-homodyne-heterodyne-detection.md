# Calibrated homodyne and heterodyne detection

Owner: `marici.Aspect`

## Bounded question

What optical authority is required to turn balanced detector currents into
phase-referenced quadratures, and how do inefficiency, unused ports,
electronics, gain mismatch, and temporal-mode mismatch enter the noise
contract? This packet fixes a single-mode convention and records the exact
finite covariance laws. It does not claim continuum photodetection completion.

## Calibration and source authority

The signal mode has mean quadratures `(x,p)` and vacuum covariance `I/2`. A
local oscillator has nonzero calibrated amplitude `beta` and phase `theta` in
the same temporal, spatial, polarization, and frequency mode. The balanced
beam splitter, output signs, detector gains, integration window, efficiency,
and electronics covariance are declared before data inspection.

The normalized homodyne mean is `X_theta=x cos(theta)+p sin(theta)`. At phases
`0` and `pi/2`, two predeclared rows reconstruct `(x,p)`. One phase has a
one-dimensional kernel. Without a nonzero local oscillator, absolute phase
origins form a `U(1)` torsor and the balanced phase-sensitive mean vanishes;
intensity alone cannot select a phase origin.

## Balanced subtraction

For real phase-aligned signal amplitude `alpha` and LO amplitude `beta`, the
balanced outputs are `(alpha+beta)/sqrt(2)` and
`(alpha-beta)/sqrt(2)`. Their intensity difference is exactly
`2 alpha beta`; common intensities cancel only when detector gains match. With
unequal gains, a residual proportional to the large LO background survives.
Gain balance is calibration data, not a conclusion inferred from a centered
trace.

## Efficiency as an environment dilation

Detection amplitude efficiency is modelled by
`X_meas=t X_signal+r X_vac`, with `t^2+r^2=1`. For `t=3/5`, `r=4/5`, retained
probability is `9/25`. Signal plus unused environment is lossless, while the
retained detector alone is lossy. A coherent input retains output variance
`1/2`, but referring noise back to the input gives `25/18`; inefficiency adds
`8/9` above intrinsic `1/2` in this convention.

Independent electronics variance `1/10` raises measured variance from `1/2`
to `3/5`. It cannot be subtracted unless independently calibrated.

## Heterodyne port

Heterodyne splits the signal and uses two phase-referenced balanced receivers
at quadrature phases. After gain rescaling, the mean map is identity on
`(x,p)`, but the unused splitter port injects independent vacuum into each
estimator. With vacuum variance `1/2`, each heterodyne quadrature has variance
`1`, compared with `1/2` for ideal homodyne. The means are jointly faithful on
the declared coherent-displacement class, but the simultaneous record carries
the exact vacuum penalty; it does not assign simultaneous sharp quantum
quadratures to an individual event.

## Temporal-mode overlap

If normalized signal and LO modes have overlap `mu`, only that component
contributes to the phase-sensitive mean. The checker uses `mu=3/5`. The
orthogonal component remains in the total record and noise budget; it is not a
phase-referenced quadrature measurement. Fitting the LO mode after viewing
outcomes is model selection, not prospective calibration.

## Detector kernels and hostile falsifiers

- one homodyne phase reconstructs both quadratures;
- phase is claimed with `beta=0`;
- inefficiency omits its vacuum environment;
- heterodyne is treated as two noiseless homodyne records;
- electronics variance is silently subtracted;
- gain mismatch is ignored under a strong LO;
- temporal overlap is fitted after observing records.

The smallest faithful mean family on the declared displacement class is two
independent phase rows. It remains invisible to global phase without the LO,
non-Gaussian structure beyond declared moments, orthogonal temporal modes,
inaccessible environments, and out-of-window detector dynamics.

## Completion boundary

Continuum completion requires detector impulse responses, quantum stochastic
input fields, bandwidth and sampling conventions, spectral noise densities,
causal filtering, finite-time estimators, and infinite-time convergence. The
finite covariance identities here do not supply those data.

Run `python research/aspect/checkers/calibrated_homodyne_heterodyne_detection.py`.
The result is
`research/aspect/results/calibrated_homodyne_heterodyne_detection.json`.
