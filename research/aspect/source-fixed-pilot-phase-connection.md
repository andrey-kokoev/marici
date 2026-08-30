# Source-fixed pilot phase connection

Author: `marici.Aspect`

Date: 2026-08-26

Status: exact optical gauge-descent fixture

## Bare phase jet

At one operating point take a signal jet

\[
\Psi=1,
\qquad
\Psi'=i.
\]

Its phase gradient is one. Under the local rephasing with \(f=1\) and
\(f'=2i\), the projective base value is unchanged but the phase gradient
becomes three. A bare conormal phase response therefore does not descend from
the projective signal line.

## Pilot connection

Derive a pilot tone from the same phase preparation before branch doubling
and transport it along a declared common path. Define the observable
connection difference

\[
J_{\rm rel}
=\operatorname{Im}\!\left(\frac{\Psi'}{\Psi}\right)
-\operatorname{Im}\!\left(\frac{P'}P\right).
\]

When the same rephasing acts on signal and pilot, each phase gradient shifts
by two and their difference remains one. This is the optical realization of
a source-fixed residual gauge: the pilot does not select a preferred phase by
declaration; it transports the phase connection from the common source.

An unrelated fixed local oscillator does not repair the gauge. If its phase
connection fails to transform with the signal, the reported jet changes from
one to three.

## Instrument contract

The packet must retain the common source event, pilot tap, optical route,
phase-lock state, calibration epoch, and pilot revision. Signal and pilot
heterodyne records must form one joint witness. Dispersion or path noise that
acts differently on them is a physical differential connection and belongs
in the uncertainty model; it must not be removed as gauge.

Deleting the pilot revision makes the referenced jet unavailable, not zero.
Positive-real gain drift and locally constant phase are harmless residual
gauges because they add no phase-gradient connection.

## Boundary

This finite fixture proves how a source-derived reference can make a conormal
phase jet descend. It does not construct Nima's required cosmological period,
cycle, or normalization. A sector-specific use must derive the analogue of
the pilot from the physical source before the doubled quotient and verify its
allowed residual gauge.

## Reproduction

Run:

    python research/aspect/checkers/source_fixed_pilot_phase_connection.py

