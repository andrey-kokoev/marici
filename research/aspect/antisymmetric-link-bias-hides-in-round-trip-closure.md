# Antisymmetric link bias hides in perfect round-trip closure

## Two-way transfer can agree with itself and mismeasure the endpoints

Let two endpoint frames `A` and `B` be exactly aligned. Measure the directed
link in both directions. Give the forward link bias `1/4` and the reverse link
bias `-1/4`.

The directed measurements are therefore `1/4` and `-1/4`. Their sum—the usual
round-trip closure residual—is exactly zero. Yet the standard half-difference
endpoint estimator reports a false offset of `1/4`.

The decomposition is exact:

```text
half sum        = symmetric link bias
half difference = endpoint offset + antisymmetric link bias
```

Two-way exchange cancels the symmetric component. It cannot distinguish a true
endpoint offset from an antisymmetric propagation term.

## Closure has a blind representation

The antisymmetric link mode transforms exactly like the desired endpoint
difference. It lies inside the science channel rather than the closure residual.
More precision on the same two directed measurements cannot separate them.

Breaking the ambiguity requires a new operation, such as:

- a third independently routed link;
- physical path reversal while holding endpoints fixed;
- wavelength or polarization exchange with a derived parity law;
- an independently calibrated local comparison;
- modulation that changes the link term without changing endpoint frames.

## Optical instrument

Run bidirectional phase or frequency transfer, then reverse fiber routing or
swap wavelengths and polarizations. Record Sagnac area, thermal gradient, and
direction-specific amplifier state. A zero round-trip residual must be reported
as a consistency result, not as proof of reciprocal endpoint accuracy.

## Claim boundary

The checker uses an additive two-direction link model with exact scalar biases.
Time-varying delay, dispersion, nonlinear phase, synchronization error, and
finite-sample uncertainty remain open.

## Verification

```text
python research/aspect/checkers/check_antisymmetric_link_bias_hides_in_round_trip_closure.py
```
