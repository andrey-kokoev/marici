# Composed detector calibration: WP658

## Common-frame experiment

Combine the two signal records with two independently supported efficiency
controls and one background-only sideband. Let \(q\) be the determinant of
the calibrated two-template response, and write the three control amplitudes
as \(\sqrt{\kappa_L}\), \(\sqrt{\kappa_R}\), and \(\sqrt{\tau}\).

For parameters

\[
(u,v,\eta_L,\eta_R,\beta),
\]

the five-record Jacobian has exact determinant

\[
\det J
=4q\sqrt{\kappa_L\kappa_R\tau}.
\]

Consequently,

\[
\det(J^\top J)=16q^2\kappa_L\kappa_R\tau.
\]

The composed experiment is jointly faithful exactly when template contrast is
nonzero and all three independent control precisions are positive.

## Four minimal failure modes

Each factor has a distinct meaning:

- \(q=0\): object-separation failure at the detector record;
- \(\kappa_L=0\): left efficiency confounds the left magnitude;
- \(\kappa_R=0\): right efficiency confounds the right magnitude;
- \(\tau=0\): the common background erases the common-rate direction.

Approaching any boundary gives completion-stability failure even before exact
rank loss.

## Disposition

This is the complete ideal detector-calibration architecture for WP652's two
magnitude directions. It is still not an experimental realization: all five
records, their common frame, covariance, support, and uncertainty-stable
singular bound must be bound to one actual experiment.

The architecture identifies source magnitudes; it does not select their
values.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp658_composed_detector_calibration.py

Generated result: results/wp658_composed_detector_calibration.json.
