# Gain calibration for the optical source monitor

## Question

Can the tap-strength family identify the untapped source when the source
monitor has unknown gain and offset at each tap setting or epoch?

## Gain-loading alias

The affine monitor record is

```text
y = g x + o,
```

where `x` is the physical tapped-source statistic. Two tap records cannot be
used for source extrapolation until their gains and offsets are placed in one
calibrated coordinate system. Ignoring them gives a wrong intercept in the
exact fixture.

A single known-bright reference is also insufficient when offset is unknown.
Changing gain and compensating offset leaves the reference record unchanged
while changing the inferred science value.

## Minimal affine calibration

At every tap strength and science epoch, record a dark input and a known-bright
reference. The dark record fixes offset; the bright-minus-dark contrast fixes
gain. Correct the science record before extrapolating across tap strength.

The checker freezes different gains and offsets at the two tap settings. The
dark/bright calibration recovers both physical records and the untapped source
`1/8` exactly.

## Boundary

This is an affine monitor theorem. Saturation requires another reference level
or a separately calibrated nonlinear response. Reference uncertainty,
interpolation between calibration epochs, and optical crosstalk between the
reference injection and source remain separate ports.

The calibration records must retain tap strength, epoch, monitor channel, and
reference lineage. A timeless scalar gain does not authorize correction.

## Verification

Run:

```text
python research/aspect/checkers/check_source_monitor_gain_calibration.py
```

The dependency-free exact checker verifies the uncalibrated error, one-reference
alias, dark/bright gain recovery, and final source extrapolation.
