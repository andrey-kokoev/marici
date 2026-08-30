# Factorial memory interaction and source-monitor gate

## Question

Can the four detector/electronics reset combinations identify an interaction
between those memory loci, and can they distinguish that interaction from a
reset-induced change in the optical source?

## Interaction contrast

Record covariance under no reset, detector reset, electronics reset, and both
resets. If the source is invariant, the four records identify source,
detector-local memory, electronics memory, and one detector–electronics
interaction. The interaction is the factorial contrast

```text
C_none - C_E - C_D + C_DE.
```

The exact fixture recovers source `1/8`, detector memory `1/16`, electronics
memory `3/32`, and interaction `1/32`.

## Source-shift non-identifiability

The four science records alone form a saturated design. If reset actuation
changes pump statistics, source temperature, timing, or optical coupling, the
same table still admits a formal invariant-source factorial fit. In the
checker, real source shifts make that naive fit report source `5/32` and
interaction `1/16`, both wrong.

Thus adding an interaction term does not repair the earlier joint-reset
residual unless source invariance is independently established.

## Source-monitor repair

Split a calibrated optical tap before the detector and electronics branches.
Measure its source-memory statistic under all four reset conditions. Subtract
the condition-keyed source record before applying the nuisance factorial
contrast. The checker then recovers the true interaction `1/32` exactly.

The monitor must be independent of the reset actuators and its back-action
must be bounded. A source monitor sharing the same electronics simply moves
the alias.

## Verification

Run:

```text
python research/aspect/checkers/check_memory_interaction_factorial_design.py
```

The dependency-free checker verifies interaction recovery under source
invariance, the reset-induced source-shift hostile, and exact correction using
the condition-keyed optical tap.
