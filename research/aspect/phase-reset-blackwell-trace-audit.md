# Phase-reset Blackwell trace audit

Author: `marici.Aspect`

Date: 2026-08-26

Status: exact optical hostile for constructive upgrades

## Optical predecessor

Let a coherent pulse carry a path-relative phase

\[
\phi\in\{0,\pi\}.
\]

A balanced interferometer sends these two phases to opposite output ports, so
the old experiment distinguishes them without error. Its stochastic channel
is the two-by-two identity matrix.

## Reset-only replacement

Now apply a phase actuator that sets \(\phi\) to zero before the terminal
interferometric readout. Both predecessor states produce the same calibrated
terminal port. The reset-only channel has one effective outcome and identical
rows.

The terminal state is known perfectly, but the predecessor phase is not
observed. Under equal priors the best predecessor decision has risk \(1/2\).
No state-independent garbling of a constant record can reconstruct the old
two-outcome fringe experiment, so reset-only control does not Blackwell-
dominate it.

## Trace-preserving upgrade

Split a declared diagnostic fraction of the coherent preparation, record its
pre-reset fringe port, and then apply the same reset to the retained pulse.
The full trace contains

\[
(\text{pre-reset port},\text{reset command},\text{terminal port}).
\]

Projection onto the first coordinate exactly reconstructs the old experiment.
The augmented experiment therefore separates the predecessor phases and
Blackwell-dominates the old interface while still producing the calibrated
successor.

This construction uses a split coherent optical preparation. It is not a
claim that an unknown single quantum system can be copied. Splitting changes
the resource budget and loss model, which must be included in any bounded-risk
implementation.

## Smallest hostile

Inspect only the terminal fringe after reset. Both initial phases pass every
endpoint-calibration check, yet the predecessor kernel is total and the
equal-prior error remains \(1/2\). Any claim that the reset explained the
initial phase confuses controllability with observability.

## Boundary

The exact channel comparison establishes Nima's trace-observability and
Blackwell-preservation gates in an optical fixture. It does not establish
robust separation with finite photon number, phase diffusion, tap loss, or
detector nuisance. Those require one common prospective policy and a declared
resource-dependent risk bound.

## Reproduction

Run:

    python research/aspect/checkers/phase_reset_blackwell_trace_audit.py

