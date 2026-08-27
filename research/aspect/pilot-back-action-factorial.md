# Factorial audit of optical pilot back-action

## A perfect label can reverse the science contrast

Freeze pre-encoder source amplitudes

```text
reset   = 1
control = 6/5.
```

The true control-minus-reset contrast is `+1/5`. Encode the reset pilot with
unit transmission and the control pilot with transmission `3/4`. The detector
then sees

```text
reset   = 1
control = 9/10,
```

whose contrast is `-1/10`. The pilot is perfectly readable and the apparent
scientific effect has the wrong sign.

Incidence fidelity and intervention neutrality are therefore independent.

## Factorial detection

Interleave pilot-off and pilot-on records for both source conditions. The
pilot-by-condition interaction is

```text
(control_on - control_off) - (reset_on - reset_off) = -3/10.
```

This nonzero interaction proves that pilot loading is condition-dependent in
the frozen model. A common insertion-loss monitor or ratio normalization cannot
repair it: the encoded control/reset ratio is `9/10`, while the source ratio is
`6/5`.

## Calibrated inverse

If the two pilot transmissions are derived independently on a source-invariant
reference before the science comparison, dividing each encoded record by its
own transmission recovers the source amplitudes and contrast exactly.

The inverse is conditional. If transmission depends on amplitude, polarization,
time, or detector state, a two-number calibration is insufficient. A pre-
encoder source tap and a post-encoder monitor are the cleanest way to locate
the change, provided the tap itself passes a back-action audit.

## Optical design implication

Phase, polarization, wavelength, and time-bin pilot schemes should be tested on
every science observable they might perturb. Preserving total intensity does
not imply preserving polarization action, temporal shape, coherence, or route.
There is no universally passive pilot outside a declared observable domain.

## Claim boundary

The checker assumes exact multiplicative memoryless transmission and an
independently calibrated inverse. Drift, nonlinearity, polarization coupling,
tap back-action, and uncertain calibration remain open.

## Verification

```text
python research/aspect/checkers/check_pilot_back_action_factorial.py
```
