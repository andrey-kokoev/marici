# Within-block phase-drift no-go and paired repair

## Question

Can one sequential acquisition of `XX`, `YY`, `XY`, and `YX` be ordered so
that affine analyzer phase drift cancels universally in the reconstructed
coherence?

## First-jet obstruction

For a drifting frame on one analyzer, the correlation derivatives at the
calibrated origin are

```text
dXX/dphase = XY
dYY/dphase = -YX
dXY/dphase = -XX
dYX/dphase = YY.
```

Let the four settings be sampled at effective times `t_XX`, `t_YY`, `t_XY`,
and `t_YX`. In the reconstructed real quadrature, the drift coefficients of
`XY` and `YX` are proportional to `t_XX` and `t_YY`. In the imaginary
quadrature, the independent coefficients of `XX` and `YY` are proportional to
`t_XY` and `t_YX`.

Universal cancellation for arbitrary labelled X-state records therefore
forces all four times to zero. No ordering of four distinct sequential samples
can achieve it.

## Decisive hostile

Using the physical asymmetric record from the determinant packet, schedule
`XX, YY, XY, YX` at times `-3,-1,1,3` with phase slope `1/100`. The true
determinant is exactly at its boundary, but the first-jet sequential record
produces false NPT residual `36789/400000000`.

## Minimal universal repair

Sample every setting twice at opposite effective times and average each pair
before reconstructing the quadratures. The affine phase term then cancels
setting by setting, independent of the state. Eight correlation samples are
required in this record-independent construction.

This is a first-jet theorem. Phase curvature leaves second-order residuals;
gain drift and finite-count allocation remain separate ports. Simultaneous
multi-channel acquisition or phase-tagging every event could avoid the
eight-sample schedule, but those are different instruments with their own
calibration contracts.

## Verification

Run:

```text
python research/aspect/checkers/check_within_block_phase_drift_no_go.py
```

The dependency-free exact checker records the coefficient obstruction, a
false-positive hostile, and exact cancellation by the paired schedule.
