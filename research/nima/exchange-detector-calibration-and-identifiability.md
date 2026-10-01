# Iteration 7: calibrated detector predictions and identifiability limits

## Fresh mutable input

The iteration6 compiler validates native comparison boundaries and retains the
anchor/mismatch packet, covariance and event provenance. This iteration executes
its actual two-pulse echo and four-pulse rectangle, then applies a conditional
coherent-state homodyne detector model. No experimental observations are used.

The compiler's real means are X quadratures here, so preparation amplitude A is
encoded as X=sqrt(2)*A. The coherent state also has independent vacuum P
quadratures. That extra physical preparation assumption is explicit: X covariance
alone cannot certify the full quantum state. The detector routine rejects a
non-vacuum X covariance rather than silently applying its coherent-state formula.
It is not a general quantum-state readout routine.

## Measurement contract

Assume constant efficiency eta, positive gain g with calibrated polarity,
offset b, independent electronic noise of variance v_e, and a local-oscillator
phase phi drawn independently per trial from a Gaussian of mean phi0 and standard
deviation s. For a real coherent displacement m in X, set

    c = exp(-s^2/2)*cos(phi0),
    c2 = (1+exp(-2*s^2)*cos(2*phi0))/2.

Loss mixes in vacuum, leaving coherent quadrature variance1/2. Total expectation
and variance of the detector signal are

    E[y] = b+g*sqrt(eta)*m*c,
    Var(y) = g^2*(1/2+eta*m^2*(c2-c^2))+v_e.

The phase-noise contribution follows from total variance. Control/readout
assumptions include stable preparation, identical detector response between
trials, independent phase noise and no intermediate destructive measurement.
Correlated phase drift or technical amplitude noise require a different model.

## Independent calibration inputs

In ideal population moments, dark and vacuum controls identify

    b = dark mean,
    v_e = dark variance,
    g^2 = 2*(vacuum variance-v_e).

This assumes the electronics contribution is unchanged between those controls
and signal acquisition. Gain polarity and phase orientation need their own
reference; noise variances determine only gain magnitude.

If the reference amplitude A and phase statistics are independently known and
c!=0, a prepared reference gives

    eta = [(reference mean-b)/(g*sqrt(2)*A*c)]^2.

This is calibration from supplied standard input, not a derivation of A or eta
from comparison counts. At eta=0 or c=0 the signed mean test is blind.

The checker recovers the declared synthetic gain and efficiency from exact
population formulas. It does not claim a finite-sample estimator, confidence
interval, detector characterization or measured calibration.

## Predictions through the compiled experiment

Under common calibration, offset-subtracted POPULATION mean ratios to a
separately prepared reference are

    exchange echo: +1,
    quarter-turn echo: -1,
    exchange rectangle, first port: 0.

The competing flat shared-leg rectangle would instead predict+1. The ratio
cancellation requires a nonzero reference mean and stable calibration between
control and event trials. It is not a statement that a ratio of noisy sample
means is unbiased.

For the illustrative declared values A=2, g=3, eta=.64, b=.2, v_e=.09,
phi0=.15 and s=.2, predicted means are approximately6.77909 for reference and
exchange echo, -6.37909 for quarter-turn echo, and .2 for the rectangle. Echo
variance is approximately4.66419; rectangle variance is4.59. These are fixtures,
not fitted parameters or experimental data.

## Two hostile identifiability tests

1. **Preparation/loss ambiguity.** A=1, eta=.64 and A=2, eta=.16 give identical
   detector mean and variance at the same gain and phase statistics. Without an
   independent preparation standard, an apparent amplitude normalization cannot
   separate source strength from loss. The corresponding prepared photon numbers
   differ by a factor of4.
2. **Phase-reference ambiguity.** A pi shift of the exchange echo's local
   oscillator produces exactly the same mean and variance as the quarter-turn
   echo at the original phase. A signed echo does not discriminate those dynamics
   if an uncontrolled phase reversal is allowed between trials.

These are limitations of the operational test, not failures of its conditional
pulse calculation. Interleaved, independently monitored phase and preparation
controls are required before interpreting a physical echo mismatch.

No normalized1/137 fluctuation share enters these calibration equations. It
cannot remove either ambiguity or determine an absolute current-field coupling.

## Verification and next integration

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_exchange_detector_calibration.py
    OPENBLAS_NUM_THREADS=1 uv run --with 'numpy>=2,<3' python research/aspect/scc/scc.py check nima-exchange-detector-calibration

Native DG checks are rerun, actual source witnesses are compiled, and propagated
packet means/covariance supply the detector predictions. Tolerance1e-10.
Report: `results/exchange-detector-calibration.json`.

Next integrate source preparation, compiler, detector contract and the proven
failure cases into one end-to-end audit. Keep native instrument selection and
absolute physical normalization as open claims, rather than letting a passing
conditional measurement calculation mark them complete.
